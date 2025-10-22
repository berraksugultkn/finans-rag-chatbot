
import os
import pandas as pd
import numpy as np
import streamlit as st
from sklearn.neighbors import NearestNeighbors
from sentence_transformers import SentenceTransformer
from typing import List, Tuple

# ============ Ayarlar ============
DATA_PATH = os.getenv("DATA_PATH", "finans_sorulari.csv")
EMB_MODEL = os.getenv("EMB_MODEL", "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")
DEFAULT_TOP_K = int(os.getenv("TOP_K", "3"))

# ============ Yardımcı Fonksiyonlar ============
@st.cache_data(show_spinner=False)
def load_csv(path: str) -> pd.DataFrame:
    df = pd.read_csv(path, sep=";")
    df.columns = [c.strip().lower() for c in df.columns]
    return df

@st.cache_resource(show_spinner=False)
def load_encoder(name: str):
    return SentenceTransformer(name)

@st.cache_resource(show_spinner=True)
def build_index(texts: List[str], model_name: str, top_k: int):
    model = load_encoder(model_name)
    embs = model.encode(texts, convert_to_numpy=True, normalize_embeddings=True, show_progress_bar=True)
    nbrs = NearestNeighbors(n_neighbors=min(top_k, len(texts)), metric="cosine")
    nbrs.fit(embs)
    return model, embs, nbrs

def retrieve(query: str, model, embs, nbrs, df: pd.DataFrame, top_k: int) -> pd.DataFrame:
    q = model.encode([query], convert_to_numpy=True, normalize_embeddings=True)
    distances, indices = nbrs.kneighbors(q, n_neighbors=min(top_k, len(df)))
    hits = df.iloc[indices[0]].copy()
    hits["score"] = 1 - distances[0]  # cosine similarity
    return hits

def generate_answer(query: str, contexts: List[Tuple[str, str, str]]) -> str:
    """
    GOOGLE_API_KEY varsa: bağlamı Gemini modeline verip yanıt üretir.
    Yoksa: en iyi eşleşmenin 'cevap' kolonunu döndürür.
    """
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        return contexts[0][1]  # Anahtarsız modda direkt cevabı döndür
    
    try:
        import google.generativeai as genai
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("models/gemini-1.5-flash")

        context_text = "\n\n".join([f"Soru: {c[0]}\nCevap: {c[1]}" for c in contexts])
        prompt = (
            "Sen bir finans asistanısın. Aşağıdaki bilgi tabanına dayanarak "
            "kullanıcı sorusunu Türkçe, kısa ve net yanıtla.\n\n"
            f"Bilgi:\n{context_text}\n\n"
            f"Kullanıcı sorusu: {query}\n\nYanıt:"
        )

        response = model.generate_content(prompt)
        return response.text.strip()

    except Exception as e:
        return f"Gemini çağrısında hata: {e}"


# ============ UI ============
st.set_page_config(page_title="Finans RAG Chatbot", page_icon="💬", layout="centered")
st.title("💬 Finans RAG Chatbot")
st.caption("Kendi CSV verinle çalışan RAG demo (Türkçe).")

with st.sidebar:
    st.header("Ayarlar")
    st.write("• OPENAI_API_KEY girersen LLM ile yanıt üretir, yoksa en yakın cevabı getirir.")
    st.write("• 'kategori' filtresi sadece eşleşen kayıtlarda öncelik verir (opsiyonel).")
    st.divider()
    openai_key = st.text_input("OPENAI_API_KEY", type="password", help="İstersen burada gir, ya da ortam değişkeni olarak ayarla.")
    if openai_key:
     os.environ["OPENAI_API_KEY"] = openai_key
google_key = st.text_input("GOOGLE_API_KEY", type="password", help="AIzaSyCmE6018lhVwz32_iyr3bfnAhfsH0j9NLg")
if google_key:
    os.environ["GOOGLE_API_KEY"] = google_key

    topk = st.slider("Top-K (bağlam sayısı)", 1, 10, DEFAULT_TOP_K)
    os.environ["TOP_K"] = str(topk)

# Veri yükle
df = load_csv(DATA_PATH)
all_cats = sorted([str(x) for x in df["kategori"].dropna().unique()]) if "kategori" in df.columns else []

st.success(f"Veri yüklendi: {len(df)} satır • Kolonlar: {list(df.columns)}")

# Embed index
topk = DEFAULT_TOP_K
st.write("🔧 Embed indeks oluşturuluyor... (ilk çalıştırmada model indirilebilir)")
model, embs, nbrs = build_index(df["soru"].astype(str).tolist(), EMB_MODEL, topk)
st.write("✅ Hazır!")

# Soru-cevap alanı
user_q = st.text_input("Sorunuzu yazın:", placeholder="Örn: 'Bileşik faiz nasıl hesaplanır?'")
use_cat = st.multiselect("Kategori (opsiyonel):", options=all_cats)
ask = st.button("Sor")

if ask and user_q.strip():
    with st.spinner("Aranıyor..."):
        hits = retrieve(user_q, model, embs, nbrs, df, topk)
        if use_cat:
            mask = hits["kategori"].astype(str).isin(use_cat)
            hits = pd.concat([hits[mask], hits[~mask]]).drop_duplicates()
        ctx = list(zip(
            hits["soru"].astype(str).tolist(),
            hits["cevap"].astype(str).tolist(),
            (hits["kategori"].astype(str).tolist() if "kategori" in hits.columns else ["-"]*len(hits))
        ))[:topk]
        answer = generate_answer(user_q, ctx)

    st.subheader("Yanıt")
    st.write(answer)

    with st.expander("Gösterilen bağlam (Top-K):"):
        for i, (soru, cevap, kat) in enumerate(ctx, 1):
            st.markdown(f"**{i}. Skor:** {hits.iloc[i-1]['score']:.3f}")
            st.markdown(f"**Kategori:** {kat}")
            st.markdown(f"**Soru:** {soru}")
            st.markdown(f"**Cevap:** {cevap}")
            st.markdown("---")

st.divider()
st.caption("ⓘ Demo amaçlıdır. Yanıtlar veri setinizle sınırlıdır.")

# Finans RAG Chatbot (Türkçe)

Bu proje, `finans_sorulari.csv` dosyanızdaki Soru–Cevap verisini kullanarak RAG tabanlı bir chatbot sunar.
- Embedding: Sentence-Transformers (multilingual)
- Retriever: Nearest Neighbors (cosine)
- Generator: OpenAI (opsiyonel; anahtarsız modda en yakın cevabı verir)
- UI: Streamlit

## Hızlı Başlangıç

```bash
# 1) Sanal ortam (önerilir)
python -m venv venv && venv\Scripts\activate    # Windows
# source venv/bin/activate                        # macOS/Linux

# 2) Gerekli paketler
pip install -r requirements.txt

# 3) Veri dosyasını proje klasörüne kopyalayın
copy "..\finans_sorulari.csv" .                  # Windows örnek komut

# 4) (Opsiyonel) OpenAI anahtarınızı ayarlayın
setx OPENAI_API_KEY "sk-...."                     # Windows kalıcı
# export OPENAI_API_KEY="sk-...."                 # macOS/Linux

# 5) Uygulamayı başlatın
streamlit run app.py
```

## Yapı
- `app.py`: Streamlit uygulaması
- `requirements.txt`: Bağımlılıklar
- `finans_sorulari.csv`: veri (id; soru; cevap; kategori)

## Notlar
- İlk çalıştırmada embedding modeli indirildiği için biraz sürebilir.
- OpenAI anahtarı girmezseniz, sistem en yakın kaydın `cevap` metnini döndürür.
- Bootcamp gereklilikleri için README'de mimari ve kurulum adımlarını anlattık.

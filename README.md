# 💰 Finans RAG Chatbot  

🎓 **Akbank GenAI Bootcamp – Yeni Nesil Proje Kampı** kapsamında geliştirilmiştir.  
Türkçe finans verileriyle çalışan bir **RAG (Retrieval-Augmented Generation)** tabanlı yapay zekâ sohbet robotudur.  

🌐 **Canlı Demo:**  
👉 [https://finans-rag-chatbot-hh3vgdtduuntdvze294u4f.streamlit.app](https://finans-rag-chatbot-hh3vgdtduuntdvze294u4f.streamlit.app)

---

## 👩‍💻 Proje Bilgileri
**Proje Türü:** Python • Yapay Zekâ • RAG (Retrieval-Augmented Generation)  
**Geliştirici:** Berraksu Gültekin  
**Bootcamp:** Akbank GenAI Bootcamp – Yeni Nesil Proje Kampı  

---

## 🎯 Proje Amacı
Bu proje, Türkçe finans verileriyle çalışan bir **RAG tabanlı chatbot** geliştirmeyi amaçlar.  
Kullanıcıların kredi, faiz, ekonomi ve yatırım gibi finansal konulardaki sorularına **önceden yüklenmiş CSV veri tabanından** yanıt verir.  

Amaç, büyük dil modellerini (LLM) gerçek veriyle birleştirerek finans alanında **akıllı, özelleştirilmiş bir asistan** oluşturmaktır.  

---

## 🧠 RAG Nedir?
**RAG (Retrieval-Augmented Generation)**, yapay zekâ modellerinin dış veriyle desteklenerek **daha doğru ve kaynak temelli** yanıtlar üretmesini sağlayan bir tekniktir.  

**Aşamalar:**  
1. **Retrieval (Getirme):** Model, kullanıcının sorusuna uygun bilgiyi veri tabanından bulur.  
2. **Augmentation (Zenginleştirme):** Bulunan bilgi modele bağlanır.  
3. **Generation (Üretim):** Eğer LLM anahtarı (ör. Google Gemini API) girilmişse, doğal dilde yeni bir yanıt üretir.  

---

## ⚙️ Kullanılan Teknolojiler
- **Python 3.11**  
- **Streamlit** → Web arayüzü  
- **Sentence Transformers** → Türkçe embedding modeli  
- **Pandas** → CSV veri işleme  
- **Google Gemini API (opsiyonel)** → LLM tabanlı yanıt üretimi  
- **sklearn NearestNeighbors** → Benzerlik tabanlı bilgi arama  

---

## 📊 Veri Seti Hakkında
Proje, `finans_sorulari.csv` adlı özel bir veri setiyle çalışır.  
Bu veri setinde **1000 Türkçe finans sorusu** ve bunlara ait yanıtlar yer alır.  

**Sütunlar:**  
- `id`: Kayıt numarası  
- `soru`: Kullanıcının finansal sorusu  
- `cevap`: Sorunun Türkçe yanıtı  
- `kategori`: (Opsiyonel) Bankacılık, Ekonomi, Yatırım gibi alan etiketleri  

Veri seti **manuel olarak derlenmiştir** ve Türk finans terminolojisine uygun olacak şekilde düzenlenmiştir.  

---

## 🧩 Çözüm Mimarisi
**Veri Akışı:**  
Kullanıcı Sorusu ⬇️  
→ **Embedding (Sentence Transformers)** ⬇️  
→ **Benzerlik Arama (sklearn NearestNeighbors)** ⬇️  
→ *(Opsiyonel)* **LLM Yanıtı (Google Gemini API)** ⬇️  
→ **Streamlit Arayüzü** 🖥️  

Bu yapı sayesinde model, kullanıcı sorularını veri tabanına göre analiz eder ve **en uygun yanıtı** anında döndürür.  


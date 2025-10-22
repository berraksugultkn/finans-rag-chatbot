# 💰 Finans RAG Chatbot

**Proje Türü:** Python • Yapay Zekâ • RAG (Retrieval-Augmented Generation)  
**Geliştirici:** Berraksu Gültekin  
**Bootcamp:** Generative AI 101 (GAIH)  

---

## 🎯 Proje Amacı
Bu proje, Türkçe finans verileriyle çalışan bir **RAG (Retrieval-Augmented Generation)** tabanlı chatbot geliştirmeyi amaçlar.  
Kullanıcıların kredi, faiz, ekonomi, yatırım gibi finansal konulardaki sorularına **önceden yüklenmiş CSV veri tabanından** yanıt verir.  
Projede amaç, büyük dil modellerini (LLM) gerçek veriyle birleştirerek alan odaklı akıllı bir finans asistanı geliştirmektir.

---

## 🧠 RAG Nedir?
**RAG (Retrieval-Augmented Generation)**, yapay zekâ modellerinin dış veriyle desteklenerek çalışmasını sağlayan bir tekniktir.  
Model önce soruya uygun bilgileri veri tabanından “getirir” (*Retrieval*),  
daha sonra bu bilgiyi kullanarak doğal bir yanıt üretir (*Generation*).  

Bu yaklaşım, modelin yalnızca eğitildiği bilgiye değil, senin yüklediğin özel veriye dayanarak yanıt vermesini sağlar.  

---

## ⚙️ Kullanılan Teknolojiler
- **Python 3.11**
- **Streamlit** → Web arayüzü  
- **Sentence Transformers** → Türkçe embedding modeli  
- **Pandas** → CSV veri işleme  
- **Google Gemini API (opsiyonel)** → LLM ile yanıt üretimi  
- **sklearn NearestNeighbors** → Benzerlik arama  

---

## 🧩 Çalışma Mantığı
1. Kullanıcı bir soru yazar.  
2. Sistem, `finans_sorulari.csv` dosyasındaki sorularla vektör benzerliği kurar.  
3. En yakın kayıtları getirir.  
4. Eğer **Google API Key** girilmişse, Gemini modeliyle doğal yanıt oluşturur.  
5. Sonuç arayüzde gösterilir.

---

## 🧰 Kurulum

### 1️⃣ Sanal ortam oluştur
```bash
python -m venv venv
venv\Scripts\activate


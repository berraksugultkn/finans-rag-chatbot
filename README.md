💰 Finans RAG Chatbot

Proje Türü: Python • Yapay Zekâ • RAG (Retrieval-Augmented Generation)
Geliştirici: Berraksu Gültekin
Bootcamp: Akbank GenAI Bootcamp – Yeni Nesil Proje Kampı

🎯 Proje Amacı

Bu proje, Türkçe finans verileriyle çalışan bir RAG (Retrieval-Augmented Generation) tabanlı chatbot geliştirmeyi amaçlar.
Kullanıcıların kredi, faiz, ekonomi ve yatırım gibi finansal konulardaki sorularına
önceden yüklenmiş CSV veri tabanından yanıt verir.

Amaç, büyük dil modellerini (LLM) gerçek veriyle birleştirerek,
finans alanına özel akıllı bir yapay zekâ asistanı geliştirmektir.

🧠 RAG Nedir?

RAG (Retrieval-Augmented Generation), yapay zekâ modellerinin dış veriyle desteklenerek
daha doğru ve kaynak temelli yanıtlar üretmesini sağlayan bir tekniktir.

Retrieval (Getirme): Model, kullanıcı sorusuna uygun veriyi CSV dosyasından bulur.

Augmentation (Zenginleştirme): Bu bilgiyi modele bağlam olarak verir.

Generation (Üretim): Eğer LLM anahtarı girilmişse, doğal dilde yeni bir yanıt üretir.

⚙️ Kullanılan Teknolojiler

Python 3.11

Streamlit → Web arayüzü

Sentence Transformers → Türkçe embedding modeli

Pandas → Veri işleme

Google Gemini API (opsiyonel) → LLM tabanlı cevap üretimi

sklearn NearestNeighbors → Benzerlik tabanlı bilgi arama

🧾 Veri Seti Hakkında

Veri seti, finans alanında sık sorulan soruların Türkçe açıklamalarından oluşur.
Her satırda şu bilgiler yer alır:

id	soru	cevap	kategori
1	Kredi kartı limiti nasıl belirlenir?	Kredi kartı limiti kişinin gelirine ve notuna göre belirlenir.	Bankacılık
2	Enflasyon nedir?	Enflasyon, genel fiyat seviyesindeki artıştır.	Ekonomi

Veri, manuel olarak hazırlanmış olup finans terminolojisine özgüdür.

🧩 Çözüm Mimarisi
Kullanıcı Sorusu
       ↓
Embedding (Sentence Transformers)
       ↓
Benzerlik Arama (NearestNeighbors)
       ↓
(Opsiyonel) LLM Yanıtı (Gemini API)
       ↓
Streamlit Arayüzü → Sonuç Gösterimi


Bu yapı sayesinde model, kullanıcı sorularını kendi veri tabanına göre anlamlandırır
ve en uygun cevabı anında üretir.

🧰 Kurulum
1️⃣ Sanal ortam oluştur
python -m venv venv
venv\Scripts\activate

2️⃣ Gerekli kütüphaneleri yükle
pip install -r requirements.txt

3️⃣ Uygulamayı başlat
streamlit run app.py

4️⃣ (Opsiyonel) API anahtarı ekle

Sol menüde “GOOGLE_API_KEY” alanına kendi anahtarını gir.
Girilmese bile sistem CSV’den en yakın cevabı döndürür.

💻 Web Arayüzü ve Kullanım

Uygulamayı başlattıktan sonra tarayıcıda otomatik açılır.

Soru kutusuna finansla ilgili bir soru yaz → Sor butonuna tıkla.

Cevap, CSV’den veya (varsa) LLM’den gelir.

“Top-K” slider’ı ile sistemin kaç benzer kayıt kullanacağını ayarlayabilirsin.

📸 Örnek:

“Kredi notu nasıl yükseltilir?” → “Kredi notu düzenli ödemeler ve düşük borç oranıyla yükselir.”

🚀 Gelecek Geliştirmeler

📂 PDF, web sitesi veya Excel’den veri ekleme desteği

🧠 Türkçe finans dili için özel embedding modeli

💬 Sohbet geçmişi hafızası (önceki sorulara göre yanıt)

📊 Faiz, kredi ve enflasyon hesaplayıcı modülleri

🌐 Streamlit Cloud üzerinde web sürümü

🧩 Akademik Temel

Bu proje, Generative AI 101 Bootcamp’teki “Akademik Tez Araştırma Asistanı” projesinden
esinlenilerek geliştirilmiş, fakat finans verileriyle özelleştirilmiştir.

Böylece, RAG mimarisinin farklı bir sektörde uygulanabilirliği gösterilmiştir.

🏁 Sonuç

Türkçe RAG sisteminin finans alanında başarıyla çalıştığı gösterildi.

Embedding ve benzerlik arama işlemleri saniyeler içinde sonuç verdi.

Basit ama etkili bir Streamlit arayüzüyle kullanıcı dostu bir deneyim oluşturuldu.

📜 Lisans

Bu proje MIT Lisansı ile paylaşılmıştır.
Serbestçe kullanabilir, düzenleyebilir ve geliştirebilirsiniz.

📎 Bağlantılar

GitHub Repo: https://github.com/berraksugultkn/finans-rag-chatbot

Bootcamp: Akbank GenAI Bootcamp – Yeni Nesil Proje Kampı

Geliştirici: Berraksu Gültekin

📌 Yarışmaya uygun formatta eksiksizdir:
✅ Proje Amacı
✅ Veri Seti
✅ Kullanılan Yöntemler
✅ Kurulum & Çalıştırma Kılavuzu
✅ Çözüm Mimarisi
✅ Web Arayüzü Açıklaması
✅ Sonuç & Lisans

---

## 🌐 Canlı Demo Linki
Proje canlı olarak bu bağlantıdan test edilebilir:  
👉 [https://finans-rag-chatbot-hh3vgdtduuntdvze294u4f.streamlit.app](https://finans-rag-chatbot-hh3vgdtduuntdvze294u4f.streamlit.app)


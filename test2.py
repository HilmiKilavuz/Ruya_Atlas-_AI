import google.generativeai as genai

# API anahtarı ayarlama
genai.configure(api_key="Your_API_Key")  # API Anahtarımız

# Modeli başlatma
model = genai.GenerativeModel("gemini-1.5-pro")

# Felsefecilere göre prompt şablonları
PHILOSOPHER_PROMPTS = {
    "1": "Sigmund Freud'un psikanalitik yaklaşımına göre bu rüyayı analiz et.",
    "2": "Carl Jung'un kolektif bilinçdışı ve arketipler kuramına göre bu rüyayı analiz et.",
    "3": "Alfred Adler'in bireysel psikoloji yaklaşımına göre bu rüyayı yorumla.",
    "4": "Erich Fromm'un insancıl psikanaliz görüşlerine göre bu rüyayı yorumla."
}

# Desteklenen diller ve prompt çevirisi (örnek: Türkçe ve İngilizce)
LANGUAGE_PROMPTS = {
    "tr": {
        "giriş": "Rüyanızı girin:",
        "seçim": "Kime göre yorumlansın?\n1 - Freud\n2 - Jung\n3 - Adler\n4 - Fromm\nSeçiminiz (1-4): "
    },
    "en": {
        "giriş": "Enter your dream:",
        "seçim": "Whose interpretation do you want?\n1 - Freud\n2 - Jung\n3 - Adler\n4 - Fromm\nYour choice (1-4): "
    }
}

# Rüyayı yorumlayan fonksiyon
def yorumla_rüya(rüya_metni, seçim, dil="tr"):
    try:
        filozof_promptu = PHILOSOPHER_PROMPTS.get(seçim)
        if not filozof_promptu:
            return "Geçersiz seçim. Lütfen 1 ile 4 arasında bir değer girin."

        prompt = f"Kullanıcının rüyası: \"{rüya_metni}\"\n\n{filozof_promptu}"
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Bir hata oluştu: {str(e)}"

# Kullanıcıdan bilgi alma ve süreci başlatma
def kullanıcıdan_rüya_al():
    dil = "tr"  # İleride otomatik dil tespiti veya seçim eklenebilir

    rüya = input(LANGUAGE_PROMPTS[dil]["giriş"])
    seçim = input(LANGUAGE_PROMPTS[dil]["seçim"])

    yorum = yorumla_rüya(rüya, seçim, dil)
    print("\n— Rüya Yorumu —")
    print(yorum)
    print("\n(Bu yorum yapay zeka tarafından oluşturulmuştur.)")

# Çalıştır
kullanıcıdan_rüya_al()

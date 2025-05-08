import google.generativeai as genai

# API anahtarı ayarlama
genai.configure(api_key="AIzaSyDI5dhVf1wfWKFrxS8QiaTliraRnA-orvc")  # API

# Modeli başlatma
model = genai.GenerativeModel("gemini-1.5-pro")

# Rüya yorumlama fonksiyonu
def yorumla_rüya(rüya_metni):
    try:
        response = model.generate_content(
            f"Rüyada '{rüya_metni}' görmek ne anlama gelir? Kapsamlı ve kişisel bir yorum yap."
        )
        yorum = response.text
        return yorum
    except Exception as e:
        return f"Bir hata oluştu: {str(e)}"

# Kullanıcıdan rüya alma ve yorumlama
def kullanıcıdan_rüya_al():
    rüya = input("Rüyanızı girin: ")
    yorum = yorumla_rüya(rüya)
    print("\n— Rüya Yorumu —")
    print(yorum)
    print("\n(Bu yorum yapay zeka tarafından oluşturulmuştur.)")

# Fonksiyonu 
kullanıcıdan_rüya_al()

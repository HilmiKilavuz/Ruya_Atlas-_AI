import google.generativeai as genai
import re 

# API anahtarı ayarlama
genai.configure(api_key="Your_API_Key")  # Kendi API anahtarınızı girin

# Modeli başlatma
model = genai.GenerativeModel("gemini-1.5-pro")

# Rüya analiz fonksiyonu - Rüyayı analiz et ve sorular üret
def analiz_et_ve_sorular_oluştur(rüya_metni):
    try:
        # Rüyadaki anahtar unsurların ve soruların çıkarılmasını isteyen bir istem oluşturuyoruz
        response = model.generate_content(
            f"Rüya metnini inceleyip, rüyadaki önemli temalar ve unsurları belirleyin. "
            f"Bu unsurlara dayalı olarak 3 dinamik soru oluşturun: {rüya_metni}"
        )
        sorular = response.text
        return sorular
    except Exception as e:
        return f"Bir hata oluştu: {str(e)}"


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


# Kullanıcıdan alınan yanıtları birleştirme
def detay_sorusu_ve_cevapla(rüya_metni):
    sorular = analiz_et_ve_sorular_oluştur(rüya_metni)
    print("\n— Yapay Zeka tarafından oluşturulan sorular —")
    print(sorular)

    yanitlar = []
    sorular_listesi = re.findall(r"\d\.\s*(.+)", sorular) or sorular.split("\n")  # Soruları satır satır ayırıyoruz

    for soru in sorular_listesi:
        if soru.strip():  # Boş satırlardan kaçınalım
            print(soru)
            cevap = input("Cevabınızı girin (geçmek için sadece enter'a basın): ")
            if not cevap.strip():
                continue
            yanitlar.append(f"{soru} -> {cevap}")

    detay = "\n".join([f"{soru} Cevap: {cevap}" for soru, cevap in zip(sorular_listesi, yanitlar)])

    return detay

# Rüya yorumlama süreci
def kullanıcıdan_rüya_al():
    rüya = input("Rüyanızı girin: ")

    # Başlangıç yorumunu al
    başlangıç_yorum = yorumla_rüya(rüya)
    print("\n— Başlangıç Rüya Yorumu —")
    print(başlangıç_yorum)

    # Detaylı sorulara geç
    print("\nDaha detaylı bir yorum almak için bazı sorular sorulacak...")
    detay = detay_sorusu_ve_cevapla(rüya)

    # Detaylı yanıtla birlikte ikinci yorum
    tam_yorum = yorumla_rüya(
        f"Kullanıcı şu rüyayı gördü:\n{rüya}\n\n"
        f"AI bu rüyaya göre aşağıdaki soruları sordu ve kullanıcı bu cevapları verdi:\n{detay}\n\n"
        "Lütfen bu detayları dikkate alarak, rüyayı daha derinlemesine ve kişisel olarak yeniden yorumla."
    )

    print("\n— Tamamlanmış Rüya Yorumu —")
    print(tam_yorum)
    print("\n(Bu yorum yapay zeka tarafından oluşturulmuştur.)")


# Fonksiyonu başlat
kullanıcıdan_rüya_al()

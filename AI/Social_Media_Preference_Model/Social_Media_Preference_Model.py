import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier

# Excel dosyasını oku ve etiketleri dönüştür
label_encoders = {}
df = pd.read_excel('database.xlsx')
for column in df.columns:
    label_encoders[column] = LabelEncoder()
    df[column] = label_encoders[column].fit_transform(df[column])

# Anket verilerini ayrıştır
X = df.drop('SosyalMedya', axis=1)
y = df['SosyalMedya']

# Random Forest sınıflandırıcısını oluştur
# rf_classifier değişkeni, Random Forest sınıflandırıcısını temsil eder. 
# Bu sınıflandırıcı, birçok karar ağacını kullanarak sınıflandırma yapabilen bir makine öğrenmesi modelidir.

# n_estimators parametresi, Random Forest modelinde kullanılacak olan karar ağacı sayısını belirtir.
# random_state parametresi, modelin tekrarlanabilirliğini sağlamak için kullanılır.
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)

# Sınıflandırıcıyı eğit
rf_classifier.fit(X, y)

# Kullanıcıya soruları sor ve seçeneklerin metnini göster
print("Yaşınızı seçin:")
print("a) -18")
print("b) 18-24")
print("c) 25-32")
print("d) 33-40")
print("e) 41-65")
print("f) +65")

# Kullanıcının cevaplarını doğru seçenek metinlerine dönüştürmek için bir sözlük kullan
answer_options = {
    "a": "-18",
    "b": "18-24",
    "c": "25-32",
    "d": "33-40",
    "e": "41-65",
    "f": "+65"
}

# Kullanıcıdan cevap al
age_answer = input("Cevabınızı girin: ")

# Seçenek metnini kullanıcının cevabına göre yazdır
print("Yaşınız:", answer_options[age_answer])

# Cinsiyet sorusu
print("Cinsiyetinizi seçin:")
print("a) Erkek")
print("b) Kadın")
gender_answer = input("Cevabınızı girin: ")
print("Cinsiyetiniz:", "Erkek" if gender_answer == "a" else "Kadın")

# Eğitim seviyesi sorusu
print("Eğitim seviyenizi seçin:")
print("a) İlkokul")
print("b) Ortaokul")
print("c) Lise")
print("d) Meslek Yüksekokulu")
print("e) Lisans")
print("f) Yüksek Lisans")
print("g) Doktora")
education_answer = input("Cevabınızı girin: ")
education_levels = ["İlkokul", "Ortaokul", "Lise", "Meslek Yüksekokulu", "Lisans", "Yüksek Lisans", "Doktora"]
print("Eğitim seviyeniz:", education_levels[ord(education_answer) - ord('a')])

# Sosyal medya kullanım sıklığı sorusu
print("Sosyal medyayı ne sıklıkla kullanıyorsunuz?")
print("a) Günlük")
print("b) Haftalık")
print("c) Aylık")
print("d) Nadiren")
usage_frequency_answer = input("Cevabınızı girin: ")
usage_frequencies = ["Günlük", "Haftalık", "Aylık", "Nadiren"]
print("Sosyal medya kullanım sıklığınız:", usage_frequencies[ord(usage_frequency_answer) - ord('a')])

# SosyalMedyaKullanımAmacı
print("Sosyal medyayı hangi amaçla kullanıyorsunuz? ")
print("a) Arkadaşlarla iletişim")
print("b) Haberleri takip etmek")
print("c) İlgi alanlarınıza yönelik içerik bulmak")
print("d) Eğlence için video ve görseller izlemek")
print("e) İş ağını genişletmek")
print("f) Ürün veya hizmet araştırması yapmak")
usage_goal_answer = input("Cevabınızı girin: ")
usage_goals = ["Arkadaşlarla iletişim", "Haberleri takip etmek", "İlgi alanlarınıza yönelik içerik bulmak", "Eğlence için video ve görseller izlemek","İş ağını genişletmek","Ürün veya hizmet araştırması yapmak"]
print("Sosyal medyayı hangi amacınız :", usage_goals[ord(usage_goal_answer) - ord('a')])


#TüketilenİçerikTürü
print("Sosyal medyada en çok hangi tür içeriği tüketiyorsunuz? ")
print("a) Haberler ve güncel olaylar")
print("b) Eğlence içerikleri")
print("c) Spor ve fitness içerikleri")
print("d) Moda ve güzellik içerikleri")
print("e) Seyahat ve gezi içerikleri")
print("f) Teknoloji ve inovasyon içerikleri")

usage_icerik_answer = input("Cevabınızı girin: ")
usage_iceriks = ["Haberler ve güncel olaylar","Eğlence içerikleri","Spor ve fitness içerikleri","Moda ve güzellik içerikleri","Seyahat ve gezi içerikleri","Teknoloji ve inovasyon içerikleri"]
print("Sosyal medyada en çok hangi tür içeriği tüketiyorsunuz? :", usage_iceriks[ord(usage_icerik_answer) - ord('a')])

#TakipEdilenHesaplar
print("Sosyal medyada en çok hangi tür hesabı takip ediyorsunuz? ")
print("a) Ünlüler ve influencer'lar")
print("b) Markalar ve şirketler")
print("c) Haber kaynakları ve gazeteler")
print("d) Eğitim ve öğrenme hesapları")
print("e) Sanat ve kültür hesapları")

usage_follow_answer = input("Cevabınızı girin: ")
usage_follows = ["Ünlüler ve influencer'lar","Markalar ve şirketler","Haber kaynakları ve gazeteler","Eğitim ve öğrenme hesapları","Sanat ve kültür hesapları"]
print("Sosyal medyada en çok hangi tür hesabı takip ediyorsunuz? :", usage_follows[ord(usage_follow_answer) - ord('a')])


#EtkileşimTürü
print("Sosyal medyada ne tür içeriklere etkileşimde bulunuyorsunuz? ")
print("a) Beğenme")
print("b) Yorum yapma")
print("c) Takip etme")
print("d) Gruplara katılma")

usage_etkilesim_answer = input("Cevabınızı girin: ")
usage_etkilesims = ["Beğenme","Yorum yapma","Takip etme","Gruplara katılma"]
print("Sosyal medyada ne tür içeriklere etkileşimde bulunuyorsunuz? :", usage_etkilesims[ord(usage_etkilesim_answer) - ord('a')])

#AlışverişTercihi
print("Sosyal medyada alışveriş yapmayı tercih ediyor musunuz? ")
print("a) Evet")
print("b) Hayır")

usage_alisveris_answer = input("Cevabınızı girin: ")
usage_alisveriss = ["Evet","Hayır"]
print("Sosyal medyada alışveriş yapmayı tercih ediyor musunuz? :", usage_alisveriss[ord(usage_alisveris_answer) - ord('a')])


#İlgilenilenÜrünTürü
print("Sosyal medyada alışveriş yaparken en çok hangi tür ürüne ilgi duyuyorsunuz? ")
print("a) Giyim ve moda")
print("b) Elektronik cihazlar")
print("c) Kozmetik ve güzellik ürünleri")
print("d) Ev eşyaları ve dekorasyon")
print("e) Spor malzemeleri")
print("f) Kitaplar ve yayınlar")


usage_ilgilenilen_answer = input("Cevabınızı girin: ")
usage_ilgileniens = ["Giyim ve moda","Elektronik cihazlar","Kozmetik ve güzellik ürünleri","Ev eşyaları ve dekorasyon","Spor malzemeleri","Kitaplar ve yayınlar"]
print("Sosyal medyada alışveriş yaparken en çok hangi tür ürüne ilgi duyuyorsunuz? :", usage_ilgileniens[ord(usage_ilgilenilen_answer) - ord('a')])

#ReklamAlgısı
print("Sosyal medyada reklamlarını nasıl algılıyorsunuz?")
print("a) İlgimi çekici buluyorum")
print("b) Rahatsız edici buluyorum")
print("c) İlgisiz buluyorum")
print("d) Reklamlara pek dikkat etmiyorum")


usage_reklam_answer = input("Cevabınızı girin: ")
usage_reklams = ["İlgimi çekici buluyorum","Rahatsız edici buluyorum","İlgisiz buluyorum","Reklamlara pek dikkat etmiyorum"]
print("Sosyal medyada reklamlarını nasıl algılıyorsunuz? :", usage_reklams[ord(usage_reklam_answer) - ord('a')])

#ReklamTercihi
print("Sosyal medyada hangi tür reklam size daha çok ilgi çekici geliyor? ")
print("a) İndirim ve kampanyalar")
print("b) Yeni ürün veya hizmetler")
print("c) Kişiselleştirilmiş öneriler")
print("d) Sosyal sorumluluk projeleri")


usage_reklamTercih_answer = input("Cevabınızı girin: ")
usage_reklamTercihis = ["İndirim ve kampanyalar","Yeni ürün veya hizmetler","Kişiselleştirilmiş öneriler","Sosyal sorumluluk projeleri"]
print("Sosyal medyada hangi tür reklam size daha çok ilgi çekici geliyor? :", usage_reklamTercihis[ord(usage_reklamTercih_answer) - ord('a')])

#AktifSaatDilimi
print("Sosyal medyada en çok hangi saat diliminde aktifsiniz? ")
print("a) Sabah (08:00 - 12:00)")
print("b) Öğleden sonra (12:00 - 18:00)")
print("c) Akşam (18:00 - 22:00)")
print("d) Gece (22:00 - 08:00)")


usage_aktifSaat_answer = input("Cevabınızı girin: ")
usage_aktifSaats = ["Sabah (08:00 - 12:00)","Öğleden sonra (12:00 - 18:00)","Akşam (18:00 - 22:00)","Gece (22:00 - 08:00)"]
print("Sosyal medyada en çok hangi saat diliminde aktifsiniz? :", usage_aktifSaats[ord(usage_aktifSaat_answer) - ord('a')])


#ÖzellikTercihi
print("Sosyal medyada hangi özelliği en çok kullanıyorsunuz? ")
print("a) Hikayeler")
print("b) Canlı yayınlar")
print("c) Gruplar ve topluluklar")
print("d) Mesajlaşma")
print("e) Etkinlikler ve etkinlik takvimi")


usage_ozellik_answer = input("Cevabınızı girin: ")
usage_ozelliks = ["Hikayeler","Canlı yayınlar","Gruplar ve topluluklar","Mesajlaşma","Etkinlikler ve etkinlik takvimi"]
print("Sosyal medyada hangi özelliği en çok kullanıyorsunuz? :", usage_ozelliks[ord(usage_ozellik_answer) - ord('a')])




# Kullanıcının cevaplarını sınıflandırıcıya uygun hale getir
user_answers = pd.DataFrame({
    'Yaş': [ord(age_answer) - ord('a')],
    'Cinsiyet': [ord(gender_answer) - ord('a')],
    'EğitimSeviyesi': [ord(education_answer) - ord('a')],
    'SosyalMedyaKullanımSıklığı': [ord(usage_frequency_answer) - ord('a')],
    'SosyalMedyaKullanımAmacı' : [ord(usage_goal_answer) - ord('a')],
    'TüketilenİçerikTürü' : [ord(usage_icerik_answer) - ord('a')],
    'TakipEdilenHesaplar' : [ord(usage_follow_answer) - ord('a')],
    'EtkileşimTürü' : [ord(usage_etkilesim_answer) - ord('a')],
    'AlışverişTercihi' : [ord(usage_alisveris_answer) - ord('a')],
    'İlgilenilenÜrünTürü' : [ord(usage_ilgilenilen_answer) - ord('a')],
    'ReklamAlgısı' : [ord(usage_reklam_answer) - ord('a')],
    'ReklamTercihi' : [ord(usage_reklamTercih_answer) - ord('a')],
    'AktifSaatDilimi' : [ord(usage_aktifSaat_answer) - ord('a')],
    'ÖzellikTercihi' : [ord(usage_ozellik_answer) - ord('a')]

    # Diğer soruların cevaplarını da buraya ekleyin
})

# Kullanıcının sosyal medya tahminini yap
predicted_social_media = label_encoders['SosyalMedya'].inverse_transform(rf_classifier.predict(user_answers))[0]
print("Önerilen sosyal medya platformu:", predicted_social_media)

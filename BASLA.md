# İşletim Sistemleri · 1. hafta

Bu paket yalnızca öğrencilerle paylaşılacak dosyaları içerir. Özel soru bankası ve anlatıcı notları ayrı bir dosyada teslim edilir.

## Mac üzerinde uygulama

ZIP’i repo klasörünün dışında, örneğin İndirilenler içinde tamamen açın. Terminalde `cd ` yazıp açılan paket klasörünü Terminale sürükleyin ve Enter’a basın. Sonra:

```bash
python3 uygula.py
```

Betikte sizin verdiğiniz mevcut İşletim Sistemleri repo yolu varsayılandır. Gerekirse farklı bir yolu açıkça verebilirsiniz:

```bash
python3 uygula.py "/Users/uzemsystem/Library/CloudStorage/OneDrive-T.C.SakaryaÜniversitesi/Github Repo/Isletim-Sistemleri-2026-2027"
```

Betik yalnızca `docs/hafta-01` öğrenci dosyalarını kopyalar; ana sayfaya ve README’ye 1. hafta bağlantılarını ekler. Önceki hedef dosyalar repo dışında tarihli klasöre yedeklenir. Diğer haftalara ve mevcut GitHub Pages iş akışına dokunmaz. Commit veya push yapmaz. Aynı paket tekrar uygulanırsa kendi eklediği hafta kartını günceller; çoğaltmaz.

`ogrenci-repo` klasörü çevrimdışı önizleme içindir; mevcut 4. haftanın yayımlanmış sürümünü de bağlam olarak içerir. Bu klasörün tamamıyla kendi reponuzu değiştirmeyin; aktarım için betiği kullanın.

## GitHub Desktop ile yayınlama

1. Yerel `docs/index.html` dosyasını tarayıcıda açın. 1. hafta ders notları, PDF ve PowerPoint bağlantılarını kontrol edin.
2. GitHub Desktop’ta mevcut İşletim Sistemleri reposunu seçin. Değişiklikler `docs/hafta-01`, `docs/index.html` ve `README.md` ile sınırlı olmalıdır; önceden kendi yaptığınız değişiklikler de varsa onları ayrıca inceleyin.
3. Commit mesajı örneği: `1. hafta giriş öğrenci materyallerini ekle`.
4. Commit ve Push origin işlemlerini yapın. Mevcut Pages iş akışı tamamlanınca https://uozbek.github.io/Isletim-Sistemleri-2026-2027/ adresinde 1. haftayı kontrol edin.

## İçerik ve dosya niteliği

- 75 kaynak slayt; sırası korunmuş, görseller HTML içine gömülmüş ayrıntılı öğrenci notları.
- 35 dakikalık hedefli hazırlık, sınıf etkinlikleri, mini ödev, öz değerlendirme.
- Özgün PDF’nin değiştirilmemiş kopyası.
- PDF görsellerinden oluşturulmuş 75 slaytlık PowerPoint. Özgün düzenlenebilir PPTX değildir; slayt içindeki metinler ayrı nesneler olarak düzenlenemez.
- Kısa öğrenci sunum metinleri ayrı HTML’de; yapılandırılmış açıklamalar `slides.json` içinde.
- Kitap PDF sıra sayfası ve basılı sayfa ayrımıyla kaynak okuma rehberi. Kitap tam metni dahil değildir.

## Doğrulama sınırı ve durum

Slayt sayısı/sırası, görsellerin gömülmesi, kaynak PDF eşitliği, PowerPoint paket yapısı, içerik dosyalarının ayrımı ve yerel bağlantılar denetlenmiştir. Tarayıcı bu çalışma ortamında başlatılamadığı için masaüstü/telefon görünümü ve arama/yakınlaştırma davranışı tarayıcı üzerinden doğrulanamamıştır; yerel önizlemede kontrol edin. Kaynak slaytların mevcut tasarımı korunmuştur.

Henüz Mac’inizdeki repoya kopyalama, commit, push veya yeni yayının doğrulanması yapılmamıştır. Hazırlanan dosya aktarım için hazırdır.

# Isletim-Sistemleri-2026-2027

Repo işletim sistemleri dersinin ders notlarını ve uygulama notlarını içermektedir.

## Öğrenci ders materyalleri

| Hafta | Konu | İçerik |
|---|---|---|
| 4 | [Thread’ler ve Eşzamanlılık](docs/hafta-04/index.html) | Önceki hafta özeti, hazırlık kaynakları, slayt açıklamaları, uygulama ve mini ödev |

GitHub dosya görünümünde HTML kaynak kodu görüntülenir. Ders sayfasını tarayıcıda kullanmak için GitHub Pages yayını etkinleştirilmelidir.

## Site yayını

1. Repository Settings → Pages → Build and deployment → Source alanında **GitHub Actions** seçin.
2. Actions → **Publish student lesson** → **Run workflow** işlemini çalıştırın.
3. İlk kurulumdan sonra `main` dalındaki `docs/` değişiklikleri yayını otomatik başlatır.

Yayın başarıyla tamamlandığında beklenen site adresi:
https://uozbek.github.io/Isletim-Sistemleri-2026-2027/

GitHub Pages yalnızca `docs/` klasörünü yayımlar. Herkese açık bu repo öğrenci materyallerini içerir; öğretim elemanına özel soru bankası ve yanıt anahtarları burada tutulmaz.

## Yerel görüntüleme

`docs/index.html` dosyasını tarayıcıda açabilirsiniz. Slayt görselleri yanındaki `assets/` klasöründen yüklenir. Harici okuma ve video kaynakları internet bağlantısı gerektirir.

## Kaynak ve uygulama

Slaytlardaki kaynak bilgileri korunmuştur. Ana ders kaynağı: Silberschatz, Galvin ve Gagne, *Operating System Concepts*, 10. baskı (2018), Bölüm 3–4. Ek okumalar ve kaynak sayfa eşleştirmeleri hafta sayfasında belirtilir.

Pthreads örneği: [sum_threads.c](docs/hafta-04/examples/sum_threads.c). Linux üzerinde derleme ve çalıştırma adımları hafta sayfasındaki mini ödev bölümündedir.

#!/usr/bin/env python3
"""Copies week 01 student materials; never commits, pushes or copies private files."""
from pathlib import Path
import sys,re,shutil,datetime,unicodedata,hashlib
BASE=Path(__file__).resolve().parent
DEFAULT='/Users/uzemsystem/Library/CloudStorage/OneDrive-T.C.SakaryaÜniversitesi/Github Repo/Isletim-Sistemleri-2026-2027'
def resolve_unicode(p):
 p=Path(p).expanduser()
 if p.exists():return p.resolve()
 # Match macOS NFC/NFD directory names component by component.
 current=Path(p.anchor)
 for name in p.parts[1:]:
  if not current.is_dir():return p
  matches=[x for x in current.iterdir() if unicodedata.normalize('NFC',x.name)==unicodedata.normalize('NFC',name)]
  if len(matches)!=1:return p
  current=matches[0]
 return current.resolve()
if len(sys.argv)>2:raise SystemExit('Kullanım: python3 uygula.py ["yerel-repo-yolu"]')
repo=resolve_unicode(sys.argv[1] if len(sys.argv)==2 else DEFAULT)
if not (repo/'.git').exists() or not (repo/'docs/index.html').is_file():raise SystemExit('Mevcut repo kökü ve docs/index.html bulunamadı. Hiçbir dosya değiştirilmedi. Repo yolunu ikinci argüman olarak verin.')
source=BASE/'ogrenci-repo/docs/hafta-01'
if not source.is_dir():raise SystemExit('Paketin ogrenci-repo/docs/hafta-01 klasörü bulunamadı. ZIP’i tamamen açın.')
old=(repo/'docs/index.html').read_text(encoding='utf-8');card=(BASE/'hafta01-karti.html').read_text(encoding='utf-8')
pattern=r'<!-- ISLETIM-HAFTA-01 -->.*?<!-- /ISLETIM-HAFTA-01 -->'
if re.search(pattern,old,re.S):updated=re.sub(pattern,lambda _:card,old,flags=re.S)
elif re.search(r'href=[\"\x27](?:\./)?hafta-01/',old):raise SystemExit('Ana sayfada farklı bir 1. hafta bağlantısı zaten var. Otomatik çoğaltma önlendi; dosya değiştirilmedi.')
elif re.search(r'<main\b[^>]*>',old):updated=re.sub(r'(<main\b[^>]*>)',lambda m:m[0]+card,old,count=1)
else:raise SystemExit('Ana sayfa yapısı beklenenden farklı. Hiçbir dosya değiştirilmedi.')
readme=repo/'README.md';rt=readme.read_text(encoding='utf-8') if readme.exists() else '# İşletim Sistemleri\n'
block='''<!-- ISLETIM-HAFTA-01 -->
## 1. Hafta · Giriş

[Ders notları](docs/hafta-01/index.html) · [PDF](docs/hafta-01/Sunum.pdf) · [PowerPoint — görsel tabanlı](docs/hafta-01/Sunum_Gorsel_Tabanli.pptx) · [Öğrenci paketi](docs/hafta-01/Ogrenci_Paketi.zip) · [Kaynak rehberi](docs/hafta-01/KAYNAK_OKUMA_REHBERI.md)
<!-- /ISLETIM-HAFTA-01 -->'''
rt=re.sub(pattern,lambda _:block,rt,flags=re.S) if re.search(pattern,rt,re.S) else rt.rstrip()+'\n\n'+block+'\n'
backup=repo.parent/('Isletim_Sistemleri_Hafta01_Yedek_'+datetime.datetime.now().strftime('%Y%m%d_%H%M%S_%f'))
files=[(p,repo/'docs/hafta-01'/p.relative_to(source)) for p in source.rglob('*') if p.is_file()]
for _,dst in files:
 if dst.exists() and dst.is_symlink():raise SystemExit('Sembolik bağlantı hedefi nedeniyle kopyalama durduruldu; dosya değiştirilmedi.')
if (repo/'docs/hafta-01').is_symlink() or (repo/'docs').is_symlink():raise SystemExit('Hedef klasör sembolik bağlantı; dosya değiştirilmedi.')
# Backup existing files outside the repository, before writing.
for dst in [repo/'docs/index.html',readme]+[d for _,d in files]:
 if dst.exists():
  b=backup/dst.relative_to(repo);b.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(dst,b)
for src,dst in files:
 dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,dst)
(repo/'docs/index.html').write_text(updated,encoding='utf-8');readme.write_text(rt,encoding='utf-8')
print('1. hafta öğrenci dosyaları kopyalandı:',repo/'docs/hafta-01')
print('Ana sayfa ve README bağlantıları eklendi. Önceki dosyaların yedeği:',backup)
print('Diğer haftalar ve Pages iş akışı korunmuştur. Commit/push yapılmadı.')
print('Şimdi docs/index.html dosyasını tarayıcıda inceleyin; ardından GitHub Desktop ile commit ve push yapın.')

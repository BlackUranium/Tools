# 🛡️ Mini Port Scanner (Nmap Style)

Tools *port scanner* sederhana yang dibuat menggunakan **Python** dengan dukungan *multi-threading*. Dibangun untuk keperluan edukasi dan eksplorasi jaringan komputer, terinspirasi dari fungsionalitas dasar Nmap.

## 🚀 Fitur Utama
* **Fast Scanning:** Menggunakan *Python threading* sehingga proses pemindaian ratusan port selesai dalam waktu sangat singkat (di bawah 1 detik).
* **Custom Port Range:** Bisa menentukan rentang port sendiri (misal dari port 1 sampai 1000).
* **CLI Interface:** Menggunakan argumen terminal yang rapi dan interaktif.
* **Error Handling:** Aman dari interupsi `Ctrl + C` (*Keyboard Interrupt*) dan validasi host target.


## 🔍 Mini Directory Fuzzer (Advanced)

Tools *web fuzzing* untuk mencari direktori, file tersembunyi, atau halaman admin pada sebuah website target, dilengkapi dengan *multi-threading*, penanganan *redirect*, dan pencarian ekstensi file otomatis.

### 🚀 Fitur Utama
* **Fast Multi-threading:** Didukung sistem *Queue* dan *threads* fleksibel yang bisa diatur kecepatannya.
* **Auto File Extensions:** Mendukung pencarian ekstensi tambahan secara otomatis (misal: `-e php,html`).
* **Redirect Handler:** Bisa mendeteksi status *redirect* (`301` / `302`) beserta tujuan foldernya.

### 💻 Cara Penggunaan
Jalankan script dengan menentukan URL target, file wordlist, ekstensi, dan jumlah threads:
```bash
python3 dir_fuzzer.py -u [https://target.com](https://target.com) -w wordlist.txt -e php,html -t 20

---

## 💻 Cara Instalasi

Pastikan komputer/laptop lo sudah terinstal Python 3. Kloning repository ini ke lokal lo:

```bash
git clone [https://github.com/BlackUranium/Tools.git](https://github.com/BlackUranium/Tools.git)

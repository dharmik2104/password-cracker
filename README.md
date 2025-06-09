# 🔐 Password Cracker – Dictionary Attack (MD5/SHA1/SHA256)

This is a Python-based dictionary attack password cracker that demonstrates how insecure hashed passwords can be cracked using common wordlists. Built as part of a hands-on cybersecurity learning journey focused on ethical hacking and offensive security



## 📌 Features

- Crack hashed passwords using a dictionary file  
- Supports common hash algorithms:  
  - ✅ MD5  
  - ✅ SHA1  
  - ✅ SHA256  
- Fast and simple CLI-based interface  
- Educational tool for red teaming, ethical hacking labs, and CTFs  



## 🛠️ Tools & Technologies

- Python 3  
- `hashlib` (Python standard library)  
- Wordlists (custom or prebuilt like `rockyou.txt`)  

---

## 🚀 How to Use

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/password-cracker.git
cd password-cracker
2. Create or Download a Wordlist
Use an existing one like /usr/share/wordlists/rockyou.txt or create your own:

echo -e "1234\nadmin\npass\nroot" > wordlist.txt
3. Run the Cracker


python3 cracker.py <HASH> <WORDLIST> --algo <md5|sha1|sha256>
🔍 Example

python3 cracker.py 21232f297a57a5a743894a0e4a801fc3 wordlist.txt --algo md5
✅ Output:
pgsql

[+] Password Found: admin
📂 File Structure
PasswordCracker/
├── cracker.py          # Main Python script
├── wordlist.txt        # Example wordlist (you can use any)
└── README.md           # Project documentation
⚠️ Disclaimer
This tool is for educational and ethical purposes only.
Do NOT use it on systems or data without explicit permission.
Always follow the law and responsible disclosure practices.

#CyberSecurity #EthicalHacking #Python #RedTeam #OffensiveSecurity #PasswordCracker #CTF

import hashlib
import argparse

# Parse command-line arguments
parser = argparse.ArgumentParser(description='Dictionary Attack Password Cracker')
parser.add_argument('hash', help='Hashed password to crack')
parser.add_argument('wordlist', help='Path to the wordlist file')
parser.add_argument('--algo', help='Hash algorithm (default=md5)', default='md5')
args = parser.parse_args()

def crack_password(hash_to_crack, wordlist_path, algo):
    try:
        with open(wordlist_path, 'r', errors='ignore') as wordlist:
            for word in wordlist:
                word = word.strip()
                if algo == 'md5':
                    hash_attempt = hashlib.md5(word.encode()).hexdigest()
                elif algo == 'sha1':
                    hash_attempt = hashlib.sha1(word.encode()).hexdigest()
                elif algo == 'sha256':
                    hash_attempt = hashlib.sha256(word.encode()).hexdigest()
                else:
                    print("Unsupported hash algorithm.")
                    return

                if hash_attempt == hash_to_crack:
                    print(f"[+] Password Found: {word}")
                    return

        print("[-] Password not found in the wordlist.")
    except FileNotFoundError:
        print("[-] Wordlist file not found.")

crack_password(args.hash, args.wordlist, args.algo)

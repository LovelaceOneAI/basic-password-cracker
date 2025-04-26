import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def brute_force_crack(target_hash, wordlist):
    for word in wordlist:
        if hash_password(word.strip()) == target_hash:
            return word.strip()
    return None

if __name__ == "__main__":
    password = input("Set a password to hash and crack: ")
    target_hash = hash_password(password)

    print(f"\n🔒 Hashed password: {target_hash}")

    guesses = ["123456", "password", "qwerty", "admin", "welcome", password]

    cracked = brute_force_crack(target_hash, guesses)

    if cracked:
        print(f"✅ Password cracked: {cracked}")
    else:
        print("❌ Password not found in wordlist.")

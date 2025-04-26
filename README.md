# Basic Password Cracker

A simple Python script that demonstrates password cracking by attempting to brute-force a hashed password using a small wordlist.

## How It Works

1. You set a password.
2. The script hashes the password using SHA-256.
3. It attempts to guess the password by hashing guesses from a predefined wordlist.
4. If a match is found, the password is "cracked."

## Usage

```bash
python password_cracker.py

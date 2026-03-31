# Decrypt an Encrypted Message

**Course:** Assets, Threats, and Vulnerabilities (Course 5)
**Certificate:** Google Cybersecurity Professional Certificate
**Status:** Completed

---

## Project Description

In this activity, I used Linux Bash shell commands to decrypt an encrypted file and recover hidden data. I navigated the filesystem to find a hidden file containing a Caesar cipher, decoded the cipher using the `tr` command, and used the revealed command to decrypt an AES-256-CBC encrypted file with `openssl`. This activity demonstrates foundational skills in encryption, decryption, and Linux command-line usage relevant to cybersecurity analysis.

---

## Task 1 — Read the Contents of a File

Listed files in the home directory and read the README.txt for instructions.

```bash
ls /home/analyst
cat README.txt
```

**Output of ls:**
```
Q1.encrypted  README.txt  caesar
```

**Output of cat README.txt:**
```
Hello,
All of your data has been encrypted. To recover your data, you will need to solve a cipher.
To get started look for a hidden file in the caesar subdirectory.
```

---

## Task 2 — Find a Hidden File

Changed into the `caesar` subdirectory, listed hidden files, read the hidden `.leftShift3` file, and decrypted the Caesar cipher using the `tr` command.

```bash
cd caesar
ls -a
cat .leftShift3
cat .leftShift3 | tr "d-za-cD-ZA-C" "a-zA-Z"
cd ~
```

**Hidden files found:**
```
.  ..  .leftShift3
```

**Decrypted Caesar cipher output:**
```
In order to recover your files you will need to enter the following command:

openssl aes-256-cbc -pbkdf2 -a -d -in Q1.encrypted -out Q1.recovered -k ettubrute
```

**How the Caesar cipher works:**
The `.leftShift3` file was encrypted by shifting each letter 3 positions to the left. The `tr` command maps the shifted character set `"d-za-cD-ZA-C"` back to `"a-zA-Z"`, reversing the encryption.

---

## Task 3 — Decrypt a File

Used the `openssl` command revealed in the previous task to decrypt `Q1.encrypted`, then verified the decrypted output.

```bash
openssl aes-256-cbc -pbkdf2 -a -d -in Q1.encrypted -out Q1.recovered -k ettubrute
ls
cat Q1.recovered
```

**Output of ls (after decryption):**
```
Q1.encrypted  Q1.recovered  README.txt  caesar
```

**Output of cat Q1.recovered:**
```
If you are able to read this, then you have successfully decrypted the classic cipher text.
You recovered the encryption key that was used to encrypt this file. Great work!
```

**Command breakdown:**
| Flag | Meaning |
|------|---------|
| `openssl aes-256-cbc` | Decrypt using AES-256-CBC symmetric cipher |
| `-pbkdf2` | Adds extra security to the encryption key |
| `-a` | Specifies base64 encoding for the output |
| `-d` | Decrypt mode |
| `-in Q1.encrypted` | Input (encrypted) file |
| `-out Q1.recovered` | Output (decrypted) file |
| `-k ettubrute` | Password used to decrypt |

---

## Screenshots

| Task | Screenshot |
|------|-----------|
| Task 1 — List files and read README | ![Task 1](assets/task1-read-readme.png) |
| Task 2 — Find hidden file and decrypt Caesar cipher | ![Task 2](assets/task2-caesar-cipher.png) |
| Task 3 — Decrypt encrypted file and read output | ![Task 3](assets/task3-decrypt-openssl.png) |

---

## Summary

This lab demonstrated three core skills in Linux-based cryptography analysis:

1. **Filesystem navigation** — Used `ls`, `cat`, `cd`, and `ls -a` to explore directories and find hidden files.
2. **Caesar cipher decryption** — Applied the `tr` command to shift characters back to their original positions, decoding a left-shift-3 Caesar cipher.
3. **AES-256-CBC decryption** — Used `openssl` to decrypt a symmetrically encrypted file using a known password, recovering the plaintext message.

These skills are directly applicable to incident response and forensic investigations where analysts may encounter encrypted files or obfuscated data.

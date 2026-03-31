# Generate and Compare Hashes

**Course:** Assets, Threats, and Vulnerabilities (Course 5)
**Certificate:** Google Cybersecurity Professional Certificate
**Status:** Completed

---

## Project Description

In this activity, I used Linux commands to generate and compare SHA-256 hash values for two files. Although the files appeared to have identical content when read with `cat`, their hash values were completely different — demonstrating how cryptographic hashing can detect even the smallest changes in a file. This skill is essential for verifying data integrity during security investigations.

---

## Task 1 — Generate Hashes for Files

Listed the files in the home directory, displayed their contents, and generated SHA-256 hashes for each file.

```bash
ls
cat file1.txt
cat file2.txt
sha256sum file1.txt
sha256sum file2.txt
```

**Contents of file1.txt and file2.txt (both appeared identical):**
```
X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*
```

> **Do the contents of the two files appear identical when using `cat`?** Yes

**SHA-256 hashes generated:**

| File | Hash |
|------|------|
| file1.txt | `131f95c51cc819465fa1797f6ccacf9d494aaaff46fa3eac73ae63ffbdfd8267` |
| file2.txt | `2558ba9a4cad1e69804ce03aa2a029526179a91a5e38cb723320e83af9ca017b` |

> **Do both files produce the same generated hash value?** No

Even though the file contents appeared identical, the hash values are completely different — indicating the files differ at a level not visible to the human eye.

---

## Task 2 — Compare Hashes

Wrote the hash values to separate files and used the `cmp` command to compare them byte by byte.

```bash
sha256sum file1.txt >> file1hash
sha256sum file2.txt >> file2hash
cat file1hash
cat file2hash
cmp file1hash file2hash
```

**Output of cmp:**
```
file1hash file2hash differ: char 1, line 1
```

> **Based on the hash values, is file1.txt different from file2.txt?** Yes

The `cmp` command confirmed that the two hash files differ at the very first character of the first line, proving the files are not identical despite appearing so visually.

---

## Key Commands

| Command | Purpose |
|---------|---------|
| `sha256sum <file>` | Generate a SHA-256 cryptographic hash of a file |
| `sha256sum <file> >> <hashfile>` | Generate hash and append output to a new file |
| `cat <file>` | Display file contents |
| `cmp <file1> <file2>` | Compare two files byte by byte and report first difference |

---

## Screenshots

**Task 1 — Generate hashes for file1.txt and file2.txt**

![Task 1](assets/task1-generate-hashes.png)

**Task 2 — Compare hash files with cmp**

![Task 2](assets/task2-compare-hashes.png)

---

## Summary

This lab demonstrated how SHA-256 hashing can detect differences in files that appear visually identical. The two files both displayed the EICAR antivirus test string when read with `cat`, but produced entirely different hash values — revealing that the files are not the same at the binary level. Using `sha256sum` to generate hashes and `cmp` to compare them are core techniques in data integrity verification, malware analysis, and digital forensics.

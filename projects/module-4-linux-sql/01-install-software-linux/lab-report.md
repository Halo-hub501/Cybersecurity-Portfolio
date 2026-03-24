# Lab Report: Install Software in a Linux Distribution

**Environment:** Debian-based Linux (Google Cloud Shell via Qwiklabs)
**Shell user:** `analyst@<instance>`

---

## Objective

Use the APT (Advanced Package Tool) package manager to install, uninstall, and manage software applications in a Linux environment.

---

## Task 1 — Ensure APT is Installed

Verified that the APT package manager is available by running:

```bash
apt
```

APT returned its help output, confirming it is installed and functional. APT is the standard package manager for Debian-based Linux distributions and is used to install, update, and remove software.

---

## Task 2 — Install and Uninstall Suricata

### Install Suricata

```bash
sudo apt install suricata
```

APT resolved and downloaded all required dependencies, then installed Suricata 1:6.0.1-3+deb11u1.

### Verify installation

```bash
suricata
```

Suricata launched and displayed its help output — confirming successful installation.

### Uninstall Suricata

```bash
sudo apt remove suricata
```

APT removed Suricata and flagged 27 packages as no longer required. Freed ~6634 kB of disk space.

### Verify uninstallation

```bash
suricata
```

Output:
```
-bash: /usr/bin/suricata: No such file or directory
```

Suricata was successfully removed. The binary no longer exists on the system.

---

## Task 3 — Install tcpdump

```bash
sudo apt install tcpdump
```

APT installed tcpdump 4.99.0-2+deb11u1 — a command-line network traffic capture tool used extensively in security analysis. Package size: 466 kB.

---

## Task 4 — List Installed Applications

```bash
apt list --installed
```

Ran a full listing of installed packages to confirm the correct state:
- `tcpdump/oldstable,now 4.99.0-2+deb11u1 amd64 [installed]` — present ✅
- Suricata — not listed (successfully uninstalled) ✅

---

## Task 5 — Reinstall Suricata

```bash
sudo apt install suricata
```

Reinstalled Suricata (1:6.0.1-3+deb11u1). Confirmed via `apt list --installed` that both `suricata` and `tcpdump` are present.

---

## Key Takeaways

- `sudo apt install <package>` installs software and resolves dependencies automatically
- `sudo apt remove <package>` uninstalls software but may leave orphaned dependencies (use `sudo apt autoremove` to clean up)
- `apt list --installed` is a quick way to audit what software is on a system — useful for verifying tool availability or spotting unauthorized installs
- Understanding package management is essential for configuring and maintaining Linux-based security tools like Suricata, tcpdump, Wireshark, and others

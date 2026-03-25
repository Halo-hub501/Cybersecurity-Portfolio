# File Permissions in Linux

**Course:** Tools of the Trade: Linux and SQL (Course 4)
**Certificate:** Google Cybersecurity Professional Certificate
**Status:** ✅ Completed

---

## Project Description

As a security professional working with a research team, part of my role is to ensure users are authorized with the appropriate permissions to keep the system secure. In this project, I examined existing file and directory permissions within the `/home/researcher2/projects` directory to determine whether they matched the level of authorization that should be granted. Where permissions did not align with organizational policy, I used Linux commands to modify them and remove unauthorized access.

---

## Check File and Directory Details

I used the following command to list all contents of the `projects` directory, including hidden files, along with their permission strings:

```bash
researcher2@9e8bcde30f6f:~/projects$ ls -la
```

```
total 32
drwxr-xr-x 3 researcher2 research_team 4096 Mar 24 20:56 .
drwxr-xr-x 3 researcher2 research_team 4096 Mar 24 21:31 ..
-rw--w---- 1 researcher2 research_team   46 Mar 24 20:56 .project_x.txt
drwx--x--- 2 researcher2 research_team 4096 Mar 24 20:56 drafts
-rw-rw-rw- 1 researcher2 research_team   46 Mar 24 20:56 project_k.txt
-rw-r----- 1 researcher2 research_team   46 Mar 24 20:56 project_m.txt
-rw-rw-r-- 1 researcher2 research_team   46 Mar 24 20:56 project_r.txt
-rw-rw-r-- 1 researcher2 research_team   46 Mar 24 20:56 project_t.txt
```

The `ls` command with the `-la` option displays a detailed listing of all file contents and returns hidden files. The output indicates there is one subdirectory named `drafts`, one hidden file named `.project_x.txt`, and five other project files. The 10-character string in the first column represents the permissions set on each file or directory.

---

## Describe the Permissions String

The 10-character permission string can be deconstructed to determine who is authorized to access a file and what specific permissions they have. Each character represents the following:

- **1st character** — File type: `d` = directory, `-` = regular file
- **2nd–4th characters** — User (owner) permissions: `r` (read), `w` (write), `x` (execute), or `-` (not granted)
- **5th–7th characters** — Group permissions: `r` (read), `w` (write), `x` (execute), or `-` (not granted)
- **8th–10th characters** — Other permissions (all other system users): `r` (read), `w` (write), `x` (execute), or `-` (not granted)

**Example — `project_t.txt` (`-rw-rw-r--`):**

Since the first character is `-`, this indicates `project_t.txt` is a regular file, not a directory. The second, fifth, and eighth characters are all `r`, indicating that the user, group, and other all have read permissions. The third and sixth characters are `w`, indicating that only the user and group have write permissions. No one has execute permissions for this file.

---

## Change File Permissions

The organization determined that `other` should not have write access to any files. After reviewing the existing permissions, I identified that `project_k.txt` had write access granted to `other` (`-rw-rw-rw-`), which needed to be removed.

```bash
researcher2@9e8bcde30f6f:~/projects$ chmod o-w project_k.txt
researcher2@9e8bcde30f6f:~/projects$ ls -la
```

```
total 32
drwxr-xr-x 3 researcher2 research_team 4096 Mar 24 20:56 .
drwxr-xr-x 3 researcher2 research_team 4096 Mar 24 21:31 ..
-rw--w---- 1 researcher2 research_team   46 Mar 24 20:56 .project_x.txt
drwx--x--- 2 researcher2 research_team 4096 Mar 24 20:56 drafts
-rw-rw-r-- 1 researcher2 research_team   46 Mar 24 20:56 project_k.txt
-rw-r----- 1 researcher2 research_team   46 Mar 24 20:56 project_m.txt
-rw-rw-r-- 1 researcher2 research_team   46 Mar 24 20:56 project_r.txt
-rw-rw-r-- 1 researcher2 research_team   46 Mar 24 20:56 project_t.txt
```

The `chmod` command changes the permissions on files and directories. The first argument indicates what permissions should be changed, and the second argument specifies the file or directory. In this example, I removed write permissions from `other` for `project_k.txt` using `o-w`. After this, I used `ls -la` to verify the update — `project_k.txt` now shows `-rw-rw-r--`, confirming the change was applied correctly.

---

## Change File Permissions on a Hidden File

The research team recently archived `.project_x.txt`. No one should have write access to this file, but the user and group should retain read access. I knew `.project_x.txt` was a hidden file because its name begins with a period (`.`).

```bash
researcher2@9e8bcde30f6f:~/projects$ chmod u-w,g-w,g+r .project_x.txt
researcher2@9e8bcde30f6f:~/projects$ ls -la
```

```
total 32
drwxr-xr-x 3 researcher2 research_team 4096 Mar 24 20:56 .
drwxr-xr-x 3 researcher2 research_team 4096 Mar 24 21:31 ..
-r--r----- 1 researcher2 research_team   46 Mar 24 20:56 .project_x.txt
drwx--x--- 2 researcher2 research_team 4096 Mar 24 20:56 drafts
-rw-rw-r-- 1 researcher2 research_team   46 Mar 24 20:56 project_k.txt
-rw-r----- 1 researcher2 research_team   46 Mar 24 20:56 project_m.txt
-rw-rw-r-- 1 researcher2 research_team   46 Mar 24 20:56 project_r.txt
-rw-rw-r-- 1 researcher2 research_team   46 Mar 24 20:56 project_t.txt
```

In this example, I applied three permission changes in a single `chmod` command using comma-separated clauses. I removed write permissions from the user with `u-w`, removed write permissions from the group with `g-w`, and added read permissions to the group with `g+r`. The updated permission string `-r--r-----` confirms that neither the user nor the group can write to the file, while both retain read access.

---

## Change Directory Permissions

My organization requires that only the `researcher2` user has access to the `drafts` directory and its contents. This means the group should not have execute permissions on the directory, as execute on a directory controls the ability to enter it.

```bash
researcher2@9e8bcde30f6f:~/projects$ chmod g-x drafts
researcher2@9e8bcde30f6f:~/projects$ ls -la
```

```
total 32
drwxr-xr-x 3 researcher2 research_team 4096 Mar 24 20:56 .
drwxr-xr-x 3 researcher2 research_team 4096 Mar 24 21:31 ..
-r--r----- 1 researcher2 research_team   46 Mar 24 20:56 .project_x.txt
drwx------ 2 researcher2 research_team 4096 Mar 24 20:56 drafts
-rw-rw-r-- 1 researcher2 research_team   46 Mar 24 20:56 project_k.txt
-rw-r----- 1 researcher2 research_team   46 Mar 24 20:56 project_m.txt
-rw-rw-r-- 1 researcher2 research_team   46 Mar 24 20:56 project_r.txt
-rw-rw-r-- 1 researcher2 research_team   46 Mar 24 20:56 project_t.txt
```

The output shows the updated permission listing for the directory. Line 1 indicates the current directory (`projects`), and line 2 indicates the parent directory (`home`). Line 3 is the hidden file `.project_x.txt`. Line 4 is the `drafts` directory, now showing `drwx------`, meaning only `researcher2` has execute permissions. It was previously determined that the group had execute permissions (`drwx--x---`), so I used `chmod g-x` to remove them. The `researcher2` user already had execute permissions, so no changes were needed for the user.

---

## Summary

I updated multiple file and directory permissions to align with the authorization requirements set by my organization for the `/home/researcher2/projects` directory. I began by using `ls -la` to examine the current permissions, including hidden files, which informed all subsequent decisions. I then used the `chmod` command to remove unauthorized write access from `other` on `project_k.txt`, restrict write access and correct read access on the hidden file `.project_x.txt`, and remove group execute permissions from the `drafts` directory so that only the `researcher2` user retains access.

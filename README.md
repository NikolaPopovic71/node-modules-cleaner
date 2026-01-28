# Node Modules Cleaner

Two Python scripts to help you clean `node_modules` folders that consume gigabytes of disk space.

## 🎯 The Problem

`node_modules` folders are notorious for:
- **Consuming 200-500 MB per project** (or even more!)
- **Slowing down backups** - thousands of small files take forever to copy
- **Wasting disk space** - they can be regenerated anytime with `npm install`
- **Making file transfers painful** - large sizes and slow compression

## ✨ The Solution

Two simple Python scripts that clean your projects **locally and safely**:

1. **`clean_node_modules.py`** - Clean ZIP archives before storing/sharing
2. **`clean_directory.py`** - Clean existing directories on your disk

### Why Local Scripts Instead of a Web Service?

Read the full explanation in our blog post: [Why I Didn't Build a Web App](https://ponitech.pro/blog/clean-node-modules-locally)

**TL;DR:** Local scripts give you:
- ✅ No file size limits
- ✅ Complete privacy (code never leaves your machine)
- ✅ Zero security risks
- ✅ Instant processing
- ✅ Free forever

---

## 📦 Installation

### Requirements

- Python 3.6 or higher
- No external dependencies (uses only Python standard library)

### Download

**Option 1: Download individual scripts**

```bash
# Download both scripts
curl -O https://raw.githubusercontent.com/NikolaPopovic71/node-modules-cleaner/main/clean_node_modules.py
curl -O https://raw.githubusercontent.com/NikolaPopovic71/node-modules-cleaner/main/clean_directory.py
```

**Option 2: Clone the repository**

```bash
git clone https://github.com/NikolaPopovic71/node-modules-cleaner.git
cd node-modules-cleaner
```

**Option 3: Download ZIP**

Download the repository as a ZIP file from the green "Code" button above.

### Make Scripts Executable (Linux/Mac)

```bash
chmod +x clean_node_modules.py
chmod +x clean_directory.py
```

---

## 🚀 Usage

### Script 1: `clean_node_modules.py` - Clean ZIP Files

Perfect for cleaning project backups before archiving or sharing.

#### Basic Usage

```bash
# Clean a ZIP file (creates my_projects_cleaned.zip)
python clean_node_modules.py my_projects.zip

# Specify custom output name
python clean_node_modules.py old_projects.zip -o archived_projects.zip
```

#### Example Output

```
Input zip: my_projects.zip
Output zip: my_projects_cleaned.zip
Original size: 1250.45 MB

Extracting zip file...
Extraction complete.

Searching for node_modules folders...
Removing: /tmp/tmpxyz/react-app/node_modules (385.23 MB)
Removing: /tmp/tmpxyz/vue-project/node_modules (421.18 MB)
Removing: /tmp/tmpxyz/next-site/node_modules (298.67 MB)

Removed 3 node_modules folder(s)
Space freed: 1105.08 MB

Creating cleaned zip file...
Cleaned zip created: my_projects_cleaned.zip
New size: 145.37 MB
Size reduction: 1105.08 MB

✓ Cleaning completed successfully!
```

**Result: 88% size reduction!** 🎉

---

### Script 2: `clean_directory.py` - Clean Directories

Perfect for cleaning already-extracted project folders on your disk.

#### Basic Usage

```bash
# Preview what would be deleted (safe mode)
python clean_directory.py /path/to/projects --dry-run

# Actually delete node_modules folders
python clean_directory.py /path/to/projects
```

#### Example Output

```
Scanning directory: D:\Projects
Dry run mode: False

Found 5 node_modules folder(s):

  react-dashboard/node_modules
    Size: 234.56 MB
    Status: ✓ Removed

  old-portfolio/node_modules
    Size: 189.23 MB
    Status: ✓ Removed

  client-project/node_modules
    Size: 456.78 MB
    Status: ✓ Removed

Skipped 142 nested folder(s) (already removed with parent)

Removed 5 folder(s)
Total space freed: 784.91 MB

✓ Cleaning completed successfully!
```

---

## Real-World Use Cases

> **Note:** Linux/Mac users should use `python3`, Windows users should use `python`

### Use Case 1: Before Cloud Backup

**Linux/Mac:**
```bash
# Without cleaning
$ du -sh ~/Projects
8.5G    /Users/nikola/Projects

# Clean it
$ python3 clean_directory.py ~/Projects

# After cleaning
$ du -sh ~/Projects
1.2G    /Users/nikola/Projects
```

**Windows (PowerShell):**
```powershell
# Without cleaning
PS> (Get-ChildItem C:\Projects -Recurse | Measure-Object -Property Length -Sum).Sum / 1GB
8.5

# Clean it
PS> python clean_directory.py C:\Projects

# After cleaning
PS> (Get-ChildItem C:\Projects -Recurse | Measure-Object -Property Length -Sum).Sum / 1GB
1.2
```

**Upload time:** 2 hours → 15 minutes ⚡

### Use Case 2: Archiving Old Projects

**Linux/Mac:**
```bash
# Create archive
$ zip -r old_projects.zip ~/OldProjects

# Clean it
$ python3 clean_node_modules.py old_projects.zip

# Compare sizes
Old: 3.2GB
New: 280MB (91% smaller!)
```

**Windows (PowerShell):**
```powershell
# Create archive
PS> Compress-Archive -Path C:\OldProjects -DestinationPath old_projects.zip

# Clean it
PS> python clean_node_modules.py old_projects.zip

# Compare sizes
Old: 3.2GB
New: 280MB (91% smaller!)
```

### Use Case 3: Before Transferring to External Drive

**Linux/Mac:**
```bash
# Clean before copying
$ python3 clean_directory.py ~/Projects --dry-run
# Review what will be deleted

$ python3 clean_directory.py ~/Projects
# Copy to external drive (much faster!)
```

**Windows (PowerShell):**
```powershell
# Clean before copying
PS> python clean_directory.py C:\Projects --dry-run
# Review what will be deleted

PS> python clean_directory.py C:\Projects
# Copy to external drive (much faster!)
```

### Use Case 4: Disk Space Emergency

**Linux/Mac:**
```bash
# Your disk is full!
$ df -h
Filesystem      Size   Used  Avail Capacity
/dev/disk1     500G   495G    5G    99%

# Clean development folder
$ python3 clean_directory.py ~/Projects

# Check again
$ df -h
Filesystem      Size   Used  Avail Capacity
/dev/disk1     500G   488G   12G    98%
```

**Windows (PowerShell):**
```powershell
# Your disk is full!
PS> Get-PSDrive C | Select-Object Used,Free

Used          Free
----          ----
531914924032  5368709120

# Clean development folder
PS> python clean_directory.py C:\Projects

# Check again
PS> Get-PSDrive C | Select-Object Used,Free

Used          Free
----          ----
524288000000  12884901888
```

**Freed 7GB in 30 seconds** 🚀

---

## Performance Comparison

| Task | Web App | Local Script |
|------|---------|--------------|
| Upload 500MB zip | 5 minutes | N/A (already local) |
| Processing | Queued (2-10 min wait) | Instant start |
| Download cleaned file | 2 minutes | N/A (already local) |
| **Total time** | **~12 minutes** | **~30 seconds** |
| Security risks | Multiple | Zero |
| File size limit | 50MB typical | Unlimited |
| Privacy | Code on remote server | Never leaves your machine |

---

## Tips & Best Practices

### For Developers

1. **Always use `--dry-run` first** to verify what will be deleted
2. **Keep the original** until you confirm the cleaned version works
3. **Add to your workflow** — clean before every backup
4. **Create an alias** for quick access:

**Linux/Mac (add to ~/.bashrc or ~/.zshrc):**
```bash
alias clean-node='python3 ~/scripts/clean_directory.py'

# Usage
clean-node ~/Projects --dry-run
```

**Windows (add to PowerShell profile):**
```powershell
# First, find your profile location
PS> $PROFILE

# Create/edit it and add:
function Clean-Node {
    python C:\scripts\clean_directory.py $args
}

# Usage
Clean-Node C:\Projects --dry-run
```

5. **Integrate with backup scripts:**

**Linux/Mac (backup.sh):**
```bash
#!/bin/bash
# backup.sh

# Clean before backing up
python3 clean_directory.py ~/Projects

# Then backup
tar -czf projects_backup.tar.gz ~/Projects
```

**Windows (backup.ps1):**
```powershell
# backup.ps1

# Clean before backing up
python clean_directory.py C:\Projects

# Then backup
Compress-Archive -Path C:\Projects -DestinationPath projects_backup.zip
```

### Safety Checklist

- ✅ Your source code and `package.json` remain intact
- ✅ You can regenerate `node_modules` anytime with `npm install`
- ✅ No hidden files or configs are deleted
- ✅ Only folders named exactly "node_modules" are removed
- ✅ The script never modifies files, only removes folders

### What Gets Removed vs. What Stays

**Removed:**
- ✅ All `node_modules` folders (any depth)
- ✅ All dependencies inside them

**Preserved:**
- ✅ Your source code (`.js`, `.jsx`, `.ts`, `.tsx`)
- ✅ Configuration files (`package.json`, `tsconfig.json`, etc.)
- ✅ Environment files (`.env`, `.env.local`)
- ✅ Build output (`dist`, `build` folders)
- ✅ Everything else

---

## Troubleshooting

### "Permission denied" error

**Problem:** Can't delete some folders

**Linux/Mac Solutions:**
```bash
# Use sudo (be careful!)
sudo python3 clean_directory.py ~/Projects

# Or fix permissions first
chmod -R u+w ~/Projects
```

**Windows Solutions:**
```powershell
# Run PowerShell as Administrator
# Right-click PowerShell → "Run as Administrator"
PS> python clean_directory.py C:\Projects

# Or take ownership of the folder
PS> takeown /F C:\Projects /R /D Y
PS> icacls C:\Projects /grant %username%:F /T
```

### "File not found" error

**Problem:** Path doesn't exist

**Linux/Mac Solutions:**
```bash
# Use absolute path
python3 clean_directory.py /Users/nikola/Projects

# Or use quotes for paths with spaces
python3 clean_directory.py "/Users/nikola/My Projects"
```

**Windows Solutions:**
```powershell
# Use absolute path
python clean_directory.py C:\Users\nikola\Projects

# Or use quotes for paths with spaces
python clean_directory.py "C:\Users\nikola\My Projects"
```

### Script runs but nothing deleted

**Possible causes:**
1. No `node_modules` folders exist in that directory
2. Case sensitivity (Linux/Mac) — must be exactly "node_modules"
3. The folders are symlinks (not actual directories)

**Verify - Linux/Mac:**
```bash
# Find all node_modules folders manually
find ~/Projects -name "node_modules" -type d
```

**Verify - Windows (PowerShell):**
```powershell
# Find all node_modules folders manually
Get-ChildItem -Path C:\Projects -Filter "node_modules" -Recurse -Directory
```

### Very slow processing

**Cause:** Large number of files

**Solution:** This is normal! Processing 500,000 files takes time. The script shows progress for each folder.

---

## ❓ FAQ

### Q: Will this delete my source code?

**No!** Only folders named exactly `node_modules` are removed. Your source code, `package.json`, and all other files remain intact.

### Q: Can I recover node_modules after deletion?

**Yes!** Simply run:
```bash
npm install
# or
yarn install
```

### Q: What about nested node_modules?

The script intelligently handles nested `node_modules` folders. When a parent folder is deleted, nested ones are skipped to avoid errors.

### Q: Is it safe to use?

**Yes!** The scripts:
- Show exactly what will be deleted
- Offer a `--dry-run` mode for previewing
- Don't modify files, only remove `node_modules` folders
- Handle errors gracefully

### Q: Why not just use `find` or `rm` (Linux/Mac) or manual deletion (Windows)?

These scripts provide:
- ✅ Cross-platform compatibility (Windows, Linux, macOS)
- ✅ Space calculation before and after
- ✅ Progress reporting
- ✅ Safe handling of special characters in paths
- ✅ ZIP archive support
- ✅ Dry run mode

### Q: What's the typical space savings?

| Project Type | Typical Size | Savings |
|--------------|--------------|---------|
| Small (CRA) | 150-200 MB | ~180 MB |
| Medium (Next.js) | 300-400 MB | ~350 MB |
| Large (Nx monorepo) | 800-1200 MB | ~1000 MB |
| Enterprise | 1500+ MB | ~1500 MB |

**For 10 projects: 3-5 GB freed!** 💾

---

## Why This Approach Wins

### The Local-First Philosophy

Instead of adding complexity:
- ❌ Authentication systems
- ❌ Rate limiting
- ❌ Job queues
- ❌ File upload handling
- ❌ Security hardening
- ❌ Server monitoring
- ❌ Database for tracking
- ❌ CDN for downloads

We get:
- ✅ A simple Python script
- ✅ Zero infrastructure
- ✅ Complete privacy
- ✅ Unlimited file sizes
- ✅ Instant processing
- ✅ Zero security attack surface

### When Local Beats Cloud

Local-first is better when:
- Processing doesn't require server-side resources
- Privacy matters
- File sizes are large
- Processing is one-time or infrequent
- Security complexity outweighs convenience

Web services are better when:
- Collaboration is needed
- Access from any device is required
- Persistent storage is necessary
- Complex orchestration is involved

For cleaning `node_modules`? **Local wins every time.**

---

## License

MIT License — Free to use for any purpose. No attribution required.

---

## Final Thoughts

Sometimes the best solution is the simplest one. Instead of building a complex web service with authentication, security hardening, and infrastructure costs, a local script gives you:

- **More power** — No file size limits
- **More control** — See exactly what's happening
- **More privacy** — Your code never leaves your machine
- **More speed** — No network latency
- **Zero costs** — No servers to maintain

Save your `node_modules` cleaning for your local machine. It's faster, safer, and more efficient.

Start reclaiming your disk space today! 🚀

---

## Credits

Built with ❤️ by [ponITech](https://ponitech.pro)

Questions? Found a bug? [Get in touch!](mailto:office@ponitech.pro)
---

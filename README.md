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

## 📚 Real-World Use Cases

### Use Case 1: Before Cloud Backup

```bash
# Before cleaning
$ du -sh ~/Projects
8.5G    /Users/nikola/Projects

# Clean it
$ python clean_directory.py ~/Projects

# After cleaning
$ du -sh ~/Projects
1.2G    /Users/nikola/Projects
```

**Upload time: 2 hours → 15 minutes ⚡**

### Use Case 2: Archiving Old Projects

```bash
# Create archive
$ zip -r old_projects.zip ~/OldProjects

# Clean it
$ python clean_node_modules.py old_projects.zip

# Result
Old: 3.2GB
New: 280MB (91% smaller!)
```

### Use Case 3: Disk Space Emergency

```bash
# Your disk is full!
$ df -h
/dev/disk1     500G   495G    5G    99%

# Clean development folder
$ python clean_directory.py ~/Projects

# Check again
$ df -h
/dev/disk1     500G   488G   12G    98%
```

**Freed 7GB in 30 seconds!** 🚀

---

## 💡 Tips & Best Practices

### For Developers

1. **Always use `--dry-run` first** to verify what will be deleted
2. **Keep the original** until you confirm the cleaned version works
3. **Add to your workflow** - clean before every backup
4. **Create an alias** for quick access:

```bash
# Add to ~/.bashrc or ~/.zshrc
alias clean-node='python3 ~/scripts/clean_directory.py'

# Usage
clean-node ~/Projects --dry-run
```

5. **Integrate with backup scripts:**

```bash
#!/bin/bash
# backup.sh

# Clean before backing up
python3 clean_directory.py ~/Projects

# Then backup
tar -czf projects_backup.tar.gz ~/Projects
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

## 🔧 Command Reference

### `clean_node_modules.py`

```bash
python clean_node_modules.py <input_zip> [-o <output_zip>]
```

**Arguments:**
- `input_zip` - Path to the ZIP file to clean (required)
- `-o, --output` - Path for the output cleaned ZIP (optional, defaults to `input_cleaned.zip`)

### `clean_directory.py`

```bash
python clean_directory.py <directory> [--dry-run]
```

**Arguments:**
- `directory` - Path to the directory to clean (required)
- `--dry-run` - Preview what would be deleted without actually deleting (optional)

---

## 🐛 Troubleshooting

### "Permission denied" error

**Problem:** Can't delete some folders

**Solutions:**
```bash
# Linux/Mac: Use sudo (be careful!)
sudo python3 clean_directory.py ~/Projects

# Or fix permissions first
chmod -R u+w ~/Projects
```

### "File not found" error

**Problem:** Path doesn't exist

**Solutions:**
```bash
# Use absolute path
python3 clean_directory.py /Users/nikola/Projects

# Or use quotes for paths with spaces
python3 clean_directory.py "/Users/nikola/My Projects"
```

### Script runs but nothing deleted

**Possible causes:**
1. No `node_modules` folders exist in that directory
2. Case sensitivity (Linux/Mac) - must be exactly "node_modules"
3. The folders are symlinks (not actual directories)

**Verify:**
```bash
# Find all node_modules folders manually
find ~/Projects -name "node_modules" -type d
```

### Very slow processing

**Cause:** Large number of files (normal behavior)

**Solution:** Processing 500,000 files takes time. The script shows progress for each folder.

---

## 📊 Typical Space Savings

Based on real-world testing:

| Project Type | Typical node_modules Size | Savings per Project |
|--------------|---------------------------|---------------------|
| Small (Create React App) | 150-200 MB | ~180 MB |
| Medium (Next.js with deps) | 300-400 MB | ~350 MB |
| Large (Nx monorepo) | 800-1200 MB | ~1000 MB |
| Enterprise (micro-frontend) | 1500+ MB | ~1500 MB |

**For 10 typical projects: 3-5 GB freed** 💾

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### Development Setup

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**ponITech** - Full-stack web development services

- Website: [ponitech.pro](https://ponitech.pro)
- LinkedIn: [Your LinkedIn](https://linkedin.com/in/yourprofile)
- Twitter: [@yourhandle](https://twitter.com/yourhandle)

---

## 📖 Related Articles

- [Clean node_modules Locally — Why I Didn't Build a Web App](https://ponitech.pro/blog/clean-node-modules-locally)

---

## ⭐ Support

If you found this helpful, please consider:
- Giving it a star ⭐ on GitHub
- Sharing it with other developers
- Contributing improvements

---

## 🙏 Acknowledgments

- Thanks to the Node.js community for creating such a vibrant ecosystem
- Thanks to everyone who deals with massive `node_modules` folders daily
- Special thanks to all contributors

---

**Built with ❤️ by [ponITech](https://ponitech.pro)**

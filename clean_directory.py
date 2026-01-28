#!/usr/bin/env python3
"""
Clean node_modules folders from a directory.
Useful if you've already extracted your zip and just want to clean it.
"""
import shutil
from pathlib import Path
import argparse

def get_folder_size(folder_path):
    """Calculate total size of a folder in bytes."""
    total_size = 0
    try:
        for item in folder_path.rglob('*'):
            if item.is_file():
                total_size += item.stat().st_size
    except (PermissionError, OSError):
        pass
    return total_size

def clean_directory(directory_path, dry_run=False):
    """
    Remove all node_modules folders from a directory.
    
    Args:
        directory_path: Root directory to clean
        dry_run: If True, only show what would be deleted without actually deleting
    """
    directory = Path(directory_path)
    
    if not directory.exists():
        raise FileNotFoundError(f"Directory not found: {directory_path}")
    
    print(f"Scanning directory: {directory_path}")
    print(f"Dry run mode: {dry_run}\n")
    
    node_modules_folders = []
    
    # Find all node_modules directories
    for node_modules_path in directory.rglob('node_modules'):
        if node_modules_path.is_dir():
            node_modules_folders.append(node_modules_path)
    
    if not node_modules_folders:
        print("No node_modules folders found.")
        return 0, 0
    
    print(f"Found {len(node_modules_folders)} node_modules folder(s):\n")
    
    total_size = 0
    removed_count = 0
    skipped_count = 0
    
    for folder_path in node_modules_folders:
        # Check if folder still exists (might have been deleted as part of parent)
        if not folder_path.exists():
            skipped_count += 1
            continue
            
        folder_size = get_folder_size(folder_path)
        total_size += folder_size
        
        relative_path = folder_path.relative_to(directory)
        size_mb = folder_size / (1024*1024)
        
        print(f"  {relative_path}")
        print(f"    Size: {size_mb:.2f} MB")
        
        if not dry_run:
            try:
                if folder_path.exists():  # Double-check before deletion
                    shutil.rmtree(folder_path)
                    print("    Status: ✓ Removed")
                    removed_count += 1
                else:
                    print("    Status: ⊘ Already removed (nested)")
                    skipped_count += 1
            except Exception as e:
                print(f"    Status: ✗ Error: {e}")
        else:
            print("    Status: Would be removed")
            removed_count += 1
        
        print()
    
    if skipped_count > 0 and not dry_run:
        print(f"Skipped {skipped_count} nested folder(s) (already removed with parent)\n")
    
    print(f"{'Would remove' if dry_run else 'Removed'} {removed_count} folder(s)")
    print(f"Total space {'that would be' if dry_run else ''} freed: {total_size / (1024*1024):.2f} MB")
    
    return removed_count, total_size

def main():
    parser = argparse.ArgumentParser(
        description='Clean node_modules folders from a directory',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s /path/to/projects              # Clean all node_modules
  %(prog)s /path/to/projects --dry-run    # Preview what would be deleted
        """
    )
    
    parser.add_argument('directory', help='Path to the directory to clean')
    parser.add_argument('--dry-run', action='store_true', 
                       help='Show what would be deleted without actually deleting')
    
    args = parser.parse_args()
    
    try:
        clean_directory(args.directory, args.dry_run)
        
        if not args.dry_run:
            print("\n✓ Cleaning completed successfully!")
        else:
            print("\n✓ Dry run completed. Use without --dry-run to actually delete.")
    except Exception as e:
        print(f"\n✗ Error: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())
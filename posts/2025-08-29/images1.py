#!/usr/bin/env python3
from pathlib import Path

# === Settings ===
folder = Path(__file__).parent        # Script folder (one level above images/)
base_name = "Whistler"                # Base name for images and markdown
ext = ".jpeg"                         # Desired final extension (keep the dot)
images_subfolder = folder / "images"  # Expected images folder
output_md = images_subfolder / f"{base_name}.md"  # Markdown output file

def normalize_and_rename_images():
    """
    Find image files in images_subfolder, normalize names to:
    base_name + zero-padded number + ext
    Example: Whistler01.jpeg, Whistler02.jpeg ...
    """
    if not images_subfolder.exists():
        print(f"Error: {images_subfolder} does not exist.")
        return []

    # Collect only image files with given extension or common formats
    valid_exts = [".jpg", ".jpeg", ".png", ".gif", ".webp"]
    files = [f for f in images_subfolder.iterdir() if f.suffix.lower() in valid_exts]

    if not files:
        print("No images found.")
        return []

    # Sort by name
    files.sort()

    renamed_files = []
    for i, f in enumerate(files, start=1):
        new_name = f"{base_name}{i:02d}{ext}"
        new_path = f.with_name(new_name)
        if f != new_path:
            f.rename(new_path)
        renamed_files.append(new_path)

    print(f"Processed {len(renamed_files)} image(s).")
    return renamed_files

def generate_markdown(images):
    """
    Write Markdown file with one image per line, captions from filenames.
    """
    lines = []
    for img in images:
        label = img.stem  # e.g., Whistler01
        line = f'![{label}](images/{img.name}){{group="{base_name}"}}'
        lines.append(line)

    output_md.write_text("\n\n".join(lines), encoding="utf-8")
    print(f"Markdown written to {output_md}")

def main():
    images = normalize_and_rename_images()
    if images:
        generate_markdown(images)

if __name__ == "__main__":
    main()
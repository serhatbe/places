import os
import re

def update_categories_in_yaml(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file == "index.qmd":
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Replace 'British Columbia' with 'BC' in categories
                updated_content = re.sub(
                    r'(\s*-\s*)British Columbia',
                    r'\1BC',
                    content
                )
                
                # Save changes back to the file if any update is made
                if content != updated_content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(updated_content)
                    print(f'Updated: {file_path}')

# Replace 'posts' with the path to your posts directory
update_categories_in_yaml('posts')

import os
from bs4 import BeautifulSoup

def extract_title(file_path):
    """Extracts the title of an HTML file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            soup = BeautifulSoup(file, 'html.parser')
            title_tag = soup.title
            return title_tag.string.strip() if title_tag else "No Title"
    except Exception as e:
        print(f"Could not extract title from {file_path}: {e}")
        return "No Title"

def generate_file_list_html(directory, ul_class):
    list_items = ""

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, directory)
                title = extract_title(file_path)
                list_items += f'<li>\n<a href="{relative_path}">\n{title}\n</a>\n</li>\n'

    ul_content = f'<ul class="{ul_class}">\n{list_items}</ul>'

    # with open(output_file, 'w', encoding='utf-8') as file:
    #     file.write(ul_content)

    # print(f'HTML file "{output_file}" with <ul> element has been created successfully.')
    print(ul_content)

# Usage
directory_to_scan = 'content/mustawa5'  # Replace with the directory you want to scan
output_html_file = 'file_list.html'  # Replace with the desired output HTML file name
ul_class_name = 'arabic-text'  # Replace with the desired class name for the <ul>

generate_file_list_html(directory_to_scan, ul_class_name)

import os

blog_folder = 'blog'
placeholder = ''

try:
    # Get all .html files from the blog folder, sorted by most recently modified
    files = sorted(
        [f for f in os.listdir(blog_folder) if f.endswith('.html')],
        key=lambda f: os.path.getmtime(os.path.join(blog_folder, f)),
        reverse=True
    )
except FileNotFoundError:
    print(f"Error: The '{blog_folder}' directory was not found. Please create it.")
    exit()

# Build the HTML list of links
html_list = '<ul>\n'
for filename in files:
    # Create a nice display name from the filename
    display_name = ' '.join(word.capitalize() for word in filename.split('.')[0].split('-'))
    html_list += f'    <li><a href="{blog_folder}/{filename}">{display_name}</a></li>\n'
html_list += '</ul>'

# Read the homepage content
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the placeholder with the generated list
content = content.replace(placeholder, html_list)

# Write the updated content back to the homepage
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print(f"✅ Homepage updated successfully with {len(files)} prediction(s).")
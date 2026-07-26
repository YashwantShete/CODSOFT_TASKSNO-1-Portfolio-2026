import os
import re

template_file = os.path.join("portfolio_app", "templates", "index.html")

if os.path.exists(template_file):
    with open(template_file, "r", encoding="utf-8") as f:
        content = f.read()

    # Replace Windows backslashes in static links with forward slashes
    content = content.replace(r"\static\", "/static/")
    content = content.replace(r"/static\", "/static/")
    content = content.replace(r"\static/", "/static/")
    
    # Fix any remaining absolute paths starting with C: or drive letters
    content = re.sub(r'["\'][a-zA-Z]:[^\'"]*?[/\\]static[/\\]', '"/static/', content)
    content = content.replace("\\", "/")

    with open(template_file, "w", encoding="utf-8") as f:
        f.write(content)
    
    print("Successfully cleaned paths in portfolio_app/templates/index.html")
else:
    print("Template file not found")

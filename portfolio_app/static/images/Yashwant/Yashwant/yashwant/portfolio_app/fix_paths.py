import os

files = [
    r"c:\Users\tejas\OneDrive\Documents\New folder\portfolio_app\templates\index.html",
    r"c:\Users\tejas\OneDrive\Documents\New folder\portfolio_app\static\js\main.js",
    r"c:\Users\tejas\OneDrive\Documents\New folder\portfolio_app\static\css\style.css"
]

search1 = r"C:\Users\tejas\OneDrive\Documents\New folder\portfolio_app\static"
search2 = r"C:/Users/tejas/OneDrive/Documents/New folder/portfolio_app\static"

for f in files:
    if os.path.exists(f):
        with open(f, "r", encoding="utf-8") as file:
            content = file.read()
            
        modified_content = content.replace(search1, "/static")
        modified_content = modified_content.replace(search2, "/static")
        modified_content = modified_content.replace(r"C:\\Users\\tejas\\OneDrive\\Documents\\New folder\\portfolio_app\\static", "/static")
        
        if content != modified_content:
            with open(f, "w", encoding="utf-8") as file:
                file.write(modified_content)
            print(f"Fixed absolute paths in {os.path.basename(f)}")

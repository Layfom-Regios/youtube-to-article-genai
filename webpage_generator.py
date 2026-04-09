def generate_html(article):
    formatted_article = article.replace("\n", "<br>")

    return f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Article</title>

<style>
body {{
    font-family: Arial, sans-serif;
    max-width: 800px;
    margin: auto;
    padding: 20px;
    line-height: 1.6;
    background: #fafafa;
}}

h1, h2, h3 {{
    color: #333;
}}

code {{
    background: #eee;
    padding: 4px;
}}

pre {{
    background: #111;
    color: #0f0;
    padding: 10px;
    overflow-x: auto;
}}
</style>
</head>

<body>
{formatted_article}
</body>
</html>
"""
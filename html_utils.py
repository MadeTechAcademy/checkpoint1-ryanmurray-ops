from pathlib import Path
import textwrap

def save_duties_to_html(duties, file_path):
    
    html_content = textwrap.dedent("""\
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Duties</title>
            <link rel="stylesheet" href="css/styles.css">
        </head>
        <body>
        <ul>
    """)

    
    for duty in duties:
        html_content += f"<li>{duty}</li>\n"
    
    html_content += "</ul>\n</body>\n</html>"

    Path(file_path).write_text(html_content) 

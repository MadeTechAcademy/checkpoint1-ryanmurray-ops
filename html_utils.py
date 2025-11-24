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
        </head>
        <body>
    """)

    
    for duty in duties:
        html_content += f"<p>{duty}</p>\n"
    
    html_content += "</body>\n</html>"

    Path(file_path).write_text(html_content) 

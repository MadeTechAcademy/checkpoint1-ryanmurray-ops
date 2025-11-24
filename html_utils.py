from pathlib import Path

def save_duties_to_html(duties, file_path):
    content = "\n".join(duties)
    Path(file_path).write_text(content) 
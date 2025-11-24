from pathlib import Path

def save_duties_to_html(duties, file_path):
    Path(file_path).write_text("") # Create an empty file
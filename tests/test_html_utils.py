from pathlib import Path
from themes import duties
from html_utils import save_duties_to_html

def test_save_duties_to_html(tmp_path):
    html_file = tmp_path / "duties.html"
    save_duties_to_html(duties, html_file)
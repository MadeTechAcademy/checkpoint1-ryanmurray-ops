from pathlib import Path
from themes import duties


def test_html_file_path(tmp_path):
    html_file = tmp_path / "duties.html"
    save_duties_to_html(duties, html_file)
from pathlib import Path
from themes import duties
from html_utils import save_duties_to_html


def test_function_exists(tmp_path):
    html_file = tmp_path / "duties.html"
    save_duties_to_html(duties, html_file)

def test_file_exists(tmp_path):
    html_file = tmp_path / "duties.html"
    save_duties_to_html(duties, html_file)
    assert html_file.exists()

def test_file_contains_first_duty(tmp_path):
    html_file = tmp_path / "duties.html"
    save_duties_to_html(duties, html_file)
    content = html_file.read_text()
    assert duties[0] in content

def test_file_contains_all_duties(tmp_path):
    html_file = tmp_path / "duties.html"
    save_duties_to_html(duties, html_file)
    content = html_file.read_text()
    for duty in duties:
        assert duty in content
from pathlib import Path
from themes import Theme
from utilities.html_utils import save_duties_to_html


def test_function_exists(tmp_path):
    html_file = tmp_path / "duties.html"
    save_duties_to_html(Theme.all_duties, html_file)

def test_file_exists(tmp_path):
    html_file = tmp_path / "duties.html"
    save_duties_to_html(Theme.all_duties, html_file)
    assert html_file.exists()

def test_file_contains_first_duty(tmp_path):
    html_file = tmp_path / "duties.html"
    save_duties_to_html(Theme.all_duties, html_file)
    content = html_file.read_text()
    assert Theme.all_duties[0] in content

def test_file_contains_all_duties(tmp_path):
    html_file = tmp_path / "duties.html"
    save_duties_to_html(Theme.all_duties, html_file)
    content = html_file.read_text()
    for duty in Theme.all_duties:
        assert duty in content

def test_full_html_boilerplate(tmp_path):
    html_file = tmp_path / "duties.html"
    save_duties_to_html(Theme.all_duties, html_file)
    content = html_file.read_text()
    assert "<!DOCTYPE html>" in content
    assert "<html" in content
    assert "<head>" in content
    assert "<meta charset=" in content
    assert "<title>" in content
    assert "<body>" in content
    assert "</body>" in content
    assert "</html>" in content

def test_html_uses_unordered_list(tmp_path):
    html_file = tmp_path / "duties.html"
    save_duties_to_html(Theme.all_duties, html_file)
    content = html_file.read_text()

    # Expect <ul> and at least one <li> to be present
    assert "<ul>" in content
    assert "</ul>" in content
    assert "<li>" in content
    assert "</li>" in content

def test_html_links_external_css(tmp_path):
    html_file = tmp_path / "duties.html"
    save_duties_to_html(Theme.all_duties, html_file)
    content = html_file.read_text()
    assert 'href="css/styles.css"' in content

from pathlib import Path
from themes import duties
from utilities.cli_utils import generate_html

def test_generate_html_create_file(tmp_path):
    output_file = tmp_path / "duties.html"
    generate_html(duties, output_file)

    assert output_file.exists()

def test_generate_html_file_contains_first_duty(tmp_path):
    output_file = tmp_path / "duties.html"
    generate_html(duties, output_file)
    content = output_file.read_text()
    assert duties[0] in content 

def test_generate_html_file_contains_all_duties(tmp_path):
    output_file = tmp_path / "duties.html"
    generate_html(duties, output_file)
    content = output_file.read_text()
    for duty in duties:
        assert duty in content

def test_generate_html_returns_correct_file_path(tmp_path):
    output_file = tmp_path / "duties.html"
    result = generate_html(duties, output_file)
    assert result == output_file
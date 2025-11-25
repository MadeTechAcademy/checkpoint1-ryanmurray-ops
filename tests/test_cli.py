from pathlib import Path
from cli import get_prompt
from cli import main

def test_prompt_text():
    prompt = get_prompt()
    assert "Welcome to apprentice themes!" in prompt
    assert "Press (1) to list all the duties" in prompt
    assert "Press (2) to generate an HTML file of duties" in prompt

def test_main_accepts_choice_parameter():
    main(1)

def test_main_option_2_generates_html():
    main("2")
    output_file = "duties.html"
    assert Path(output_file).exists()

def test_prompt_text_includes_theme_option():
    prompt = get_prompt()
    assert "Press (3) to view duties by theme" in prompt

def test_main_option_3_prints_themes(capsys):
    main("3")
    captured = capsys.readouterr()
    assert "Bootcamp" in captured.out
    assert "Automate!" in captured.out 






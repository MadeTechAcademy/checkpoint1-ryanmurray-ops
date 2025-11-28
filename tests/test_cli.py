from pathlib import Path
from cli import get_prompt, main
from standard_cli import StandardRenderer
from unittest.mock import patch
from utilities.cli_utils import get_theme_choice, get_main_choice

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
    main("3", theme_number=1)
    captured = capsys.readouterr()
    assert "Bootcamp" in captured.out
    assert "Automate!" in captured.out 

def test_main_option_3_generates_html():
    main("3", theme_number=1)
    output_file = "bootcamp.html"
    assert Path(output_file).exists()

def test_main_option_1_prints_duties_via_renderer(capsys):
    renderer = StandardRenderer()
    main(choice="1", renderer=renderer)
    captured = capsys.readouterr()
    assert "Script and code in at least one general purpose language" in captured.out
    assert "Initiate and facilitate knowledge sharing" in captured.out

def test_main_option_2_uses_renderer(capsys):
    renderer = StandardRenderer()
    main(choice="2", renderer=renderer)
    captured = capsys.readouterr()
    assert "Duties saved to duties.html" in captured.out

def test_main_option_3_uses_renderer(capsys):
    renderer = StandardRenderer()
    main(choice="3", theme_number=1, renderer=renderer)
    captured = capsys.readouterr()
    assert "Theme 'Bootcamp' saved to" in captured.out
    assert "Duties in 'Bootcamp':" in captured.out
    assert "Script and code in at least one general purpose language" in captured.out

def test_main_invalid_option_choice(capsys):
    main(choice="99")
    captured = capsys.readouterr()
    assert "Invalid choice, please select 1, 2 or 3" in captured.out

def test_get_theme_choice_reterns_integer():
    renderer = StandardRenderer()
    with patch("builtins.input", return_value="1"):
        choice = get_theme_choice(renderer)
    assert choice == 1

def test_get_theme_choice_invalid_then_valid(capsys):
    renderer = StandardRenderer()
    with patch("builtins.input", side_effect=["99", "2"]):
        choice = get_theme_choice(renderer)

    captured = capsys.readouterr()
    assert "Invalid theme number" in captured.out
    assert choice == 2

def test_get_main_choice_returns_valid_integer():
    renderer = StandardRenderer()
    with patch("builtins.input", return_value="2"):
        choice = get_main_choice(renderer)
    assert choice == 2

def test_get_main_choice_invalid_then_valid(capsys):
    renderer = StandardRenderer()
    with patch("builtins.input", side_effect=["99", "2"]):
        choice = get_main_choice(renderer)

    captured = capsys.readouterr()
    assert "Invalid choice" in captured.out
    assert choice == 2

def test_launcher_standard_renderer_prints_main_menu(capsys):
        with patch("builtins.input", return_value="2"):
            main()
        
        captured = capsys.readouterr()
        assert "Press (1) to list all duties" in captured.out
        assert "Press (2) to generate an HTML file of duties" in captured.out
        assert "ress (3) to view duties by theme" in captureed.out
        








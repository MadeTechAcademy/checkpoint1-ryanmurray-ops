from cli import get_prompt
from cli import main

def test_prompt_text():
    prompt = get_prompt()
    assert "Welcome to apprentice themes!" in prompt
    assert "Press (1) to list all the duties" in prompt
    assert "Press (2) to generate an HTML file of duties" in prompt

def test_main_accepts_choice_parameter():
    main(1)

def test_main_option_2_generates_html(tmp_path):
    output_file = tmp_path / "duties.html"
    main(("2", output_file))
    assert output_file.exists()

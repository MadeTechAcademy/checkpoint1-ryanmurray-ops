from launcher import select_renderer, launch_selected_terminal
from rich_cli import RichRenderer
from standard_cli import StandardRenderer
from unittest.mock import patch

def test_select_renderer_returns_rich_renderer():
    renderer = select_renderer(choice="1")
    assert isinstance(renderer, RichRenderer)

def test_select_renderer_returns_standard_renderer():
    renderer = select_renderer(choice="2")
    assert isinstance(renderer, StandardRenderer)

def test_launch_selected_terminal_uses_standard_renderer(capsys):
    launch_selected_terminal(choice="1", renderer_choice="2")
    captured = capsys.readouterr().out
    assert "Script and code in at least one general purpose language" in captured

def test_launch_selected_terminal_uses_rich_renderer(capsys):
    launch_selected_terminal(choice="1", renderer_choice="1")
    captured = capsys.readouterr().out
    assert "Script and code in at least one general purpose language" in captured
    assert "Initiate and facilitate knowledge sharing" in captured

def test_launch_selected_terminal_invalid_choice(capsys):
    launch_selected_terminal(choice="1", renderer_choice="99")
    captured = capsys.readouterr().out
    assert "Invalid choice, please select 1 or 2" in captured

def test_launch_selected_terminal_with_user_input_rich(capsys):
    with patch("builtins.input", return_value="1"):
        launch_selected_terminal(choice=None, renderer_choice=None)
    captured = capsys.readouterr().out
    assert "Script and code in at least one general purpose language" in captured
    
def test_launcher_exit_option(capsys):
    with patch("builtins.input", return_value="3"):
        launch_selected_terminal(choice=None, renderer_choice=None)

        captured = capsys.readouterr().out
        assert "Exiting Program... Goodbye!" in captured

def test_launcher_loops_until_valid_renderer(capsys):
    from launcher import launch_selected_terminal
    from unittest.mock import patch

    # First input invalid "5", second input valid "2"
    with patch("builtins.input", side_effect=["5", "2"]):
        launch_selected_terminal(choice=None)
    
    captured = capsys.readouterr().out

    # Assert invalid choice message appears
    assert "Invalid choice" in captured

    # Assert it prompts for input again
    assert "Please Enter your preferred terminal" in captured


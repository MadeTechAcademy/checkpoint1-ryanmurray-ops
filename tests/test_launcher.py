from launcher import select_renderer
from rich_cli import RichRenderer
from cli import StandardRenderer

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

from launcher import select_renderer
from rich_cli import RichRenderer
from cli import StandardRenderer

def test_select_renderer_returns_rich_renderer():
    renderer = select_renderer(choice="1")
    assert isinstance(renderer, RichRenderer)

def test_select_renderer_returns_standard_renderer():
    renderer = select_renderer(choice="2")
    assert isinstance(renderer, StandardRenderer)

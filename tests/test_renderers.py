from cli import main, StandardRenderer
from rich_cli import RichRenderer

def test_standard_renderer_print():
    renderer = StandardRenderer()
    renderer.print("Hello")

def test_rich_renderer_print():
    renderer = RichRenderer()
    renderer.print("Hello", style="bold green")

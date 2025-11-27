from cli import main
from rich_cli import RichRenderer
from standard_cli import StandardRenderer

def test_standard_renderer_print():
    renderer = StandardRenderer()
    renderer.print("Hello")

def test_rich_renderer_print():
    renderer = RichRenderer()
    renderer.print("Hello", style="bold green")

from cli import StandardRenderer
from rich_cli import RichRenderer

def test_standard_renderer_print():
    renderer = StandardRenderer()
    renderer.print("Hello")

def test_rich_renderer_print():
    renderer = RichRenderer()
    renderer.print("Hello", style="bold green")

def test_main_prints_duties_via_renderer(capsys):
    renderer = StandardRenderer()
    main(renderer=renderer, choice="1")
    captured = capsys.readouterr
    assert "Script and code in at least one general purpose language" in captured.out
    assert "Initiate and facilitate knowledge sharing" in captured out

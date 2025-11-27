from rich.console import Console

console = Console()

class RichRenderer:
    def print(self, text, style=None):
        if style:
            console.print(text, style=style)
        else:
            console.print(text)
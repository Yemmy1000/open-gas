
from rich.console import Console
# from rich.markdown import Markdown
# from rich import print

from IPython.display import display
from IPython.display import Markdown

class DisplayScript:

    def hdisplay(self, header):
        console = Console()
        markdown_head = Markdown(header)
        console.print(markdown_head)

    def tdisplay(self, text):
        console = Console()
        markdown_text = Markdown(text)
        console.print(markdown_text)
from rich.console import Console
from rich.table import Table
from rich import box

def Display_Table(data):
    fields, *data = data

    console = Console()
    table = Table(show_header=True, show_lines=True, box = box.SQUARE_DOUBLE_HEAD)

    for field in fields:
        table.add_column(field, justify='center')

    for row in data: 
        table.add_row(*row)
        
    console.print(table)
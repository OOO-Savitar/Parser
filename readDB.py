import sqlite3

from rich.table import Table
from rich.console import Console

console = Console()


def Make_Table(results):
    table = Table(show_header=True, header_style="bold magenta")

    table.add_column("Title", style="dim", width=16)
    table.add_column("Price")
    table.add_column("Property")
    table.add_column("Image Link")
    table.add_column("Product Link")

    for line in results:
        table.add_row(str(line[0]), str(line[1]), str(line[2]), str(line[3]))

    console.print(table)


def Read():
    conn = sqlite3.connect('myDatabase.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Cards;")
    all_results = cursor.fetchall()
    return all_results


def main():
    all_results = Read()
    Make_Table(all_results)

if __name__ == '__main__':
    main()
#!/usr/bin/env python3
import requests
import rich
from rich.align import Align
from rich.table import Table
from rich.box import SIMPLE, SQUARE, MINIMAL, ASCII, ROUNDED, HEAVY, DOUBLE, HORIZONTALS
from rich.console import Console, Group
from rich.panel import Panel

crypto = open('currencies.txt', 'r')
allCrypto = crypto.read().splitlines()
crypto.close()

crypto_string = ",".join(allCrypto)
    # https://api.coingecko.com/api/v3/simple/price?ids=<список монет>&vs_currencies=usdt
url = f'https://api.coingecko.com/api/v3/simple/price?ids={crypto_string}&vs_currencies=usd'
response = requests.get(url)
data = response.json() # get json info

# beatifull otput in console with rich
from rich.console import Console
console = Console()
from rich.table import Table

table = Table(title="", box=ROUNDED)

# Add columns to the table with optional styles
table.add_column("currencies", justify="center" )  
table.add_column("prices (USD)", justify="center" )             

# Loop through each item in the data dictionary
for coin, price_info in data.items():
    # Get the price in USD for the current coin
    price = price_info.get("usd") 

    # Add a new row to the table with:
    # - coin name capitalized (e.g. 'bitcoin' -> 'Bitcoin')
    # - price formatted as a string with a dollar sign
    table.add_row(coin.capitalize(), f"${price}")
    


console = Console()
ascii_art = """
⠀⠀⠀⠀⣿⡇⠀⢸⣿⡇⠀⠀⠀⠀
⠸⠿⣿⣿⣿⡿⠿⠿⣿⣿⣿⣶⣄⠀
⠀⠀⢸⣿⣿⡇⠀⠀⠀⠈⣿⣿⣿⠀
⠀⠀⢸⣿⣿⡇⠀⠀⢀⣠⣿⣿⠟⠀
⠀⠀⢸⣿⣿⡿⠿⠿⠿⣿⣿⣥⣄⠀
⠀⠀⢸⣿⣿⡇⠀⠀⠀⠀⢻⣿⣿⣧
⠀⠀⢸⣿⣿⡇⠀⠀⠀⠀⣼⣿⣿⣿
⢰⣶⣿⣿⣿⣷⣶⣶⣾⣿⣿⠿⠛⠁
⠀⠀⠀⠀⣿⡇⠀⢸⣿⡇⠀⠀⠀⠀

"""



content = Group(
    Align.center(table),
    Align.center(ascii_art)
)



panel = Panel(content, title="Crypto prices", expand=False)

# printing it by center
console.print(Align.center(panel))

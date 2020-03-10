from tkinter import *
import requests
import json

import os
x = os.path.abspath("C:/Users/Prashant/Desktop/API/coin.ico")

pycrypto = Tk()
pycrypto.title("My Crypto Portfolio")
pycrypto.iconbitmap(x)

def font_color(amount):
    if amount > 0:
        return "green"
    else:
        return "red"
    

def my_portfolio():
    api_request = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=100&convert=USD&CMC_PRO_API_KEY=985943cb-9119-4856-822d-7aeac34c4b32")
    api = json.loads(api_request.content)
    coins = [              # Coins purchesed
        {
            "symbol" : "BTC",
            "amount_owned" : 2,
            "price_per_coin" : 3200
        },
        {
            "symbol" : "ETH",
            "amount_owned" : 100,
            "price_per_coin" : 222
        },
        {
            "symbol" : "LTC",
            "amount_owned" : 75,
            "price_per_coin" : 37.15
        }
    ]
    coin_row = 1

    c = 0
    total_current_value = 0
    total_spend = 0
    for i in range(0,100):
        for coin in coins:
            if api["data"][i]["symbol"] == coin["symbol"]:
                total_paid = coin["amount_owned"] * coin["price_per_coin"]
                current_value = coin["amount_owned"] * api["data"][i]["quote"]["USD"]["price"]
                pl_percoin = api["data"][i]["quote"]["USD"]["price"] - coin["price_per_coin"]
                total_pl_coin = pl_percoin * coin["amount_owned"]

                c = c + total_pl_coin
                total_current_value = total_current_value + current_value
                total_spend = total_spend + total_paid

                Name = Label(pycrypto, text = api["data"][i]["symbol"], bg = "#c4ccc8",fg = "black", font = "Lato 12 ", padx = "2", pady = "2", borderwidth = 2, relief = "groove")
                Name.grid(row= coin_row,column =0, sticky=N+S+E+W)

                price = Label(pycrypto, text = "${0:.2f}".format(api["data"][i]["quote"]["USD"]["price"]), bg = "#c4ccc8",fg = "black", font = "Lato 12 ", padx = "2", pady = "2", borderwidth = 2, relief = "groove")
                price.grid(row= coin_row,column =1, sticky=N+S+E+W)

                no_coins = Label(pycrypto, text = coin["amount_owned"], bg = "#c4ccc8",fg = "black", font = "Lato 12 ", padx = "2", pady = "2", borderwidth = 2, relief = "groove")
                no_coins.grid(row= coin_row,column =2, sticky=N+S+E+W)

                amount_paid = Label(pycrypto, text = "${0:.2f}".format(total_paid), bg = "#c4ccc8",fg = "black", font = "Lato 12 ", padx = "2", pady = "2", borderwidth = 2, relief = "groove")
                amount_paid.grid(row= coin_row,column =3, sticky=N+S+E+W)

                current_val = Label(pycrypto, text = "${0:.2f}".format(current_value), bg = "#c4ccc8",fg = "black", font = "Lato 12 ", padx = "2", pady = "2", borderwidth = 2, relief = "groove")
                current_val.grid(row= coin_row,column =4, sticky=N+S+E+W)

                pl_coin = Label(pycrypto, text = "${0:.2f}".format(pl_percoin), bg = "#c4ccc8",fg = font_color(float("{0:.2f}".format(pl_percoin))), font = "Lato 12 ", padx = "2", pady = "2", borderwidth = 2, relief = "groove")
                pl_coin.grid(row= coin_row,column =5, sticky=N+S+E+W)

                total_pl = Label(pycrypto, text = "${0:.2f}".format(total_pl_coin), bg = "#c4ccc8",fg = font_color(float("{0:.2f}".format(total_pl_coin))), font = "Lato 12 ", padx = "2", pady = "2", borderwidth = 2, relief = "groove")
                total_pl.grid(row = coin_row,column =6, sticky=N+S+E+W)

                coin_row = coin_row + 1
                
                total_sp = Label(pycrypto, text = "${0:.2f}".format(total_spend), bg = "#c4ccc8",fg = "black", font = "Lato 12 ", padx = "2", pady = "2", borderwidth = 2, relief = "groove")
                total_sp.grid(row = coin_row,column =3, sticky=N+S+E+W)
                
                total_cv = Label(pycrypto, text = "${0:.2f}".format(total_current_value), bg = "#c4ccc8",fg = "black", font = "Lato 12 ", padx = "2", pady = "2", borderwidth = 2, relief = "groove")
                total_cv.grid(row = coin_row,column =4, sticky=N+S+E+W)
                
                total_pl = Label(pycrypto, text = "${0:.2f}".format(c), bg = "#c4ccc8",fg = "black", font = "Lato 12 ", padx = "2", pady = "2", borderwidth = 2, relief = "groove")
                total_pl.grid(row = coin_row,column =6, sticky=N+S+E+W)
                
                #api =""
                
                update = Button(pycrypto, text = 'Update', bg = "#01086b",fg = "white", font = "Lato 12 ", padx = "2", pady = "2", borderwidth = 2, relief = "groove")
                update.grid(row = coin_row + 1 ,column =6, sticky=N+S+E+W)
                

if __name__ == '__main__':

    Name = Label(pycrypto, text = "Coin Name", bg = "#01086b",fg = "#f2e4e4", font = "Lato 12 bold", padx = "5", pady = "5", borderwidth = 2, relief = "groove")
    Name.grid(row= 0,column =0, sticky=N+S+E+W)

    price = Label(pycrypto, text = "Price", bg = "#01086b",fg = "#f2e4e4", font = "Lato 12 bold", padx = "5", pady = "5", borderwidth = 2, relief = "groove")
    price.grid(row= 0,column =1, sticky=N+S+E+W)

    no_coins = Label(pycrypto, text = "Coin Owned", bg = "#01086b",fg = "#f2e4e4", font = "Lato 12 bold", padx = "5", pady = "5", borderwidth = 2, relief = "groove")
    no_coins.grid(row= 0,column =2, sticky=N+S+E+W)

    amount_paid = Label(pycrypto, text = "Total anount paid", bg = "#01086b",fg = "#f2e4e4", font = "Lato 12 bold", padx = "5", pady = "5", borderwidth = 2, relief = "groove")
    amount_paid.grid(row= 0,column =3, sticky=N+S+E+W)

    current_val = Label(pycrypto, text = "Currect Value", bg = "#01086b",fg = "#f2e4e4", font = "Lato 12 bold", padx = "5", pady = "5", borderwidth = 2, relief = "groove")
    current_val.grid(row= 0,column =4, sticky=N+S+E+W)

    pl_coin = Label(pycrypto, text = "P/L per Coin", bg = "#01086b",fg = "#f2e4e4", font = "Lato 12 bold", padx = "5", pady = "5", borderwidth = 2, relief = "groove")
    pl_coin.grid(row= 0,column =5, sticky=N+S+E+W)

    totalpl = Label(pycrypto, text = "Total P/L with Coin", bg = "#01086b",fg = "#f2e4e4", font = "Lato 12 bold", padx = "5", pady = "5", borderwidth = 2, relief = "groove")
    totalpl.grid(row = 0,column =6, sticky=N+S+E+W)

    my_portfolio()

    pycrypto.mainloop()
    print("Program Completed")

stock_sold_today = 20
total_store_stock = 100

def stock_check():
    remaining_stock = total_store_stock - stock_sold_today
    print(f"{remaining_stock} units of stock remain")


stock_check()
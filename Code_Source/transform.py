from read import raw_transaction_list
from classes import Raw_Transaction, Transaction, Raw_Basket, Basket
from datetime import date

clean_transaction_list = []
raw_basket_list = []
clean_basket_list =[]

def get_date():
    today = date.today()
    d = today.strftime("%m/%d/%y")
    return(d)
    
def clean_transactions():
    for raw_transaction in raw_transaction_list:
        id_number = raw_transaction.id_number
        split_date_and_time= raw_transaction.date.split()
        raw_date = split_date_and_time[0]
        raw_time = split_date_and_time [1]
        day, month, year = f"{raw_date}".split('/')
        new_date = f"{month}-{day}-{year}"
        clean_date = f"{new_date} {raw_time}"
        day = get_date()
        location = raw_transaction.location
        abbreviation = location[:4].upper() 
        customer_name = raw_transaction.customer_name
        first_name = customer_name.split()[0]
        total = float(raw_transaction.pay_amount)
        basket = raw_transaction.basket
        identification = f"{day}-{abbreviation}-{id_number}"
        clean_transaction = Transaction(unique_id = identification, 
                                        date = clean_date, 
                                        location = location, 
                                        first_name= first_name, 
                                        total= total,
                                        basket = basket)
        clean_transaction_list.append(clean_transaction)
    return clean_transaction_list

def update_raw_basket():
    for transaction in clean_transaction_list:
        transaction_id = transaction.unique_id
        basket = transaction.basket.replace("\"", "")
        items = basket.split(",")
        for item in items:
            combined_basket = Raw_Basket(transaction_id = transaction_id, basket_items = item)
            raw_basket_list.append(combined_basket)
    return raw_basket_list
          
def clean_basket_items():
    for sale in raw_basket_list:
        identifier = sale.transaction_id
        order = sale.basket_items
        item, cost = order.rsplit("-", 1)
        basket_item = Basket (trans_id = identifier,
                              item = item,
                              cost = cost)
        clean_basket_list.append(basket_item)
    return clean_basket_list
        
       
        
  
    #         yield raw_basket
    # return raw_basket_list
    
    #       baskets = []
    # for sale in basket.strip('"').split(', '):
    #     item, cost = sale.rsplit(' - ', 1)
    #     baskets.append(Basket(item=item, cost=cost))
    # return baskets
        
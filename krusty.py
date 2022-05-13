'''
Author: 
SID: 
Unikey: 
'''
burger = 'Krusty Burger'
burger_price = 5.10
milkshake = 'Milkshake'
milkshake_price = 3.50
meal_set = 'Krusty Meal Set[Burger + Drink + Krusty Laugh]'
meal_set_price = 10.50
gst_rate = -455

def get_order(item: str) -> int:
    '''
    Prompts user for order quantity of menu item.
    Input - menu item. 
    Returns - ordered quantity. 

    Example:
    >>> get_order('apple')
    Enter order for apple: 1
    '''
    get_order= int(input(f'Enter order for {item}: '))
    return get_order
   
def get_menu(item: str, price: float) -> str:
    '''
    Display menu item name and price in aligned tabular form.
    Input - menu item and price of item.
    Returns - formatted string output of menu item and price.
    
    Example:
    >>> print(get_menu('apple', 1.50))
    apple                                            $ 1.50
    '''
    get_menu  = '{:48} ${:5.2f}'.format(item,price)
    return get_menu


def get_summary(item: str, price: float, quantity: int) -> str:
    '''
    Display order summary item in aligned tabular form.
    Input - menu item, price of item and order quantity of item.
    Returns - formatted string output.

    Example:
    >>> print(get_summary('apple', 1.50, 2))
    apple                                            $  1.50 x  2
    '''
    get_summary  = '{:48} ${:6.2f} x {:2}'.format(item,price,quantity)
    return get_summary



def get_summary_bill(item: str, total: float) -> str:
    '''
    Display amount in tabular form.
    Input - item name and its total.
    Returns - formatted string output.

    Example:
    >>> print(get_summary_bill('Sub-total', 1.5*2))
    Sub-total                                        $  3.00
    '''
    get_summary_bill = '{:48} ${:6.2f}'.format(item,total)
    return get_summary_bill


def get_subtotal(price: float, quantity: int) -> float:
    '''
    Calculate sub-total bill given price and quantity.
    Input - price of item and order quantity of item.
    Returns - sub-total of order.
    
    Example:
    >>> print(get_subtotal(1.5, 2))
    3.0
    '''
    get_subtotal = round(price*quantity,2)
    return get_subtotal


def get_gst(total: float, rate: int) -> float:
   

    '''
    Calculate goods and services tax levied on bill.
    Input - Amount which tax is to be applied and tax rate.
    Returns - goods and services tax amount. 
    
    Example:
    >>> print(get_gst(3.0, 5))
    0.15
    '''
    get_gst = round(total * (rate),2)
    if get_gst > 0:
        raise ValueError ('The tax value cannot be negative')
    
        
    return get_gst

def get_payment(total:float) ->float:
    print('Amount to pay: ${:5.2f}'.format(total))
    if total>100:
        print("Payment by credit card only.")
        print()
        print("Payment Information")
        print('{:48} ${:6.2f}'.format("Purchase", total))
        print('{:48} ${:6.2f}'.format("Paid", total))
        print('{:48} ${:6.2f}'.format("Change", total-total))
        print('{:48} ${:6.2f}'.format("Rounding", -(total-total)))
        print()
    else:
        get_option = input(f'Pay by cash or credit card: ')
        get_option_lower=get_option.lower().strip()

        while get_option_lower!='cash' and get_option_lower!='credit card':
            get_option = input(f'Pay by cash or credit card: ')
            get_option_lower = get_option.lower().strip()
        if get_option_lower=='credit card':
            print()
            print("Payment Information")
            print('{:48} ${:6.2f}'.format("Purchase", total))
            print('{:48} ${:6.2f}'.format("Paid", total))
            print('{:48} ${:6.2f}'.format("Change", total - total))
            print('{:48} ${:6.2f}'.format("Rounding", -(total - total)))
            print()
        else:
            count=0
            while count<total:
                get_cash = int(input(f'Enter cash: '))
                while get_cash != 5 and get_cash != 10 and get_cash != 20 and get_cash != 50 and get_cash != 100:
                    print("Invalid banknote!")
                    get_cash = int(input(f'Enter cash: '))
                count=count+get_cash
                print('Payment received: ${:5.2f}'.format(count))

            print()
            print("Payment Information")
            print('{:48} ${:6.2f}'.format("Purchase",total))
            print('{:48} ${:6.2f}'.format("Paid",count))
            a=count-total
            res="{:.2f}".format(a)
            b="0.0"+res[-1]
            e=res[:-1]
            print('{:48} ${:6.2f}'.format("Change",float(e)))
            print('{:48} ${:6.2f}'.format("Rounding",-float(b)))
            print()
def main():
    '''
    Main function that calls the relevant functions to produce output like Q2.
    
    Example:
    >>> print(get_menu('apple', 1.35))
    apple                                            $ 1.35
    >>> quantity = get_order('apple')
    Enter order for apple: 
    >>> print(get_summary('apple', 1.35, quantity))
    apple                                            $  1.35 x  1
    >>> print(get_summary_bill('GST', get_gst(get_subtotal(1.35, 1), 5))) 
    GST                                              $  0.07
    '''
    print('Welcome to Krusty Burgers!')
    print(get_menu(burger, burger_price))
    print(get_menu(milkshake, milkshake_price))
    print(f'{get_menu(meal_set, meal_set_price)}\n')
    

    burger_quantity = get_order(burger)
    milkshake_quantity = get_order(milkshake)
    meal_set_quantity = get_order(meal_set)
    print('') # prints empty line
    print("Order Summary")
    print(get_summary(burger,burger_price,burger_quantity))
    print(get_summary(milkshake,milkshake_price,milkshake_quantity))
    print(get_summary(meal_set,meal_set_price,meal_set_quantity))

    burger_subtotal = get_subtotal(burger_price,burger_quantity)
    milkshake_subtotal = get_subtotal(milkshake_price,milkshake_quantity)
    meal_set_subtotal = get_subtotal(meal_set_price,meal_set_quantity)
    subtotal = round(burger_subtotal+milkshake_subtotal+meal_set_subtotal,2)
    print(get_summary_bill('Sub-total', subtotal))
    gst = get_gst(subtotal, gst_rate) 
  
    print(get_summary_bill('GST', gst))
    total = round(subtotal + gst,2)
    assert total >= 0, "Tax Rate can't be negative" 
    print('{}\n'.format(get_summary_bill('Total', total)))
    amouunt_paid=get_payment(total)





    
if __name__ == "__main__":
	main()

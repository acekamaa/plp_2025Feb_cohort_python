#function calculate_discount(price, discount_percent)
def calculate_discount(price, discount_percent):

    #prompt user for price and discount_percent
    price = float(input("Enter the price of the item: "))
    discount_percent = float(input("Enter the discount percent: "))
    discount = price * discount_percent / 100

    if discount >= 20/100:
        print("Discount applied: ", discount)
    else:
        print("Discount not applied, original price: ", price)

#call function calculate_discount
calculate_discount(0, 0)

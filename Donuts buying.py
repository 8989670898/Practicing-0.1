price=int(input("Enter the price of donut: Rs. "))
quantity=int(input("Enter the amount of donut required: "))
amount=price*quantity

if amount>1000:
    print("Yay.. 10% discount is available: ")
    discount=amount*10/100
    amount=amount-discount

else:
    print("Yay.. 5% discount is available: ")
    discount=amount*5/100
    amount=amount-discount
print("Your total amount is: Rs. ",amount)

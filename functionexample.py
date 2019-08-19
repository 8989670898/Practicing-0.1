def predict(m1,m2,m3):
    total=m1+m2+m3
    if total>=15000:
        print("Yes, you can get a new phone!.\n")
    else:
        print(("Sorry, this is not the right time to get the smartphone.\n"))
    return

gift=int(input("gift money from the family: Rs. "))
saving=int(input("Saving: Rs."))
internship=int(input("Internship, earned with sweat and blood: Rs. "))
predict(gift,saving,internship)

#Supermarket Bill Generation Using Python

from datetime import datetime
print("Welcome to Super Market")
name=input("Enter your name:")
print("Hello",name,"!")
list='''
Rice        Rs 80/kg
Sugar       Rs 40/kg
Salt        Rs 20/kg
Tomatoes    Rs 20/kg
Onion       Rs 15/kg
Toothpaste  Rs 110/each
ToothBrush  Rs 20/each
Maggie      Rs 56/each
'''
price=0
pricelist=[]
totalprice=0
finalprice=0
ilist=[]    #items
qlist=[]    #quantity
plist=[]    #price

items={'rice':80,'sugar':40,"salt":20,'tomatoes':20,'onion':15,'toothpaste':110,'toothbrush':20,'maggie': 56}
option=int(input("Press 1, for list of items:"))
if option==1:
    print(list)
for i in range(len(items)):
    inp=int(input("Press 1, to buy \nPress 2, to exit\nPress 1 or 2:"))
    if inp==2:
        break
    if inp==1:
        item=input('Enter your items:')
        quantity=int(input("Enter the required quantity:"))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalprice=gst+totalprice
        else:
            print("Sorry! The item you have selected is out of stock")
    else:
        print("Wrong Input!")
    #billgeneration
inp1=input("Would you like to print the bill?\nPress Y for yes and N for no :")
if inp1=='Y':
    pass
    if finalprice!=0:
        print(30*"=","Super Market",30*"=")
        print(33*" ","Vizag")
        print("Name:",name,30*" ","Date:",datetime.now())
        print(75*"-")
        print("{:<15}".format("S.No"),"{:<20}".format("Items"),"{:<25}".format("Quantity"),"{:<10}".format("Price"))
        print(75*"-")
        for i in range(len(pricelist)):
            print("{:<15}".format(i),"{:<20}".format(ilist[i]),"{:<25}".format(qlist[i]),"{:<10}".format(plist[i]))
        print(75*"-")
        print(50*" ","Total Amount:","Rs.",totalprice)
        print(50*" ","GST Amount:",2*" ","Rs.",gst)
        print(75*"-")
        print(50*" ","Final Amount:","Rs.",finalprice)
        print(75*"-")
        print(20*" ","Thank You🙏 Visit Again😊")
        print(75*"-")
#Welcome message and personal details


print('Hello and welcome to Sam fruit stand, please provide us some details')
name = input ('Enter your name: ')
phoneNumber = input ('Enter you phone number: ')
postalCode = input ('Enter your postal code: ')
print ('Thank you very much for providing the information, the following are our products:- ')

#Products to be sold


product1 = "Apples"
product1price = 0.50
product2 = "Oranges"
product2price = 0.65
product3 = "Bananas"
product3price = 0.23
product4 = "Grapefruit"
product4price = 0.99
product5 = "Dragon Fruit"
product5price = 1.99

print('First We have',product1,'at',product1price,)
product1quantity = int ((input('How many would you like ? \n')))

print('=========================================')

print('Second we have', product2,'at',product2price)
product2quantity = int ((input('How many would you like ?\n')))

print('=========================================')

print('Next we have',product3,'at',product3price,)
product3quantity = int ((input('How many would you like ?\n')))

print('==========================================')

print('Then we have',product4,'at',product4price)
product4quantity = int (input('How many would you like ? \n'))

print('===========================================')

print('Finally we have',product5,'at',product5price)
product5quantity = int (input('How many would you like ? \n'))

print('===========================================')

discount = int (input('What is your discount ? (0-100) \n'))

print('============================================')

print('Thank You for your purchase ! Here is your receipt, Have a nice day')

#Processing 

total1 = product1quantity*product1price
total2 = product2quantity*product2price
total3 = product3quantity*product3price
total4 = product4quantity*product4price
total5 = product5quantity*product5price
subTotal1= total1+total2+total3+total4+total5 #adds and stores the total of all products
HST= 0.13 #tax
HSTinDollar =subTotal1*HST 
subTotal2= subTotal1 + HSTinDollar #total after adding HST
discount= subTotal2*(discount/100) #discount on purchase
amount= subTotal1-discount #final amount after discount

#output

print("============================================================================")
print("|", format("The Fruit Stand", '>25s'),"|  Customer:", format(name,'>33s'), "|")
print("|",format("www.samsfruitstand.com",'>25s'), "| ",format(phoneNumber, '>43s'), "|")
print("|  ", format("|", ">25s"),format(postalCode,'>44s'), "|")
print("|==========================================================================|")
print("|", format("PRODUCT", '>28s'), "  |  QUANTITY  |  UNIT PRICE  |  TOTAL PRICE|")
print("|", format(product1, '>28s'), "  |", format(product1quantity,'>10d'),"|", format(product1price, '>12.2f'),"|", format(total1, '>11.2f'),"|")
"""print("|", format("a", '>28s'), "  |", format(1,'>10d'),"|", format(2.012, '>12.2f'),"|", format(2.012, '>11.2f'),"|")
print("|", format("a", '>28s'), "  |", format(1,'>10d'),"|", format(2.012, '>12.2f'),"|", format(2.012, '>11.2f'),"|")
print("|", format("a", '>28s'), "  |", format(1,'>10d'),"|", format(2.012, '>12.2f'),"|", format(2.012, '>11.2f'),"|")
print("|", format("a", '>28s'), "  |", format(1,'>10d'),"|", format(2.012, '>12.2f'),"|", format(2.012, '>11.2f'),"|")
print("|", format("a", '>28s'), "  |", format(1,'>10d'),"|", format(2.012, '>12.2f'),"|", format(2.012, '>11.2f'),"|")"""
print("|", format(product2, '>28s'), "  |", format(product2quantity,'>10d'),"|", format(product1price, '>12.2f'),"|", format(total2, ">11.2f"),"|")
print("|", format(product3, '>28s'), "  |", format(product3quantity,'>10d'),"|", format(product3price, '>12.2f'),"|", format(total3, ">11.2f"),"|")
print("|", format(product4, '>28s'), "  |", format(product4quantity,'>10d'),"|", format(product4price, '>12.2f'),"|", format(total4, ">11.2f"),"|")
print("|", format(product5, '>28s'), "  |", format(product5quantity,'>10d'),"|", format(product5price, '>12.2f'),"|", format(total5, ">11.2f"),"|")
print("|------------------------------------------------------------|-------------|")
print("|",format("Sub Total 1|",'>60s'), format(subTotal1,'>11f'),"|")
print("|",format("H.S.T |",'>60s'), format(HSTinDollar,'>11f'),"|")
print("|",format("Sub Total 2 |",'>60s'), format(subTotal2,'>11f'),"|")
print("|",format("Discount (10%) |",'>60s'), format(discount,'>11f'),"|")
print("|",format("Amount Due |",'>60s'), format(amount,'>11f'),"|")
print("============================================================================")

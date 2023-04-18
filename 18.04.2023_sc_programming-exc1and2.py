print("Welcome to Furkan's Store")
product_name=input(" Please Write Your Product Name: ")
while True:
    try:
        product_price_net = int(input ("Please Write Your Product Price Net: " ))
        break
    except:
        print("Your Data Type is Wrong")
client_email = input("Please Write Client Email:")
client_phone = input ("Please Write Client Phone:")
groos_price = (product_price_net)+ ((product_price_net)* 23/100)

print("name: ", product_name)

print("net price: ", product_price_net)

print("gross price: ", groos_price)

print("email: ", client_email)

print("phone: ", client_phone)


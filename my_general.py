import time
import mysql.connector as connection
myconn = connection.connect(host = "127.0.0.1", user = 'faith', passwd = "", database = 'sqi')
cursor = myconn.cursor()
def admin_reg():
    print("welcome!follow the prompt to register as an admin in the mall's database")
    time.sleep(2)
    querry = "INSERT INTO admin_details (Name, Username, Password) VALUES(%s, %s, %s)"
    name = ("Name: ")
    uname = input("Username: ")
    pwrd = input("Password: ")
    val = (name, uname, pwrd)
    cursor.execute(querry, val)
    myconn.commit()
    print("Please wait....")
    time.sleep(2)
    print("Registration complete")
    login()

def login():
    username = input("Enter your username: ")
    pwd = input("Enter your password: ")
    val = (username, pwd)
    querry = "select * from admin_details where Username=%s and Password=%s"
    cursor.execute(querry, val)
    result = cursor.fetchone()
    print("verifying....")
    time.sleep(2)
    if result:
        print("You have successfully logged in")
        product_entry()
    else:
        print("Invalid username or password")
        login()


def product_entry():
    print("welcome! \n Press 1 to enter product id and corresponding details")
    dec = input(">>> ")
    while dec == "1":
        querry = "INSERT INTO product_table(Product Name, Price, wholesale Price, Available_quantity)VALUES(%s, %s, %s, %s)"
        product_name = input("enter product name: ")
        price = input("Enter price: ")
        wholesale_price = input("Enter wholesale price: ")
        available_qty = input("Enter the available quantity: ")
        val =(product_name, price, wholesale_price, available_qty)
        cursor.execute(querry, val)
        myconn.commit()
        time.sleep(3)
        print("Product database created")
        product_entry()
    else:
        print("Wrong entry. Pls try again")
        product_entry()

def sales_table():
    print("Enter all products id in this table ")
    querry = "INSERT INTO product_sale(Product Id, Product Name, Available_quantity,) VALUES(%s, %s, %s)"
    product_id = input("Product Id: ")
    prod_name = input("Product name: ")
    avail_qty = input("Qty Availabe: ")
    val = (product_id, prod_name, avail_qty)
    cursor.execute(querry, val)
    myconn.commit()
    time.sleep(3)
    print("Sales table created successfully!")
    sales_table()

def check_out():
    print("Welcome to GEMS MALL. pls shop and enter product Id below \n please enter press 1 to enter all the product purchased \n Press 2 to proceed to payment options")
    decision = input(">>> ")
    while decision == "1":
        prod_id = input("Enter the product id:")
        val = (prod_id, )
        querry = "select * from product_table where Product Id =%s"
        cursor.execute(querry, val)
        result = cursor.fetchone
        if result:
            print(result[1])
            print(result[2])
            print(result[4])
            quantity_purcahsed = input("please enter desired quantity: ")
            if quantity_purcahsed <= result[4]:
                amount_paid = (result[2]*quantity_purcahsed)
                print ("The amount is " + (amount_paid))
                quantity_left = result[4]-quantity_purcahsed
                val = (quantity_left, amount_paid)
                querry = "UPDATE product_sale SET quantity_purchased=%s, quantity_left=%s, amount_paid=%s where Product Id =%s"
                cursor.execute(querry, val)
                myconn.commit()
                print("Thank youn for shopping with us")
                check_out()
            else:
                print("sorry! the quantity available is less than your request.")
        decision = input(">>> ")
    # else:
    #     while decision == "2":
    #         print("Proceed to pay Enter card details.")
    #         bank_name = input("Please enter Bank name: ")
    #         cvv = input("enter cvv: ")
    #         amount = input("Enter total amount: ")
    #         pin = input("Enter card pin: ")

print("Hello World")
            
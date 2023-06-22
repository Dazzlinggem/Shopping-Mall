def homepage():
    print("Welcome to Gems Mall. Enter 1 to register as Admin \n Enter 2 to  register new products. \n Enter 3 to shop")
    dec =input(">>> ")
    if dec == "1":
        from my_general import admin_reg
        admin_reg()
    elif dec == "2":
        from my_general import login
        login()
        from my_general import product_entry
        product_entry()
    elif dec == "3":
        from my_general import sales_table
        sales_table()
        from my_general import check_out
        check_out()
homepage()

from tabulate import tabulate
import pandas as pd

Exit = False
while not Exit:
    print("\n\n------------------------------------------------------------")
    print("Choose a valid operation to perform:")
    operation = int(input("1.Show all products\t\t2.Add new product\t\t3.Edit product\t\t4.Exit: "))
    print("------------------------------------------------------------\n\n")

    # Display all products
    if operation == 1:
        df = pd.read_csv("C:\\Users\\hasee\\ICT project\\product.csv")
        matrix = df.to_numpy()
        print(tabulate(matrix, headers=["Product Id", "Name", "Price", "Stock", "Category", "Supplier"]))

    # Adding new product
    elif operation == 2:
        Id = input("Enter product ID: ")
        name = input("Enter product name: ")
        price = input("Enter price of product: ")
        stock = input("Enter stock available: ")
        category = input("Enter Product category: ")
        supplier = input("Enter supplier of product: ")
        product = {'ID': [Id], 'Name': [name], 'Price': [price], 'Stock': [stock], 'Category': [category],
                   'Supplier': [supplier]}
        df = pd.DataFrame(product)
        df.to_csv("C:\\Users\\hasee\\ICT project\\product.csv", mode='a', index=False, header=False)
        print("\n------------------------\nProduct added successfully.\n------------------------\n")

    elif operation == 3:
        pass
    elif operation == 4:
        Exit = True

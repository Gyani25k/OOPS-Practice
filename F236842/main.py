from car_rental import Car, Customer, VIPCustomer, RentalShop

if __name__ == "__main__":
    
    # Initial stock of cars
    total_hatchbacks = 10
    total_sedans = 15
    total_suvs = 8

    hatchback = Car("hatchback", total_hatchbacks)
    sedan = Car("sedan", total_sedans)
    suv = Car("SUV", total_suvs)

    car_stock = [hatchback, sedan, suv]

    print("\nStock before transactions:")

    # Create a rental shop with the initial car stock
    shop = RentalShop(car_stock)

    # Create customers
    customer1 = Customer("John")
    customer2 = VIPCustomer("Alice")
    customer3 = VIPCustomer("Meklit")

    # Inquire and display stock prices for customers
    customer1.inquire_stock_prices(shop)
    customer1.rent_car(shop, "hatchback", 7)
    customer2.rent_car(shop, "SUV", 9)
    customer3.rent_car(shop,"sedan",5)
    customer1.return_car(shop, shop.rentals[0])
    customer3.return_car(shop,shop.rentals[1])

    print("\nStock after transactions:")
    # Display the updated inventory and prices
    shop.display_inventory_prices()

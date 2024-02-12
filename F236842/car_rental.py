
class Car:
    def __init__(self, type, total):

        """
        This is Car Class that consists two parameters ::->

        type: The type of car (hatchback, sedan, suv)
        total: Total Number of each type of cars  

        """
        self.type = type
        self.total = total  # Total number of cars
        self.remaining = total  # Initially, all cars are available

class Customer:
    def __init__(self, name):

        """
        This is Customer Class that has one parameter ::->

        name: The name of the customer.

        """
        self.name = name

    def inquire_stock_prices(self, shop):

        """
        This Function used to inquire about stock prices by displaying inventory prices.

        It show all the car types with remaining and total count.

        Consist of one parameter i.e., - shop (RentalShop): The RentalShop object.
        
        """
        shop.display_inventory_prices()

    def rent_car(self, shop, car_type, num_days):

        """
        This Function used to rent a car by making a rental request to the shop.

        Parameters:
        - shop (RentalShop): The RentalShop object.
        - car_type (str): The type of the car to be rented.
        - num_days (int): The number of days for the rental.

        """
        shop.process_rental_request(self, car_type, num_days)

    def return_car(self, shop, rental):
        """
        This Function used to return a rented car, and the shop issues a bill.

        Parameters:
        - shop (RentalShop): The RentalShop object.
        - rental (dict): Rental information including customer, car, num_days, and total_payment.

        """
        shop.issue_bill(self, rental)

class VIPCustomer(Customer):
    def __init__(self, name):
        """
        This is VIPCustomer object that inherits parameter (name) from Customer Class [Shows Inheritence].

        Parameters:
        - name (str): The name of the VIP customer.

        """
        super().__init__(name)

    def rent_car(self, shop, car_type, num_days):
        """
        This Function used to rent a car with additional VIP privileges.

        Parameters:
        - shop (RentalShop): The RentalShop object.
        - car_type (str): The type of the car to be rented.
        - num_days (int): The number of days for the rental.
        """
        shop.process_rental_request(self, car_type, num_days, vip=True)

class RentalShop:
    def __init__(self, stock):
        """
        This is RentalShop Class.

        Parameters:
        - stock (list): List of Car objects representing the available stock.
        """
        self.stock = stock
        self.rentals = []

    def display_inventory_prices(self):
        """
        This Function is used to display the prices and availability of cars in the inventory.
        
        """
        for car in self.stock:
            print(f"{car.type}: Available - {car.remaining}/{car.total}")

    def process_rental_request(self, customer, car_type, num_days, vip=False):
        """
        This function is used to process a rental request from a customer.

        Parameters:
        - customer (Customer): The Customer or VIPCustomer object making the request.
        - car_type (str): The type of the car to be rented.
        - num_days (int): The number of days for the rental.
        - vip (bool, optional): True if the customer is a VIP, False otherwise.
        """
        for car in self.stock:
            if car.type == car_type and car.remaining > 0:
                # Calculate the rental details and update the car's availability
                daily_rate = self.calculate_daily_rate(car_type, num_days, vip)
                total_payment = daily_rate * num_days
                print(f"You have rented a {car.type} car for {num_days} days. "
                      f"You will be charged £{daily_rate} per day. Total payment: £{total_payment}. "
                      f"We hope that you enjoy our service.")
                car.remaining -= 1  # Reduce the available cars by 1
                # Record the rental details
                self.rentals.append({"customer": customer, "car": car, "num_days": num_days, "total_payment": total_payment})
                break
        else:
            print(f"Sorry, no available {car_type} cars for the specified period.")

    def issue_bill(self, customer, rental):
        """
        This Function used to issue a bill for the returned car.

        Parameters:
        - customer (Customer): The Customer or VIPCustomer returning the car.
        - rental (dict): Rental information including customer, car, num_days, and total_payment.
        """
        for rented_car_info in self.rentals:
            if rented_car_info == rental:
                rented_car = rented_car_info["car"]
                print(f"Bill for {customer.name}: "
                      f"Car Type: {rented_car_info['car'].type}, "
                      f"Number of Days: {rented_car_info['num_days']}, "
                      f"Total Payment: £{rented_car_info['total_payment']}")
                rented_car.remaining += 1  # Increase the available cars by 1
                # Remove the rental record from the list
                self.rentals.remove(rented_car_info)
                break
        else:
            print("No matching rental found.")

    def calculate_daily_rate(self, car_type, num_days, vip):
        """
        This Function is to calculate the daily rental rate based on car type, number of days, and VIP status.

        Parameters:
        - car_type (str): The type of the car.
        - num_days (int): The number of days for the rental.
        - vip (bool): True if the customer is a VIP, False otherwise.

        Returns:
        - int: The calculated daily rental rate.
        """
        if vip:
            rates = {"hatchback": 20, "sedan": 35, "SUV": 80}
        else:            
            # Rent a car for less than a week: Hatchback £30, sedan £50, SUV £100 per day. 
            if num_days < 7:
                rates = {"hatchback": 30, "sedan": 50, "SUV": 100}
            else:
            # Rent a car for a longer period: Hatchback £25, sedan £40, SUV for £90 per day. 
                rates = {"hatchback": 25, "sedan": 40, "SUV": 90}
        return rates[car_type]

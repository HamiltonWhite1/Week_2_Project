

# Parking Garage Class

class Parking_Garage:
    def __init__(self, tickets_available, parking_spaces, current_ticket):
        self.tickets_available = tickets_available
        self.parking_spaces = parking_spaces
        self.current_ticket = current_ticket
        self.customer_ticket = {"Paid": False}
        self.parking = []
        # for i in self.parking_spaces:
    
    def take_ticket():
        pass
    
    def pay_for_parking(self):
        payment = int(input("Welcome to the parking garage. Please input your payment total to the terminal to claim your space: "))
        if payment > 0:
            print("Your parking has been paid for you. You have 15 minutes. Please enjoy your visit.")
            self.customer_ticket["Paid"] = True

    def leave_garage(self):
        if self.customer_ticket["Paid"] == True:
            print("Thank you, have a nice day!")
            self.parking.append("space")
        elif self.customer_ticket["Paid"] == False:
            payment = int(input("Whoopsies, looks like we need to pay for that there parking ticket: "))
            if payment > 0:
                self.customer_ticket["Paid"] = True
                print("Thank you, have a nice day!")
                self.parking.append("space")
               

garage = Parking_Garage(10, 10, 1)
print(garage.pay_for_parking())

"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: tuni.fi:50745580
Name:Oussama Bahri
Email:oussama.bahri@tuni.fi

Template for pricelist assignment.
"""

PRICES = {
    "milk": 1.09, "fish": 4.56, "bread": 2.10,
    "chocolate": 2.70, "grasshopper": 13.25,
    "sushi": 19.90, "noodles": 0.97, "beans": 0.87,
    "bananas": 1.05, "Pepsi": 3.15,  "pizza": 4.15,
}


def main():
    user_input = input("Enter product name: ").split()
    # checking if the returned list is not empty
    if user_input:
        # if list not empty, we check if the item is not listed in PRICES so we
        # we keep looping and prompting the user
        while user_input[0] not in PRICES:
            print(f"Error: {user_input[0]} is unknown.")
            user_input = input("Enter product name: ").split()
        # if user_input[0] in PRICES:
        else:
            print(f"The price of {user_input[0]} is {PRICES[user_input[0]]} e")


    else:
        # if returned list is empty:
        print("Bye!")



if __name__ == "__main__":
    main()

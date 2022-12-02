# table.add_column('Availability',available*5)
from prettytable import PrettyTable
import coffe as c
amount = 0
starting_ingredients = {'Milk':200,'Coffe':200,'Ice':200,'Sugar':200}
table = PrettyTable()

available = "Yes"
choice = 0

def availablity(choice):
    global amount
    drink = list(c.coffe)[choice-1]


    li = c.coffe[drink]["ingredients"].values()

    for a,b in zip(starting_ingredients.keys(),li):
        if starting_ingredients[a] <= 0:
            print("Sorry does not have sufficent resources to make",drink)
            break
        else:
            starting_ingredients[a] -= b


    else:
        print(f'Your {drink} is ready...')
        amount += c.coffe[drink]["cost"]

def menu():
    types_of_coffes = [i for i in c.coffe.keys()]
    table.add_column('Sl No.',[i for i in range(1,len(c.coffe)+1)])
    table.add_column('Types of Coffe',types_of_coffes)
    table.add_column('Price',[(c.coffe[i]['cost']) for i in types_of_coffes])
    print(table)
    while True:
        try:
            choice = int(input("Enter Your Choice (0 to exit) : "))
            if choice == 0:
                break
            availablity(choice)
        except:
                password = input()
                if password == 'Iam A Admin':
                    print(amount)

                    print("Resources Available : ",starting_ingredients)
                else:
                    print("Please enter any option which is available in order table")
    print("Thank you for Drinking Me visting again....")
menu()
from dis import disco
from fileinput import lineno
from datetime import date, timedelta
import random

totalcost = 0
ticketcount = 0
discountcount = 0
extracost = 0

def breakline():
    print('')

def line():
    print("------------------------")

class Ticket:
    def __init__(self, tickettype, onedaycost, twodaycost):
        self.tickettype = tickettype
        self.onedaycost = onedaycost
        self.twodaycost = twodaycost

adult = Ticket("One Adult", 20.00, 30.00,)
child = Ticket("One Child", 12.00, 18.00)
senior = Ticket("One Senior", 16.00, 24.00)
family = Ticket("Family Ticket (up to 2 adults or seniors and 3 children)", 60.00, 90.00)
group = Ticket("Groups of 6 people or more, price per person", 15.00, 22.50)
lion = Ticket("Lion Feeding", 2.50, 2.50)
penguin = Ticket("Penguin Feeding", 2.00, 2.00)
barbecue = Ticket("Evening Barbecue (Two-day ticket only)", 0, 5.00)

print('Dates Available')
print("Option 1 - ", date.today() + timedelta(days=0))
print("Option 2 - ", date.today() + timedelta(days=1))
print("Option 3 - ", date.today() + timedelta(days=2))
print("Option 4 - ", date.today() + timedelta(days=3))
print("Option 5 - ", date.today() + timedelta(days=4))
selecteddate = int(input("I pick Option "))

print("")
days = int(input("Are you planning to visit for 1 or 2 days? "))
dayvisitloop = 0
while dayvisitloop == 0:
    if days == 1:
        print("You will visit for, ", days, "days.")
        dayvisitloop += 1
        print("One Day Costs")
        line()
        print(adult.tickettype, "- $", adult.onedaycost)
        print(child.tickettype, "- $", child.onedaycost)
        print(senior.tickettype, "- $", senior.onedaycost)
        print(family.tickettype, "- $", family.onedaycost)
        print(group.tickettype, "- $", group.onedaycost)
    elif days == 2:
        print("You will visit for, ", days, "days.")
        dayvisitloop += 1
        print("Two Day Costs")
        line()
        print(adult.tickettype, "- $", adult.twodaycost)
        print(child.tickettype, "- $", child.twodaycost)
        print(senior.tickettype, "- $", senior.twodaycost)
        print(family.tickettype, "- $", family.twodaycost)
        print(group.tickettype, "- $", group.twodaycost)
    else:
        print("Error: Bad Integer")
        dayvisitloop += 0

breakline()
if days == 1:
    print("Extra Attraction for One day")
    line()
    print(lion.tickettype, "- $", lion.onedaycost)
    print(penguin.tickettype, "- $", penguin.onedaycost)
elif days == 2:
    print("Extra Attraction for Two days")
    line()
    print(lion.tickettype, "- $", lion.twodaycost)
    print(penguin.tickettype, "- $", penguin.twodaycost)
    print(barbecue.tickettype, "- $", barbecue.twodaycost)

costloop = 0                #loop to input ticket type amount
specialticket = 0           #loop to check if y or n is input
while costloop == 0:
    if days == 1:
        while specialticket == 0:
            breakline()
            specialticketcheck = str(input("Are you buying a family ticket or a group ticket? [y/n] "))
            if specialticketcheck == "n":
                specialticketcheck = False
                specialticket += 1
                adultcount = int(input("How many adults? "))
                totalcost += adultcount * adult.onedaycost
                ticketcount += adultcount
                childcount = int(input("How many children? "))
                totalcost += childcount * child.onedaycost
                ticketcount += childcount
                seniorcount = int(input("How many seniors? "))
                totalcost += seniorcount * senior.onedaycost
                ticketcount += seniorcount
                costloop += 1
            elif specialticketcheck == "y":
                specialticketcheck = True
                specialticket += 1
                familycount = int(input("How many family tickets? "))
                totalcost += familycount * family.onedaycost
                groupcount = int(input("How many group tickets? "))
                totalcost += groupcount * group.onedaycost
                costloop += 1
            else:
                print("Error: Bad Input")
    elif days == 2:
         while specialticket == 0:
            breakline()
            specialticketcheck = str(input("Are you buying a family ticket or a group ticket? [y/n] "))
            if specialticketcheck == "n":
                specialticketcheck = False
                specialticket += 1
                adultcount = int(input("How many adults? "))
                totalcost += adultcount * adult.twodaycost
                ticketcount += adultcount
                childcount = int(input("How many children? "))
                totalcost += childcount * child.twodaycost
                ticketcount += childcount
                seniorcount = int(input("How many seniors? "))
                totalcost += seniorcount * senior.twodaycost
                ticketcount += seniorcount
                costloop += 1
            elif specialticketcheck == "y":
                specialticketcheck = True
                specialticket += 1
                familycount = int(input("How many family tickets? "))
                totalcost += familycount * family.twodaycost
                groupcount = int(input("How many group tickets? "))
                totalcost += groupcount * group.twodaycost
                costloop += 1
            else:
                print("Error: Bad Input")

extraloop = 0           #loop to check if extra costs are added
if days == 1:
    while extraloop == 0:
        breakline()
        lioncount = int(input("How many tickets for lion feeding? "))
        extracost += lioncount * lion.onedaycost
        penguincount = int(input("How many tickets for penguin feeding? "))
        extracost += penguincount * penguin.onedaycost
        extraloop += 1
elif days == 2:
    while extraloop == 0:
        lioncount = int(input("How many tickets for lion feeding? "))
        extracost += lioncount * lion.twodaycost
        penguincount = int(input("How many tickets for penguin feeding? "))
        extracost += penguincount * penguin.twodaycost
        bbqcount = int(input("How many tickets for the evening barbecue? "))
        extracost += bbqcount * barbecue.twodaycost
        extraloop += 1

breakline()
if days == 1:
    if totalcost == 76.00 or totalcost == 72.00 or totalcost == 68.00 and ticketcount == 6:
        print("You are eligible for a family ticket which is cheaper than your current selection.")
        discountcount += 60
    elif ticketcount >= 6:
        print("You have more than 6 people in your group and eligible for a group ticket for six people.")
        discountcount += ticketcount * group.onedaycost
elif days == 2:
    if totalcost == 114.00 or totalcost == 108.00 or totalcost == 78.00 and ticketcount == 6:
        print("You are eligible for a family ticket which is cheaper than your current selection.")
        discountcount += 90
    elif ticketcount >= 6:
        print("You have more than 6 people in your group and eligible for a group ticket for six people.")
        discountcount += ticketcount * group.twodaycost 

#Final Output
breakline()
print('Your ticket is valid on', date.today() + timedelta(days=selecteddate-1), "for", days ,"day(s)")
print("Your total is $", totalcost + extracost)
print("Your total, with the best value is $", extracost + discountcount)
print("Your booking number is", random.randrange(1, 100000, 6))
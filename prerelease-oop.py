from dis import disco
from fileinput import lineno
from datetime import date, timedelta
import random

totalcost = 0
discountcost = 0
discountcountcounter = 0
discountvaluecounter = 0
extracost = 0

def breakline():
    print('')

def line():
    print("------------------------")

class Ticket:
    def __init__(self, tickettype, onedaycost, twodaycost, discountcostoneday, discountcosttwoday, discountcount, discountweight):
        self.tickettype = tickettype
        self.onedaycost = onedaycost
        self.twodaycost = twodaycost
        self.discountcostoneday = discountcostoneday
        self.discountcosttwoday = discountcosttwoday
        self.discountcount = discountcount
        self.discountweight = discountweight 

adult = Ticket("One Adult", 20.00, 30.00, 15.00, 22.50, 1, 2)
child = Ticket("One Child", 12.00, 18.00, 15.00, 22.50, 1, 1)
senior = Ticket("One Senior", 16.00, 24.00, 15.00, 22.50, 1, 2)
family = Ticket("Family Ticket (up to 2 adults or seniors and 3 children)", 60.00, 90.00, 60.00, 90.00, 0, 0)
group = Ticket("Groups of 6 people or more, price per person", 15.00, 22.50, 15.00, 22.50, 0, 0)
lion = Ticket("Lion Feeding", 2.50, 2.50, 0, 0, 0, 0)
penguin = Ticket("Penguin Feeding", 2.00, 2.00, 0, 0, 0, 0)
barbecue = Ticket("Evening Barbecue (Two-day ticket only)", 0, 5.00, 0, 0, 0, 0)

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
        print("Invalid Input")
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

costloop = 0
specialticket = 0
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
                discountcost += adultcount * adult.discountcostoneday
                discountcountcounter += adult.discountcount
                discountvaluecounter += adult.discountweight
                childcount = int(input("How many children? "))
                totalcost += childcount * child.onedaycost
                discountcost += childcount * child.discountcostoneday
                discountcountcounter += child.discountcount
                discountvaluecounter += child.discountweight
                seniorcount = int(input("How many seniors? "))
                totalcost += seniorcount * senior.onedaycost
                discountcost += seniorcount * senior.discountcostoneday
                discountcountcounter += senior.discountcount
                discountvaluecounter += senior.discountweight
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
                print("Invalid Input")
    elif days == 2:
         while specialticket == 0:
            breakline()
            specialticketcheck = str(input("Are you buying a family ticket or a group ticket? [y/n] "))
            if specialticketcheck == "n":
                specialticketcheck = False
                specialticket += 1
                adultcount = int(input("How many adults? "))
                totalcost += adultcount * adult.twodaycost
                discountcost += adultcount * adult.discountcosttwoday
                discountcountcounter += adult.discountcount
                discountvaluecounter += adult.discountweight
                childcount = int(input("How many children? "))
                totalcost += childcount * child.twodaycost
                discountcost += childcount * child.discountcosttwoday
                discountcountcounter += child.discountcount
                discountvaluecounter += child.discountweight
                seniorcount = int(input("How many seniors? "))
                totalcost += seniorcount * senior.twodaycost
                discountcost += seniorcount * senior.discountcosttwoday
                discountcountcounter += senior.discountcount
                discountvaluecounter += senior.discountweight
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
                print("Invalid Input")

#Final Output
breakline()
print('Your ticket is valid on', date.today() + timedelta(days=selecteddate-1), "for", days ,"day(s)")
print("Your total, without discount, is ", totalcost)
print("Your extra attraction total, without discount, is ", extracost)
print("Your total, with discount is ", discountcost + extracost)
print("Your booking number is,", random.randrange(1, 100000, 6))
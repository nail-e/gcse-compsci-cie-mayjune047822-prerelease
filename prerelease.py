from datetime import date, timedelta
import random

onedayprice = [0.00, 20.00, 12.00, 16.00, 60.00, 15.00]
twodayprice = [0.00, 30.00, 18.00, 24.00, 90.00, 22.50]
extraprice = [0.00, 2.50, 2.00, 5.00]

def breakline():
    print('Type 0 to cancel/confirm')

def onedaycost(): 
    print('One Day Costs')
    print('-------------')
    print('1. One Adult - $20.00')
    print('2. One Child - $12.00')
    print('3. One Senior - $16.00')
    print('4. Family Ticket (up to 2 adults or seniors and 3 children) - $60.00')
    print('5. Groups of 6 people or more, price per person - $15.00')

def twodaycost():
    print('')
    print('Two Day Costs')
    print('-------------')
    print('1. One Adult - $30.00')
    print('2. One Child - $18.00')
    print('3. One Senior - $24.00')
    print('4. Family Ticket (up to 2 adults or seniors and 3 children) - $90.00')
    print('5. Groups of 6 people or more, price per person - $22.50')

def extracost():
    print('')
    print('Extra Costs')
    print('-------------')
    print('1. Lion Feeding - $2.50')
    print('2. Penguin Feeding - $2.00')
    print('3. Evening Barbecue (Two-day ticket only) - $5.00')

onedaycost()
twodaycost()
extracost()

print('')
print('Dates Available')
for i in range (0,5):
    availabledates = date.today() + timedelta(days=i)
    print(availabledates)

daytries = 0
print('')
print('Booking')
print('-------------')
while daytries == 0:
    days = int(input('How many days are you going to visit the park for? '))
    if days == 1:
        print ('You have chosen to stay for ', days, 'day(s)')
        daytries = daytries + 1
    elif days == 2:
        print ('You have chosen to stay for ', days, 'day(s)')
        daytries = daytries + 1
    else:
        print ('You have input an invalid amount of days')

totalcosttries = 0
while totalcosttries == 0:
    totalcost = 0
    pricetries = 0
    print('')
    if days == 1:
        onedaycost()
        breakline()
        while pricetries == 0:
            ainput = int(input('Pick an option '))
            if ainput == 1:
                totalcost = totalcost + onedayprice[ainput]
            if ainput == 2:
                totalcost = totalcost + onedayprice[ainput]
            if ainput == 3:
                totalcost = totalcost + onedayprice[ainput]
            if ainput == 4:
                totalcost = totalcost + onedayprice[ainput]
            if ainput == 5:
                totalcost = totalcost + onedayprice[ainput]
            if ainput == 0:
                pricetries = 0
                break
            elif ainput > 5:
                print('Invalid Input')
                break
        extracost()
        breakline()    
        while pricetries == 0:
            ainputb = int(input('Pick an option '))
            if ainputb == 1:
                totalcost = totalcost + extraprice[ainputb]
            if ainputb == 2:
                totalcost = totalcost + extraprice[ainputb]
            if ainputb == 3:
                print('Option 3 is not available for the one-day')
            if ainputb == 0:
                pricetries = pricetries + 1
                break
            elif ainputb > 3:
                print('Invalid Input')
        totalcosttries = totalcosttries + 1
    elif days == 2:
        twodaycost()
        breakline()
        while pricetries == 0:
            binput = int(input('Pick an option '))
            if binput == 1:
                totalcost = totalcost + twodayprice[binput]
            if binput == 2:
                totalcost = totalcost + twodayprice[binput]
            if binput == 3:
                totalcost = totalcost + twodayprice[binput]
            if binput == 4:
                totalcost = totalcost + twodayprice[binput]
            if binput == 5:
                totalcost = totalcost + twodayprice[binput]
            if binput == 0:
                pricetries = 0
                break
            elif binput > 5:
                print('Invalid Input')
                break
            print(totalcost)
        extracost()
        breakline()    
        while pricetries == 0:
            binputb = int(input('Pick an option '))
            if binputb == 1:
                totalcost = totalcost + extraprice[binputb]
            if binputb == 2:
                totalcost = totalcost + extraprice[binputb]
            if binputb == 3:
                totalcost = totalcost + extraprice[binputb]
            if binputb == 0:
                pricetries = pricetries + 1
                break
            elif binputb > 3:
                print('Invalid Input')
        totalcosttries = totalcosttries + 1
    else:
        print('Invalid Input')

bookingletter = "x"
if days == 1:
    dayoneletter = bookingletter = "A"
elif days == 2:
    dayoneletter = bookingletter = "B"
print("Your booking number is", bookingletter + str(random.randrange(1, 100000, 5)))
print("Your total cost is $", totalcost)

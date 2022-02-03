from datetime import date, timedelta    #used for days for booking
import random                           #used for booking number

onedayprice = [0.00, 20.00, 12.00, 16.00, 60.00, 15.00]     #array first value is 0.00 due as first value seen in an array is value 0 while second value seen is value 1 
twodayprice = [0.00, 30.00, 18.00, 24.00, 90.00, 22.50]     #test
extraprice = [0.00, 2.50, 2.00, 5.00]

#Task 1
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

def extracosts():
    print('')
    print('Extra Costs')
    print('-------------')
    print('1. Lion Feeding - $2.50')
    print('2. Penguin Feeding - $2.00')
    print('3. Evening Barbecue (Two-day ticket only) - $5.00')

onedaycost()
twodaycost()
extracosts()

print('')
print('Dates Available')
for i in range (0,5):
    availabledates = date.today() + timedelta(days=i)   #timedelta is the day from the program starting
    print('Option',i+1,'-',availabledates)

#Task 2 Body

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
        
discount = 0          #counts how much should removed if a discount is applicable
discountcount = 0     #counts how much should be replaced if a discount is applied
count = 0     #counts how many tickets
value = 0     #weighs each ticket for task 3
extracost = 0 #counts extra costs
totalcosttries = 0
while totalcosttries == 0:      #loops repeats until totalcosttries reaches 1
    totalcost = 0
    pricetries = 0
    print('')
    if days == 1:
        onedaycost()
        breakline()
        while pricetries == 0:
            ainput = int(input('Pick an option '))
            if ainput == 1:
                totalcost = totalcost + onedayprice[ainput]         #onedayprice refers to the array, see array notes
                discount = discount + onedayprice[ainput]
                discountcount = discountcount + 15
                count = count + 1
                value = value + 2
            if ainput == 2:
                totalcost = totalcost + onedayprice[ainput]
                discount = discount + onedayprice[ainput]
                discountcount = discountcount + 15
                count = count + 1
                value = value + 1
            if ainput == 3:
                totalcost = totalcost + onedayprice[ainput]
                discount = discount + onedayprice[ainput]
                discountcount = discountcount + 15
                count = count + 1
                value = value + 2
            if ainput == 4:
                totalcost = totalcost + onedayprice[ainput]
                discount = discount + onedayprice[ainput]
            if ainput == 5:
                totalcost = totalcost + onedayprice[ainput]
                discount = discount + onedayprice[ainput]
            if ainput == 0:             #see array notes, no value added
                pricetries = 0          #for consistency
                break
            elif ainput > 5:
                print('Invalid Input')
                break                   #ends first loop
        extracosts()
        breakline()    
        while pricetries == 0:          #new loop for extra costs
            ainputb = int(input('Pick an option '))
            if ainputb == 1:
                extracost = extracost + extraprice[ainputb]
            if ainputb == 2:
                extracost = extracost + extraprice[ainputb]
            if ainputb == 3:
                print('Option 3 is not available for the one-day')
            if ainputb == 0:
                pricetries = pricetries + 1
                break
            elif ainputb > 5:
                print('Invalid Input')
        totalcosttries = totalcosttries + 1         #ends 2nd loop permanently
    elif days == 2:
        twodaycost()
        breakline()
        while pricetries == 0:
            binput = int(input('Pick an option '))
            if binput == 1:
                totalcost = totalcost + twodayprice[binput]
                discountcount = discountcount + 22.5
                count = count + 1
                value = value + 2           
            if binput == 2:
                totalcost = totalcost + twodayprice[binput]
                discountcount = discountcount + 22.5
                count = count + 1
                value = value + 1           
            if binput == 3:
                totalcost = totalcost + twodayprice[binput]
                discountcount = discountcount + 22.5 
                count = count + 1
                value = value + 2           
            if binput == 4:
                totalcost = totalcost + twodayprice[binput]
            if binput == 5:
                totalcost = totalcost + twodayprice[binput]
            if binput == 0:
                pricetries = 0
                break
            elif binput > 5:
                print('Invalid Input')
        extracosts()
        breakline()    
        while pricetries == 0:
            binputb = int(input('Pick an option '))
            if binputb == 1:
                extracost = extracost + extraprice[binputb]
            if binputb == 2:
                extracost = extracost + extraprice[binputb]
            if binputb == 3:
                extracost = extracost + extraprice[binputb]
            if binputb == 0:
                pricetries = pricetries + 1
                break
            elif binputb > 3:
                print('Invalid Input')
        totalcosttries = totalcosttries + 1
    else:
        print('Invalid Input')

#Task 3 Body
if days == 1:
    if count == 5 and value == 7:
        totalcost = totalcost - totalcost
        totalcost = totalcost + 60
        print('Your inputs are eligible for a One Day family ticket which is $60.00.')
    elif count >= 6:
        totalcost = totalcost - totalcost
        totalcost = totalcost + discountcount
        print('Your inputs are eligble for a Group of six ticket with $15 per person.')
    else:
        print('')
 
elif days == 2:
    if count == 5 and value == 7:
        totalcost = totalcost - totalcost
        totalcost = totalcost + 90
        print('Your inputs are eligible for a Two Day family ticket which is $90.00.')
    elif count >= 6:
        totalcost = totalcost - totalcost
        totalcost = totalcost + discountcount
        print('Your inputs are eligble for a Group of six ticket with $22.50 per person.')
    else:
        print('You are not eligble for any discount')
        
#final output       
bookingletter = "x"
if days == 1:
    dayoneletter = bookingletter = "A"
elif days == 2:
    dayoneletter = bookingletter = "B"
print("Your booking number is", bookingletter + str(random.randrange(1, 100000, 5)))
print("Your total cost with the cheapeast possible tickets is $", totalcost + extracost)

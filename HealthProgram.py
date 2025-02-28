
#Food Program for the Health Discord
#2/26/2025 v1.0
import os
import time

#Clear the screen
def clear_screen():
    if os.name == 'nt':
        os.system('cls')

def isWholeNumber(num):
    i = 0
    while i == 0:
        try:
            if(num == 'q'):
                exit()
            elif(num.isdigit()):
                num = int(num) #converting the string into an interger
                i = 1 #to break the loop
            elif(float(num)): #checking to see if it's a float.
                num = int(round(float(num))) #convert the string to interger after rounding. 
                i = 1
        except(TypeError, ValueError):
            print("You've entered a invalid option. Try again\n")
            num = input("Enter a number: ")
    return num


def ingredients(fs):
    print("""Which of the following fits the product?\n
    All natural ingredients: [1]\n
    1 to 3 Bad ingredients: [2]\n
    4 to 5 Bad ingredients: [3]\n
    6 or more Bad ingredints: [4]\n
    Quit: [5]\n""")
    ans = input("Enter Answer: ")
    ans = isWholeNumber(ans)
    while(True):
        if(ans == 1): #All natural ingredients
            fs += 10
            print("Is all the ingredints Organic? ")
            isOrganic = input("Yes [Y]/ No [N]/ Quit [Q]: ").lower()
            while(True):
                if(isOrganic == 'y'):
                    fs += 3
                    break
                elif(isOrganic == 'n'):
                    break
                elif(isOrganic == 'q'):
                    exit()
                else:
                    print("You've entered a invalid option. Try again\n")
                    isOrganic = input("Enter Answer: ")
            break
        elif(ans == 2): # 1 to 3 Bad ingredients
            fs += 3
            break
        elif(ans == 3): #4 to 5 Bad ingredients
            fs -= 5
            break
        elif(ans == 4): #6 or more Bad ingredints
            fs -= 8
            break
        elif(ans == 5): #Quit the program
            exit()
        else:
            print("You've entered a invalid option. Try again\n")
            ans = int(input("Enter Answer: "))
    return fs

def CaloriesMulti(fs, multi):
    print("Quit [Q]")
    calories = input("Enter the amount of calories: ")
    calories = isWholeNumber(calories)
    if(calories < 200): #per Serving
        fs += 1

    calories *= multi #To get the total amount of calories for th next condition
    if(calories < 850): #Total Calories 
        fs += 2
    else:
        fs -= 2

    if(calories >= 3000): #If the food item is way too high in calories
        fs -= 8

    return fs

def CaloriesDivide(fs, divide):
    print("Quit [Q]")
    calories = input("Enter the amount of calories: ")
    calories = isWholeNumber(calories)

    if(calories < 850): #Total Calories 
        fs += 2
    else:
        fs -= 2

    if(calories >= 3000): #If the food item is way too high in calories
        fs -= 8

    calories /= divide  #To get the single serving amount for calories for the next condition
    if(calories < 200): #per Serving
        fs += 1

    return fs

def CarbsMulti(fs, multi):
    print("Quit [Q]")
    carbs = input("Enter the amount of carbs: ")
    carbs = isWholeNumber(carbs)

    if(carbs < 10): #Per Serving 
        fs += 1

    carbs *= multi  #To get the Total serving amount for carbs for the next condition
    if(carbs < 50): #Total Carbs
        fs += 1
    else:
        fs -= 2

    if(carbs >= 300): #If the food item is way too high in Carbs
        fs -= 8

    return fs

def CarbsDivide(fs, divide):
    print("Quit [Q]")
    carbs = input("Enter the amount of carbs: ")
    carbs = isWholeNumber(carbs)

    if(carbs < 50): #The Total
        fs += 1
    else:
        fs -= 2

    if(carbs >= 300): #If the food item is way too high in Carbs
        fs -= 8

    carbs /= divide  #To get the single serving amount for calories for the next condition
    if(carbs < 10): #Per Serving 
        fs += 1

    return fs

def fatsMulti(fs, multi):
    print("Quit [Q]")
    s_fat = input("Enter the amount of Saturated Fat: ")
    s_fat = isWholeNumber(s_fat)
    t_fat = input("Enter the amount of Trans Fat: ")
    t_fat = isWholeNumber(t_fat)
    allFat = input("Enter Total fat listed: ")
    allFat = isWholeNumber(allFat)
    p_fat = input("Enter the amount of Ployunsaturated Fat: ")
    p_fat = isWholeNumber(p_fat)
    m_fat = input("Enter the amount of Monounsaturated Fat: ")
    m_fat = isWholeNumber(m_fat)

    if((s_fat + t_fat) <= 6): #Per Serving 
        fs += 1
    else:
        fs -= 1
    
    if((s_fat + t_fat) * multi >= 30): #Total Saturated and Trans Fat is greater than 30g
        fs -= 2

    if((s_fat + t_fat) * multi >= 80): #If the food item is way too high in Saturated and Trans Fat Total
        fs -= 8

    allFat *= multi  #To get the Total serving amount for Fat for the next condition
    if(allFat < 30): #Total of all Fat
        fs += 2
    elif(allFat > 50): #Total of all Fat greater than 50g
        fs -= 3
    else:
        fs -= 2 #30g or More and 50g or less Totals: -2

    if(allFat >= 200): #If the food item is way too high in Fat Total
        fs -= 8

    #Note: We don't need to do any math for Monounsaturated or Polyunsaturated Fats. If there's any in the product, add 2 points each.
    if(p_fat > 0): #Total of Ployunsaturated Fat greater than 0g
        fs += 2

    if(m_fat > 0):  #Total of Monounsaturated Fat greater than 0g
        fs += 2

    return fs

def fatsDivide(fs, divide):
    print("Quit [Q]")
    s_fat = input("Enter the amount of Saturated Fat: ")
    s_fat = isWholeNumber(s_fat)
    t_fat = input("Enter the amount of Trans Fat: ")
    t_fat = isWholeNumber(t_fat)
    allFat = input("Enter Total fat listed: ")
    allFat = isWholeNumber(allFat)
    p_fat = input("Enter the amount of Ployunsaturated Fat: ")
    p_fat = isWholeNumber(p_fat)
    m_fat = input("Enter the amount of Monounsaturated Fat: ")
    m_fat = isWholeNumber(m_fat)

    if((s_fat + t_fat) >= 80): #If the food item is way too high in Saturated and Trans Fat Total
        fs -= 8

    if((s_fat + t_fat)/divide <= 6): #Per Serving 
        fs += 1
    else:
        fs -= 1
    
    if((s_fat + t_fat) >= 30): #Total Saturated and Trans Fat is greater than 30g
        fs -= 2

    #Here, the fat is already Total
    if(allFat < 30): #Total of all Fat
        fs += 2
    elif(allFat > 50): #Total of all Fat greater than 55g
        fs -= 3
    else:
        fs -= 2 #30g or More and 50g or less Totals: -2

    if(allFat >= 200): #If the food item is way too high in Fat Total
        fs -= 8

    #Note: We don't need to do any math for Monounsaturated or Polyunsaturated Fats. If there's any in the product, add 2 points each.
    if(p_fat > 0): #Total of Ployunsaturated Fat greater than 0g
        fs += 2

    if(m_fat > 0):  #Total of Monounsaturated Fat greater than 0g
        fs += 2

    return fs

def ProteinMulti(fs, multi):
    print("Quit [Q]")
    protein = input("Enter the amount of protein: ")
    protein = isWholeNumber(protein)

    if(protein >= 12): #Per Serving 
        fs += 3
    
    protein *= multi  #To get the Total serving amount for Protein for the next condition
    if(protein >= 30): #The Total
        fs += 2

    return fs

def ProteinDivide(fs, divide):
    print("Quit [Q]")
    protein = input("Enter the amount of protein: ")
    protein = isWholeNumber(protein)

    if(protein >= 30): #The Total
        fs += 2

    protein /= divide  #To get the single serving amount for Protein for the next condition
    if(protein >= 12): #Per Serving 
        fs += 3

    return fs

def CholesterolMulti(fs, multi):
    print("Quit [Q]")
    chol = input("Enter the amount of Cholesterol: ")
    chol = isWholeNumber(chol)
    allFat = input("Enter the amount of Total Fat again: ")
    allFat = isWholeNumber(allFat)

    if(chol < 25): #Per Serving
        fs += 2
    else:
        fs -= 2

    chol *= multi  #To get the Total serving amount for Cholesterol for the next condition
    if(chol < 40): #Total Serving
        fs += 4
    else:
        fs -= 2

    allFat *= multi #To get the Total Fat serving amount for the next condition
    if((chol >= 40) and (allFat >= 35)):
        fs -= 5
    elif((chol >= 200) and (allFat >= 120)): #If the food item is way too high in Cholesterol and Fat Total
        fs -= 10

    if(chol >= 200): #If the food item is way too high in Cholesterol Total
        fs -= 10

    return fs

def CholesterolDivide(fs, divide):
    print("Quit [Q]")
    chol = input("Enter the amount of Cholesterol: ")
    chol = isWholeNumber(chol)
    allFat = input("Enter the amount of Total Fat again: ")
    allFat = isWholeNumber(allFat)

    if(chol < 40): #Total Serving
        fs += 4
    else:
        fs -= 2

    if((chol >= 40) and (allFat >= 35)):
        fs -= 5
    elif((chol >= 200) and (allFat >= 120)): #If the food item is way too high in Cholesterol and Fat Total
        fs -= 10

    if(chol >= 200): #If the food item is way too high in Cholesterol Total
        fs -= 10

    chol /= divide #To get the Total Fat serving amount for the next condition
    if(chol < 25): #Per Serving
        fs += 2
    else:
        fs -= 2

    return fs

def Sugar(fs):
    print("Quit [Q]")
    sugar = input("Enter the amount of Sugar: ")
    sugar = isWholeNumber(sugar)
    carbs = input("Enter the amount of Carbs again: ")
    carbs = isWholeNumber(carbs)
    sugarAns = input("Is it clear that this product has 'Added Sugars'? \nYes [Y]/ No [N]: ").lower()
    while(True):
        if((sugarAns == 'y') or (sugarAns == 'n') or (sugarAns =='q')):
            if(sugarAns == 'y'): #if it's clear is has added sugar
                sugarAdded = input("Is it more than 0g?: \nYes [Y]/ No [N]: ")
                if((sugarAdded == 'y') or (sugarAdded == 'n') or (sugarAdded =='q')):
                    break
                else:
                    print("You've entered a invalid option. Try again\n")
                    sugarAdded = input("Enter Answer: ")
            break #if not clear it has added sugar, break
        else:
            print("You've entered a invalid option. Try again\n")
            sugarAns = input("Enter Answer: ")


    if(sugar == 0): 
        fs += 1
    else:
        fs -= 2
    
    if(sugarAns == 'y' and sugarAdded == 'n' and sugar >= 1):
        fs += 2 #no Added Sugar
    elif(sugarAns == 'y' and sugarAdded == 'n' and sugar == 0):
        fs += 3 #no Added Sugar with 0 sugar, Extra bonus.
    elif(sugarAns == 'y' and sugarAdded == 'y'):
        fs -= 10 #Has Added Sugar. 
    elif(sugarAns == 'n' and sugar >= 10 and carbs >= 25 ):
        fs -= 6 #if it's not clear, but the sugars are high, -6. Not sure if it's "Added Sugar" but the sugar is too high
    elif(sugarAns == 'n' and sugar >= 1 and sugar < 10 and carbs >= 1 and carbs < 25 ):
        fs += 1 #if it's not clear, but the sugars are very low, +1
    elif(sugarAns == 'n' and sugar == 0):
        fs += 2
    else:
        fs += 0 #If nothing fits, add nothing

    if(sugar >= 100): #If the food item is way too high in Sugar Total
        fs -= 8

    return fs

def SodiumMulti(fs, multi):
    print("Quit [Q]")
    sodium = input("Enter the amount of Sodium: ")
    sodium = isWholeNumber(sodium)

    if(sodium < 450): #Per Serving 
        fs += 1
    else:
        fs -= 2

    sodium *= multi  #To get the Total serving amount for sodium for the next condition
    if(sodium < 1050): #The Total
        fs += 2
    elif(sodium > 1500):
        fs -= 3
    else:
        fs -= 2 # If not fits, -2 

    if(sodium >= 3500): #If the food item is way too high in Sodium Total
        fs -= 8

    return fs

def SodiumDivide(fs, divide):
    print("Quit [Q]")
    sodium = input("Enter the amount of Sodium: ")
    sodium = isWholeNumber(sodium)

    if(sodium < 1050): #The Total
        fs += 2
    elif(sodium > 1500):
        fs -= 3
    else:
        fs -= 2 # If not fits, -2 

    if(sodium > 3500): #If the food item is way too high in Sodium Total
        fs -= 8

    sodium /= divide  #To get the single serving amount for sodium for the next condition
    if(sodium < 450): #Per Serving 
        fs += 1
    else:
        fs -= 2

    return fs


print("Welcome to the Food Health Discord Program.")
input("Press Enter to Continue.")
clear_screen()

i = 0
FoodScore = 10
while i == 0:

    print("""Enter the Serving Size in Total of the item. Example, if you buy crazy bread and it has 8 sticks, enter the number '8'. 
    This number can't be Zero. To Quit: [Q] """)
    s_size = input("Enter Number: ").lower()
    s_size = isWholeNumber(s_size)
    
    if(s_size == 'q'): #quits the program.
        exit()
    clear_screen()
    i = 1
    
print("Next, when entering the numbers for Calories, Fat, Sugar, etc., will it be the total?")
ans = input("Yes [Y]/ No [N]/ Quit [Q]: ").lower()
i =0 # Reseting for the next while loop
while(i == 0):
    if(ans == 'q'):
        exit() #quits the program
    elif(ans == 'y'):
        break
    elif(ans == 'n'):
        break
    else:
        print("You've entered a invalid option. Try again\n")
        ans = input("Yes [Y]/ No [N]/ Quit [Q]: ")

clear_screen()

FoodScore = ingredients(FoodScore)
clear_screen()
#We're going to divide the total by the number of items purchased in total
#We're going to multiply the numbers by the number of items purchased.

if(ans == 'y'):
    FoodScore = CaloriesDivide(FoodScore, s_size)
elif(ans == 'n'):
    FoodScore = CaloriesMulti(FoodScore, s_size)
clear_screen()

if(ans == 'y'):
    FoodScore = CarbsDivide(FoodScore, s_size)
elif(ans == 'n'):
    FoodScore = CarbsMulti(FoodScore, s_size)
clear_screen()

if(ans == 'y'):
    FoodScore = fatsDivide(FoodScore, s_size)
elif(ans == 'n'):
    FoodScore = fatsMulti(FoodScore, s_size)
clear_screen()

if(ans == 'y'):
    FoodScore = ProteinDivide(FoodScore, s_size)
elif(ans == 'n'):
    FoodScore = ProteinMulti(FoodScore, s_size)
clear_screen()

if(ans == 'y'):
    FoodScore = CholesterolDivide(FoodScore, s_size)
elif(ans == 'n'):
    FoodScore = CholesterolMulti(FoodScore, s_size)
clear_screen()

FoodScore = Sugar(FoodScore)
clear_screen()

if(ans == 'y'):
    FoodScore = SodiumDivide(FoodScore, s_size)
elif(ans == 'n'):
    FoodScore = SodiumMulti(FoodScore, s_size)
clear_screen()

print("The Food Score is: " + str(FoodScore))
input("Press Enter to Close")

#The BMI calculator by Jorge Viso #Data used from CDC.gov and Healthline.com
#This program (So far...) serves as a basic questionairre with the function of assessing health based on user input

#The first set of arguments collects the users info to calculate BMI:
print("Hello! I am going to ask you a series of questions to determine your Body Mass Index. First of all, what is your name?")
username = input()
#end= argument used to format the greeting
print("Hey there",username, end ="! ")
print("What is your weight? (pounds)")
weight = float(input())
print("What is your height? (Inches)")
height = float(input())
#Here is the BMI formula
BMI = weight / (height ** 2) * 703
#Here are my recommendations for the users diet, depending on BMI output
lowcarbs = "Your carbohydrate intake is low, consider snack options like bananas, apples, and raisins to supplement more glucose!"
lowprotein = "Your protein intake is low, consider a quality whey or vegetarian based protein supplement in-between meals!"
lowfat = "Your fat intake is low, consider sliced avocado, almond butter, and olive oil to keep you satisfied and curb cravings!"
highcarbs = "Your carbohydrate intake is high, make an effort to avoid added sweeteners. If you already do, then simply be mindful of your carb consumption, as this is the main determinant of weight gain."
#In each scenario, the user is asked to input their rough or calculated macronutrient percentages and is given feedback depending on BMI
if BMI < 18.5:
    #Here I am formatting the value of BMI to reach only two decimal places
    print("Your current BMI is", format(BMI, "0.2f")+",","Which is classified as underweight.")
    print("In order to gain healthy weight, you must make an effort to consume plenty of protein, carbohydrate, and some fat. Speaking of macronutrients, what would you assume your current macronutrient percentages are?")
    #macro ratios are collected
    dailyfat = int(input("Fat% "))
    dailyprotein = int(input("Protein% "))
    dailycarbs = int(input("Carbs% "))
    #Sep and end arguments are used to format the totals
    print("Your current Macronutrient ratios are:", end = ' ')
    print(dailyfat, "% Fat", end = '-', sep ='')
    print(dailyprotein, "% Protein", end = '-', sep = '')
    print(dailycarbs, "% Carbs", sep = '')
    #the * string operation is used to repeat the variables as well as logical operators to determine output
    if dailycarbs < 30: print(lowcarbs * 1)
    if dailyprotein < 40: print(lowprotein * 1)
    else:
        print("This is a good ratio! Try to eat frequently to ensure you don't lose any more weight!")
#Each outcome performs the same basic procedure
if BMI >= 18.5 and BMI <= 24.9:
    print("Your current BMI is", format(BMI, "0.2f")+",","Which is classified as a healthy weight!")
    print("Whatever you're doing is working! But remember, maintaining weight is just as technical as losing or gaining it.")
    print("What would you estimate your current macronutrient ratios are?")
    dailyfat = int(input("Fat% "))
    dailyprotein = int(input("Protein% "))
    dailycarbs = int(input("Carbs% "))
    print("Your current Macronutrient ratios are:", end = ' ')
    print(dailyfat, "% Fat", end = '-', sep ='')
    print(dailyprotein, "% Protein", end = '-', sep = '')
    print(dailycarbs, "% Carbs", sep = '')
    if dailycarbs > 30: print(highcarbs * 1)
    else:
        print("This is a good ratio! Keep up the great work!")
if BMI >= 25.0 and BMI <= 29.9:
    print("Your current BMI is", format(BMI, "0.2f")+",","Which is classified as overweight.")
    print("In your case, the weight loss is not necessarily urgent, so I advise reaching for good sources of fat and protein while keeping a log of carb consumption!")
    print("What would you estimate your current macronutrient ratios are?")
    dailyfat = int(input("Fat% "))
    dailyprotein = int(input("Protein% "))
    dailycarbs = int(input("Carbs% "))
    print("Your current Macronutrient ratios are:", end = ' ')
    print(dailyfat, "% Fat", end = '-', sep ='')
    print(dailyprotein, "% Protein", end = '-', sep = '')
    print(dailycarbs, "% Carbs", sep = '')
    if dailycarbs > 25: print(highcarbs * 1)
    if dailyfat < 30: print(lowfat * 1)
    if dailyprotein < 55: print(lowprotein * 1)
    else:
        print("You are already on track to lose weight! What are you doing here!?!?")
if BMI > 30:
    print("Your current BMI is", format(BMI, "0.2f")+",","Which is classified as obese. But fear not, anyone can get healthy at any point in life! ")
    print("What would you estimate your current macronutrient ratios are?")
    dailyfat = int(input("Fat% "))
    dailyprotein = int(input("Protein% "))
    dailycarbs = int(input("Carbs% "))
    print("Your current Macronutrient ratios are:", end = ' ')
    print(dailyfat, "% Fat", end = '-', sep ='')
    print(dailyprotein, "% Protein", end = '-', sep = '')
    print(dailycarbs, "% Carbs", sep = '')
    if dailycarbs > 15: print(highcarbs * 1)
    if dailyprotein < 50: print(lowprotein * 1)
    if dailyfat < 35: print(lowfat * 1)
    else:
        print("You are already on track to lose weight.")

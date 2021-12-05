"""The Health Auditor"""
__author__ = "Jorge Viso"


# Data used from CDC.gov and Healthline.com
# This program serves as a basic questionnaire with the function of assessing health based on user input
# The first set of arguments uses a function to collect the users info to calculate BMI:
# In each scenario, the user is asked to input their rough or calculated macronutrient percentages and is given
# feedback depending on BMI


def underweight(bmi, lowcarbs, lowprotein):
    """The purpose of this function is to offer advice to the user who's weight is classified as underweight."""
    # Formatting the value of BMI to reach only two decimal places
    # BMI is given to user, with corresponding advice
    print("Your current BMI is", format(bmi, "0.2f") + ",", "Which is classified as underweight.")
    print(
        "In order to gain healthy weight, you must make an effort to consume plenty of protein, carbohydrate, "
        "and some fat. Speaking of macronutrients, what would you assume your current macronutrient percentages "
        "are?")
    # Macronutrient ratios are collected from user
    # A while statement is used to create a loop, in which the try/except statements are executed
    while True:
        try:
            dailyfat = int(input("Fat% "))
        except ValueError:
            print("Please enter a real number.")
            continue
        try:
            dailyprotein = int(input("Protein% "))
        except ValueError:
            print("Please enter a real number.")
            continue
        try:
            dailycarbs = int(input("Carbs% "))
        except ValueError:
            print("Please enter a real number.")
            continue
        # The macronutrient ratios are displayed in cascading format
        print("Your current Macronutrient ratios are:", end=' ')
        print(dailyfat, "% Fat", end='-', sep='')
        print(dailyprotein, "% Protein", end='-', sep='')
        print(dailycarbs, "% Carbs", sep='')
        # The * string operation is used to repeat the variables as well as logical operators to determine output The
        # if statements determine if any of the macronutrient percentages are too high or low, depending on the users
        # bmi
        if dailycarbs < 30:
            print(lowcarbs * 1)
        if dailyprotein < 40:
            print(lowprotein * 1)
        else:
            print("This is a good ratio! Try to eat frequently to ensure you don't lose any more weight!")
        break


# Each outcome performs the same basic procedure


def healthyweight(bmi, highcarbs):
    """The purpose of this function is to offer advice to the user who's weight is classified as healthy."""
    print("Your current BMI is", format(bmi, "0.2f") + ",", "Which is classified as a healthy weight!")
    print(
        "Whatever you're doing is working! But remember, maintaining weight is just as technical as losing or gaining "
        "it.")
    print("What would you estimate your current macronutrient ratios are?")
    # Same process as the other functions
    while True:
        try:
            dailyfat = int(input("Fat% "))
        except ValueError:
            print("Please enter a real number.")
            continue
        try:
            dailyprotein = int(input("Protein% "))
        except ValueError:
            print("Please enter a real number.")
            continue
        try:
            dailycarbs = int(input("Carbs% "))
        except ValueError:
            print("Please enter a real number.")
            continue
        print("Your current Macronutrient ratios are:", end=' ')
        print(dailyfat, "% Fat", end='-', sep='')
        print(dailyprotein, "% Protein", end='-', sep='')
        print(dailycarbs, "% Carbs", sep='')
        if dailycarbs > 30:
            print(highcarbs * 1)
        else:
            print("This is a good ratio! Keep up the great work!")
        break


def overweight(bmi, highcarbs, lowfat, lowprotein):
    """The purpose of this function is to offer advice to the user who's weight is classified as underweight."""
    print("Your current BMI is", format(bmi, "0.2f") + ",", "Which is classified as overweight.")
    print(
        "In your case, the weight loss is not necessarily urgent, so I advise reaching for good sources of fat and "
        "protein while keeping a log of carb consumption!")
    print("What would you estimate your current macronutrient ratios are?")
    while True:
        try:
            dailyfat = int(input("Fat% "))
        except ValueError:
            print("Please enter a real number.")
            continue
        try:
            dailyprotein = int(input("Protein% "))
        except ValueError:
            print("Please enter a real number.")
            continue
        try:
            dailycarbs = int(input("Carbs% "))
        except ValueError:
            print("Please enter a real number.")
            continue
        print("Your current Macronutrient ratios are:", end=' ')
        print(dailyfat, "% Fat", end='-', sep='')
        print(dailyprotein, "% Protein", end='-', sep='')
        print(dailycarbs, "% Carbs", sep='')
        if dailycarbs > 25:
            print(highcarbs * 1)
        if dailyfat < 30:
            print(lowfat * 1)
        if dailyprotein < 55:
            print(lowprotein * 1)
        else:
            print("You are already on track to lose weight!")
        break


def obese(bmi, highcarbs, lowprotein, lowfat):
    """The purpose of this function is to offer advice to the user who's weight is classified as obese."""
    print("Your current BMI is", format(bmi, "0.2f") + ",",
          "Which is classified as obese. But fear not, anyone can get healthy at any point in life! ")
    print("What would you estimate your current macronutrient ratios are?")
    while True:
        try:
            dailyfat = int(input("Fat% "))
        except ValueError:
            print("Please enter a real number.")
            continue
        try:
            dailyprotein = int(input("Protein% "))
        except ValueError:
            print("Please enter a real number.")
            continue
        try:
            dailycarbs = int(input("Carbs% "))
        except ValueError:
            print("Please enter a real number.")
            continue
        print("Your current Macronutrient ratios are:", end=' ')
        print(dailyfat, "% Fat", end='-', sep='')
        print(dailyprotein, "% Protein", end='-', sep='')
        print(dailycarbs, "% Carbs", sep='')
        if dailycarbs > 15:
            print(highcarbs * 1)
        if dailyprotein < 50:
            print(lowprotein * 1)
        if dailyfat < 35:
            print(lowfat * 1)
        else:
            print("You are already on track to lose weight.")
        break


def weightprogram():
    """The purpose of this function is to offer a weight program to the user."""
    print("Let me recommend an exercise program.")
    while True:
        try:
            # Here the user is prompted to enter what they believe to be their maximum one-repetition weight for each
            # major weight exercise
            benchmax = int(input("What do you think is the most weight you can bench press? "))
        except ValueError:
            print("Please Enter a real number.")
            continue
        benchweights = [(.8 * benchmax), (.85 * benchmax), (.9 * benchmax)]
        print("Here is my bench press recommendation.")
        for weight in benchweights:
            print("3 x", int(weight))
        try:
            squatmax = int(input("What do you think is the most weight you can squat? "))
        except ValueError:
            print("Please enter a real number.")
            continue
        squatweights = [(.6 * squatmax), (.65 * squatmax), (.7 * squatmax), (.75 * squatmax), (.8 * squatmax)]
        print("Here is my squat recommendation.")
        for weight in squatweights:
            print("4 x", int(weight))
        try:
            deadmax = int(input("Lastly, what is your maximum deadlift? "))
        except ValueError:
            print("Please enter a real number.")
            continue
        deadweights = [(.6 * deadmax), (.65 * deadmax), (.7 * deadmax), (.75 * deadmax), (.8 * deadmax)]
        print("Here is my deadlift recommendation.")
        for weight in deadweights:
            print("3 x", int(weight))
        break


def main():
    """The purpose of this function is to wrap up the program into a main menu."""
    # Here are my recommendations for the users diet, depending on BMI output
    lowcarbs = "Your carbohydrate intake is low, consider snack options like bananas, apples, and raisins to " \
               "supplement " \
               "more glucose! "
    lowprotein = "Your protein intake is low, consider a quality whey or vegetarian based protein supplement " \
                 "in-between " \
                 "meals! "
    lowfat = "Your fat intake is low, consider sliced avocado, almond butter, and olive oil to keep you satisfied and "
    "curb cravings! "
    highcarbs = "Your carbohydrate intake is high, make an effort to avoid added sweeteners. If you already do, " \
                "then simply be mindful of your carb consumption, as this is the main determinant of weight gain. "
    # here the program prompts the user to enter their username
    print(
        "Hello! I am going to ask you a series of questions to determine your Body Mass Index. First of all, "
        "what is your name?")
    username = input()
    # end= argument used to format the greeting
    print("Hey there", username, end="! ")
    print("What is your weight? (Pounds)")
    while True:
        try:
            weight = float(input())
        except ValueError:
            print("Please enter a real number.")
            continue
        print("What is your height? (Inches)")
        try:
            height = float(input())
        except ValueError:
            print("Please enter a real number")
            continue
        bmi = (weight / (height ** 2)) * 703
        if bmi < 18.5:
            underweight(bmi, lowcarbs, lowprotein)
        elif 18.5 <= bmi <= 24.9:
            healthyweight(bmi, highcarbs)
        elif 25.0 <= bmi <= 29.9:
            overweight(bmi, highcarbs, lowfat, lowprotein)
        else:
            obese(bmi, highcarbs, lowprotein, lowfat)
        weightprogram()
        print("That is all for now. Thank you!")


main()

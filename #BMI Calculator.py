#BMI Calculator
#Teacher remember you said that I had the permission to submit it late because I have excuse. Thank you Teacher.

system = input("Welcome to the BMI calculator. Would you like to use the imperial system or metric system? ")

while True:
      
    if system.lower() == "imperial system" or system.lower()=="the imperial system":
        try:
            weight = float(input("What is your weight (pounds)? "))
            height = float(input("What is your height (inches)?"))

            BMII= weight*703 / height**2
            print(f"Your BMI is (using the imperial system) is {BMII}.")

            if BMII <= 18:
                classif = "underweight"

            elif BMII >= 19 and BMII <= 24:
                classif = "healthy"

            elif BMII >= 25 and BMII <= 29:
                classif = "overweight"

            elif BMII >= 30 and BMII <= 39:
                classif = "obese"

            else:
                classif = "extremely obese"
            print(f"Your BMI (using the metric system) is {BMII} and you are {classif}")
            break


        except:
            print("Not valid numbers or inputs")
        finally:
            print("Thank you for using the BMI calculator")

    elif system.lower() == "metric system" or system.lower()== "the metric system":
        try:
            weight2 = float(input("What is your weight (kilograms)? "))
            height2 = float(input("What is your height (meters)? "))
            BMIM=weight2 / height2**2

            if BMIM <= 18:
                classif = "underweight"

            elif BMIM >= 19 and BMIM <= 24:
                classif = "healthy"

            elif BMIM >= 25 and BMIM <= 29:
                classif = "overweight"

            elif BMIM >= 30 and BMIM <= 39:
                classif = "obese"

            else:
                classif = "extremely obese"
            print(f"Your BMI (using the metric system) is {BMIM} and you are {classif}")
            break

        except:
            print("Not valid numbers or inputs")
        finally:
            print("Thank you for using the BMI calculator")
    else:
         print("Thats not in the options")



# Jay J. Patel and Julian Ornelas
# jpatel194@student.gsu.edu
# jornelas2@student.gsu.edu
# Section 008
# 11/14/22

from datetime import date

def inch_to_cm(user_feet,user_inches):
    total_inches = (user_feet * 12) + user_inches
    cm = total_inches * 2.54
    return cm

def pound_to_kg(user_pounds):
    total_kgs = user_pounds * 0.4535924
    return total_kgs

def BMI_Conversion(user_weight,user_height):
    weight = user_weight 
    height = (user_height / 100) ** 2
    BMI_Calculation = weight / height
    return BMI_Calculation


if __name__ == '__main__':

    print("Jay and Julian's Body Mass Index Calculator\n")

    # Requests and concatonates the name of the user.
    firstname = str(input("What is your first name?: "))
    lastname = str(input("What is your last name?: "))
    fullname = (f"{firstname} {lastname}")
    print()

    # Checks whether the user prefers to input measurements in imperial or metric.
    measurement_system = input("Do you use the imperial or metric system?: ")
    if measurement_system == "metric":
        imperial = False
    # With an invalid input, assumes user uses imperial.
    else:
        imperial = True

    print()

    # Depending on whether user chose imperial or metric, it asks for user measurements accordingly.
    if imperial:
        user_feet = int(input("Enter your height's feet: "))
        user_inches = int(input("Enter your height's inches: "))

        user_height = inch_to_cm(user_feet,user_inches)
        user_pounds = float(input("Enter your Weight in pounds: "))

        user_weight = pound_to_kg(user_pounds)

    else:
        user_height = float(input("Enter your your height in centimeters: "))
        user_weight = float(input("Enter your weight in kilograms: "))

    print()

    BMI = BMI_Conversion(user_weight, user_height)

    today_date = date.today()

    # What gets printed on the logging file.
    underweight = f'{today_date}, {fullname} your BMI is {BMI:.2f}, you are in the underweight range'
    overweight = f'{today_date}, {fullname} your BMI is {BMI:.2f}, you are in the overweight range'
    normalweight = f'{today_date}, {fullname} your BMI is {BMI:.2f}, you are in the normal weight range'

    # According to user BMI, runs a if/else to add corresponding text onto log file.
    if BMI < 18.5:
        print(underweight)
        B_M_I = open("BMI Record.txt", "a")
        B_M_I.write(f'{underweight} \n')
        B_M_I.close()

    elif 18.5 <= BMI < 24.9:
        print(normalweight)
        B_M_I = open("BMI Record.txt", "a")
        B_M_I.write(f'{normalweight} \n')
        B_M_I.close()
    else:
        print(overweight)
        B_M_I = open("BMI Record.txt", "a")
        B_M_I.write(f'{overweight} \n')
        B_M_I.close()

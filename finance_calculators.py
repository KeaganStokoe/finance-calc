# This is a Python program that allows the user to elect between the use of
# an investment calculator or a bond calculator. The investment calculator 
# calculates the amount of interest they'll earn. The bond calculator 
# calculates the amount they'll have to pay on a home loan.

# import required modules
import math

# provide initial explanation to user
print("Choose either 'investment' or 'bond' based on the descriptions below.")
print("Investment: to calculate the amount of interest you'll earn.")
print("Bond: to calculate the amount you'll have to pay on a home loan.")

# request user input which specifies calculator they wish to use
calculator_type = (input("Please elect the calculator you wish to use:")).lower()

# calculations based on investment calculator
if (calculator_type == "investment"):
    principal_value = float(input("Please enter the amount of money you are investing:"))
    interest_rate = float(input("Please enter the interest rate as a percentage. It is not necessary to include the % symbol:"))
    investment_period = float(input("Please enter the number of years you plan to invest for:"))
    interest_type = (input("Please indicate whether you wish to calculate simple or compound interest:")).lower()
    # simple interest calculation
    if (interest_type == "simple"):
        total_value = round((principal_value * (1 + ((interest_rate/100) * investment_period))), 2)
        print(f"The total value of your investment, based on the information supplied, is R{total_value}.")
    # compound interest calculation
    elif(interest_type == "compound"):
        total_value = round(principal_value * math.pow((1 + interest_rate/100), investment_period), 2)
        print(f"The total value of your investment, based on the information supplied, is R{total_value}.")
# calculations based on bond calculator
elif (calculator_type == "bond"):
    house_value = float(input("Please enter the present value of the house you wish to pay off:"))
    interest_rate = float(input("Please enter the interest rate as a percentage. It is not necessary to include the % symbol:"))
    investment_period = int(input("Please enter the number of months you intend to take to pay off the bond:"))
    # montly repayment calculation based on formula provided
    monthly_repayment = round((interest_rate/100/12 * house_value) / (1 - ((1 + interest_rate/100/12)**(-investment_period))), 2)
    print(f"Your monthly bond repayments, based on the information provided, will be R{monthly_repayment} per month for {investment_period} months.")
# catch input errors and provide error message
else:
    print("Unfortunately, we do not provide that calculator. Please, try again.")


    

    
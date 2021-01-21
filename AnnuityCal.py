import math

loan_principal = 'Loan principal: 1000'
final_output = 'The loan has been repaid!'
first_month = 'Month 1: repaid 250'
second_month = 'Month 2: repaid 250'
third_month = 'Month 3: repaid 500'

# write your code here
loan = int(input("Enter the loan principal:"))
need = input("""What do you want to calculate?
type "m" - for number of monthly payments,
type "p" - for the monthly payment:""")

if need == 'm':
    payment = int(input("Enter the monthly payment:"))
    result = math.ceil(loan / payment)
    if result == 1:
        word = "month"
    else:
        word = "months"
    print("It will take {0} {1} to repay the loan".format(result, word))
else:
    month = int(input("Enter the number of months:"))
    payment = loan % month
    if payment == 0:
        print("Your monthly payment = {0}".format(loan // month))
    else:
        usually_payment = math.ceil(loan / month)
        last_payment = loan - (usually_payment * (month - 1))
        print("Your monthly payment = {0} and the last payment = {1}".format(usually_payment, last_payment))

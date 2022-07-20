import argparse
import math
import sys

error = "Incorrect parameters"

def calculate_differentiate_payments():
    global user_credit_principal
    global calculated_interest
    global user_number_of_periods
    payments = []
    for i in range(0, user_number_of_periods):
        i += 1
        pay = math.ceil((user_credit_principal / user_number_of_periods) + (calculated_interest *(user_credit_principal - ((user_credit_principal * (i - 1)) / user_number_of_periods))))
        payments.append(pay)
        print("Month: " + str(i) +  ": paid out " + str(pay))
    calculated_total_paid = math.ceil(sum(payments))
    overpayment = calculated_total_paid - user_credit_principal
    print("Overpayment = " + str(overpayment))

def calculate_number_months():
    global user_credit_principal
    global user_monthly_payment
    global calculated_interest
    calculated_number_periods = math.ceil(math.log(user_monthly_payment / (user_monthly_payment - (calculated_interest * user_credit_principal)), 1 + calculated_interest))
    if calculated_number_periods <= 12:
        print("You need " + str(calculated_number_periods) + " months to repay this credit!")
    elif calculated_number_periods > 12 and calculated_number_periods % 12 == 0:
        print("You need " + str(calculated_number_periods // 12) + " years to repay this credit!")
    else:
        print("You need " + str(calculated_number_periods // 12) + " years and " + str(calculated_number_periods % 12) + " months to repay this credit!")
    calculated_total_paid = calculated_number_periods * user_monthly_payment
    overpayment = calculated_total_paid - user_credit_principal
    print("Overpayment = " + str(math.ceil(overpayment)))

def calculate_annuity_pay():
    global user_credit_principal
    global user_number_of_periods
    global calculated_interest
    calculated_annuity_pay = (user_credit_principal * (calculated_interest * ((1 + calculated_interest) ** user_number_of_periods)) / (
                            ((1 + calculated_interest) ** user_number_of_periods) - 1))
    calculated_annuity_pay = math.ceil(calculated_annuity_pay)
    ##calculated_annuity_pay = math.ceil((user_credit_principal * (calculated_interest * ((1 + calculated_interest) ** user_number_of_periods)) / ((1 + calculated_interest) ** user_number_of_periods) - 1))
    print("Your annuity payment = " + str(calculated_annuity_pay) + "!")
    calculated_total_paid = calculated_annuity_pay * user_number_of_periods
    overpayment = calculated_total_paid - user_credit_principal
    print("Overpayment = " + str(overpayment) + "!")
    
def calculate_credit_principal():
    global user_monthly_payment
    global user_number_of_periods
    global calculated_interest
    calculated_credit_principal = math.ceil(user_monthly_payment / ((calculated_interest * ((1 + calculated_interest) ** user_number_of_periods)) / (((1 + calculated_interest) ** user_number_of_periods) - 1)))
    calculated_total_paid = user_monthly_payment * user_number_of_periods
    overpayment = calculated_total_paid - calculated_credit_principal
    print("Your credit principal = " + str(calculated_credit_principal) + "!")
    print("Overpayment = " + str(math.ceil(overpayment)) + "!")

if len(sys.argv) >= 4:
    parser = argparse.ArgumentParser()
    parser.add_argument("--type", type=str, help="Type of calculation you would like to do")
    parser.add_argument("--payment", type=int, help="Monthly payment")
    parser.add_argument("--principal", type=int, help="Credit principal")
    parser.add_argument("--periods", type=int, help="Number of periods")
    parser.add_argument("--interest", type=float, help="Interest rate")
    args = parser.parse_args()
    
    if (args.payment or args.principal or args.periods or args.interest) < 0:
        print(error)
    else:
        if args.type not in ("annuity", "diff"):
            print(error)
        else:
            if args.type == 'diff' and args.payment is not None:
                print(error)
            else:
                if args.interest is None:
                    print(error)
                else:
                    user_credit_interest = args.interest
                    calculated_interest = user_credit_interest / (12 * 100)
                    if args.type == 'diff':
                        user_credit_principal = args.principal
                        user_number_of_periods = args.periods
                        calculate_differentiate_payments()
                    elif args.type == 'annuity':
                        if args.payment is None:
                            user_credit_principal = args.principal
                            user_number_of_periods = args.periods
                            calculate_annuity_pay()
                        elif args.principal is None:
                            user_monthly_payment = args.payment
                            user_number_of_periods = args.periods
                            calculate_credit_principal()
                        elif args.periods is None:
                            user_monthly_payment = args.payment
                            user_credit_principal = args.principal
                            calculate_number_months()
                        else:
                            print(error)
                    else:
                        print(error)

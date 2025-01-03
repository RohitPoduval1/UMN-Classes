def compute_monthly_payment():
    loan_amount = float(input("Enter a loan amount: "))
    annual_interest_rate = float(input("Enter an annual interest rate: "))
    loan_duration_months = int(input("Enter a loan duration (in months): "))
    r = (annual_interest_rate / 12)
    print("$", (r * loan_amount) / (1 - ((1 + r) ** -loan_duration_months)), sep="")
    

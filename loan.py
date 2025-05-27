mport math

# --- Constants and Configuration ---
MIN_LOAN_AMOUNT = 10000  # Minimum allowed loan amount
MAX_LOAN_AMOUNT = 10000000  # Maximum allowed loan amount
MIN_INTEREST_RATE = 1.0  # Minimum annual interest rate (percentage)
MAX_INTEREST_RATE = 30.0  # Maximum annual interest rate (percentage)
MIN_LOAN_TERM_MONTHS = 12  # Minimum loan term in months
MAX_LOAN_TERM_MONTHS = 360  # Maximum loan term in months (30 years)

# --- Function Definitions ---

def get_numeric_input(prompt, value_type=float, min_val=None, max_val=None):
    """
    Prompts the user for numeric input and validates it.

    Args:
        prompt (str): The message to display to the user.
        value_type (type): The desired type for the input (e.g., float, int).
        min_val (numeric, optional): The minimum allowed value. Defaults to None.
        max_val (numeric, optional): The maximum allowed value. Defaults to None.

    Returns:
        numeric: The validated numeric input.
    """
    while True:
        try:
            user_input = input(prompt)
            value = value_type(user_input)

            if min_val is not None and value < min_val:
                print(f"Error: Value must be at least {min_val}.")
            elif max_val is not None and value > max_val:
                print(f"Error: Value must be at most {max_val}.")
            else:
                return value
        except ValueError:
            print("Error: Invalid input. Please enter a numeric value.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

def calculate_emi(principal, annual_interest_rate, loan_term_months):
    """
    Calculates the Equated Monthly Installment (EMI) for a loan.

    Formula: EMI = P * r * (1 + r)^n / ((1 + r)^n - 1)
    Where:
        P = Principal loan amount
        r = Monthly interest rate (annual_interest_rate / 12 / 100)
        n = Loan term in months

    Args:
        principal (float): The total loan amount.
        annual_interest_rate (float): The annual interest rate in percentage (e.g., 10 for 10%).
        loan_term_months (int): The loan term in months.

    Returns:
        float: The calculated EMI, or None if calculation is not possible (e.g., zero interest rate).
    """
    if annual_interest_rate == 0:
        # Handle zero interest rate case: simple principal / months
        return principal / loan_term_months if loan_term_months > 0 else 0

    monthly_interest_rate = (annual_interest_rate / 100) / 12
    
    # Check for valid term to avoid division by zero or negative exponents
    if loan_term_months <= 0:
        print("Error: Loan term must be greater than zero months.")
        return None

    # Calculate (1 + r)^n
    power_factor = math.pow(1 + monthly_interest_rate, loan_term_months)

    # Calculate EMI
    emi = principal * monthly_interest_rate * power_factor / (power_factor - 1)
    return emi

def generate_repayment_schedule(principal, annual_interest_rate, loan_term_months, emi):
    """
    Generates and prints the detailed loan repayment schedule.

    Args:
        principal (float): The total loan amount.
        annual_interest_rate (float): The annual interest rate in percentage.
        loan_term_months (int): The loan term in months.
        emi (float): The calculated Equated Monthly Installment.
    """
    print("\n--- Loan Repayment Schedule ---")
    print(f"{'Month':<7} | {'Opening Balance':<18} | {'Interest Paid':<15} | {'Principal Paid':<16} | {'Closing Balance':<18}")
    print("-" * 90)

    remaining_balance = principal
    monthly_interest_rate = (annual_interest_rate / 100) / 12
    total_interest_paid = 0

    for month in range(1, loan_term_months + 1):
        # Calculate interest for the current month
        interest_paid = remaining_balance * monthly_interest_rate
        
        # Calculate principal paid for the current month
        # Ensure principal_paid does not exceed remaining_balance for the final month
        principal_paid = emi - interest_paid
        if month == loan_term_months:
            principal_paid = remaining_balance # Adjust for final payment to clear balance

        closing_balance = remaining_balance - principal_paid

        # Accumulate total interest paid
        total_interest_paid += interest_paid

        print(f"{month:<7} | {remaining_balance:<18.2f} | {interest_paid:<15.2f} | {principal_paid:<16.2f} | {closing_balance:<18.2f}")
        remaining_balance = closing_balance
        
        # If the remaining balance becomes very small due to floating point inaccuracies, set to 0
        if abs(remaining_balance) < 0.01:
            remaining_balance = 0.0

    print("-" * 90)
    print(f"\nTotal Interest Paid: {total_interest_paid:.2f}")
    print(f"Total Amount Paid (Principal + Interest): {(principal + total_interest_paid):.2f}")


def main():
    """
    Main function to run the loan calculator application.
    """
    print("Welcome to the Python Loan Calculator!")
    print("-------------------------------------")

    # Get loan details from the user with validation
    loan_amount = get_numeric_input(
        f"Enter the loan amount (between {MIN_LOAN_AMOUNT} and {MAX_LOAN_AMOUNT}): ",
        min_val=MIN_LOAN_AMOUNT,
        max_val=MAX_LOAN_AMOUNT
    )

    annual_interest_rate = get_numeric_input(
        f"Enter the annual interest rate (in % e.g., 7.5 for 7.5%, between {MIN_INTEREST_RATE} and {MAX_INTEREST_RATE}): ",
        min_val=MIN_INTEREST_RATE,
        max_val=MAX_INTEREST_RATE
    )

    loan_term_years = get_numeric_input(
        f"Enter the loan term in years (between {MIN_LOAN_TERM_MONTHS/12} and {MAX_LOAN_TERM_MONTHS/12}): ",
        value_type=int,
        min_val=MIN_LOAN_TERM_MONTHS/12,
        max_val=MAX_LOAN_TERM_MONTHS/12
    )
    loan_term_months = loan_term_years * 12

    print("\n--- Loan Summary ---")
    print(f"Loan Amount: {loan_amount:.2f}")
    print(f"Annual Interest Rate: {annual_interest_rate:.2f}%")
    print(f"Loan Term: {loan_term_years} years ({loan_term_months} months)")

    # Calculate EMI
    emi = calculate_emi(loan_amount, annual_interest_rate, loan_term_months)

    if emi is not None:
        print(f"\nYour Equated Monthly Installment (EMI): {emi:.2f}")
        
        # Generate and display the repayment schedule
        generate_repayment_schedule(loan_amount, annual_interest_rate, loan_term_months, emi)
    else:
        print("\nCould not calculate EMI. Please check your input values.")

    print("\nThank you for using the Loan Calculator!")

# Entry point of the script
if __name__ == "__main__":

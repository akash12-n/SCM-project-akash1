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
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple Loan Calculator</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Inter', sans-serif;
        }
        .form-input:focus {
            border-color: #60A5FA; /* Blue-400 */
            box-shadow: 0 0 0 2px #BFDBFE; /* Blue-200 */
        }
        .btn-primary {
            background-color: #3B82F6; /* Blue-500 */
        }
        .btn-primary:hover {
            background-color: #2563EB; /* Blue-600 */
        }
        .result-box {
            background-color: #EFF6FF; /* Blue-50 */
            border-left-width: 4px;
            border-color: #3B82F6; /* Blue-500 */
        }
    </style>
</head>
<body class="bg-gray-100 flex items-center justify-center min-h-screen p-4">

    <div class="bg-white p-6 md:p-8 rounded-xl shadow-2xl w-full max-w-lg">
        <h1 class="text-2xl md:text-3xl font-bold text-center text-gray-800 mb-6">Loan Calculator</h1>

        <div class="mb-4">
            <label for="loanAmount" class="block text-sm font-medium text-gray-700 mb-1">Loan Amount ($)</label>
            <input type="number" id="loanAmount" name="loanAmount" placeholder="e.g., 10000" class="form-input w-full px-4 py-2.5 border border-gray-300 rounded-lg shadow-sm focus:outline-none sm:text-sm" value="10000">
        </div>

        <div class="mb-4">
            <label for="interestRate" class="block text-sm font-medium text-gray-700 mb-1">Annual Interest Rate (%)</label>
            <input type="number" id="interestRate" name="interestRate" placeholder="e.g., 5" step="0.01" class="form-input w-full px-4 py-2.5 border border-gray-300 rounded-lg shadow-sm focus:outline-none sm:text-sm" value="5">
        </div>

        <div class="mb-6">
            <label for="loanTerm" class="block text-sm font-medium text-gray-700 mb-1">Loan Term (Years)</label>
            <input type="number" id="loanTerm" name="loanTerm" placeholder="e.g., 5" class="form-input w-full px-4 py-2.5 border border-gray-300 rounded-lg shadow-sm focus:outline-none sm:text-sm" value="5">
        </div>

        <button id="calculateBtn" class="btn-primary w-full text-white font-semibold py-3 px-4 rounded-lg shadow-md hover:shadow-lg transition-all duration-150 focus:outline-none focus:ring-2 focus:ring-blue-400 focus:ring-opacity-75">
            Calculate
        </button>

        <div id="resultsArea" class="mt-6 space-y-3 hidden">
            <h2 class="text-xl font-semibold text-gray-700 mb-3">Results:</h2>
            <div class="result-box p-4 rounded-md">
                <p class="text-sm text-gray-600">Monthly Payment:</p>
                <p id="monthlyPayment" class="text-lg font-semibold text-blue-600">$0.00</p>
            </div>
            <div class="result-box p-4 rounded-md">
                <p class="text-sm text-gray-600">Total Interest Paid:</p>
                <p id="totalInterest" class="text-lg font-semibold text-blue-600">$0.00</p>
            </div>
            <div class="result-box p-4 rounded-md">
                <p class="text-sm text-gray-600">Total Amount Paid:</p>
                <p id="totalAmount" class="text-lg font-semibold text-blue-600">$0.00</p>
            </div>
        </div>
        <div id="errorBox" class="mt-4 p-3 rounded-md text-sm text-center hidden bg-red-100 text-red-700"></div>

    </div>

    <script>
        const loanAmountInput = document.getElementById('loanAmount');
        const interestRateInput = document.getElementById('interestRate');
        const loanTermInput = document.getElementById('loanTerm');
        const calculateBtn = document.getElementById('calculateBtn');
        const resultsArea = document.getElementById('resultsArea');
        const monthlyPaymentEl = document.getElementById('monthlyPayment');
        const totalInterestEl = document.getElementById('totalInterest');
        const totalAmountEl = document.getElementById('totalAmount');
        const errorBox = document.getElementById('errorBox');

        calculateBtn.addEventListener('click', () => {
            // Clear previous errors and hide results
            errorBox.classList.add('hidden');
            errorBox.textContent = '';
            resultsArea.classList.add('hidden');

            const principal = parseFloat(loanAmountInput.value);
            const annualInterestRate = parseFloat(interestRateInput.value);
            const loanTermYears = parseInt(loanTermInput.value);

            if (isNaN(principal) || principal <= 0 ||
                isNaN(annualInterestRate) || annualInterestRate < 0 ||
                isNaN(loanTermYears) || loanTermYears <= 0) {
                errorBox.textContent = 'Please enter valid positive numbers for all fields.';
                errorBox.classList.remove('hidden');
                return;
            }

            const monthlyInterestRate = (annualInterestRate / 100) / 12;
            const numberOfPayments = loanTermYears * 12;

            let monthlyPayment;
            if (monthlyInterestRate === 0) { // Handle zero interest rate
                monthlyPayment = principal / numberOfPayments;
            } else {
                monthlyPayment = principal * (monthlyInterestRate * Math.pow(1 + monthlyInterestRate, numberOfPayments)) / (Math.pow(1 + monthlyInterestRate, numberOfPayments) - 1);
            }

            const totalAmountPaid = monthlyPayment * numberOfPayments;
            const totalInterestPaid = totalAmountPaid - principal;

            if (isNaN(monthlyPayment) || !isFinite(monthlyPayment)) {
                 errorBox.textContent = 'Could not calculate payment. Please check your inputs (e.g., interest rate might be too high for the term).';
                errorBox.classList.remove('hidden');
                return;
            }

            monthlyPaymentEl.textContent = `$${monthlyPayment.toFixed(2)}`;
            totalInterestEl.textContent = `$${totalInterestPaid.toFixed(2)}`;
            totalAmountEl.textContent = `$${totalAmountPaid.toFixed(2)}`;

            resultsArea.classList.remove('hidden');
        });
    </script>

</body>
</html>
if __name__ == "__main__":

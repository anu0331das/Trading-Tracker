# Author   : Anurag Dasgupta  
# Email    : asdasgupta@umass.edu
# Spire ID : 35147486

# (DICTIONARY) Maps tickers to their point values (MES = $5/pt, MNQ = $2/pt)
contract_data = {
    "MES": 5.0,
    "MNQ": 2.0
}


#FUNCTION 1
def get_multiplier(ticker):
    """ This just grabs the dollar value from my dictionary. """
    # Requirement: Retrieve value by key from dictionary
    return contract_data.get(ticker.upper(), 0)

#FUNCTION 2
def calculate_pl(ticker, entry, exit, qty, direction):
    """ This is the math function that handles Longs vs Shorts. """
    mult = get_multiplier(ticker)
    
    # (BRANCHING AND EXPRESSIONS)
    if direction.lower() == "long":
        points = exit - entry
    elif direction.lower() == "short":
        points = entry - exit
    else:
        points = 0
        
    # Requirement: Arithmetic Expression
    return points * mult * qty

#FUNCTION3
def save_trade(trade_info):
    """ This writes my trade results into a log file so I don't lose them. My 'trade log' """
    # Requirement: Writing to a file (.txt)
    file = open("trade_log.txt", "a")
    file.write(trade_info + "\n")
    file.close()

#FUNCTION 4
def get_valid_ticker():
    """ I only trade Micros, so this keeps me from entering the wrong ticker. """
    while True:
        t = input("Enter Ticker (MES/MNQ): ").upper()
        # Requirement: Logical Operators (or)
        if t == "MES" or t == "MNQ":
            return t
        print("Invalid ticker! Please use MES or MNQ.")

# (TESTING) runs fake trades to ensure math works correctly.
def run_tests():
    
    print("--- System Self-Check ---")
    
    # Test 1: 1 contract MES, Long, 10 point gain should be $50.00
    test1 = calculate_pl("MES", 4500, 4510, 1, "long")
    if test1 == 50.0:
        print("Test 1 (MES Long): Passed!")
    else:
        print("Test 1: FAILED")

    # Test 2: 1 contract MNQ, Short, 20 point price drop should be $40.00
    test2 = calculate_pl("MNQ", 15000, 14980, 1, "short")
    if test2 == 40.0:
        print("Test 2 (MNQ Short): Passed!")
    else:
        print("Test 2: FAILED")
    print("--- End of Self-Check ---\n")

# --- Requirement: Functions (5 of 5) ---
def main():
    """ This is the main part of the program that talks to the user. """
    print("--- Futures Trade Tracker ---")
    
    # Requirement: Advanced Feature (List Comprehension)
    # Requirement: List/Sequence usage
    tickers_list = [t for t in contract_data.keys()]
    print("Current tickers supported: " + str(tickers_list))

    # Requirement: Loops (While)
    keep_going = "y"
    while keep_going == "y":
        ticker = get_valid_ticker()
        
        # Requirement: Input/Try for error handling
        try:
            # Requirement: Casting (float and int)
            entry = float(input("Entry Price: "))
            exit_p = float(input("Exit Price: "))
            qty = int(input("Number of Contracts: "))
        except ValueError:
            print("Error: Please enter numbers only!")
            continue # Requirement: Continue

        direction = input("Direction (Long/Short): ").lower()
        
        # Requirement: Logical (and/not)
        if not (direction == "long" or direction == "short"):
            print("Invalid direction! Type long or short.")
            continue

        # Calculate result
        total_pl = calculate_pl(ticker, entry, exit_p, qty, direction)
        
        # Requirement: Nesting (Branching inside a loop)
        if total_pl >= 0:
            result_msg = "WIN"
        else:
            result_msg = "LOSS"
            
        final_string = result_msg + " | " + ticker + " | P&L: $" + str(total_pl)
        print("Result: " + final_string)
        
        # Log to file
        save_trade(final_string)
        
        # Requirement: Logical / Choice to exit
        keep_going = input("Add another trade? (y/n): ").lower()
        
        # Requirement: Break
        if keep_going != "y":
            break

    print("Program closed. All trades saved to trade_log.txt")


#Final Run
# First I verify the math, then I start the actual logger
run_tests()
main()
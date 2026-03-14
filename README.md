A Python program that helps me organize and log my futures trading, specifically for MES (Micro S&P 500) and MNQ (Micro Nasdaq) contracts. The program will calculate the Profit and Loss (P&L) of individual trades based on the contract's tick value and the direction of the trade (Long or Short), then save those results into a persistent text file to keep a history of my trading performance.P

The project has these 6 functions:

    get_multiplier(ticker): A function that uses a dictionary to look up the dollar per point value for a specific ticker (e.g., MES is $5, MNQ is $2). This uses a dictionary to retrieve values by key.

    calculate_pl(ticker, entry, exit, qty, direction): A function for calculating the math. It will use branching (if-elif-else) to determine the calculation based on whether the trade was "Long" or "Short." It uses arithmetic expressions to find the final P&L.

    get_valid_ticker(): A function that uses a while loop and logical operators (or) to ensure the user only enters "MES" or "MNQ." This handles the requirement for meaningful loops and logical expressions.

    save_trade(trade_info): A function that handles the File I/O requirement. It will open a .txt file in "append" mode to save the trade details so the data isn't lost when the program closes.

    run_tests(): A function dedicated to Testing. It will call calculate_pl with hardcoded values and use if/else statements to print whether the output matches the expected result. This provides tangible proof of testing.

    main(): The "controller" function. It will use a while loop to allow for multiple trade entries in one sitting. It will include try/except blocks to handle invalid price inputs (casting strings to floats) and use nesting (a branch inside the loop) to categorize trades as a "Win" or "Loss." It will also use an advanced feature (list comprehension) to display supported tickers.

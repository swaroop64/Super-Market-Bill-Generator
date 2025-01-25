# Super-Market-Bill-Generator
### Overview
The script is a Python-based program designed to simulate a billing system for a supermarket. It allows users to select items, specify quantities, and generate a detailed bill including GST. The system is interactive, providing prompts for user inputs and displaying appropriate responses based on those inputs.

### Key Features
1. **User Interaction**: The script prompts the user for their name, item choices, and quantities.
2. **Item List Display**: Shows a predefined list of items with their prices.
3. **Item Selection and Purchase**: Allows the user to select items and specify quantities.
4. **Price Calculation**: Calculates the total price, GST, and final price.
5. **Bill Generation**: Generates and prints a detailed bill with itemized costs, total amount, GST, and final amount.
6. **Error Handling**: Provides feedback for invalid inputs and out-of-stock items.

### Technologies Used
- **Python**: The programming language used to write the script.
- **datetime module**: Used to display the current date and time on the bill.

### Functionality Breakdown

1. **Introduction and User Input**:
    - The script starts with a welcome message.
    - Prompts the user to enter their name.
    - Displays a greeting with the user's name.

2. **Item List Display**:
    - A hardcoded list of items and their prices is displayed if the user chooses to view it.

3. **Item Selection and Purchase Loop**:
    - The user is repeatedly prompted to either buy an item or exit.
    - If the user chooses to buy:
        - The user enters the item name and quantity.
        - The script checks if the item is in the predefined dictionary of items.
        - If the item is available, the price is calculated and added to the total.
        - The item details (name, quantity, price) are stored in lists for later use.
        - The total price and GST are updated.

4. **Bill Generation**:
    - After exiting the purchase loop, the user is asked if they want to print the bill.
    - If the user chooses to print and there are purchased items:
        - A formatted bill is printed with the following details:
            - Supermarket name and location.
            - Customer name and current date and time.
            - Itemized list of purchases with serial number, item name, quantity, and price.
            - Total amount before GST.
            - GST amount.
            - Final amount after adding GST.
            - A thank you message.

5. **Error Handling**:
    - The script handles invalid inputs by displaying appropriate messages.
    - Checks for out-of-stock items and informs the user if an item is not available.

### Example Workflow
1. User starts the script.
2. User enters their name and chooses to view the item list.
3. User decides to buy items, enters the item names and quantities.
4. The script calculates the total price and updates the list of purchased items.
5. User finishes shopping and chooses to print the bill.
6. The script prints a detailed bill including itemized costs, total amount, GST, and final amount.

This script is a simple and effective way to simulate a supermarket billing system, providing a hands-on way to understand basic concepts in programming, user interaction, and billing processes.

--

Feel free to explore, modify, and improve the project. Contributions are welcome!

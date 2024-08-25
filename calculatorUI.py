import tkinter as tk
from operations.add import add
from operations.subtract import subtract
from operations.multiply import multiply
from operations.divide import division

# Create the main window
root = tk.Tk()
root.title("Calculator")

# input/output widget
entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief="solid")
entry.grid(row=0, column=0, columnspan=4)

def update_entry(text: str) -> None:
    """
    Updates the entry widget by appending the provided text.

    Args:
        text: The text to append to the current content of the entry widget.

    Returns:
        None
    """
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current_text + text)

def evaluate() -> None:
    """
    Evaluates the arithmetic expression in the entry widget and displays the result.

    This function handles basic arithmetic operations (+, -, *, /) and updates
    the entry widget with the result. If the expression is invalid, an error
    message is displayed.

    Returns:
        None
    """
    expression = entry.get()
    try:
        if '+' in expression:
            operands = expression.split('+')
            result = add(float(operands[0]), float(operands[1]))
        elif '-' in expression:
            operands = expression.split('-')
            result = subtract(float(operands[0]), float(operands[1]))
        elif '*' in expression:
            operands = expression.split('*')
            result = multiply(float(operands[0]), float(operands[1]))
        elif '/' in expression:
            operands = expression.split('/')
            result = division(float(operands[0]), float(operands[1]))
        else:
            result = "Error"
        
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def clear() -> None:
    """
    Clears the content of the entry widget.

    This function deletes all text currently displayed in the entry widget.

    Returns:
        None
    """
    entry.delete(0, tk.END)

def on_button_click(symbol: str) -> None:
    """
    Handles button clicks and updates the entry widget based on the symbol.

    Args:
        symbol: The symbol of the button that was clicked. It can be a number,
                operator, 'C' for clear, or '=' for evaluate.

    Returns:
        None
    """
    if symbol == "=":
        evaluate()
    elif symbol == "C":
        clear()
    else:
        update_entry(symbol)

# Define the calculator buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

# Create buttons and add them to the grid
row = 1
col = 0
for button in buttons:
    action = lambda x=button: on_button_click(x)
    tk.Button(root, text=button, width=5, height=2, font=('Arial', 18), command=action).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Start the Tkinter event loop
root.mainloop()

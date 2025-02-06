import tkinter as tk

# Function to update the input field
def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)  # Clear the current entry field
    entry.insert(tk.END, current + value)  # Append the clicked value to the entry

# Function to clear the entry field
def clear():
    entry.delete(0, tk.END)

# Function to evaluate the expression
def evaluate():
    try:
        result = eval(entry.get())  # Using eval to evaluate the string as a mathematical expression
        entry.delete(0, tk.END)  # Clear the entry field
        entry.insert(tk.END, result)  # Insert the result into the entry field
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Initialize the main window
root = tk.Tk()
root.title("Calculator")

# Create the input field for the calculator
entry = tk.Entry(root, width=20, font=("Arial", 24), borderwidth=2, relief="solid", justify="right")
entry.grid(row=0, column=0, columnspan=4)

# Button layout: buttons for digits and operations
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

# Create the buttons dynamically
for (text, row, col) in buttons:
    if text == 'C':
        btn = tk.Button(root, text=text, width=5, height=2, font=("Arial", 18), command=clear)
    elif text == '=':
        btn = tk.Button(root, text=text, width=5, height=2, font=("Arial", 18), command=evaluate)
    else:
        btn = tk.Button(root, text=text, width=5, height=2, font=("Arial", 18), command=lambda t=text: button_click(t))
    btn.grid(row=row, column=col)

# Start the main event loop to run the calculator
root.mainloop()
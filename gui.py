import tkinter as tk
from tkinter import ttk
from calculator import CalcLexer, CalcParser


class CalculatorApp:
    def __init__(self, master):
        # Initialize the Tkinter application
        self.master = master
        master.title("Calculator")

        # Create lexer and parser instances
        self.lexer = CalcLexer()
        self.parser = CalcParser()

        # Create entry widget for displaying input and result
        self.entry = ttk.Entry(master, width=30)
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Define buttons layout
        buttons = [
            ("7", 1, 0),
            ("8", 1, 1),
            ("9", 1, 2),
            ("*", 1, 3),
            ("4", 2, 0),
            ("5", 2, 1),
            ("6", 2, 2),
            ("+", 2, 3),
            ("1", 3, 0),
            ("2", 3, 1),
            ("3", 3, 2),
            ("-", 3, 3),
            ("C", 4, 0),
            ("0", 4, 1),
            ("=", 4, 2),
            ("/", 4, 3),
        ]

        # Create buttons and assign their functionality
        for text, row, col in buttons:
            ttk.Button(
                master, text=text, command=lambda t=text: self.on_button_click(t)
            ).grid(row=row, column=col, padx=5, pady=5)

        # Configure grid weights for responsive layout
        master.grid_columnconfigure(0, weight=1)
        master.grid_columnconfigure(1, weight=1)
        master.grid_columnconfigure(2, weight=1)
        master.grid_columnconfigure(3, weight=1)
        master.grid_rowconfigure(0, weight=1)
        master.grid_rowconfigure(1, weight=1)
        master.grid_rowconfigure(2, weight=1)
        master.grid_rowconfigure(3, weight=1)
        master.grid_rowconfigure(4, weight=1)

    def on_button_click(self, value):
        # Handle button click events
        if value == "=":
            # Get the input expression from the entry widget
            expression = self.entry.get()

            # Parse the input expression and evaluate
            result = self.parser.parse(self.lexer.tokenize(expression))
            calculation_result = self.parser.evaluate(result)

            # Calculate prefix and postfix notations
            prefix_notation = self.parser.prefix(result)
            postfix_notation = self.parser.postfix(result)

            # Display calculation result, prefix notation, and postfix notation in the terminal
            print("Input Expression:", expression)
            print("Calculation Result:", calculation_result)
            print("Prefix Notation:", prefix_notation)
            print("Postfix Notation:", postfix_notation)

            # Update the entry widget with the calculation result
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(calculation_result))
        elif value == "C":
            # Clear the input field
            self.entry.delete(0, tk.END)
        else:
            # Append the clicked button value to the input field
            self.entry.insert(tk.END, value)

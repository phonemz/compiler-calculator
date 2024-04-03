import tkinter as tk
from calculator import CalcLexer, CalcParser


class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")

        self.input_entry = tk.Entry(root)
        self.input_entry.pack()

        self.calculate_button = tk.Button(
            root, text="Calculate", command=self.calculate
        )
        self.calculate_button.pack()

        self.result_label = tk.Label(root, text="Result: ")
        self.result_label.pack()

        self.parser = CalcParser()

    def calculate(self):
        expression = self.input_entry.get()
        result = self.parser.parse(CalcLexer().tokenize(expression))
        self.result_label.config(text=f"Result: {result}")


if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()

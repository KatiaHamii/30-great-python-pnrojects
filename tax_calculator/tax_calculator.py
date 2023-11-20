import customtkinter as ctk


class TaxCalculator:
    def __init__(self):
        #Initialize our window
        self.window = ctk.CTk()
        self.window.title("Tax Caldulator")
        self.window.geometry('200 * 200')
        self.window.resizable(False, False)

        #Income label and entry
        self.padding:dict = {'padx' : 20, 'pady' : 10}
        self.income_label = ctk.CTkLabel(self.window, text="Income:")
        self.income_label.grid(row=0, column=0, **self .padding)
        self.income_entry = ctk.CTkEntry(self.window)
        self.income_entry.grid(row=0, column=1, **self.padding)

        # Tax label and entry
        self.padding: dict = {'padx': 20, 'pady': 10}
        self.tax_label = ctk.CTkLabel(self.window, text="Tax percentage:")
        self.tax_label.grid(row=1, column=0, **self.padding)
        self.tax_entry = ctk.CTkEntry(self.window)
        self.tax_entry.grid(row=1, column=1, **self.padding)

        #Result label
        self.padding: dict = {'padx': 20, 'pady': 10}
        self.result_label = ctk.CTkLabel(self.window, text="Tax part:")
        self.result_label.grid(row=2, column=0, **self.padding)
        self.result_entry = ctk.CTkEntry(self.window)
        self.result_entry.insert(0, '0')
        self.result_entry.grid(row=2, column=1, **self.padding)

        self.your_pure_income = ctk.CTkLabel(self.window, text="Your pure income:")
        self.your_pure_income.grid(row=3, column=0, **self.padding)
        self.your_pure_income = ctk.CTkEntry(self.window)
        self.your_pure_income.insert(0, '0')
        self.your_pure_income.grid(row=3, column=1, **self.padding)

        # Calculate button
        self.calculate_button = ctk.CTkButton(self.window, text='Calculate', command=self.calculate_tax)
        self.calculate_button.grid(row=4, column=1, **self.padding)

    def update_result(self, text: str, text2 : str):
        self.result_entry.delete(0, ctk.END)
        self.result_entry.insert(0, text)
        self.your_pure_income.delete(0, ctk.END)
        self.your_pure_income.insert(0, text2)

    def calculate_tax(self):
        try:
            income: float = float(self.income_entry.get())
            tax_rate: float = float(self.tax_entry.get())
            tax_part = income*(tax_rate/100)
            self.update_result(f'€ {tax_part}',  f'€ {income -(income*(tax_rate/100)):,.2f}' )
        except ValueError:
            self.update_result('Invalid input')

    def run(self):
        self.window.mainloop()


if __name__ == '__main__':
    tc = TaxCalculator()
    tc.run()



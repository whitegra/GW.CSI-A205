import tkinter as t
from tkinter import messagebox

class GWinvestmentCalculatorGUI:
    def __init__(self):
        #main window createtio + titole
        self.window = t.Tk()
        self.window.title("Investment Calculator")

        # Set the window bg color, create widgets, and start the GUI loop for events
        self.window.config(bg="#FFCCFF")#light pink bg
        self.create_widgets()
        self.window.mainloop()

    # CREATE WIDGETS FOR INFORMATION AND CALCULATIONS:
    def create_widgets(self):
        """Purpose: Creates the widgets for entry fields and buttons"""
        # Frame to hold the widgets, it will inherit the window background color 
        frame = t.Frame(self.window, bg="#FFCCFF")
        frame.pack(padx=25, pady=25)

        #ENTRY FIELD TO ENTER AMOUNT
        t.Label(frame, text="Investment Amount($):").pack(anchor='w')
        self.investment_entry = t.Entry(frame)
        self.investment_entry.pack(fill='x', pady=10)

        #ENTRY FIELD FOR INTREST RATE
        t.Label(frame, text="Interest Rate (Annual%):").pack(anchor='w')
        self.interest_rate_entry = t.Entry(frame)
        self.interest_rate_entry.pack(fill='x', pady=10)

        #ENTRY FIELD FOR NUMBER OF YEARS OF INVESTMET
        t.Label(frame, text="Investment Time (in years):").pack(anchor='w')
        self.years_entry = t.Entry(frame)
        self.years_entry.pack(fill='x', pady=10)

        #FUTURE INVESTMENT VALUE: 
        t.Label(frame, text="Future Investment Value:").pack(anchor='w')
        self.future_value_label = t.Label(frame, text="")
        self.future_value_label.pack(fill='x', pady=10)

        # CREATE BUTTONS AND FRAMES
        buttons_frame = t.Frame(self.window, bg="#FF99FF")
        buttons_frame.pack(pady=10)

        # Calculate button
        calculate_button = t.Button(buttons_frame, text="Calculate", command=self.calculate_future_investment)
        calculate_button.pack(side='left', padx=5)

        # Exit button
        exit_button = t.Button(buttons_frame, text="Quit", command=self.window.quit)
        exit_button.pack(side='right', padx=5)

    def calculate_future_investment(self):
        """Purpos: to calculate the future value of the investment."""
        try:
            #get user input for investment value, the intrest rate (anually) and the number of years
            investment = float(self.investment_entry.get())
            annual_rate = float(self.interest_rate_entry.get()) / 100
            years = int(self.years_entry.get())

            #calculate monthly intrest rate from hte yearly one
            monthly_rate = annual_rate / 12

            #then compute the future value of investment
            future_value = investment * ((1 + monthly_rate) ** (years * 12))

            #THIS IS TO DISPLAY THE FUTURE VALUE
            self.future_value_label.config(text=f"${future_value:,.2f}")
        except ValueError:
            #except if there is an error so the program dosent break
            messagebox.showerror("Invalid Input")

# Run the program
if __name__ == "__main__":
    GWinvestmentCalculatorGUI()

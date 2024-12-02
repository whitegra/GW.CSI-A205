import tkinter as t
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class GWgraphGeneratorGUI:
    def __init__(self):
        # Create the main window
        self.window = t.Tk()
        #add a title
        self.window.title("Gracie's Grade Graph Generator")
        self.window.config(bg="#E6E6FA")  #set the bg to lavender

        #Create the GUI layout with widgets
        self.create_widgets()
        #Start the main event loop 
        self.window.mainloop()

    def create_widgets(self):
        """Purpose: Creates the input fields, buttons, and frames for the GUI program."""
        #create the input frame for the user's entered data:
        input_frame = t.Frame(self.window, bg="#CDCDFA", pady=10) #make the input frame and set the bg color 
        input_frame.pack() #pack it 

        #now create the input fields for each category of grades
        t.Label(input_frame, text="Quizzes:").pack(anchor='w')
        self.quizzes_entry = t.Entry(input_frame)
        self.quizzes_entry.pack(fill='x', padx=5, pady=5)

        t.Label(input_frame, text="Project:").pack(anchor='w')
        self.project_entry = t.Entry(input_frame)
        self.project_entry.pack(fill='x', padx=5, pady=5)

        t.Label(input_frame, text="Midterm:").pack(anchor='w')
        self.midterm_entry = t.Entry(input_frame)
        self.midterm_entry.pack(fill='x', padx=5, pady=5)

        t.Label(input_frame, text="Final:").pack(anchor='w')
        self.final_entry = t.Entry(input_frame)
        self.final_entry.pack(fill='x', padx=5, pady=5)

        #dropdown menu to select chart type
        t.Label(input_frame, text="Select Graph Type:").pack(anchor='w')
        self.graph_type = t.StringVar()
        self.graph_type.set("Pie Graph")  #make the default chart type the pie chart
        graph_menu = t.OptionMenu(input_frame, self.graph_type, "Pie Graph", "Bar Graph")#create the option menu 
        graph_menu.pack(fill='x', padx=5, pady=5) #pack the option menu 

        #create te frame to hold the buttons
        button_frame = t.Frame(self.window, pady=10)
        button_frame.pack()

        #'Generate Graph' button
        generate_button = t.Button(button_frame, text="Generate Graph", command=self.generate_graph)
        generate_button.pack(side='left', padx=5) #pack it to the left 

        #make the quit button
        quit_button = t.Button(button_frame, text="Quit", command=self.window.quit)
        quit_button.pack(side='right', padx=5)

        #create the frame to display the final graph
        self.graph_frame = t.Frame(self.window)
        self.graph_frame.pack(pady=10) #pack it

    def generate_graph(self):
        """Purpose: Generates and displays the graph based on user input data and graph selection."""
        # use the try method in case there is an error so it will not break the program
        try:
            #get and assign the user's input values into the categories of grades:
            project = float(self.project_entry.get())
            quizzes = float(self.quizzes_entry.get())
            midterm = float(self.midterm_entry.get())
            final = float(self.final_entry.get())

            # ensure all of the percentages add to 100% of the total grade:
            data = [project, quizzes, midterm, final] #here is the list of the users inputted data
            if sum(data) != 100: #if it dosent equal 100 then raise the error messagebox and return to try again
                messagebox.showerror("Input Error", "The total of all the grade percentages must equal 100%.")
                return

            #if there is an existing graph in the graph widged frame then erase it before displaying the next one
            for widget in self.graph_frame.winfo_children():
                widget.destroy()

            #create the new figure 
            fig = Figure(figsize=(10, 6))
            ax = fig.add_subplot(111)

            if self.graph_type.get() == "Pie Graph":
                ax.pie(data, labels=[
                    f'Project -- {project}%',
                    f'Quizzes -- {quizzes}%',
                    f'Midterm -- {midterm}%',
                    f'Final -- {final}%'
                ], autopct='%1.1f%%', startangle=90)
                ax.set_title('Pie Graph of Grade Percentages')

            elif self.graph_type.get() == "Bar Graph":
                bars = ax.bar(
                    ['Project', 'Quizzes', 'Midterm', 'Final'], 
                    data, color=['red', 'blue', 'green', 'orange']
                )
                ax.set_title('Bar Graph of Grade Percentages')
                ax.set_ylim(0, 50)

                #add value labels on top of the bars 
                for bar in bars:
                    height = bar.get_height()
                    ax.text(bar.get_x() + bar.get_width() / 2, height, f'{height}%', 
                            ha='center', va='bottom')

            #now display the chart in the tkinter window using the canvas widget
            canvas = FigureCanvasTkAgg(fig, master=self.graph_frame)
            canvas.get_tk_widget().pack()
            canvas.draw()

        except ValueError:
            messagebox.showerror("Please enter valid float values.")

# Run the program
if __name__ == "__main__":
    GWgraphGeneratorGUI()


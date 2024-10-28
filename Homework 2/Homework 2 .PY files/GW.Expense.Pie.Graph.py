#first, import the matplotlib library for the pie chart:
import matplotlib.pyplot as plt

def read_expenses(filename):
    """
    purpose: to read the expenses file and convert to lists
    input: the file
    output: the lists with expenses and cost
    """
    #first, innitialize the empty lists:
    expense = []
    cost = []
    with open(filename, 'r') as file:
        for line in file: #read per line
            expense, cost = line.split('=')#split at the '=' between the expense kind and the cost amount
            expense.append(expense.strip()) # strip to get rid of whitelines and append to the expense list
            cost.append(float(cost.strip())) # same idea, just make it a float for the cost
    return expense, cost

def plot_pie_chart(expense, cost):
    """
    purpose: will plot the pie chart with the expenses and costs
    inputs: expenses and costs
    output: will display the pie chart
    """
    plt.pie(cost,labels=expense)
    plt.title('Expenses and Costs')
    plt.show()

def main():
    """
    this is the main program function, will dislay the pie chart, and read the txt file
    """
    file_path = ('costs.txt')
    #read the expenses from the file into two lists, expense --> cost
    expense, cost = read_expenses('costs.txt')
    #then , call the function to plot the expenses and costs as a pie chart
    plot_expenses_pie_chart(expense, cost)
    # for simplicity, I wil not use a while loop here.

if __name__ == "__main__":
    main()

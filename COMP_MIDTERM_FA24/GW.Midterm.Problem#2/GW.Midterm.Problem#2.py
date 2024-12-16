# needed libraries:
import random
import matplotlib.pyplot as plt

def generate_gas_prices(file):
    """
    purpose: to generate a file with random gas prices
    """
    # manually create a list with the months needed:
    months = ["January 2023", "Feburary 2023", "March 2023", "April 2023", "May 2023", "June 2023", "July 2023", "August 2023", "September 2023", "October 2023", "November 2023", "December 2023"]

    gas_price_min = 2.50 #min gas price
    gas_price_max = 4.00 #max possible price

    #now create the text file and populate it
    with open(file, 'w') as file:
        for month in months:
            gas_price = round(random.uniform(gas_price_min, gas_price_max), 2)#make it a uniform random dist
            file.write(f"{month} : {gas_price}\n") #now write the month and corresponding price to the text file. 
            
                              
def plot(file):
    months = []
    gas_prices = []

    with open(file, 'r') as file:
        for line in file:
            month, gas_price = line.split(': ') #plit by the ':"
            months.append(month)
            gas_prices.append(float(gas_price)) #MUST DEFINE AS A FLOAT

    # now plot:
    plt.bar(months, gas_prices)
    xtick_labels = ['Jan 2023', 'Jun 2023', 'Dec 2023'] #assign x labels to get rid of cluttering
    tick_positons = [0, 5, 11] #make the, even on plot
    plt.xlabel("month")
    plt.xticks(ticks=tick_positons, labels=xtick_labels)
    plt.ylabel("gas price")
    plt.title("Bar chart for average gas prices in 2023")


def main():
    file = '2023_gas_prices.txt' #define the file name
    generate_gas_prices(file)
    plot(file)
    plt.show()


if __name__ == "__main__":
    main()

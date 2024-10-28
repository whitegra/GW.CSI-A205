# first, import the necissary libraries:
import matplotlib.pyplot as plt
import numpy as np

def main():
    """
    purpose: main function since this is a short code 
    input: the txt file but it is defined within the function
    output: will plot a graph with average gas prices/week
    """
    average_gas_prices = np.loadtxt('1994_Weekly_Gas_Averages.txt') #just load the file contents straight into a numpy array
    weeks = np.arange(1, len(average_gas_prices) + 1) # start at 1, then for every element in average gas prices, add 1 for the corresponding week.

    #now, plot:
    plt.plot(weeks, average_gas_prices,color='pink')#plot the data
    plt.title('Average Gas Prices Per Week In The Year 1994')
    plt.xlabel('1994_Week')
    plt.ylabel('Average Gas Price')
    plt.grid(True)# show a grid for better visualization purposes
    plt.show()#show the plot     
    
if __name__ == "__main__":
    main()    
        

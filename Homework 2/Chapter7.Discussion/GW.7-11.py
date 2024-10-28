import matplotlib.pyplot as plt

def main():
    x_coords = [0, 1, 2, 3, 4]
    y_coords = [0, 3, 1, 5, 2]
    
    plt.plot(x_coords, y_coords)
    plt.title('Sample Data')
    plt.xlabel('X axis')
    plt.ylabel('Y axis')
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    main()

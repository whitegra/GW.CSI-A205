def main():
    with open('test_averages.csv', 'r') as csv_file:
        lines = csv_file.readlines()
        for line in lines:
            scores = line.split(',')

            total = 0.0
            for score in scores:
                total += float(score)

            average = total / len(scores)
            print(f"Average: {average}")

if __name__ == "__main__":
    main()

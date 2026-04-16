#added loop to code and let user select highs or lows or exit
while True:
    selection = input('Press 1 for Highs, 2 for Lows, or press 0 to exit: ')
    if selection == '1':

        import csv
        from datetime import datetime

        from matplotlib import pyplot as plt

        filename = 'sitka_weather_2018_simple.csv'
        with open(filename) as f:
            reader = csv.reader(f)
            header_row = next(reader)

            # Get dates and high temperatures from this file.
            dates, highs = [], []
            for row in reader:
                current_date = datetime.strptime(row[2], '%Y-%m-%d')
                dates.append(current_date)
                high = int(row[5])
                highs.append(high)

        # Plot the high temperatures.
        #plt.style.use('seaborn')
        fig, ax = plt.subplots()
        ax.plot(dates, highs, c='red')

        # Format plot.
        plt.title("Daily high temperatures - 2018", fontsize=24)
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)", fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)

        plt.show()
    if selection == '2':
        #Copied and pasted from above, just edited it for lows and changed the color of the line to blue
        import csv
        from datetime import datetime

        from matplotlib import pyplot as plt

        filename = 'sitka_weather_2018_simple.csv'
        with open(filename) as f:
            reader = csv.reader(f)
            header_row = next(reader)

            # Get dates and low temperatures from this file.
            dates, lows = [], []
            for row in reader:
                current_date = datetime.strptime(row[2], '%Y-%m-%d')
                dates.append(current_date)
                low = int(row[6])
                lows.append(low)

        # Plot the low temperatures.
        # plt.style.use('seaborn')
        fig, ax = plt.subplots()
        ax.plot(dates, lows, c='blue')

        # Format plot.
        plt.title("Daily low temperatures - 2018", fontsize=24)
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)", fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)

        plt.show()
    #added the option to exit
    if selection == '0':
        print('Have a great day!')
        quit()
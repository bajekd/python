import csv
from matplotlib import pyplot as plt
from datetime import datetime

# Get dates, high and low temperatures from csv file, conversion from fahrenheit to celsius
# and rounded to 1 digit after comma
filename = 'death_valley.csv'
with open(filename) as file:
    reader = csv.reader(file)
    header_row = next(reader)

    '''
        # Find number for row with temperature
        for index, column_header in enumerate(header_row):
            print(index, column_header)
    '''

    dates, high_temperatures, low_temperatures = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high_temperature = int(row[1])
            low_temperature = int(row[3])

        except ValueError:
            print(current_date, "missing data")
        else:
            dates.append(current_date)
            high_temperatures.append(high_temperature)
            low_temperatures.append(low_temperature)

    # Conversion from fahrenheit to celsius
    high_temperatures_in_celsius = list(map(lambda x: (x - 32) * 5/9, high_temperatures))
    low_temperatures_in_celsius = list(map(lambda x: (x - 32) * 5/9, low_temperatures))

# Plot data
fig = plt.figure(figsize=(10, 8))
plt.plot(dates, high_temperatures_in_celsius, c='red', alpha=0.5)
plt.plot(dates, low_temperatures_in_celsius, c='blue', alpha=0.5)
plt.fill_between(dates, high_temperatures_in_celsius, low_temperatures_in_celsius, facecolor=(0, 0, 1), alpha=0.05)

# Format plot
plt.title("Daily high and low temperatures - 2014\n Death Valley, CA", fontsize=24)
plt.xlabel("", fontsize=16)

# Draws the date labels diagonally (prevention from overlapping)
fig.autofmt_xdate()

plt.ylabel("Temperature (C)", fontsize=16)
plt.tick_params(axis="both", labelsize=16)

plt.show()

import csv
from matplotlib import pyplot as plt
from datetime import datetime


# Get dates, high and low temperatures from csv file, conversion from fahrenheit to celsius
# and rounded to 1 digit after comma
filename = 'sitka.csv'
with open(filename) as file:
    reader = csv.reader(file)
    header_row = next(reader)

    '''
        # Find number for row with temperature
        for index, column_header in enumerate(header_row):
            print(index, column_header)
    '''

    dates, high_temperatures_in_celsius, low_temperatures_in_celsius = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)

        high_temperature_in_fahrenheit = int(row[1])
        high_temperature_in_celsius = (high_temperature_in_fahrenheit - 32) * 5/9
        high_temperatures_in_celsius.append(round(high_temperature_in_celsius, 1))

        low_temperature_in_fahrenheit = int(row[3])
        low_temperature_in_celsius = (low_temperature_in_fahrenheit - 32) * 5/9
        low_temperatures_in_celsius.append(round(low_temperature_in_celsius, 1))

    ''' For future, try this:
      items = [1, 2, 3, 4, 5]
      squared = list(map(lambda x: x**2, items))
    '''

# Plot data
fig = plt.figure(figsize=(10, 8))
plt.plot(dates, high_temperatures_in_celsius, c='red', alpha=0.75)
plt.plot(dates, low_temperatures_in_celsius, c='blue', alpha=0.75)
plt.fill_between(dates, high_temperatures_in_celsius, low_temperatures_in_celsius, facecolor=(0, 0, 1), alpha=0.1)

# Format plot
plt.title("Daily high and low temperatures - 2014", fontsize=24)
plt.xlabel("", fontsize=16)

# Draws the date labels diagonally (prevention from overlapping)
fig.autofmt_xdate()

plt.ylabel("Temperature (C)", fontsize=16)
plt.tick_params(axis="both", labelsize=16)

plt.show()
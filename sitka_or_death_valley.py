import csv
from datetime import datetime
import matplotlib.pyplot as plt

file_names = ["sitka_weather_2018_simple.csv", "death_valley_2018_simple.csv"]
i = 0

subnames = []

fig, ax = plt.subplots(2)

for name in file_names:
    open_file = open(name, "r")

    csv_file = csv.reader(open_file, delimiter=",")

    header_row = next(csv_file)

    # The enumerate() function returns both the index of each item and the value of each item as you loop through a list
    for index, column_header in enumerate(header_row):
        print("Index:", index, "Column Name:", column_header)

    # assigning index values based on corresponding column names in header
    max_index = header_row.index("TMAX")
    min_index = header_row.index("TMIN")
    date_index = header_row.index("DATE")
    name_index = header_row.index("NAME")

    highs = []
    dates = []
    lows = []

    for row in csv_file:
        try:
            high = int(row[max_index])
            low = int(row[min_index])
            subname = row[name_index]
            converted_date = datetime.strptime(row[date_index], "%Y-%m-%d")
        except ValueError:
            print(f"missing data for {converted_date}")
        else:
            highs.append(high)
            lows.append(low)
            dates.append(converted_date)
        subnames.append(subname)

    # plot highs on a chart

    ax[i].plot(dates, highs, c="red")
    ax[i].plot(dates, lows, c="blue")

    fig.autofmt_xdate()

    ax[i].fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)

    plt.suptitle(
        "Temperature comparison between " + subnames[0] + " and " + subnames[-1],
        fontsize=10,
    )

    ax[i].set_title(subname, fontsize=13)
    plt.xlabel("", fontsize=12)
    plt.tick_params(axis="both", labelsize=12)
    i += 1

plt.show()

#! /usr/bin/env python3

# Import the required libraries and modules.
import pandas as pd
import matplotlib.pyplot as plt

# Read the csv data file. It is encoded in UTF-8.
# The values to plot are in column X.
# Set "date" as the index.
chart_data = pd.read_csv('xmr.csv', parse_dates=True, index_col='Date')


# Define for the X chart the graph title and subtitle, and the x and y axis labels.
x_chart_title = 'Individuals Control Chart'
x_chart_subtitle = 'Travel Cost'
x_chart_ylabel = 'Travel Cost (USD)'
x_chart_xlabel = 'Date'
subgroup_size = 2

# Determine d2 and d3 constants.
constants = pd.read_csv('control_chart_constants.csv')
d_two = constants['d2'][constants['n'] == subgroup_size].values[0]
d_three = constants['d3'][constants['n'] == subgroup_size].values[0]

# Define for the mR chart the graph title and subtitle, and the x and y axis labels.
mr_chart_title = 'Moving Range Control Chart'
mr_chart_subtitle = 'Travel Cost Difference'
mr_chart_ylabel = 'Travel Cost Moving Range (USD)'
mr_chart_xlabel = 'Date'

# Moving range chart statistics
# Calculate average range.
average_moving_range = (chart_data['X'].rolling(2).agg(lambda x: x[0] - x[1]).abs()).mean()
# Calculate the range chart upper control limit.
range_chart_upper_control_limit = average_moving_range + average_moving_range * 3 * d_three / d_two
# Calculate the range chart lower control limit.
range_chart_lower_control_limit = average_moving_range - average_moving_range * 3 * d_three / d_two
if range_chart_lower_control_limit < 0:
    range_chart_lower_control_limit = 0

# X chart statistics
# Calculate the average of all values.
average = chart_data['X'].mean()
# Calculate the individual chart upper control limit.
individual_chart_upper_control_limit = average + 3 * average_moving_range / d_two
# Calculate the individual chart lower control limit.
individual_chart_lower_control_limit = average - 3 * average_moving_range / d_two

# Create a graph of "individual values v. date".
ax = chart_data[['X']].plot.line(legend=False, marker='o', markersize=3, color='blue')
ax.axhline(y=average, color='b')
ax.axhline(y=individual_chart_upper_control_limit, color='r')
ax.axhline(y=individual_chart_lower_control_limit, color='r')
# Remove the top and right spines.
for spine in 'right', 'top':
    ax.spines[spine].set_color('none')
# Add the chart title and subtitle.
    ax.set_title(x_chart_title + '\n' + x_chart_subtitle)
# Add the Y axis label.
ax.set_ylabel(x_chart_ylabel)
# Add the X axis label.
ax.set_xlabel(x_chart_xlabel)
# Save the graph as svg and pdf.
ax.figure.savefig('x.svg', format='svg')
ax.figure.savefig('x.pdf', format='pdf')

plt.close()

# Create a graph of "moving range values v. date".
ax = chart_data['X'].rolling(2).agg(lambda x: x[0] - x[1]).abs().plot.line\
        (legend=False, marker='o', markersize=3, color='blue')
ax.axhline(y=average_moving_range, color='b')
ax.axhline(y=range_chart_upper_control_limit, color='r')
ax.axhline(y=range_chart_lower_control_limit, color='r')
# Remove the top and right spines.
for spine in 'right', 'top':
    ax.spines[spine].set_color('none')
# Add the chart title and subtitle.
ax.set_title(mr_chart_title + '\n' + mr_chart_subtitle)
# Add the Y axis label.
ax.set_ylabel(mr_chart_ylabel)
# Add the X axis label.
ax.set_xlabel(mr_chart_xlabel)
# Save the graph as svg and pdf.
ax.figure.savefig('mr.svg', format='svg')
ax.figure.savefig('mr.pdf', format='pdf')

print('Upper control limit',
      individual_chart_upper_control_limit,
      sep=' = ')
print('Average',
      average,
      sep=' = ')
print('Lower control limit',
      individual_chart_lower_control_limit,
      sep=' = ')

print('Upper control limit',
      range_chart_upper_control_limit,
      sep=' = ')
print('Average moving range',
      average_moving_range,
      sep=' = ')
print('Lower control limit',
      range_chart_lower_control_limit,
      sep=' = ')

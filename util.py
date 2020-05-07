import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def plot_distribution (df, grouping_criterium1, grouping_criterium2, order, x_label):
	"""
	Description: Plot the distribution of one of the characteristics over a second one.

	Arguments:
		df: dataframe. 
		grouping_criterium1: first category to group by. X-axis on the chart.
		grouping_criterium1: second category to group by. Category, through which the distribution is calculated
		order: list with all categories from grouping_criterium1 in the correct order for displaying them
		x_label: x label for the chart
	Returns:
		None, just a plot with the distribution
	"""
	# Grouping
	df_grouped = (df.groupby([grouping_criterium1, grouping_criterium2])['id'].count()).to_frame()
	df_grouped = df_grouped.reset_index()
	grouping_1 = (df.groupby(grouping_criterium1)['id'].count()).to_frame()
	df_grouped = df_grouped.merge(grouping_1, how ='left', on =grouping_criterium1)
	df_grouped['percentage'] = df_grouped['id_x']/df_grouped['id_y']*100
	df_grouped = df_grouped.set_index([grouping_criterium1, grouping_criterium2])
	
	# Plotting
	ax = df_grouped['percentage'].unstack().reindex(order).plot(kind='bar', stacked=True);
	ax.set_title('Distribution of accomodation types per {}'.format(x_label))
	ax.set_xlabel(x_label)
	ax.set_ylabel('Percentage')
	ax.set_ylim(0,100)
	ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left');
	
	
def plot_average (df, grouping_criterium1, grouping_criterium2, avg_cat, order, x_label):
	"""
	Description: Grouped plot of the average of one of the characteristics over a second one grouped by a third one.

	Arguments:
		df: dataframe. 
		grouping_criterium1: first category to group by. X-axis on the chart.
		grouping_criterium1: second category to group by. Category, through which the distribution is calculated
		avg_cat: numerical feature to calculate averages on.
		order: list with all categories from grouping_criterium1 in the correct order for displaying them
		x_label: x label for the chart
	Returns:
		None, just a plot with the averages
	"""
	
	# Grouping
	df.groupby([grouping_criterium1, grouping_criterium2])[avg_cat].mean().unstack().reindex(order).plot.bar(figsize=(10,5), grid = True)
	df.groupby([grouping_criterium1])[avg_cat].mean().reindex(order).rename('Mean {}'.format(avg_cat)).plot(color = 'k', style = '--', linewidth=0.75, grid = True);
	
	# Plotting
	plt.legend()
	plt.xticks(rotation = 90)
	plt.xlabel(x_label)
	plt.ylabel('Average {}'.format(avg_cat));
	plt.title('Average {} over different {}'.format(avg_cat, x_label));
	
	
def plot_time_series (df, grouping_criterium1, cat, agg_criteria, y_label):
	"""
	Description: Time series plot of the different values of a feature using the defined aggregation criteria and table with percentual changes over time.

	Arguments:
		df: dataframe. 
		grouping_criterium1: category to group by.
		cat: feature to calculate aggregation on.
		order: list with all categories from grouping_criterium1 in the correct order for displaying them
		y_label: y label for the chart
	Returns:
		None, just a plot with the time series
	"""
	
	# Grouping
	df_grouped = df.groupby(['origin_file', grouping_criterium1])[cat].agg(agg_criteria).unstack()
	
	# Plotting
	df_grouped.plot(kind = 'line', grid = True, marker = 'o', figsize = (12,8));
	plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left');
	plt.xlabel('Time')
	plt.ylabel(y_label);
	plt.title('Evolution of the {} over time'.format(y_label));
	
	# Percentual changes
	print((((df_grouped.pct_change(periods = 9).dropna().reset_index(drop=True)).T)*100).rename(columns={0: "Percentual change"}))
	
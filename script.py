import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')

print(ad_clicks.head())

# source views count
source_views = ad_clicks.groupby(['utm_source']).user_id.count()
print(source_views)

# add is_click column
ad_clicks['is_click'] = ~ad_clicks.ad_click_timestamp.isnull()
print(ad_clicks.head())

# count clicks on ads from each utm_source
clicks_by_source = ad_clicks.groupby(['utm_source', 'is_click']).user_id.count().reset_index()
print(clicks_by_source)

# clicks pivot table
clicks_pivot = clicks_by_source.pivot(
  columns='is_click',
  index= 'utm_source',
  values= 'user_id'
).reset_index()
print(clicks_pivot)

# percent of clicks
clicks_pivot['percent_clicked'] = clicks_pivot[True] / (clicks_pivot[True] + clicks_pivot[False])
print(clicks_pivot)

# experimental ads distribution (perentage)
exp_ads = ad_clicks.groupby('experimental_group').user_id.count().reset_index()
exp_ads['percentage'] = exp_ads.user_id / (exp_ads.user_id.sum())
print(exp_ads)

# which experimental Ad has a higher number of clicks
clicks_experimental = ad_clicks.groupby(['experimental_group', 'is_click']).user_id.count().reset_index()

# pivot table
clicks_exp_pivot = clicks_experimental.pivot(columns='is_click', index='experimental_group', values='user_id').reset_index()
print(clicks_exp_pivot)

# Task 9
# create new dataframes a_clicks and b_clicks
a_clicks = ad_clicks[ad_clicks.experimental_group == 'A']
b_clicks = ad_clicks[ad_clicks.experimental_group == 'B']

# Task 10
# grougpby and pivot table Ad A and Ad B
a_clicks = a_clicks.groupby(['is_click', 'day']).user_id.count().reset_index()
a_clicks_pivot = a_clicks.pivot(index='day', columns='is_click', values='user_id').reset_index()

b_clicks = b_clicks.groupby(['is_click', 'day']).user_id.count().reset_index()
b_clicks_pivot = b_clicks.pivot(index='day', columns='is_click', values='user_id').reset_index()

# add new column for clicks percentage of Ad A and Ad B
a_clicks_pivot['percent_clicked'] = a_clicks_pivot[True] / (a_clicks_pivot[True] + a_clicks_pivot[False])
print(a_clicks_pivot)

b_clicks_pivot['percent_clicked'] = b_clicks_pivot[True] / (b_clicks_pivot[True] + b_clicks_pivot[False])
print(b_clicks_pivot)

# Task 11
# - Comparing the two dataframes, Ad A has an higher number of clicks by day of the week than Ad B, except for Tuesday.
# - Ad A have a higher impact of clicks than Ad B in average
# - In conclusion, Ad A is a better choise due to the performance on A/B testing

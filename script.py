import codecademylib
import numpy as np
import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')

print (ad_clicks.head())

utms= ad_clicks.groupby('utm_source').user_id.count().reset_index()
#print (utms)

ad_clicks['is_click'] = ~ad_clicks.ad_click_timestamp.isnull()

#print (ad_clicks)

clicks_by_source = ad_clicks.groupby(['utm_source','is_click'])\
.user_id.count().reset_index()

print (clicks_by_source)

clicks_pivot = clicks_by_source.pivot(
  columns = 'is_click',
  index = 'utm_source',
  values = 'user_id'
).reset_index()
print (clicks_pivot)


sinolo = clicks_by_source.user_id.sum()
#print (sinolo)
clicks_pivot['percent_clicked'] = \
   clicks_pivot[True] / \
   (clicks_pivot[True] + 
    clicks_pivot[False])
print (clicks_pivot)


ab = ad_clicks.groupby(['experimental_group']).user_id.count().reset_index()
print (ab)


cl = ad_clicks.groupby(['experimental_group', 'is_click']).user_id.count().reset_index()

print (cl)

cl_pivot = cl.pivot(
  columns = 'is_click',
  index = 'experimental_group',
  values = 'user_id'
).reset_index()



cl_pivot ['percent'] = cl_pivot[True]/ (cl_pivot[True]+cl_pivot[False])

print (cl_pivot)

a_clicks = ad_clicks[ad_clicks.experimental_group == 'A'].reset_index()
print (a_clicks)

b_clicks = ad_clicks[ad_clicks.experimental_group == 'B'].reset_index()
print (b_clicks)

aper = a_clicks.groupby(['is_click', 'day']).user_id.count().reset_index()
print (aper)

aper_pivot = aper.pivot(
  columns = 'is_click',
  index = 'day',
  values = 'user_id'
).reset_index()

print (aper_pivot)

bper = b_clicks.groupby(['is_click', 'day']).user_id.count().reset_index()
print (bper)

bper_pivot = bper.pivot(
  columns = 'is_click',
  index = 'day',
  values = 'user_id'
).reset_index()

print (bper_pivot)


aper_pivot['pc'] = aper_pivot[True] / (aper_pivot[True] + aper_pivot[False])
print (aper_pivot)

bper_pivot['pc'] = bper_pivot[True] / (bper_pivot[True] + bper_pivot[False])
print (bper_pivot)


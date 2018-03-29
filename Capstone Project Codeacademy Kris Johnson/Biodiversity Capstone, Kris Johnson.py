
# coding: utf-8

# In[1]:


# Biodiversity Capstone Project, Kris Johnson.


# In[2]:


# Code for steps 1-4.


# In[5]:


# import codecademylib
import pandas as pd
import matplotlib as plt
# Load .csv.
species = pd.read_csv('species_info.csv')
# Inspect first 10 rows of csv.
print species.head()
# Number of unique species.
species_count =     species.scientific_name.nunique()
# Number of unique species.
species_type = species.category.unique()
# Conservation statuses.
conservation_statuses = species.conservation_status.nunique()
# Conservation status numbers.
conservation_counts = species.groupby('conservation_status')     .scientific_name.nunique().reset_index()
# Replaces NaN with 'No Intervention.
species.fillna('No Intervention', inplace = True)
# Groups and sorts species conservation status.
conservation_counts_fixed = species.groupby('conservation_status')     .scientific_name.nunique().reset_index()
# inspect.
print conservation_counts_fixed
    


# In[6]:


# COnservation Status by Species Bar Chart.


# In[8]:


# import codecademylib
import pandas as pd
from matplotlib import pyplot as plt
# Import csv.
species = pd.read_csv('species_info.csv')
# Replace NaN with new text.
species.fillna('No Intervention', inplace = True)
# New dataframe.
protection_counts = species.groupby('conservation_status')     .scientific_name.nunique().reset_index()     .sort_values(by='scientific_name')
# Defines new plot size.
plt.figure(figsize=(10,4))
ax = plt.subplot()
# The bar chart
plt.bar(range(len(protection_counts)),
    protection_counts.scientific_name)
# Xticks and labels
ax.set_xticks(range(len(protection_counts)))
ax.set_xticklabels(protection_counts     .conservation_status)
# Y labels and title
plt.ylabel('Number of Species')
plt.title('Conservation Status by Species')
# Show the chart
plt.show()
plt.savefig('Conservation_Status_by_species.png')


# In[9]:


# Steps Number 6 and 7


# In[11]:


# import codecademylib
import pandas as pd
from matplotlib import pyplot as plt

species = pd.read_csv('species_info.csv')
# Replaces NaN with new text.
species.fillna('No Intervention', inplace = True)

# New column in species to highlight intervention status. 
species['is_protected'] =     species.apply(lambda row: 'True'
                  if row['conservation_status'] \
                      != 'No Intervention'
                  else 'False', axis=1)

# Groups 'category' and 'is_protected'.
category_counts =     species.groupby(['category', 'is_protected'])         .scientific_name.nunique().reset_index()
# category_counts pivot.
category_pivot =     category_counts.pivot(columns = 'is_protected',
                          index = 'category',
                          values = 'scientific_name') \
                              .reset_index()
# Rename category_pivot columns.  
category_pivot.columns = ['category', 'not_protected', 'protected']

# Calculate percentage of protected species
category_pivot['percent_protected'] =     category_pivot['protected'] /   (category_pivot['protected'] +     category_pivot['not_protected']) 


# inspect. 
print category_pivot



# In[12]:


# Parts 8 and 9.


# In[14]:


# import codecademylib
import pandas as pd
from matplotlib import pyplot as plt

species = pd.read_csv('species_info.csv')
# Replaces NaN with new text.
species.fillna('No Intervention', inplace = True)

# New column in species to highlight intervention status. 
species['is_protected'] =     species.apply(lambda row: 'True'
                  if row['conservation_status'] \
                      != 'No Intervention'
                  else 'False', axis=1)

# Groups 'category' and 'is_protected'
category_counts =     species.groupby(['category', 'is_protected'])         .scientific_name.nunique().reset_index()
# Category_counts pivot
category_pivot =     category_counts.pivot(columns = 'is_protected',
                          index = 'category',
                          values = 'scientific_name') \
                              .reset_index()
    
category_pivot.columns = ['category', 'not_protected', 'protected']

# calculate percentage of protected species
category_pivot['percent_protected'] =     category_pivot['protected'] /   (category_pivot['protected'] +     category_pivot['not_protected']) 
# inspect 
print category_pivot

### 'Conservation Status by Species' Bar Graph Code ###
''' 
# Import csv.
species = pd.read_csv('species_info.csv')
# Replace NaN with new text.
species.fillna('No Intervention', inplace = True)
# New dataframe.
protection_counts = species.groupby('conservation_status') \
    .scientific_name.nunique().reset_index() \
    .sort_values(by='scientific_name')
# Defines new plot size.
 plt.figure(figsize=(10,4))
 ax = plt.subplot()
# The bar chart.
 plt.bar(range(len(protection_counts)),
    protection_counts.scientific_name)
# Xticks and labels.
 ax.set_xticks(range(len(protection_counts)))
 ax.set_xticklabels(protection_counts.conservation_status)
# Y labels and title.
 plt.ylabel('Number of Species')
 plt.title('Conservation Status by Species')
# Show the chart.
 plt.show() '''
### End Bar Graph Code ###

# import scypy for chi2 test
from scipy.stats import chi2_contingency
# contingency table for mammal and bird
contingency = [[30, 146],
               [75, 413]]
# chi2 test
chi2, pval, dof, expected =     chi2_contingency(contingency)

  # inspect pval
print pval
pval = pval

# contingency table for mammal and reptile
reptile_mammal_contingency = [[30, 146],
                              [5, 73]]
# chi2 test
chi2, pval, dof, expectd =     chi2_contingency(reptile_mammal_contingency)
#inspect
print pval
# saves pval from chi2 test #2
pval_reptile_mammal = pval


# In[15]:


# Part 10 - 12.


# In[24]:


# import codecademylib
import pandas as pd
from matplotlib import pyplot as plt

# import and clean species.csv
species = pd.read_csv('species_info.csv')
species.fillna('No Intervention', inplace = True)
species['is_protected'] = species.conservation_status != 'No Intervention'

# import observations.csv
observations = pd.read_csv('observations.csv')
# add 'is_sheep column to species and select for sheep species.
species['is_sheep'] =     species.common_names.apply(lambda x: 
                               'Sheep' in x)
# select and save is_sheep column.
species_is_sheep = species['is_sheep']
# inspect
print species_is_sheep 
# select is_sheep result if category == mammal.
sheep_species =     species[(species.is_sheep) 
    & (species.category == 'Mammal')]
# inspect.
print sheep_species
# merge observations and sheep_species.
sheep_observations = pd.merge(sheep_species, 
                              observations)
# inspect
print sheep_observations.head(10)
# group and sum observations to determine sightings #.
obs_by_park =     sheep_observations.groupby(['park_name'])         .observations.sum().reset_index()
# inspect 
print obs_by_park


# In[25]:


# Part 13 # of observations of Sheep per Week


# In[27]:


# import codecademylib
import pandas as pd
from matplotlib import pyplot as plt
# load and clean species.csv
species = pd.read_csv('species_info.csv')
species['is_sheep'] =     species.common_names.apply(lambda x: 'Sheep' in x)
sheep_species =     species[(species.is_sheep) 
    & (species.category == 'Mammal')]

# load observations.csv
observations = pd.read_csv('observations.csv')

# merge sheep_observations and sheep_species.
sheep_observations = observations.merge(sheep_species)
# group observations sum by park_name.
obs_by_park =     sheep_observations.groupby('park_name')         .observations.sum().reset_index()

# set figure size.
plt.figure(figsize=(16,4))
# axes object.
ax = plt.subplot()
# bar chart for observations column in obs_by_park.
plt.bar(range(len(obs_by_park.park_name)),
    obs_by_park.observations)

# xticks and labels
ax.set_xticks(range(len(obs_by_park.park_name)))
ax.set_xticklabels(obs_by_park.park_name)
plt.ylabel('Number of Observations')
plt.title('Observations of Sheep per Week')

# inspect
plt.show()


# In[28]:


# Parts 14 and the Final, 15.


# In[29]:


# baseline based on previous years infection data.
baseline = 15
# Park wants to observe a 5% reduction in diseased sheep.
minimum_detectable_effect = 100*5/15
# inspect
print minimum_detectable_effect
# sample size needed based on saple size calculator.
sample_size_per_variant = 890
# 507 sheep per week can be observed according to data. 
yellowstone_weeks_observing = 1.75
# 250 sheep can be observed according to data.
bryce_weeks_observing = 3.56


# In[30]:


# Thank you for reviewing your feedback is greatly appriciated!...


# In[ ]:


# It is fantastic to have learnt a new skill having never coded before and having some level of a satisfactory result!


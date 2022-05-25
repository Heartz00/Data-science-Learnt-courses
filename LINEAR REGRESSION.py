#!/usr/bin/env python
# coding: utf-8

# In[20]:


import pandas as pd
from sklearn.datasets import load_boston
boston_dataset = load_boston()

boston = pd.DataFrame(boston_dataset.data, columns = boston_dataset.feature_names)
boston['MEDV'] = boston_dataset.target
print(boston[['CRIM', 'RM', 'AGE', 'RAD', 'MEDV']].head(5))


# In[ ]:





# In[ ]:





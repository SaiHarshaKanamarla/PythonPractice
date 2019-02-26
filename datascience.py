# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 16:44:16 2019

@author: siddh
"""

import pandas as pd

d = pd.Series(['Dave','cchen','mike','oscar'],index = [1,2,3,4]);
#print(d);

dict = {'name':pd.Series(['harsha','sai','siddu'],index = [1,2,3]),
        'age':pd.Series([21,22,23],index = [1,2,3]),
        'survived':pd.Series([True,False,True],index = [1,2,3]),
        };
        
#print(dict);"""

"""
dict = {'name':['sai','harsha','wassup'],
        'age' : [21,21,21], 
        'gender': [ 'male','male','male']
       };

d = pd.DataFrame(dict);
print(d);
"""
d = pd.DataFrame(dict);
#print(d);                


dict1 = {'name': ['harsha','sai','018'],
         'age': [22,23,24],
          'height' : [123,234,123]
    };

result = pd.DataFrame(dict1);
#print(result);

print(result['age']);
print(result[result['age'] > 22])
print("--------------*")
#fetching the data frame with height values where age is > 22

print(result['height'][result['age']>22])

print("harsha")
print("adding new prints")
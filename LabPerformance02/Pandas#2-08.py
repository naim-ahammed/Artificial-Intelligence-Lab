# Pandas#2: Fill missing values in a dataset with column-wise means.

import pandas as pd

data = {
    'Product': ['Book', 'Shirt', 'Pant', 'Fan', 'Pant'],
    'Quantity': [30, 50, None, 20, 30],
    'Price': [800, 500, 300, 800, None]
}

df = pd.DataFrame(data)
df['Quantity'] = df['Quantity'].fillna(df['Quantity'].mean())
df['Price'] = df['Price'].fillna(df['Price'].mean())
print(df)

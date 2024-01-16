import pandas as pd

data = pd.read_excel('test.xlsx')


print(type(data))
# print(data)
email = data['test '].values
print(email)
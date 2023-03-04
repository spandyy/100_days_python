import pandas as pd

df = pd.DataFrame({'Chemistry': [67,90,66,32],

        'Physics': [45,92,72,40], 

        'Mathematics': [50,87,81,12], 

        'English': [19,90,72,68]})
# df += [10, 20, 10, 10]
# print(df)

print(df.sort_values(by="Physics"))
# import pandas as pd

# df = pd.DataFrame([[54.2,'a'],[658,'d']],
#                   index = list('pq'))

# print(df)
# df.columns = df.index
# print(df.columns.values)
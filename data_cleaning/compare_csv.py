import pandas as pd

# # Create two dataframes for the purpose of this example
# data1 = pd.DataFrame({
#     'x1':range(0, 6),
#     'x2':['x', 'y', 'x', 'x', 'y', 'x'],
#     'x3':range(2, 8)
# })

# data2 = pd.DataFrame({
#     'x1':range(3, 8),
#     'x2':['x', 'x', 'x', 'y', 'y'],
#     'x3':range(5, 10)
# })

# data1.to_csv('data_cleaning/data1.csv', index=False)
# data2.to_csv('data_cleaning/data2.csv', index=False)

input1 = input ("Enter filepath to first CSV: ")
input2 = input ("Enter filepath to second CSV: ")

with open(input1, 'r') as csv1, open(input2, 'r') as csv2:
    import1 = csv1.readlines()
    import2 = csv2.readlines()

with open('data_cleaning/data_diff.csv', 'w') as outFile:
    for row in import2:
        if row not in import1:
            outFile.write(row)

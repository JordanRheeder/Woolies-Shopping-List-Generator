import pandas as pd
import os

exportPath = open("outputList.json", "w")

for filename in os.listdir('.'):
    if filename.startswith('inputList'):
        importPath = (filename)

fileData = pd.read_json('file://' + os.path.realpath(importPath))
		
df1 = pd.DataFrame(fileData, columns=['productDisplayName', 'quantity']).drop_duplicates()
productDisplayName = df1['productDisplayName'].map(lambda x: str(x)[0:])
quantity = df1['quantity'].map(lambda x: str(x)[0:])


listLen = len(df1['quantity'].map(lambda x: str(x)[0:]))
i = 0
output = ''
shoppingList = []
while (i < listLen):
	shoppingList = (str(quantity.iloc[i]) + ' * ' + str(productDisplayName.iloc[i]) + '\n')
	exportPath.write(str(shoppingList))
	i += 1

print(listLen)
exportPath.close()

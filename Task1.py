import numpy as np
fname = 'ABBREV.csv'

arr = np.genfromtxt('ABBREV.csv', delimiter=';', dtype=None, names=True, encoding="utf8")
arr = np.sort(arr, order=['Energ_Kcal', 'Shrt_Desc'])
print(f'Самый калорийный: {arr[-1][1]} ({arr[-1][3]} Ккал)')
arr = np.sort(np.sort(arr, order='Shrt_Desc')[::-1], order='Sugar_Tot_g', kind='stable')
print(f'Несладкий, но полезный: {arr[0][1]} ({arr[0][9]} г)')
arr = np.sort(np.sort(arr, order='Shrt_Desc')[::-1], order='Protein_g', kind='stable')
print(f'Самый протеиновый: {arr[-1][1]} ({arr[-1][4]} г)')
arr = np.sort(arr, order='Vit_C_mg', kind='stable')
print(f'Самый С-шный: {arr[-1][1]} ({arr[-1][20]} мг)')
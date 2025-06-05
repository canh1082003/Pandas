import pandas as pd
import numpy as np

nhanvien = pd.DataFrame({
    'ID': [101, 102, 103, 104, 105, 106],
    'Name': ['An', 'Bình', 'Cường', 'Dương', np.nan, 'Hạnh'],
    'Age': [25, np.nan, 30, 22, 28, 35],
    'Department': ['HR', 'IT', 'IT', 'Finance', 'HR', np.nan],
    'Salary': [700, 800, 750, np.nan, 710, 770]
})

phongban = pd.DataFrame({
    'Department': ['HR', 'IT', 'Finance', 'Marketing'],
    'Manager': ['Trang', 'Khoa', 'Minh', 'Lan']
})
print(nhanvien.isnull())
nhanvien = nhanvien[nhanvien.isnull().sum(axis=1) <= 2]

nhanvien['Name'] = nhanvien['Name'].fillna("Chưa rõ")

mean_age = nhanvien['Age'].mean()
nhanvien['Age'] = nhanvien['Age'].fillna(mean_age)

nhanvien['Department'] = nhanvien['Department'].fillna("Unknown")

nhanvien['Salary'] = nhanvien['Salary'].ffill()
print(nhanvien)

nhanvien['Age'] = nhanvien['Age'].astype(int)
nhanvien['Salary'] = nhanvien['Salary'].astype(int)

nhanvien['Salary_after_tax'] = (nhanvien['Salary'] * 0.9).astype(int)
print(nhanvien ,"6")

loc_it = nhanvien[(nhanvien['Department'] == 'IT') & (nhanvien['Age'] > 25)]
print(loc_it ,"7")


nhanvien_sorted = nhanvien.sort_values(by='Salary_after_tax', ascending=False)
print(nhanvien_sorted ,"8")

luong_tb = nhanvien.groupby('Department')['Salary'].mean()
print(luong_tb ,"9")

nhanvien_merged = pd.merge(nhanvien, phongban, on='Department', how='left')
print(nhanvien_merged ,"10")


nhanvien_moi = pd.DataFrame({
    'ID': [107, 108],
    'Name': ['Huy', 'Lan'],
    'Age': [27, 29],
    'Department': ['Marketing', 'IT'],
    'Salary': [720, 810]
})

nhanvien_moi['Salary_after_tax'] = (nhanvien_moi['Salary'] * 0.9).astype(int)
nhanvien_merged = pd.merge(nhanvien, phongban, on='Department', how='left')
print(nhanvien_moi['Salary_after_tax'] ,"11")
nhanvien_moi = nhanvien_moi[['ID', 'Name', 'Age', 'Department', 'Salary', 'Salary_after_tax']]
print(nhanvien_moi)
nhanvien_final = pd.concat([nhanvien, nhanvien_moi], ignore_index=True)
print(nhanvien_final)

import pandas as pd

data = {
    'Name': ['Anh', 'Bình', 'Châu', 'Dũng', 'Hà', 'Hùng', 'Lan', 'Mai', 'Nam', 'Tú'],
    'Age': [20, 21, 22, 20, 23, 21, 22, 20, 24, 23],
    'Gender': ['Nam', 'Nam', 'Nữ', 'Nam', 'Nữ', 'Nam', 'Nữ', 'Nữ', 'Nam', 'Nữ'],
    'Score': [6.5, 7.0, 4.5, 5.0, 8.5, 3.0, 9.0, 6.0, 2.5, 7.5]
}

df_students = pd.DataFrame(data)


print("Toàn bộ dữ liệu:")
print(df_students)

print("\n3 dòng đầu tiên:")
print(df_students.head(3))

print("\nindex=2 và cột Name:")
print(df_students.loc[2, 'Name'])

if 10 in df_students.index:
    print("\nindex=10 và cột Age:")
    print(df_students.loc[10, 'Age'])
else:
    print("\nKhông tồn tại index=10.")

print("\nCác cột Name và Score:")
print(df_students[['Name', 'Score']])

df_pass = df_students.copy()
df_pass['Pass'] = df_pass['Score'] >= 5

print("\nThêm cột 'Pass':")
print(df_pass)

df_sorted = df_students.sort_values(by='Score', ascending=False)

print("\n Sắp xếp theo Score giảm dần:")
print(df_sorted)
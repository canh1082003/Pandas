import pandas as pd

def get_invoice_data(filepath="meinvoice.xlsx"):
    try:
        df = pd.read_excel(filepath)
        print(df)
        data = df[["Mã Tra Cứu", "Url"]].dropna()
        return data.to_dict(orient="records") 
    except Exception as e:
        print(f"Lỗi khi đọc file Excel: {e}")
        return []

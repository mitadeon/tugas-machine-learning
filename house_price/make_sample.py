import pandas as pd

# Membaca dataset training
data = pd.read_csv("train.csv")

# Mengambil satu baris dan menghapus kolom target
sample = data.drop(columns=["SalePrice"]).iloc[[0]]

# Menyimpan satu baris sebagai JSON object
json_data = sample.to_json(orient="records")

# Menghapus tanda [] agar formatnya menjadi object
json_data = json_data[1:-1]

with open("sample_input.json", "w") as file:
    file.write(json_data)

print("File sample_input.json berhasil dibuat!")
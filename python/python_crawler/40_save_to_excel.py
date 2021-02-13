import pandas as pd

def save(df, filename):
    writer = pd.ExcelWriter(filename)
    df.to_excel(writer, 'Sheet1')
    writer.save()

# dataframe => 표
df = pd.read_json("./셔츠.json")

print(df.count())

save(df, "./셔츠.xlsx")
import pandas as pd
url = "https://dts.twse.com.tw/opendata/t187ap03_L.csv"
df = pd.read_csv(url)
all = df["公司簡稱"]
import random
Condition1 = random.choices(all, k =100)
Condition2 = random.choices(all, k =180)
print(set(Condition1) & set(Condition2))
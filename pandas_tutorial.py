import pandas as pd
import seaborn as sns

series = pd.Series([10, 77, 12, 4, 5])
print(series)

series.index
series.dtype
series.size
series.ndim
series.values
type(series.values)
series.head(3)
series.tail(2)

df = pd.read_csv("advertising.csv")
df.head()
df.tail()
df.info()
df.columns
df.isnull().values.any()
df.isnull().sum()
df["newspaper"].value_counts()

df = sns.load_dataset("titanic")
df["sex"].value_counts()
df.columns.nunique()
df[["pclass", "parch"]].nunique()
df["embarked"].astype('category')

df[0:13]
df.drop(0, axis=0).head()

df.loc[:, df.columns.str.contains("age")].head()
df.loc[:, ~df.columns.str.contains("age")].head()

df.loc[0:3, "age"]
df.iloc[0:4, 3]

col_names = ["age", "embarked", "alive"]
df.loc[0:3, col_names]

df[df["age"] > 50]["age"].count()

df.loc[df["age"] > 50, ["age", "class"]].head()

df_new = df.loc[(df["age"] > 50) & (df["sex"] == "male")
                & ((df["embark_town"] == "Cherbourg") | (df["embark_town"] == "Southampton")),
                ["age", "class", "embark_town"]]

df["age"].mean()

df.groupby("sex")["age"].mean()

df.groupby(["sex", "embark_town", "class"]).agg({"age": "mean",
                       "survived": "mean",
                       "sex": "count"})

df.pivot_table("survived", "sex", "embark_town")

df.pivot_table("survived", "sex", "embark_town", aggfunc="std")

df.pivot_table("survived", "sex", ["embarked", "class"])

df["new_age"] = pd.cut(df["age"], [0, 10, 18, 25, 40, 90])

df.pivot_table("survived", "sex", "new_age")

df["age2"] = df["age"]*2
df.head()

df[["age", "age2"]].apply(lambda x: x**2).head()

df.loc[:, df.columns.str.contains("age")] = df.loc[:, df.columns.str.contains("age")].apply(lambda x: (x - x.mean())/ x.std()).head()

df.head()


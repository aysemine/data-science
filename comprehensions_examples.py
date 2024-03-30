import seaborn as sns
df = sns.load_dataset("car_crashes")

df.columns = [col.upper() for col in df.columns]

df.columns = ["FLAG_" + col if "INS" in col else "NO_FLAG_" +col for col in df.columns ]

num_cols = [col for col in df.columns if df[col].dtype != "0"]

dict = {}
agg_list = ["mean", "min", "max", "sum"]


new_dict = {col : agg_list for col in num_cols}

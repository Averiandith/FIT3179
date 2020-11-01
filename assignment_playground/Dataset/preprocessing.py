import pandas

df = pandas.read_csv("2019.csv")
new_df = pandas.read_csv("2019.csv")

columns = ["Overall_Rank", "Country", "Latitude", "Longitude", "Score", "GDP_Per_Capita", "Social_Support", "Healthy_Life_Expectancy", "Freedom_To_Make_Life_Choices", "Generosity", "Perceptions_Of_Corruption"]

# print(df)
new_df["Major_Factor"] = df[columns[5:]].rank(axis=0, numeric_only=True, method="max").idxmax(axis=1)

# Compare between GDP vs Social_Support (Done)

# Compare between Health_Life_Expectancy vs Generosityl
# new_df["Major_Factor"] = df[columns[8:10]].idxmax(axis=1)
# new_df["Major_Factor"] = df[columns[7:10]].idxmax(axis=1)

print(new_df)

new_df.to_csv("2019_adv_factors.csv", header = True)
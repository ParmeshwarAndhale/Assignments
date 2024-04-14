Import pandas as pd
# Create the dataset
Data = {‘No’: [1, 2, 3, 4],
 ‘Company’: [‘Tata’, ‘MG’, ‘Kia’, ‘Hyundai’],
 ‘Model’: [‘Nexon’, ‘Astor’, ‘Seltos’, ‘Creta’],
 ‘Year’: [2017, 2021, 2019, 2015]}
Df = pd.DataFrame(data)
# Convert categorical values into numeric format
Df[‘Company’] = pd.Categorical(df[‘Company’])
Df[‘Model’] = pd.Categorical(df[‘Model’])
Df[‘Company’] = df[‘Company’].cat.codes
Df[‘Model’] = df[‘Model’].cat.codes
Print(df)
From mlxtend.frequent_patterns import apriori
From mlxtend.frequent_patterns import association_rules
# Generate frequent itemsets with min_sup = 0.5
Frequent_itemsets = apriori(df, min_support=0.5, use_colnames=True)
Print(frequent_itemsets)
# Generate association rules with min_threshold = 0.7
Association_rules = association_rules(frequent_itemsets, metric=”confidence”, min_threshold=0.7)
Print(association_rules)

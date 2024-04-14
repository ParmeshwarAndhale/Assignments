Import pandas as pd
From mlxtend.preprocessing import TransactionEncoder
From mlxtend.frequent_patterns import apriori, association_rules
# Load the dataset
Df = pd.read_csv(‘market_basket.csv’)
# Drop any rows with null values
Df.dropna(inplace=True)
# Convert categorical values to numeric format
Te = TransactionEncoder()
Te_ary = te.fit(df.values).transform(df.values)
Df = pd.DataFrame(te_ary, columns=te.columns_)
# Generate frequent itemsets
Frequent_itemsets = apriori(df, min_support=0.01, use_colnames=True)
# Generate association rules
Rules = association_rules(frequent_itemsets, metric=”lift”, min_threshold=1)
# Display information about the dataset
Print(“Dataset information:”)
Print(df.info())
# Display the frequent itemsets
Print(“\nFrequent itemsets:”)
Print(frequent_itemsets)
# Display the association rules
Print(“\nAssociation rules:”)
Print(rules)

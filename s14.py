From mlxtend.preprocessing import TransactionEncoder
From mlxtend.frequent_patterns import apriori
# Create the dataset
TID = {1:[“apple”,”mango”,”banana”],
 2:[“mango”,”banana”,”cabbage”,”carrots”],
 3:[“mango”,”banana”,”carrots”],
 4:[“mango”,”carrots”]}
# Convert the categorical values into numeric format
Te = TransactionEncoder()
Te_ary = te.fit([TID[i] for i in TID]).transform([TID[i] for i in TID])
Df = pd.DataFrame(te_ary, columns=te.columns_)
# Apply the apriori algorithm with different min_sup values
Min_sup_values = [0.25, 0.5, 0.75]
For min_sup in min_sup_values:
 Frequent_itemsets = apriori(df, min_support=min_sup, use_colnames=True)
 Print(“Frequent itemsets with min_sup =”, min_sup)
 Print(frequent_itemsets)
 Print(“\n”)

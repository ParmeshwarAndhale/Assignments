Import pandas as pd
From mlxtend.preprocessing import TransactionEncoder
From mlxtend.frequent_patterns import apriori, association_rules
# create the dataset
TID = 
{1:[“bread”,”milk”],2:[“bread”,”diaper”,”beer”,”eggs”],3:[“milk”,”diaper”,”beer”,”coke”],4:[“bread”,”mil
k”,”diaper”,”beer”],5:[“bread”,”milk”,”diaper”,”coke”]}
Transactions = []
For key, value in TID.items():
 Transactions.append(value)
# convert the categorical values into numeric format
Te = TransactionEncoder()
Te_ary = te.fit_transform(transactions)
Df = pd.DataFrame(te_ary, columns=te.columns_)
# apply the apriori algorithm with different min_sup values
Min_sup_values = [0.2, 0.4, 0.6]
For min_sup in min_sup_values:
 Frequent_itemsets = apriori(df, min_support=min_sup, use_colnames=True)
 Rules = association_rules(frequent_itemsets, metric=”confidence”, min_threshold=0.7)
 Print(“Min_sup:”, min_sup)
 Print(“Frequent Itemsets:”)
 Print(frequent_itemsets)
 Print(“Association Rules:”)
 Print(rules

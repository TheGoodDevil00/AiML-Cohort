import pandas as pd
dataset = {
    #init a dataframe
    "name":["A","B","C","D","E"],
    "age":[18,19,18,19,20],
    "branch":["EnTC","IT","Comp","EnTC","Elec"]
}
df = pd.DataFrame(dataset)
print(df)

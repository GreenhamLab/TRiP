import pandas as pd


def geno_match(exp_data, geno_data):
    geno = pd.read_csv(geno_data)
    exp = pd.read_csv(exp_data)
    merged = pd.merge(exp, geno, on = 'ID')
    merged.to_csv(f'merged_{exp_data}', index=False)

#Replace files with correct file names

geno_match("Stand1.csv", "key.csv")

import pandas as pd


if __name__ == '__main__':
    df = pd.read_csv('.\day2\input.txt', sep=' ', header=None)
    print(df)
    df_grouped = df.groupby(df.columns[0]).sum().reset_index()
    df_dict = dict(zip(df_grouped[0], df_grouped[1]))
    print((df_dict['up'] - df_dict['down']) * df_dict['forward'])

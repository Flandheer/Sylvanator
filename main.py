import pandas as pd


def sylvanator(csv_file):
    '''
    :param df: dataframe of current fleet information
    :return: pivot fleet information to plan
    '''

    df = pd.read_csv(csv_file)
    df['loadDate'] = df['loadDate'].str[:10]
    df['dayofweek'] = list(
    df['loadDate'].map(str) + " " + pd.to_datetime(df['loadDate'], format='%Y-%m-%d').dt.day_name())
    new = list(df['loadlocation'].map(str) + " " + df['weight'].map(str) + "mt" + " " + df['volume'].map(str) + "m3" + " " + df['product'].map(str) + "-" + df['dischargeLocation'].map(str) + "(" + df['supplier'].map(str) + ")")
    df["new"] = new
    df = df.drop_duplicates(subset=["ship", "dayofweek"])
    sylvanator = df.pivot(index = 'ship', columns = 'dayofweek')['new']

    print(sylvanator.head())


    return sylvanator


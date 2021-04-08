import pandas as pd


def sylvanator(csv_file):
    '''
    :param df: dataframe of current fleet information
    :return: pivot fleet information to plan
    '''

    df = pd.read_csv(csv_file)
    df['dayofweek'] = list(df['loadDate'].map(str) + " " + pd.to_datetime(df['loadDate'], format='%Y-%m-%d').dt.day_name() )
    new = list(df['loadlocation'].map(str) + " > "+ df['dischargeLocation'].map(str) + " " + df['product'].map(str) + " "+ df['weight'].map(str)+ "t" + " "+ df['volume'].map(str)+ "v"+  " "+ df['supplier'].map(str))
    df["new"] = new
    df = df.drop_duplicates(subset=["loadlocation", "dayofweek"])
    sylvanator = df.pivot(index = 'ship', columns = 'dayofweek')['new']

    print(sylvanator.head())


    return sylvanator


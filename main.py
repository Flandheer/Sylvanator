import pandas as pd


def sylvanator(csv_file):
    '''
    :param df: dataframe of current fleet information
    :return: pivot fleet information to plan
    '''

    df = pd.read_csv(csv_file)
    df['dayofweek'] = list(df['date'].map(str) + " " + pd.to_datetime(df['date'], format='%Y-%m-%d').dt.day_name() )
    new = list(df['description'].map(str)+ " "+ df['name.1'].map(str) + " "+ df['weight'].map(str)+ " "+ df['name.2'].map(str))
    df['new'] = new
    sylvanator = df.pivot(index = 'name', columns = 'dayofweek')['new']

    print(sylvanator.head())


    return sylvanator


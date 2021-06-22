import pandas as pd


def planning(df):
    df['loadDate'] = df['loadDate'].str[:10]
    df['dayofweek'] = list(
    df['loadDate'].map(str) + " " + pd.to_datetime(df['loadDate'], format='%Y-%m-%d').dt.day_name())
    new = list(df['loadlocation'].map(str) + " " + df['weight'].map(str) + "mt" +" " + df['volume'].map(str) +
               "m3" + " " +df['product'].map(str) + "-" + df['dischargeLocation'].map(str) +
               "(" + df['supplier'].map(str) + ")")
    df['new'] = new

    barge = list(df['ship'].map(str) + " " + df['operator'].map(str))
    df['barge'] = barge

    df = df.drop_duplicates(subset=["ship", "dayofweek"])
    planning_result = df.pivot(index='barge', columns='dayofweek')['new']

    return planning_result


def status(df):
    barge = list(df['ship'].map(str) + " " + df['operator'].map(str))
    df['barge'] = barge
    status = df[['barge', 'current_location', 'current_status', 'eta', 'ata']]
    status = status.drop_duplicates()
    status['status'] = list( status['current_location'].map(str) + " " + status['current_status'].map(str) + " ETA: "
                             + status['eta'].map(str) + " ATA: " + status['ata'].map(str))
    status_result = status[['barge', 'status']]

    return status_result


def sylvanator(csv_file):
    df = pd.read_csv(csv_file)
    plan = planning(df)
    state = status(df)
    sylvanator = plan.merge(state, how='left', left_on='barge', right_on="barge")
    sylvanator = sylvanator[
        [sylvanator.columns[0], sylvanator.columns[-1], sylvanator.columns[1], sylvanator.columns[2],
         sylvanator.columns[3], sylvanator.columns[4], sylvanator.columns[5]]]

    return sylvanator


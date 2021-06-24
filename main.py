import pandas as pd


def planning(df):
    df['loadDate'] = df['loadDate'].str[:10]
    df['dayofweek'] = list(df['loadDate'].map(str) + " "
                           + pd.to_datetime(df['loadDate'], format='%Y-%m-%d').dt.day_name())

    new = list(df['loadlocation'].map(str) + " " + df['loadingReference'].map(str) + " " + df['weight'].map(str) +
               "mt" +" " + df['volume'].map(str) + "m3" + " " +df['product'].map(str) + "-" +
               df['dischargeLocation'].map(str) + " " + df['loadingReference'].map(str) + "(" +
               df['supplier'].map(str) + ")")
    df['new'] = new

    df = df.drop_duplicates(subset=["ship", "dayofweek"])
    planning_result = df.pivot(index='ship', columns='dayofweek')['new']

    return planning_result


def status(df):
    status = df[['ship', 'operator', 'current_location', 'current_status', 'eta', 'ata']]
    status['eta'] = status['eta'].str.replace("T"," ").str[:16]
    status['ata'] = status['ata'].str.replace("T"," ").str[:16]

    status = status.drop_duplicates()
    status['status'] = list(status['current_location'].map(str) + " " + status['current_status'].map(str) + " ETA: "
                            + status['eta'].map(str) + " ATA: "
                            + status['ata'].map(str))

    status_result = status[['ship', 'operator', 'status']]

    return status_result


def sylvanator(csv_file):
    df = pd.read_csv(csv_file)
    plan = planning(df)
    state = status(df)
    sylvanator = plan.merge(state, how='left', left_on='ship', right_on="ship")
    sylvanator = sylvanator[
        [sylvanator.columns[0], sylvanator.columns[-2], sylvanator.columns[-1], sylvanator.columns[1], sylvanator.columns[2],
         sylvanator.columns[3], sylvanator.columns[4], sylvanator.columns[5]]]

    return sylvanator


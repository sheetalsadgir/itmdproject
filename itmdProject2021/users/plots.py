import base64
from datetime import datetime
from io import BytesIO
import matplotlib.pyplot as plt
import pandas as pd
from .data import df


def get_graphToPrint():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph


def plotCrimes():
    s = df[['primary_type']]  # get a series from data frame
    crime_count = pd.DataFrame(s.groupby('primary_type').size().sort_values(ascending=True).rename('counts'))
    data = crime_count.iloc[-10:-5]  # retrieving select rows by loc method
    print(data[::-1])
    data.plot(kind='barh')
    plt.subplots_adjust(left=0.33, right=0.89)
    plt.show()


####################

def plotTopFiveCrimes(chart_type):
    # Top 5 crimes count bet my area and university of chicago
    s2 = df[['primary_type']]  # get a series from data frame
    topFiveCrimes = pd.DataFrame(s2.groupby('primary_type').size().sort_values(ascending=False).head().rename('counts'))
    topFiveCrimes['primary_type'] = topFiveCrimes.index
    print('****** Top 5 Crimes ******')
    print(topFiveCrimes)
    topFiveCrimes = topFiveCrimes[::-1]
    plt.switch_backend('AGG')
    if chart_type == 'bar':
        plt.bar(topFiveCrimes['primary_type'], topFiveCrimes['counts'])
    if chart_type == 'line':
        plt.plot(topFiveCrimes['primary_type'], topFiveCrimes['counts'])
    if chart_type == 'scatter':
        plt.scatter(topFiveCrimes['primary_type'], topFiveCrimes['counts'])

    print('****** Top 5 Crimes: Stats ******')
    print('Mean', topFiveCrimes['counts'].mean())
    print('Standard Deviation', topFiveCrimes['counts'].std())
    print('Variance', topFiveCrimes['counts'].var())

    plt.subplots_adjust(left=0.10, right=0.89, bottom=0.50)
    plt.xticks(rotation=90)
    plt.title("Top 5 Crimes in my neighborhood \n", fontdict={'fontsize': 10, 'color': '#bb0e14'})
    plt.ylabel("Crimes Count", fontdict={'fontsize': 10})
    plt.xlabel("Type of Crime", fontdict={'fontsize': 10})
    plt.gcf().canvas.manager.set_window_title('Top 5 Crimes Bar Chart')
    plt.show()
    graph = get_graphToPrint()
    return graph


####################

def plotArrestsRatio():
    # Ratio of arrests to non arrests between my area and university of chicago
    s3 = df[['arrest']]  # get a series from data frame
    arrests = pd.DataFrame(s3.groupby('arrest').size().sort_values(ascending=False).rename('arrestCounts'))
    print('****** Arrests/Non-Arrests Ratio in my Neighbourhood ******')
    print(arrests)
    arrestList = []
    arrestList.append(arrests.loc[True].values[0])
    arrestList.append(arrests.loc[False].values[0])
    print(arrestList)
    plt.switch_backend('AGG')
    explode = (0.1, 0.5)
    colors = ("orange", "cyan")
    plt.subplots(figsize=(6, 5))
    plt.title("Arrests/Non-Arrests Ratio near my area \n")
    arr = ['Arrests', 'Non-Arrests']
    plt.pie(arrestList, explode=explode, shadow=True, autopct=make_autopct(arrestList), colors=colors, labels=arr)
    plt.gcf().canvas.manager.set_window_title('Arrests Ratio Pie Chart')
    plt.show()
    graph = get_graphToPrint()
    return graph


####################

def plotDomesticRatio():
    # Ratio of domestic violences between my area and university of chicago
    s3 = df[['domestic']]  # get a series from data frame
    domesticViolences = pd.DataFrame(
        s3.groupby('domestic').size().sort_values(ascending=False).rename('domesticCounts'))
    print('****** Domestic/Non-Domestic  ******')
    print(domesticViolences)
    domesticViolenceList = []
    domesticViolenceList.append(domesticViolences.loc[True].values[0])
    domesticViolenceList.append(domesticViolences.loc[False].values[0])
    print(domesticViolenceList)
    plt.switch_backend('AGG')
    explode = (0.1, 0.5)
    colors = ("orange", "cyan")
    plt.subplots(figsize=(7, 5))
    plt.title("Domestic/Non-Domestic Violences Ratio near my area \n")
    arr = ['Domestic Violence', 'Non-Domestic Violence']
    plt.pie(domesticViolenceList, explode=explode, shadow=True, autopct=make_autopct(domesticViolenceList),
            colors=colors, labels=arr)
    plt.gcf().canvas.manager.set_window_title('Domestic Violence Ratio Pie Chart')
    plt.show()
    graph = get_graphToPrint()
    return graph


####################


def plotTheftByDates(chart_type):
    # Theft crimes near my area by dates within a range
    crimes = df.copy()
    # print(crimes)
    theftByDates = df[(df["primary_type"] == "THEFT") & ((df["date"] > '2019-01-01') & (df["date"] < '2019-12-31'))]
    # print(theftByDates)

    s2 = theftByDates[['date']]  # get a series from data frame
    totalTheftcount = 0
    for i in range(0, len(s2)):
        totalTheftcount = totalTheftcount + 1
        s2.iloc[i].date = df.iloc[i].date[:10]
    crimesByTheft = pd.DataFrame(s2.groupby('date').size().rename('thefts'))
    crimesByTheft['date'] = crimesByTheft.index
    # crimeList = ['THEFT']
    # crimes = crimes[crimes['primary_type'].isin(crimeList)]
    # # theftsByDate = crimes.groupby('date').size().apply(lambda x: datetime.strptime(str(x[0]),'%Y-%m-%d').date).rename('theftsByDate')
    # theftsByDate = crimes.groupby('date').size().rename('theftsByDate')
    # theftsByDate = theftsByDate.groupby('date')

    print('****** Total Thefts between Jan 2019 - Dec 2019  ******')
    # print('Total Thefts between Jan 2019- Dec 2019:',totalTheftcount)
    print(totalTheftcount)

    # print(crimesByTheft.loc['THEFT'].values[0])
    crimesByTheft = crimesByTheft[::-1]
    # crimesByTheftData.plot(kind='barh')
    plt.switch_backend('AGG')
    if chart_type == 'bar':
        plt.bar(crimesByTheft['date'], crimesByTheft['thefts'])
    if chart_type == 'line':
        plt.plot(crimesByTheft['date'], crimesByTheft['thefts'])
    if chart_type == 'scatter':
        plt.scatter(crimesByTheft['date'], crimesByTheft['thefts'])

    plt.subplots_adjust(left=0.33, right=0.89)
    plt.title("Total Thefts between Jan 2019 - Dec 2019 \n", fontdict={'fontsize': 10, 'color': '#bb0e14'})
    plt.ylabel("Count of Thefts", fontdict={'fontsize': 10})
    plt.xlabel("Theft Date", fontdict={'fontsize': 10})
    plt.gcf().canvas.manager.set_window_title('Thefts Bar Chart')
    plt.show()
    graph = get_graphToPrint()
    return graph


####################

def plotLineChartForTheftByDates():
    # Theft crimes near my area by dates within a range
    crimes = df.copy()
    # print(crimes)
    # theftByDates = df[(df["primary_type"]=="THEFT") & ((datetime.strptime(str(df["date"]), "%d/%m/%Y %H:%M:%S.%f") > "2019-01-01") & (df["date"] <= "2019-02-01T21:00:00.000") )]
    theftByDates = df[(df["primary_type"] == "THEFT")]
    # theftByDates =datetime.strptime(str(theftByDates.loc[:, 'date']),  "%d/%m/%Y %H:%M:%S.%f")
    # for i in theftByDates.loc[:, 'date']:
    #     i=
    # print(theftByDates)

    s2 = theftByDates[['date']]  # get a series from data frame
    totalTheftcount = 0
    for i in range(0, len(s2)):
        totalTheftcount = totalTheftcount + 1
        s2.iloc[i].date = s2.iloc[i].date[:10]
        s2.iloc[i].date = datetime.strptime(s2.iloc[i].date, "%Y-%m-%d")
        # print(s2)
    # a=datetime.strptime("2020-09-12", "%Y-%m-%d")
    # print(type(a))
    k = s2['date'].apply(
        lambda x: (x < datetime.strptime('2019-01-31', '%Y-%m-%d')) & (x > datetime.strptime('2019-01-01', '%Y-%m-%d')))
    print(k)
    crimesByTheft = pd.DataFrame(k.groupby('date').size().sort_values(ascending=True).rename('thefts'))
    # df['date'] = pandas.to_datetime(crimesByTheft['date'])
    # for i in range(0, len(s2)):
    #     s2.iloc[i].date = pandas.to_datetime(s2.iloc[i].date)
    #     print(type(s2.iloc[i].date))
    # crimesByTheft = crimesByTheft.loc["date"] > "2019-01-01"
    # print(crimesByTheft)
    # crimeList = ['THEFT']
    # crimes = crimes[crimes['primary_type'].isin(crimeList)]
    # theftsByDate = crimesByTheft.groupby('date').size().apply(lambda x: datetime.strptime(str(x[0]),'%Y-%m-%d').date).rename('theftsByDate')
    # theftsByDate = crimes.groupby('date').size().rename('theftsByDate')
    # theftsByDate = theftsByDate.groupby('date')

    print('****** Total Thefts between Jan 2019 - Dec 2019  ******')
    print('Total Thefts between Jan 2019- Dec 2019:', totalTheftcount)
    # print(crimesByTheft)

    # print(crimesByTheft.loc['THEFT'].values[0])

    crimesByTheftData = crimesByTheft[::-1]

    # plt.plot(crimesByTheftData)
    plt.title("Total Thefts between Jan 2019 - Dec 2019 \n", fontdict={'fontsize': 10, 'color': '#bb0e14'})
    plt.xlabel("Count of Thefts", fontdict={'fontsize': 10})
    plt.ylabel("Theft Date", fontdict={'fontsize': 10})
    plt.gcf().canvas.manager.set_window_title('Thefts Bar Chart')
    # plt.show()


def plotTopFiveCrimesByBlock(chart_type):
    # Top 5 crimes count bet my area and university of chicago
    s2 = df[['block']]  # get a series from data frame
    topFiveCrimes = pd.DataFrame(s2.groupby('block').size().sort_values(ascending=False).head().rename('blockCounts'))
    topFiveCrimes['block'] = topFiveCrimes.index
    print('****** Top 5 Blocks by Crime Frequency ******')
    print(topFiveCrimes)
    # crime_count2 = pd.DataFrame(topFiveCrimes.groupby('005XX E 35TH ST'))
    # print(topFiveCrimes.loc['005XX E 35TH ST'][0])
    topFiveCrimes = topFiveCrimes[::-1]
    plt.switch_backend('AGG')
    if chart_type == 'bar':
        plt.bar(topFiveCrimes['block'], topFiveCrimes['blockCounts'])
    if chart_type == 'line':
        plt.plot(topFiveCrimes['block'], topFiveCrimes['blockCounts'])
    if chart_type == 'scatter':
        plt.scatter(topFiveCrimes['block'], topFiveCrimes['blockCounts'])
    print('****** Top 5 Blocks Stats: ******')

    print('Mean', topFiveCrimes['blockCounts'].mean())
    print('Standard Deviation', topFiveCrimes['blockCounts'].std())
    print('Variance', topFiveCrimes['blockCounts'].var())

    plt.subplots_adjust(left=0.16, right=0.89, bottom=0.567)
    plt.title("Top 5 Nearest blocks with most crimes \n", fontdict={'fontsize': 13, 'color': '#bb0e14'})
    plt.xlabel("block Count", fontdict={'fontsize': 11})
    plt.ylabel("Type of block", fontdict={'fontsize': 11})
    plt.xticks(rotation=90)
    plt.gcf().canvas.manager.set_window_title('Top 5 Crimes Bar Chart')
    plt.show()
    graph = get_graphToPrint()
    return graph


def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct * total / 100.0))
        return '{p:.2f}%  ({v:d})'.format(p=pct, v=val)

    return my_autopct

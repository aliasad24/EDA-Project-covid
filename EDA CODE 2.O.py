import pandas as pd
import numpy as np

covid = pd.read_csv("covid.csv")

#print(data)
#print(covid.head())
#print(covid.columns)

#print(data.isnull().sum())

#Getting the cases in india
India_case= covid[covid["location"]=="India"]

print(India_case.head())

import matplotlib.pyplot as plt
import seaborn as sns


#Total cases with dates
# sns.lineplot(x="date",y="total_cases", data=India_case)
# plt.show()


#Total cases with people vaccinated
#sns.relplot(x="total_cases",y="people_vaccinated", data= India_case)
#plt.show()

#new cases with new vaccinations
#sns.relplot(x="new_cases",y="new_vaccinations", data= India_case)
#plt.show()

#new vaccinations with new deaths
# sns.relplot(x="new_vaccinations",y="new_deaths", data= India_case)
# plt.show()


####---------------- the second data set  I used ( not my code ) link for the code attached in my essay ---------#####

# First we will import the required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df=pd.read_csv("../input/corona-virus-report/country_wise_latest.csv")
df.head()

df.shape

df.info()

grouped=df[["Confirmed","Deaths","Recovered","Country/Region"]]
grouped.head()

import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
import plotly.express as px

pio.templates.default = "plotly_dark"

fig=px.bar(grouped,y="Confirmed",x="Country/Region",title="Country having Highest CASES")

fig.show()

df1=pd.read_csv("../input/corona-virus-report/covid_19_clean_complete.csv", parse_dates=['Date'])
df1.head()

date_c = df1.groupby('Date')['Date', 'Confirmed', 'Deaths',"Lat","Long","Country/Region"].sum().reset_index()
date_c.head()

pio.templates.default = "plotly_dark"

px.line(date_c,x="Date",y="Deaths",title="WORLD WIDE DEATHS")

px.line(df1,x="Date",y="Recovered",title="Wolrd Wide Recovered")

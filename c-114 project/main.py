import pandas as pd
import plotly.express as px

df= pd.read_csv("main.csv")

fig= px.scatter(df,df["TOEFL Score"],df["Chance of Admit"],trendline="ols")

#slope and intercept were calculated outside of python using good old fashioned math! :)
slope=0.01857142857
intercept=-1.27

toefl=int(input("Enter TOEFL score: "))

chances=toefl*slope+intercept

print("Your chances of admit are approximately: "+str(chances*100)+"%")

fig.show()
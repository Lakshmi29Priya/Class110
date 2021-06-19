from os import stat
import plotly.express as px
import plotly.figure_factory as ff
import statistics
import plotly.graph_objects as go
import random
import pandas as pd
import csv

df=pd.read_csv("data.csv")
data=df["average"].tolist()

def random_set_of_data(counter):
    dataSet=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        dataSet.append(value)
    mean=statistics.mean(dataSet)
    return mean

def show_fig(mean_list):
    df=mean_list
    mean=statistics.mean(df)
    fig=ff.create_distplot([df],["average"],show_hist=False)  
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode="lines",name="Mean"))
    fig.show()

def setup():
    mean_list=[]
    for i in range(0,1000):
        set_of_means=random_set_of_data(100)
        mean_list.append(set_of_means)
    show_fig(mean_list)

    mean=statistics.mean(mean_list)
    print("mean of sampling distribution:",mean)
setup()  

population_mean=statistics.mean(data)
print("population mean:",population_mean)

def standard_deviation():
    mean_list=[]
    for i in range(0,1000):
        set_of_means=random_set_of_data(100)
        mean_list.append(set_of_means)
    std_dev=statistics.stdev(mean_list)
    print("standard deviation of sampling distribution:",std_dev)
standard_deviation()        

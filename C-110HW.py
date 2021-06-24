import pandas as pd 
import plotly.figure_factory as ff
import statistics
import random
import plotly.graph_objects as go

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()
stdPopData = statistics.stdev(data)
meanPopData = statistics.mean(data)
print("The standard deviation of the population data reading time is ", stdPopData)
print("The mean of the population data reading time is ", meanPopData)

def random_set_of_mean():
    dataset = []
    for i in range(0,30):
        random_index = random.randint(0, len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

def show_fig(mean_list):
    dataFrame = mean_list
    fig = ff.create_distplot([dataFrame], ["reading_time"], show_hist = False)
    fig.show()

def setup():
    mean_list = []
    for i in range(0,100):
        set_of_means = random_set_of_mean()
        mean_list.append(set_of_means)
    stdSampleData = statistics.stdev(mean_list)
    meanSampleData = statistics.mean(mean_list)
    print("The standard deviation of the sample data reading time is ", stdSampleData)
    print("The mean of the sample data reading time is ", meanSampleData)
    show_fig(mean_list)

setup()
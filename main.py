import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go


print("----------------------------------------------------------------")


data = pd.read_csv("Screentime-App-Details.csv")
print(data.head())


print("----------------------------------------------------------------")


data.isnull().sum()  # check for missing values in the dataset
print(data.isnull().sum())


print("----------------------------------------------------------------")

print(data.describe())



# Usage of Apps by User (Bar Chart)
AppUsagefigure = px.bar(data_frame=data, 
                x = "Date", 
                y = "Usage", 
                color="App", 
                title="Usage")
AppUsagefigure.show()



# Notifications of Apps to the User (Bar Chart)
NotificationsFigure = px.bar(data_frame=data, 
                x = "Date", 
                y = "Notifications", 
                color="App", 
                title="Notifications")
NotificationsFigure.show()



# Number of times Apps opened by the User (Bar Chart)
TimesOpenedFigure = px.bar(data_frame=data, 
                x = "Date", 
                y = "Times opened", 
                color="App",
                title="Times Opened")
TimesOpenedFigure.show()




# Relationship between the number of notifications and the amount of usage(in the form of scatter plot)
figure = px.scatter(data_frame = data, 
                    x="Notifications",
                    y="Usage", 
                    size="Notifications", 
                    trendline="ols", 
                    title = "Relationship Between Number of Notifications and Usage")
figure.show()


print("Summary: This is how we analyze a user's screen time using Python, focusing on which applications and websites they use and for how long. There’s a linear relationship between the number of notifications and the amount of usage. It means that more notifications result in more use of smartphones.")
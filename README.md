
# Screen Time Analysis Project

This project aims to analyze a user's screen time using Python, focusing on which applications and websites they use and for how long. The project utilizes various libraries such as pandas, numpy, plotly.express, and plotly.graph_objects to process, visualize, and analyze the data.

## How to run this project

To run the project, you would typically follow these steps:

1. **Clone the repository** : If the project is hosted on a version control system like GitHub, you would first clone the repository to your local machine.

```
git clone https://github.com/username/project-name.git
```

Replace `https://github.com/username/project-name.git` with the actual URL of the repository.

2. **Navigate to the project directory** : Use the `cd` command to navigate to the project directory.

```
cd project-name
```

3. **Install dependencies** : Most JavaScript projects use npm (Node Package Manager) to manage dependencies. Run the following command to install the project's dependencies:

```
npm install
```

4. Enter the below one:

```
python3 main.py
```

If the project is not hosted on a version control system, you would need to obtain the project files through other means, such as downloading a ZIP file and extracting it. The rest of the steps would remain the same.


## Data

The data used in this project is stored in a CSV file named "Screentime-App-Details.csv". The dataset contains information about the user's screen time, including the date, app, usage, notifications, and the number of times the app was opened.

## Data Preprocessing

The data is preprocessed using pandas to check for missing values and to generate descriptive statistics.

## Data Visualization

The project includes several visualizations to help analyze the data:

1. **Usage of Apps by User (Bar Chart)** : This chart shows the usage of different apps by the user on different dates.
2. **Notifications of Apps to the User (Bar Chart)** : This chart shows the number of notifications received from different apps on different dates.
3. **Number of times Apps opened by the User (Bar Chart)** : This chart shows the number of times different apps were opened by the user on different dates.
4. **Relationship between the number of notifications and the amount of usage (Scatter Plot)** : This plot shows the relationship between the number of notifications and the amount of usage. The size of the points represents the number of notifications, and a trendline is added to show the linear relationship between the two variables.

## Summary

The project provides a summary of the analysis, which states that there is a linear relationship between the number of notifications and the amount of usage. This means that more notifications result in more use of smartphones.

## Usage

To run the project, simply execute the Python script. The visualizations will be displayed in the browser.

## Dependencies

The project requires the following libraries:

* pandas
* numpy
* plotly.express
* plotly.graph_objects

These libraries can be installed using pip:

pip3 install pandas numpy plotly

## License

This project is licensed under the MIT License.

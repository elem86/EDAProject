# Step 1. Project Prerequisites

Created an account on github.com, with the required new git repository, gitignore file and README.md.

Installed pandas, plotly-express in the EDA.ipynb file. 

Created an account on render.com and linked it with my Github repository.


# Step 2. Download the data file

Downloaded the vehicles_us.csv file and placed in the root folder.


# Step 3. Exploratory Data Analysis

Created the notebooks folder and created the EDA.ipynb file.

Installed pandas, plotly-express, streamlit in this file.

At ths point I cleaned the dataset and created the charts.

## Histograms:
Distribution of Cars by Condition - Wanted to see the amount of ads per condition.

Distribution of Cars by Manufacturer - A histogram to show the amount of ads per manufacturer.

## Scatterplots:
Average Price by Manufacturer and Year - This plot shows how much the year and manufacturer affects the price.

Year vs. days listed - Here I wantede to show how much the age of the car affects how long the car is on the market.


# Step 4. Develop the web application dashboard

Created the app.py file in the root of the project’s directory and imported streamlit, pandas and plotly_express.

I copied over and modified the charts from the Jupiter notebook and added a checkbox.

With the checkbox you can choose between younger than 3 months and older than 3 months ads.

# Step 5. Deploy the final version of the application to Render

Created .streamlit/config.toml structure. Set up the webapp on render.com.

## URL for app on Render:
https://edaproject6.onrender.com
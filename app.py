import pandas as pd
import streamlit as st
import plotly.express as px
import numpy as np
import altair as alt

df = pd.read_csv("vehicles_us.csv")

df['is_4wd'] = df['is_4wd'].fillna(0).astype(bool)
df.groupby("is_4wd")["is_4wd"].count()

df["model_year"] = df["model_year"].fillna(df.groupby('model')["model_year"].transform('median'))
df["cylinders"] = df["cylinders"].fillna(df.groupby('model')["cylinders"].transform('median'))
df["odometer"] = df["odometer"].fillna(df.groupby('model_year')["odometer"].transform('median'))

df['odometer'] = df['odometer'].fillna(0)
# found a row where the odometer was 0, probably a new car, this is the fix I applied. Since it is one row of data, there is no significance to it. 

types_to_replace = ['model_year', 'cylinders', 'odometer']
for column in types_to_replace:
    df[column] = df[column].apply(np.int64)

df["paint_color"] = df["paint_color"].fillna("unknown")
# paint_color was the only non numberic column with mising values, replaced those values with "unknown".

df["date_posted"] = df["date_posted"].astype("datetime64[ns]")
# converted the date_posted column to datetime type.

df["manufacturer"] = df["model"].apply(lambda x: x.split()[0])

# create a text header above the dataframe
st.header("Data viewer")
# display the dataframe with streamlit
st.dataframe(df)


st.header("Distribution of Cars by Model Year")

fig = px.histogram(df, x="model_year", nbins=25, histnorm='density',                     
                    color_discrete_sequence=["blue"],
                    barmode='overlay')

st.write(fig)


st.header("Year vs. days listed")

show_younger_10 = st.checkbox("Less than three months old ads")
if show_younger_10:
    df = df.loc[(df["days_listed"] < 90)]

show_younger_5 = st.checkbox("More than three months old ads")
if show_younger_5:
    df = df.loc[(df["days_listed"] > 90)]

fig = px.scatter(
    df,
    x="model_year",
    y="days_listed",
    labels={"model_year": "Year", "days_listed": "Days Listed"},
)
st.write(fig)

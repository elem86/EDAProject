import pandas as pd
import streamlit as st
import plotly.express as px

df = pd.read_csv("vehicles_us.csv")

df["is_4wd"] = df["is_4wd"].fillna(0).astype(int)
df.groupby("is_4wd")["is_4wd"].count()

types_to_replace = ["model_year", "cylinders", "odometer"]
for column in types_to_replace:
    df[column] = df[column].fillna(df[column].median()).astype(int)

df["paint_color"] = df["paint_color"].fillna("unknown")
# paint_color was the only non numberic column with mising values, replaced those values with "unknown".

df["date_posted"] = df["date_posted"].astype("datetime64[ns]")
# converted the date_posted column to datetime type.

df["manufacturer"] = df["model"].apply(lambda x: x.split()[0])

# create a text header above the dataframe
st.header("Data viewer")
# display the dataframe with streamlit
st.dataframe(df)


st.header("Distribution of Cars by Condition")

fig = px.histogram(
    df,
    x="condition",
    histnorm="density",
    color_discrete_sequence=["blue"],
    barmode="overlay",
)
fig.update_layout(xaxis={"categoryorder": "total descending"})
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
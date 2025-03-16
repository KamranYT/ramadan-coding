import streamlit as st # for creating web interface
import pandas as pd # for data manipulation
import datetime #  for handling dates
import csv # for reading and writting csv files.
import os # for file operations

# Define the file name for storing mood data
MOOD_FILE = "mood_log.csv"

def load_mood_data():
    if not os.path.exists(MOOD_FILE):
        return pd.DataFrame(columns=["Date", "Mood"])
    return pd.read_csv(MOOD_FILE)

def save_mood_data(date, mood):
    with open(MOOD_FILE, "a") as file:

        writer = csv.writer(file)

        writer.writerow([date, mood])

st.set_page_config(page_title="Mood Tracker", page_icon="👻")
st.title("Mood Tracker")

today = datetime.date.today()

st.subheader("How are you feeling today?")

mood = st.selectbox("Select your mood", ["Happy", "Sad", "Angry", "Neutral"])

if st.button("Log Mood"):

    save_mood_data(today, mood)
    
    st.success("Mood Logged Successfully!")

data = load_mood_data()

if not data.empty:

    st.subheader("Mood Treds Over Time")

    data["Date"] = pd.to_datetime(data["Date"])

    mood_counts = data.groupby("Mood").count()["Date"]

    st.bar_chart(mood_counts)

    st.write("Build by [Muhammad Kamran](https://github.com/KamranYT)")
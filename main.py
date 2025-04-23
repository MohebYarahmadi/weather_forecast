import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast for Next Days")
place = st.text_input("City: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                help="Select the number of forecated days")
option = st.selectbox("Select data to view",
                    ("Temperature", "Sky"))

if place:
    try:
        filtered_data = get_data(place, days)
        st.subheader(f"{option} for the next {days} days in {place}")
        # Get data


        if option == "Temperature":
            temperature = [dict["main"]["temp"] / 10 for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            # Create Temperature plot
            figure = px.line(x=dates, y=temperature,
                    labels={"x": "Date", "y": "Temperature (C)"})
            st.plotly_chart(figure)

        if option == "Sky":
            images = {
                    "Clear": "images/clear.png",
                    "Clouds": "images/cloud.png",
                    "Rain": "images/rain.png",
                    "Snow": "images/snow.png"
                    }
            sky = [dict["weather"][0]["main"] for dict in filtered_data]
            image_paths = [images[condition] for condition in sky]
            # Create Sky Plot
            st.image(image_paths, width=85)
    except KeyError:
        st.subheader(f"Is {place} a real place? ")

else:
    st.subheader("First, type a city name!")

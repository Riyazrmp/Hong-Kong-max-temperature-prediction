import streamlit as st
import pickle
import numpy as np


def load_model():
    with open('WeatherRidgeModel.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

regressor = data["model"]
# le_country = data["le_country"]
# le_education = data["le_education"]

def show_predict_page():
    st.title("Hong Kong Maximum Temperature prediction")

    st.write("""### We need some information about today's weather to predict next day's Maximum Temperature""")

    # countries = (
    #     "United States",
    #     "India",
    #     "United Kingdom",
    #     "Germany",
    #     "Canada",
    #     "Brazil",
    #     "France",
    #     "Spain",
    #     "Australia",
    #     "Netherlands",
    #     "Poland",
    #     "Italy",
    #     "Russian Federation",
    #     "Sweden",
    # )

    # education = (
    #     "Less than a Bachelors",
    #     "Bachelor’s degree",
    #     "Master’s degree",
    #     "Post grad",
    # )

    # country = st.selectbox("Country", countries)
    # education = st.selectbox("Education Level", education)

    # expericence = st.slider("Years of Experience", 0, 50, 3)
#mean_temp	grass_min_temp	max_temp	mean_amount_of_cloud	mean_dew_point_temp	mean_wet_bulb_temp	min_temp	pressure	rainfall	rh
    mean_temp = st.text_input("Mean temperature (ºC)","")
    grass_min_temp = st.text_input("Grass Minimum Temperature (ºC)","")
    max_temp = st.text_input("Maximum temperature (ºC)","")
    min_temp = st.text_input("Minimum temperature (ºC)","")
    mean_amount_of_cloud = st.text_input("Max amount of clouds (%)","")
    mean_dew_point_temp = st.text_input("Mean dew point temperature (ºC)","")
    mean_wet_buld_temperature = st.text_input("Mean wet bulb temperature (ºC)","")
    pressure = st.text_input("Pressure (hpa)","")
    rainfall = st.text_input("rainfall (mm)","")
    rh = st.text_input("Relative Humidity (%)","")
    


    ok = st.button("Calculate Max Temperature")
    if ok:
        X = np.array([[mean_temp, grass_min_temp, max_temp,mean_amount_of_cloud,mean_dew_point_temp,mean_wet_buld_temperature,min_temp,pressure,rainfall,rh ]])
        # X[:, 0] = le_country.transform(X[:,0])
        # X[:, 1] = le_education.transform(X[:,1])
        X = X.astype(float)

        temp = regressor.predict(X)
        st.subheader(f"Next day's max temperature will be about {temp[0]:.2f} ºC")
show_predict_page()
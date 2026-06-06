import streamlit as st
import requests

API_KEY = "ce96f6905391e6123e67e7eaee921765"

st.set_page_config(
    page_title="AgriShield",
    page_icon="🌾",
    layout="wide"
)

st.title("🌾 AgriShield")
st.subheader("AI-Powered Farmer Disaster Early Warning System")

farmer = st.text_input("Farmer Name")
city = st.text_input("Location (City)")

crop = st.selectbox(
    "Select Crop",
    ["Wheat", "Rice", "Cotton", "Maize", "Sugarcane"]
)

if st.button("Check Disaster Risk"):

    if city == "":
        st.error("Please enter a city name")
    else:

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

        response = requests.get(url)

        if response.status_code == 200:

            data = response.json()

            temp = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            wind = data["wind"]["speed"]
            weather = data["weather"][0]["description"]

            st.success("Weather Data Retrieved Successfully")

            col1, col2, col3 = st.columns(3)

            col1.metric("🌡 Temperature", f"{temp} °C")
            col2.metric("💧 Humidity", f"{humidity}%")
            col3.metric("🌬 Wind Speed", f"{wind} m/s")

            st.info(f"Current Weather: {weather}")

            flood_risk = "Low"
            heat_risk = "Low"
            storm_risk = "Low"
            crop_damage = "Low"

            if humidity > 85:
                flood_risk = "High"

            if temp > 40:
                heat_risk = "High"

            if wind > 10:
                storm_risk = "High"

            if crop == "Wheat" and temp > 40:
                crop_damage = "High"

            elif crop == "Rice" and humidity > 85:
                crop_damage = "High"

            elif crop == "Cotton" and wind > 10:
                crop_damage = "High"

            elif crop == "Maize" and temp > 42:
                crop_damage = "High"

            elif crop == "Sugarcane" and humidity > 90:
                crop_damage = "Medium"

            st.header("📊 Risk Analysis")

            c1, c2, c3, c4 = st.columns(4)

            c1.metric("Flood Risk", flood_risk)
            c2.metric("Heatwave Risk", heat_risk)
            c3.metric("Storm Risk", storm_risk)
            c4.metric("Crop Damage Risk", crop_damage)

            st.header("🤖 Recommendations")

            recommendations = []

            if heat_risk == "High":
                recommendations.append(
                    "Increase irrigation and avoid field work during peak afternoon heat."
                )

            if flood_risk == "High":
                recommendations.append(
                    "Improve drainage and move stored seeds to a safe location."
                )

            if storm_risk == "High":
                recommendations.append(
                    "Secure equipment and monitor weather alerts regularly."
                )

            if crop_damage == "High":
                recommendations.append(
                    f"Your {crop} crop may be affected by current weather conditions."
                )

            if len(recommendations) == 0:
                recommendations.append(
                    "Weather conditions are currently favorable for farming."
                )

            for rec in recommendations:
                st.success(rec)

            st.header("🌍 Impact")

            st.write(
                """
                AgriShield helps farmers by:
                - Providing early weather-based warnings
                - Reducing crop losses
                - Supporting climate resilience
                - Improving agricultural decision making
                """
            )

        else:
            st.error("City not found or API key is not active yet.")

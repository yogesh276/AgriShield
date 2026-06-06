import streamlit as st

st.set_page_config(page_title="AgriShield", page_icon="🌾")

st.title("🌾 AgriShield")
st.subheader("AI-Powered Farmer Disaster Early Warning System")

farmer = st.text_input("Farmer Name")
location = st.text_input("Location")

crop = st.selectbox(
    "Select Crop",
    ["Wheat", "Rice", "Cotton", "Maize", "Sugarcane"]
)

if st.button("Check Disaster Risk"):

    st.metric("Flood Risk", "Medium")
    st.metric("Heatwave Risk", "Low")
    st.metric("Storm Risk", "High")

    st.warning("Overall Risk Level: Medium")

    st.write("### AI Recommendations")

    st.success("Store seeds in a safe dry location")
    st.success("Monitor local weather alerts")
    st.success("Keep irrigation systems ready")

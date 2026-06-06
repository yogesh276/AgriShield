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
    st.warning("Risk Level: Medium")

    st.write("### Recommendations")
    st.write("✅ Monitor weather updates")
    st.write("✅ Keep irrigation ready")
    st.write("✅ Protect crops from extreme weather")

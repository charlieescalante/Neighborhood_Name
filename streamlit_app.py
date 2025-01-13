import streamlit as st
from geopy.geocoders import Nominatim
import time

# Fetch user agent from Streamlit secrets
user_agent = st.secrets["USER_AGENT"]
geolocator = Nominatim(user_agent=user_agent, timeout=10)  # Increase timeout to 10 seconds

# Title of the app
st.title("Reverse Geocoding App")

# User input for latitude and longitude
latitude = st.text_input("Enter Latitude:", "31.2158271")
longitude = st.text_input("Enter Longitude:", "-85.3634326")

# Button to trigger reverse geocoding
if st.button("Get Address"):
    try:
        # Perform reverse geocoding
        location = geolocator.reverse(f"{latitude},{longitude}")
        time.sleep(1)  # Pause for 1 second to respect rate limits
        if location:
            st.success(f"Address: {location.raw['display_name']}")
        else:
            st.error("No address found for the given coordinates.")
    except Exception as e:
        st.error(f"An error occurred: {e}")

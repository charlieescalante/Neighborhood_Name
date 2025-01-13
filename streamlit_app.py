import streamlit as st
from geopy.geocoders import Nominatim

# Fetch user agent from Streamlit secrets
user_agent = st.secrets["USER_AGENT"]
geolocator = Nominatim(user_agent=user_agent, timeout=10)  # Set a reasonable timeout

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
        if location:
            # Display the result
            st.success(f"Address: {location.raw['display_name']}")
        else:
            # Handle case where no result is found
            st.error("No address found for the given coordinates.")
    except Exception as e:
        # Catch errors and display them
        st.error(f"An error occurred: {e}")

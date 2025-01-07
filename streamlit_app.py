import streamlit as st
import requests

# App Title
st.title("Neighborhood Finder")

# Input Section
latitude = st.text_input("Enter Latitude:")
longitude = st.text_input("Enter Longitude:")

# Button to Get Neighborhood
if st.button("Get Neighborhood"):
    if latitude and longitude:
        try:
            # Reverse Geocoding API Call (Nominatim)
            url = f"https://nominatim.openstreetmap.org/reverse?lat={latitude}&lon={longitude}&format=json"
            response = requests.get(url)
            data = response.json()

            # Extract Neighborhood
            if "address" in data and "neighbourhood" in data["address"]:
                neighborhood = data["address"]["neighbourhood"]
                st.success(f"Neighborhood: {neighborhood}")
            else:
                st.warning("No neighborhood data found for these coordinates.")
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.error("Please enter both latitude and longitude.")

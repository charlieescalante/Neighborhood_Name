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
            # Validate inputs
            lat = float(latitude)
            lon = float(longitude)
            if not (-90 <= lat <= 90 and -180 <= lon <= 180):
                st.error("Latitude must be between -90 and 90, Longitude must be between -180 and 180.")
            else:
                # Reverse Geocoding API Call
                url = f"https://nominatim.openstreetmap.org/reverse?lat={lat}&lon={lon}&format=json"
                response = requests.get(url)
                st.write(f"Raw Response: {response.text}")  # Debugging step

                if response.status_code == 200:
                    try:
                        data = response.json()
                        if "address" in data and "neighbourhood" in data["address"]:
                            neighborhood = data["address"]["neighbourhood"]
                            st.success(f"Neighborhood: {neighborhood}")
                        else:
                            st.warning("No neighborhood data found for these coordinates.")
                    except ValueError:
                        st.error("Invalid JSON response from the API.")
                else:
                    st.error(f"API call failed with status code {response.status_code}.")
        except ValueError:
            st.error("Please enter valid numerical values for latitude and longitude.")
    else:
        st.error("Please enter both latitude and longitude.")

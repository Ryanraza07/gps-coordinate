#!/usr/bin/env python
# coding: utf-8

# In[1]:


from geopy.geocoders import Nominatim

def get_gps_coordinates(location):
    try:
        location_info = Nominatim(user_agent="gps_coordinates_finder").geocode(location)
        return location_info.latitude, location_info.longitude
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    your_location = "Your Location"
    coordinates = get_gps_coordinates(your_location)
    
    if coordinates:
        print(f"GPS Coordinates for {your_location}: Latitude {coordinates[0]}, Longitude {coordinates[1]}")
    else:
        print("Unable to find GPS coordinates.")


# In[ ]:





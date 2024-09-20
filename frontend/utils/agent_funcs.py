import streamlit as st
import requests

def agentInit(userData):
    #start and end details are a tuple of (layman address, (lat, long))
    st.session_state.agent_active = True

    url = "http://3.89.63.81:80/collect-user-data" 
    
    try:
        # Send user details to backend API to store info
        res = requests.post(url, json=userData)

        if res.status_code == 200:
            st.success(f"Response from backend: {res.json()['message']}")
        else:
            st.error(f"Error: {res.status_code} - {res.text}")
    except Exception as e:
        st.error(f"Request failed: {e}")
    
    return 

def agentRouting():
    url = "http://3.89.63.81:80/generate_route"

    # Define the headers
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json"
    }
    # Make the POST request
    response = requests.post(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        st.success("Successfully generated route!")
        return response.json()
    else:
        st.error(f"Failed with status code {response.status_code}")
    

# streamlit_client.py

import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8000"


# (Yeh line Streamlit UI par "Todo App" ka title display karta hai.)
st.title("Todo App")



def create_todo():
     # Text input fields for Todo title and description
    title = st.text_input("Enter Todo Title")
    description = st.text_area("Enter Todo Description")
    # Button to trigger Todo creation
    if st.button("Add Todo"):
        # Sending a POST request to create a new Todo
        response = requests.post(f"{BASE_URL}/todos/", json={"title": title, "description": description})

        # Checking if the request was successful (status code 200)
        if response.status_code == 200:
            st.success("Todo added successfully")


def delete_todo():
    # Number input field for Todo ID to be deleted
    todo_id = st.number_input("Enter Todo ID to delete")

    # Button to trigger Todo deletion
    if st.button("Delete Todo"):
        # Sending a DELETE request to delete the specified Todo
        response = requests.delete(f"{BASE_URL}/todos/{todo_id}")

        # Checking if the request was successful (status code 200)
        if response.status_code == 200:
            st.success("Todo deleted successfully")


# (Yeh check karta hai ki script directly run kiya gaya hai ya kisi aur script se import kiya gaya hai. 
# Agar script directly run kiya gaya hai, toh 'create_todo()' aur 'delete_todo()' functions call hote hain.)
if __name__ == "__main__":
    create_todo()
    delete_todo()
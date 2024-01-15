# python_console_client.py

import requests


# (Yeh variable ek base URL store karta hai, jise hum API ke endpoints ke sath combine karke requests bhejte hain.)
BASE_URL = "http://127.0.0.1:8000"


# (Yeh Ek function hai jo Todo create karne ke liye POST request bhejta hai. 
# User se input lekar title aur description define kiye jaate hain.)
def create_todo():
    title = input("Enter Todo Title: ")
    description = input("Enter Todo Description: ")
    response = requests.post(f"{BASE_URL}/todos/", json={"title": title, "description": description})
    if response.status_code == 200:
        print("Todo added successfully")


# (Yeh Ek aur function hai jo Todo delete karne ke liye DELETE request bhejta hai. 
# User se input lekar Todo ID define kiya jata hai.)
def delete_todo():
    todo_id = input("Enter Todo ID to delete: ")
    response = requests.delete(f"{BASE_URL}/todos/{todo_id}")
    if response.status_code == 200:
        print("Todo deleted successfully")


# (Yeh check karta hai ki script directly run kiya gaya hai ya kisi aur script se import kiya gaya hai. 
# Agar script directly run kiya gaya hai, toh 'create_todo()' aur 'delete_todo()' functions call hote hain.)
if __name__ == "__main__":
    create_todo()
    delete_todo()
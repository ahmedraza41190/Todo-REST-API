from pydantic import BaseModel


# (Yeh TodoCreate class ek Pydantic model hai jo Todo items ko create karne ke liye use hota hai.
# Ismein title aur description fields hain, dono string type ke hain. 
# Yeh ek aasan tareeka hai data ko validate karne ka, 
# jisse aapko type errors se bachne mein madad milti hai.)
class TodoCreate(BaseModel):
    title: str
    description: str
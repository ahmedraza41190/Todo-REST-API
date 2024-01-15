/// nodejs_console_client.ts

import axios from 'axios';


// (Yeh variable ek base URL store karta hai jise hum API ke endpoints ke sath combine karke requests bhejte hain.)
const BASE_URL = "http://127.0.0.1:8000";


// (Ek asynchronous function hai jo 'createTodo' ke naam se define ki gayi hai. 
// Ismein naya Todo create karne ke liye ek POST request bheja jata hai.)
async function createTodo() {
    const title = 'Sample Title';
    const description = 'Sample Description';
    try {
        const response = await axios.post(`${BASE_URL}/todos/`, { title, description });
        console.log("Todo added successfully");
    } catch (error) {
        console.error("Error:", error.message);
    }
}


// (Ek aur asynchronous function hai jo 'deleteTodo' ke naam se define ki gayi hai. 
// Ismein ek DELETE request bheja jata hai specified Todo ko delete karne ke liye.)
async function deleteTodo() {
    const todoId = 1; // Replace with the desired Todo ID
    try {
        const response = await axios.delete(`${BASE_URL}/todos/${todoId}`);
        console.log("Todo deleted successfully");
    } catch (error) {
        console.error("Error:", error.message);
    }
}


// (In lines se yeh functions call hote hain, jisse actual API requests bheje ja sakte hain.)
createTodo();
deleteTodo();

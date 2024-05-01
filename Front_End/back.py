from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import mysql.connector

mydatabase = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="ttt" 
)


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with your frontend origin
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

@app.get("/{batch}")
async def getter(batch: str):  # Define 'batch' as a required path parameter
    try:
        cursor = mydatabase.cursor()

        # Use parameterized query with %s for user-provided data
        query = "SELECT * FROM alldata WHERE batch = %s"
        cursor.execute(query, (batch,))

        data = cursor.fetchall()


        cursor.close()
        return data

    except mysql.connector.Error as err:
        print(f"Error reading data from MySQL: {err}")
        return {"error": "Failed to read data from database"}
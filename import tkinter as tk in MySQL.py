import tkinter as tk
from tkinter import messagebox
import mysql.connector
from datetime import datetime

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="yourpassword",
    database="ecotrack"
)

cursor = db.cursor()

def calculate_and_save():
    try:
        username = entry_username.get()
        transportation = float(entry_transport.get())
        electricity = float(entry_electricity.get())
        diet = float(entry_diet.get())
        shopping = float(entry_shopping.get())
        
        total_emissions = (
            transportation * 0.21 +
            electricity * 0.5 +
            diet * 1.5 +
            shopping * 2.0
        )
        
        query = """
        INSERT INTO users (username, transportation, electricity, diet, shopping, total_footprint)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        data = (username, transportation, electricity, diet, shopping, total_emissions)
        cursor.execute(query, data)
        db.commit()
        
        result_label.config(text=f"Total Carbon Footprint: {total_emissions:.2f} kg CO2")
        messagebox.showinfo("Success", "Data saved successfully!")
        load_data()
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")

def load_data():
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    
    data_display.delete(1.0, tk.END)
    for row in rows:
        user_data = f"User: {row[1]}, Footprint: {row[6]:.2f} kg CO2, Date: {row[7]}\n"
        data_display.insert(tk.END, user_data)

window = tk.Tk()
window.title("EcoTrack - Carbon Footprint Calculator")
window.geometry("600x600")

tk.Label(window, text="Username:").pack()
entry_username = tk.Entry(window)
entry_username.pack()

tk.Label(window, text="Transportation (km traveled):").pack()
entry_transport = tk.Entry(window)
entry_transport.pack()

tk.Label(window, text="Electricity Usage (kWh):").pack()
entry_electricity = tk.Entry(window)
entry_electricity.pack()

tk.Label(window, text="Diet (meals per day):").pack()
entry_diet = tk.Entry(window)
entry_diet.pack()

tk.Label(window, text="Shopping (items purchased):").pack()
entry_shopping = tk.Entry(window)
entry_shopping.pack()

calculate_button = tk.Button(window, text="Calculate & Save", command=calculate_and_save)
calculate_button.pack()

result_label = tk.Label(window, text="Total Carbon Footprint: --")
result_label.pack()

tk.Label(window, text="Stored User Data:").pack()
data_display = tk.Text(window, height=10, width=70)
data_display.pack()

load_data()

window.mainloop()

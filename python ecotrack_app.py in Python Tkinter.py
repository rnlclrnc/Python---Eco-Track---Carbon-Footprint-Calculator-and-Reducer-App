import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Function to calculate carbon footprint
def calculate_footprint():
    try:
        transportation = float(entry_transport.get())
        electricity = float(entry_electricity.get())
        diet = float(entry_diet.get())
        shopping = float(entry_shopping.get())
        
        # Carbon footprint calculation (example formula)
        total_emissions = (
            transportation * 0.21 +  # kg CO2 per km
            electricity * 0.5 +     # kg CO2 per kWh
            diet * 1.5 +            # kg CO2 per meal
            shopping * 2.0          # kg CO2 per item
        )
        
        result_label.config(text=f"Total Carbon Footprint: {total_emissions:.2f} kg CO2")
        suggest_tips(total_emissions)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")

# Function to suggest tips based on total emissions
def suggest_tips(total_emissions):
    tips_text.delete(1.0, tk.END)
    tips_text.insert(tk.END, "Suggestions to reduce your footprint:\n\n")
    
    if total_emissions > 1000:
        tips_text.insert(tk.END, "- Consider carpooling or using public transport.\n")
        tips_text.insert(tk.END, "- Switch to energy-efficient appliances.\n")
    elif total_emissions > 500:
        tips_text.insert(tk.END, "- Reduce meat consumption in your diet.\n")
        tips_text.insert(tk.END, "- Minimize online shopping.\n")
    else:
        tips_text.insert(tk.END, "- Keep up the good work! Aim for even smaller emissions.\n")

# Function to show a pie chart of contributions
def show_pie_chart():
    try:
        transportation = float(entry_transport.get())
        electricity = float(entry_electricity.get())
        diet = float(entry_diet.get())
        shopping = float(entry_shopping.get())
        
        labels = ['Transportation', 'Electricity', 'Diet', 'Shopping']
        values = [
            transportation * 0.21,
            electricity * 0.5,
            diet * 1.5,
            shopping * 2.0
        ]
        
        fig, ax = plt.subplots()
        ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=140)
        ax.set_title("Carbon Footprint Breakdown")
        
        # Display the pie chart in the Tkinter window
        canvas = FigureCanvasTkAgg(fig, master=window)
        canvas.draw()
        canvas.get_tk_widget().pack()
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")

# Create the Tkinter window
window = tk.Tk()
window.title("EcoTrack - Carbon Footprint Calculator")
window.geometry("500x600")

# Input fields
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

# Calculate button
calculate_button = tk.Button(window, text="Calculate Footprint", command=calculate_footprint)
calculate_button.pack()

# Result label
result_label = tk.Label(window, text="Total Carbon Footprint: --")
result_label.pack()

# Suggestions section
tk.Label(window, text="Suggestions to Reduce Your Footprint:").pack()
tips_text = tk.Text(window, height=10, width=50)
tips_text.pack()

# Pie chart button
pie_chart_button = tk.Button(window, text="Show Pie Chart", command=show_pie_chart)
pie_chart_button.pack()

# Run the application
window.mainloop()

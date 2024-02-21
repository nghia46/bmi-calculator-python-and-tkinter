import tkinter as tk
def bmi_to_classification(bmi):
    if bmi < 16:
        return "Severe Thinness"
    elif bmi >= 16 and bmi < 17:
        return "Moderate Thinness"
    elif bmi >= 17 and bmi < 18.5:
        return "Mild Thinness"
    elif bmi >= 18.5 and bmi < 25:
        return "Normal"
    elif bmi >= 25 and bmi < 30:
        return "Overweight"
    elif 30 <= bmi < 35:
        return "Obese Class I (Moderate)"
    elif 35 <= bmi < 40:
        return "Obese Class II (Severe)"
    else:
        return "Obese Class III (Very Severe)"

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get()) / 100
        
        if weight <= 0 or height <= 0:
            result_label.config(text="Invalid input. Please enter positive values for weight and height.")
            return
        # Calculate BMI
        bmi = weight / (height ** 2)

        # Display result to result lable
        result_label.config(text=f"Your BMI is: {bmi:.2f}",fg="black")

        # Display classification
        classification = bmi_to_classification(bmi)
        classification_lable.config(text=f"Classification: {classification}")
    except Exception:
        result_label.config(text="Error while calculate",fg="red")

root = tk.Tk()
root.geometry("400x300")
root.title("BMI Calculator")  # Correct title assignment

# Create title label
title_label = tk.Label(root, text="BMI Calculator", font=("Helvetica", 20),fg="red")
# Create weight label
weight_label = tk.Label(root, text="Weight (kg):", font=("Helvetica", 12))
# Create height label
height_label = tk.Label(root, text="Height (cm):", font=("Helvetica", 12))
# Create weight entry
weight_entry = tk.Entry(root, width=30, font=("Helvetica", 12))
# Create height entry
height_entry = tk.Entry(root, width=30, font=("Helvetica", 12))
# Create Calc button
calc_btn = tk.Button(root, text="Calculate", width=10, font=("Helvetica", 12),fg="blue",command=calculate_bmi)
# Create result lable
result_label = tk.Label(root, font=("Helvetica", 12),text="result")
# Create classification lable
classification_lable = tk.Label(root,font=("Helvetica", 12),text="classification")
# Grid layout
title_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)  # Span across two columns
weight_label.grid(row=2, column=0, padx=5, pady=10)
height_label.grid(row=1, column=0, padx=5, pady=10)
weight_entry.grid(row=2, column=1, padx=5, pady=10)
height_entry.grid(row=1, column=1, padx=5, pady=10)
calc_btn.grid(row=3, column=0, columnspan=2, padx=10, pady=10)  # Span across two columns
result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=(30,5))  # Span across two columns
classification_lable.grid(row=5,column=0,columnspan=2,padx=10,pady=0)

root.mainloop()

import tkinter as tk
from tkinter import ttk


def perform_conversion():
    unit = unit_var.get()
    conversion = conversion_var.get()
    value = float(entry.get())

    if unit == "Length":
        if conversion == "Centimeter to Meter":
            result =float(value / 100)
        elif conversion == "Meter to Centimeter":
            result = value * 100
        elif conversion == "Centimeter to Inch":
            result = value / 2.54
        elif conversion == "Inch to Centimeter":
            result = value * 2.54
        elif conversion == "Centimeter to Kilometer":
            result = value / 100000
        elif conversion == "Kilometer to Centimeter":
            result = value * 100000
        elif conversion == "Centimeter to Feet":
            result = value / 30.48
        elif conversion == "Feet to Centimeter":
            result = value * 30.48
        elif conversion == "Kilometer to Mile":
            result = value / 1.609
        elif conversion == "Mile to Kilometer":
            result = value * 1.609
        elif conversion == "Centimeter to Feet":
            result = value / 30.48
        elif conversion == "Feet to Inches":
            result = value * 12
        elif conversion == "Square Feet to Square Meters":
            result = value / 10.764

    elif unit == "Mass":
        if conversion == "Gram to Kilogram":
            result = value / 1000
        elif conversion == "Kilogram to Gram":
            result = value * 1000
        elif conversion == "Kilogram to Tonne":
            result = value / 1000
        elif conversion == "Tonne to Kilogram":
            result = value * 1000
        elif conversion == "Milligram to Kilogram":
            result = value / 1e+6
        elif conversion == "Kilogram to Milligram":
            result = value * 1e+6
        elif conversion == "Milligram to Gram":
            result = value / 1000
        elif conversion == "Gram to Milligram":
            result = value * 1000
        elif conversion == "Kilogram to Pound (lb)":
            result = value * 2.20462
        elif conversion == "Pound (lb) to Kilogram":
            result = value / 2.20462
        elif conversion == "Micrograms to Gram":
            result = value / 1e+6
        elif conversion == "Micrograms to Kilogram":
            result = value / 1e+9
        
    elif unit == "Temperature":
        if conversion == "Celsius to Fahrenheit":
            result = (value * 9/5) + 32
        elif conversion == "Celsius to Kelvin":
            result = value + 273.15
        elif conversion == "Fahrenheit to Celsius":
            result = (value - 32) * 5/9
        elif conversion == "Fahrenheit to Kelvin":
            result = (value - 32) * 5/9 + 273.15
        elif conversion == "Kelvin to Celsius":
            result = value - 273.15
        elif conversion == "Kelvin to Fahrenheit":
            result = (value * 9/5) - 459.67
        
    elif unit == "Speed":
        if conversion == "Mile per hour to kilometer per hour":
            result = value * 1.60934
        elif conversion == "Kilometer per hour to Mile per hour":
            result = value / 1.60934
        elif conversion == "Mile per hour to Meter per Second":
            result = value / 2.237
        elif conversion == "Meter per Second to Mile per hour":
            result = value * 2.237
        elif conversion == "Kilometer per hour to Meter per Second":
            result = value / 3.6
        elif conversion == "Meter per Second to Kilometer per hour":
            result = value * 3.6
        
    elif unit == "Energy":
        if conversion == "Joule to Kilojoule":
            result = value / 1000
        elif conversion == "Kilojoule to Joule":
            result = value * 1000
        elif conversion == "Joule to Kilocalorie":
            result = value / 4184
        elif conversion == "Kilocalorie to Joule":
            result = value * 4184
        elif conversion == "Kilojoule to Kilocalorie":
            result = value / 4.184
        elif conversion == "Kilocalorie to Kilojoule":
            result = value * 4.184
            
    elif unit == "Pressure":
        if conversion == "Bar to Pascal":
            result = value * 100000
        elif conversion == "Bar to Standard atmosphere":
            result = value / 1.013
        elif conversion == "Pascal to Bar":
            result = value / 100000
        elif conversion == "Pascal to Standard atmosphere":
            result = value / 101325
        elif conversion == "Standard atmosphere to Pascal":
            result = value * 101325
        elif conversion == "Standard atmosphere to Bar":
            result = value * 1.01325

    elif unit == "Area":
        if conversion == "Square Feet to Square Meter":
            result = value /10.764
        elif conversion == "Square Feet to Acres":
            result = value /43560
        elif conversion == "Square Feet to Hectres":
            result = value /107639.104
        

    return result


window = tk.Tk()
window.title("Unit Converter")
window.geometry("400x250")


unit_var = tk.StringVar()
conversion_var = tk.StringVar()


entry_label = tk.Label(window, text="Enter a number to convert:")
entry_label.pack()

entry = tk.Entry(window)
entry.pack()


unit_label = tk.Label(window, text="Select Unit:")
unit_label.pack()

unit_menu = ttk.Combobox(window, textvariable=unit_var)
unit_menu['values'] = ("Length", "Mass", "Temperature", "Time", "Speed", "Energy", "Pressure", "Area")
unit_menu.pack()


def update_conversion_options(event):
    selected = unit_var.get()
    if selected == "Length":
        conversion_options = [
            "Centimeter to Meter",
            "Meter to Centimeter",
            "Centimeter to INCH",
            "INCH to Centimeter",
            "Centimeter to KiloMetre",
            "KiloMetre to Centimeter",
            "Centimeter to FOOT",
            "FOOT to Centimeter",
            "Kilometre to Mile",
            "Mile to Kilometre",
            "Centimeter to Feets",
            "Feet to Inches",
            "Sqft to sqmtrs",
            "Sqft to Hectare/Acres"
        ]
    elif selected == "Mass":
        conversion_options = [
            "Gram to Kilogram",
            "Kilogram to Gram",
            "Kilogram to Tonne",
            "Tonne to Kilogram",
            "Milligram to Kilogram",
            "Kilogram to Milligram",
            "Milligram to Gram",
            "Gram to Milligram",
            "kilogram to pound (lb)",
            "pound (lb) to Kilogram",
            "Micrograms to gram",
            "Micrograms to Kilogram"
        ]
    elif selected == "Temperature":
        conversion_options = [
            "Celsius to Fahrenheit",
            "Celsius to Kelvin",
            "Fahrenheit to Celsius",
            "Fahrenheit to Kelvin",
            "Kelvin to Celsius",
            "Kelvin to Fahrenheit"
        ]
    elif selected == "Time":
        conversion_options = [
            "Second to Minute",
            "Minute to Second",
            "Second to Hour",
            "Minute to Hour",
            "Hour to Minute",
            "Day to Hour",
            "Hour to Day"
        ]
    elif selected == "Speed":
        conversion_options = [
            "Mile per hour to kilometer per hour",
            "Kilometer per hour to Mile per hour",
            "Mile per hour to Meter per Second",
            "Meter per Second to Mile per hour",
            "Kilometer per hour to Meter per Second",
            "Meter per Second to Kilometer per hour"
        ]
    elif selected == "Energy":
        conversion_options = [
            "Joule to Kilojoule",
            "Kilojoule to Joule",
            "Joule to Kilocalorie",
            "Kilocalorie to Joule",
            "Kilojoule to Kilocalorie",
            "Kilocalorie to Kilojoule"
        ]
    elif selected == "Pressure":
        conversion_options = [
            "Bar to Pascal",
            "Bar to Standard atmosphere",
            "Pascal to Bar",
            "Pascal to Standard atmosphere",
            "Standard atmosphere to Pascal",
            "Standard atmosphere to Bar"
        ]
    elif selected == "Area":
        conversion_options = [
            "Square Feet to Square Meter",
            "Square Feet to Acres",
            "Square Feet to Hectres"
        ]
        

    else:
        conversion_options = []

    conversion_menu['values'] = conversion_options
    conversion_var.set("")


unit_menu.bind("<<ComboboxSelected>>", update_conversion_options)


conversion_label = tk.Label(window, text="Select Conversion:")
conversion_label.pack()


conversion_menu = ttk.Combobox(window, textvariable=conversion_var)
conversion_menu.pack()


def convert_and_display():
    result = perform_conversion()
    if result is not None:
        result_label.config(text=f"Result: {result}")
    else:
        result_label.config(text="Invalid conversion")
        
result_label = tk.Label(window, text="")
result_label.pack()



convert_button = tk.Button(window, text="Convert", command=convert_and_display)
convert_button.pack()

window.mainloop()
import tkinter as tk
from tkinter import messagebox

root = tk.Tk() #Creates the main application window. Every Tkinter app starts with a root window.
root.title("Impulse Purchase Checker") #This sets the title shown at the top of the window.
root.geometry("700x650") #This sets the size of the window to 620 pixels wide and 560 pixels tall.
root.configure(bg="#f7f4ef") #This changes the background color of the window to a light cream color using a hex color code.

history = [] #This creates an empty list called history that stores saved purchase results.
remaining_budget = 0.0

title_label = tk.Label(root, text="Impulse Purchase Checker", font=("Arial", 18, "bold"), fg="#34e5eb", bg="#f7f4ef")
title_label.pack(pady=10)
#This creates a label widget for the title of the app. root means it is placed on the main window.
# text is what the label says, font changes the font style and size. fg sets the text color
#title_label.pack places the title label in the window using .pack().
# .pack() automatically places the widget in the next available spot
#pady=10 adds 10 pixels of vertical space above and below it

instruction_label = tk.Label(
    root,
    text="Enter the item details below to see whether this purchase seems thoughtful or impulsive.",
    font=("Arial", 10),
    fg="#34e5eb",
    bg="#f7f4ef",
    wraplength=600
) #This creates another label with instructions for the user.
#wraplength=560 means if the sentence is too long, it wraps onto the next line after about 560 pixels

instruction_label.pack(pady=5) #This places the instruction label below the title with 5 pixels of vertical padding.

budget_frame = tk.Frame(root, bg="#f7f4ef")
budget_frame.pack(pady=10)

# Create a label widget for the starting budget input
starting_budget_label = tk.Label(
    budget_frame, #frame where the label will be placed
    text="Monthly Starting Budget ($):", #Text displayed on the label
    bg="#f7f4ef", # Background color of the label
    fg="#34e5eb", # # Text (foreground) color
    font=("Arial", 11), #Font style and size
)
# Position the label in the grid layout
starting_budget_label.grid(row=0, column=0, sticky="e", padx=10, pady=6)
# Place in row 0, column 0 of the grid, sticky="e",       # Align text to the right (east)
#padx=10, pady=6   # Add horizontal and vertical padding

#Create an entry widget where the user types their budget
starting_budget_entry = tk.Entry(budget_frame, width=25) # Width of the input box
starting_budget_entry.grid(row=0, column=1, padx=10, pady=6)
# Place in row 0, column 1, Add spacing around it


# Function that runs when the user clicks "Set Budget"
def set_budget():
    global remaining_budget #Declare a global variable to store the budget
    try:
        #Get the value from the entry box and convert it to a float
        remaining_budget = float(starting_budget_entry.get())
        if remaining_budget < 0: ## Check if the value is negative
            messagebox.showerror("Input Error", "Starting budget cannot be negative.")
            return #Stop the function early
        #Update the label to display the new budget (formatted to 2 decimal places)
        budget_display_label.config(text=f"Remaining Monthly Budget: ${remaining_budget:.2f}")
        messagebox.showinfo("Budget Set", "Your monthly starting budget has been set.")
        #Show confirmation popup
    except ValueError: # If the user enters something that is not a number
        messagebox.showerror("Input Error", "Please enter a valid number for the starting budget.")

#Create a button that triggers the set_budget function
set_budget_button = tk.Button(
    budget_frame, #Parent Container
    text="Set Budget", #Button text
    command=set_budget,  #Function to run when clicked
    width=15, #Button width
    bg="#cdeac0" #Background color
)
#Position the button in the grid (next to entry box)
set_budget_button.grid(row=0, column=2, padx=10, pady=6)
#Place in row 0, column 2. padx and pady = add spacing

#Create a label to display the remaining budget
budget_display_label = tk.Label(
    root,  #Placed in the main window (not the frame)
    text="Remaining Monthly Budget: $0.00", #Default starting text
    font=("Arial", 12, "bold"), #Font styling
    fg="#34e5eb", #Text color
    bg="#f7f4ef" #Background color
)
budget_display_label.pack(pady=5) #Pack the label into the window (different layout system than grid)
#pady adds vertical spacing

form_frame = tk.Frame(root, bg="#f7f4ef") #This creates a frame inside the root window. A frame is like a container used to organize other widgets.
form_frame.pack(pady=10) #This places the frame in the main window with vertical padding.

item_label = tk.Label(form_frame, text="Item Name:", bg="#f7f4ef", fg="#34e5eb", font=("Arial", 11)) #This creates the label for the item name field.
item_label.grid(row=0, column=0, sticky="e", padx=10, pady=6) #This places the label inside the frame using .grid().
#row=0, column=0 means first row, first column,
# sticky="e" aligns the label to the east/right side of the grid cell. padx=10 adds horizontal space. pady=6 adds vertical space
item_entry = tk.Entry(form_frame, width=30) # This creates a text entry box where the user types the item name.
item_entry.grid(row=0, column=1, padx=10, pady=6) #This places the entry box in row 0, column 1, next to the label.

price_label = tk.Label(form_frame, text="Price ($):", bg="#f7f4ef", fg="#34e5eb", font=("Arial", 11)) #This creates the label for the price field.
price_label.grid(row=1, column=0, sticky="e", padx=10, pady=6) #This places the price label in the second row, first column.
price_entry = tk.Entry(form_frame, width=30) #This creates the input box for the price.
price_entry.grid(row=1, column=1, padx=10, pady=6) #This creates the input box for the price.

need_label = tk.Label(form_frame, text="Need Level (1-10):", bg="#f7f4ef", fg="#34e5eb", font=("Arial", 11)) #This creates the label for the need level.
need_label.grid(row=2, column=0, sticky="e", padx=10, pady=6) #This places that label in row 2, column 0.
need_entry = tk.Entry(form_frame, width=30) #This creates the entry box for the need level.
need_entry.grid(row=2, column=1, padx=10, pady=6) #This places the need level box beside the label.

wait_label = tk.Label(form_frame, text="Days Waited:", bg="#f7f4ef", fg="#34e5eb", font=("Arial", 11))
#This creates the label for the number of days waited.
wait_label.grid(row=3, column=0, sticky="e", padx=10, pady=6) #This places it in row 3.
wait_entry = tk.Entry(form_frame, width=30) #This creates the entry box for days waited.
wait_entry.grid(row=3, column=1, padx=10, pady=6) #This places it next to the label.

budget_label = tk.Label(form_frame, text="Budget Left This Month ($):", bg="#f7f4ef", fg="#34e5eb", font=("Arial", 11))
#This creates the label for the remaining budget.
budget_label.grid(row=4, column=0, sticky="e", padx=10, pady=6) #This places the budget label in row 4.
budget_entry = tk.Entry(form_frame, width=30) #This creates the entry box for the budget amount.
budget_entry.grid(row=4, column=1, padx=10, pady=6) #This creates the entry box for the budget amount.

result_label = tk.Label( #creates the large label where the result message appears.
    root,
    text="Result will appear here.", #gives the starting message
    font=("Arial", 12, "bold"),
    fg="#34e5eb",
    bg="#fff8dc", #changes the background color
    width=62, #control size
    height=3, #control size
    wraplength=580, #wraps long result text
    relief="ridge" #gives the box a raised border style
)
result_label.pack(pady=15) #creates the large label where the result message appears.

score_label = tk.Label(root, text="Impulse Score: N/A", font=("Arial", 11), bg="#f7f4ef", fg="#34e5eb")
score_label.pack(pady=3) #This creates a label that shows the calculated impulse score and places the score label below the result box.



history_title = tk.Label(root, text="Saved Purchase Checks", font=("Arial", 12, "bold"), bg="#f7f4ef", fg="#34e5eb")
#This creates the heading for the saved history section.
history_title.pack(pady=(15, 5)) #This places the heading with padding. 15 pixels on top and 5 on bottom.

history_listbox = tk.Listbox(root, width=85, height=8) #This creates a listbox, which displays saved purchase check results in a list format.
history_listbox.pack(pady=5) #This places the listbox in the window.

def evaluate_purchase():
    global remaining_budget

    item = item_entry.get().strip()     #runs only when called. This gets the text the user typed in the item box.
#.get() reads the input
#.strip() removes extra spaces at the beginning or end
    try: #This tries to convert the user input into numbers.
        price = float(price_entry.get()) #float used for decimal numbers like price or budget
        need = int(need_entry.get()) # int used for whole numbers like need level or days waited
        waited = int(wait_entry.get())
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for price, need level, and days waited.")
        return #If the user types something invalid, like letters instead of numbers, the program shows an error message and stops the function using return.

    if remaining_budget <= 0:
        messagebox.showerror("Budget Error", "Please set your monthly starting budget first.")

    if item == "":
        messagebox.showerror("Input Error", "Please enter an item name.")
        return #This checks whether the item name box is empty. If it is, an error message appears.

    if need < 1 or need > 10:
        messagebox.showerror("Input Error", "Need level must be between 1 and 10.")
        return #This checks whether the need level is within the valid range of 1 to 10.

    if waited < 0:
        messagebox.showerror("Input Error", "Days waited cannot be negative.")

    score = 0 #This starts the impulse score at 0.

    if price > remaining_budget * 0.5:
        score += 3 #If the item costs more than half of the user’s remaining budget, 3 points are added to the score.
    if price > 100:
        score += 2 #If the item costs more than $100, 2 more points are added.
    if need <= 4:
        score += 3
    elif need <= 7:
        score += 1 #If the need is low, the app adds more points because the purchase may be more impulsive.
#If the need is moderate, it adds only 1 point.
    if waited < 2:
        score += 3
    elif waited < 7:
        score += 1
#If the user waited less than 2 days, it adds 3 points. If they waited less than 7 days, it adds 1 point.

    if score >= 7: #This decides which message to show based on the score.
        result = f"{item}: This looks like an IMPULSE purchase. Wait a little longer before buying."
    elif score >= 4:
        result = f"{item}: This purchase is questionable. Think it through and compare alternatives."
    else:
        result = f"{item}: This seems like a more thoughtful purchase."

    remaining_budget -= price
    budget_display_label.config(text=f"Remaining Monthly Budget: ${remaining_budget:.2f}")

    if remaining_budget < 0:
        result += " Warning: You have gone over your monthly budget."

    result_label.config(text=result) #This updates the result label to display the purchase message.
    # .config() changes a widget’s settings after it has already been created
    score_label.config(text=f"Impulse Score: {score}/11") #This updates the score label to show the final score out of 11.


def save_result():
    current_result = result_label.cget("text") #gets the current text from the result label.
    if current_result == "Result will appear here.":
        messagebox.showinfo("Nothing to Save", "Evaluate a purchase before saving it.")
        return #This checks if the user has not run the evaluation yet. If no result exists, it shows a pop-up message.

    saved_text = f"{current_result} | Budget Left: {budget_display_label.cget('text').split('$')[-1]}"
    history.append(saved_text)
    history_listbox.insert(tk.END, saved_text)

def clear_fields():
    item_entry.delete(0, tk.END)
    price_entry.delete(0, tk.END)
    need_entry.delete(0, tk.END)
    wait_entry.delete(0, tk.END)
    result_label.config(text="Result will appear here.") #This resets the result label to its original message.
    score_label.config(text="Impulse Score: N/A") #This resets the score label.

def reset_budget_and_history():
    global remaining_budget
    remaining_budget = 0.0
    starting_budget_entry.delete(0, tk.END)
    budget_display_label.config(text="Remaining Monthly Budget: $0.00")
    history.clear()
    history_listbox.delete(0, tk.END)
    clear_fields()

button_frame = tk.Frame(root, bg="#f7f4ef")  #This creates another frame to hold the buttons.
button_frame.pack(pady=12) #This places the button frame in the window.

check_button = tk.Button(button_frame, text="Check Purchase", command=evaluate_purchase, width=18, bg="#d8bfd8")
#This creates a button labeled “Check Purchase.”, command=evaluate_purchase means clicking the button runs that function
check_button.grid(row=0, column=0, padx=8) #This places the button in the first row and first column of the button frame.

save_button = tk.Button(button_frame, text="Save Result", command=save_result, width=18, bg="#b0e0e6")
#This creates a button that runs the save_result() function when clicked.
save_button.grid(row=0, column=1, padx=8) #This places the save button in the next column.

clear_button = tk.Button(button_frame, text="Clear", command=clear_fields, width=18, bg="#f4a6a6")
#This places the save button in the next column.
clear_button.grid(row=0, column=2, padx=8) #This places the clear button in the third column.

reset_button = tk.Button(
    button_frame,
    text="Reset Budget/History",
    command=reset_budget_and_history,
    width=18,
    bg="#f7d794"
)
reset_button.grid(row=0, column=3, padx=8)

root.mainloop()
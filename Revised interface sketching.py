import tkinter as tk

def submit_button_click():
    input_text=[]
    for entries in rows.values():
        print(entries)
        input_text.append(entries.get())
        print(input_text)
    outcomes=", ".join(input_text)
    label.config(text=f"You entered: {outcomes}")
    
# Create the main window
root = tk.Tk()
root.title("Simple Tkinter Workspace")

# Create and place widgets
label = tk.Label(root, text="Enter something:")
label.grid(row=0)

entrycount=[0]

rows={}
for box in entrycount:
    name=tk.Entry(root)
    rows[box]=name
    name.grid(row=1)

###must make it so that it doesn't eat up the pre-existing rows, just adds a new
#boxcount=4

def add_row():
    entrycount.append(max(entrycount)+1)
    for box in entrycount[1:]:
        if box not in rows:
            loc=box+2
            name=tk.Entry(root)
            rows[box]=name
            name.grid(row=loc)

    return entrycount

submit_button = tk.Button(root, text="Submit", command=submit_button_click)
add_more = tk.Button(root, text="add another row", command=add_row)
submit_button.grid(row=19)
add_more.grid(row=20)
# Start the main loop
root.mainloop()
import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        todo.append(task)
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You need to enter a task.")

def view_tasks():
    listbox.delete(0, tk.END)
    for index, item in enumerate(todo):
        listbox.insert(tk.END, f"{index}: {item}")

def remove_task():
    try:
        index = int(entry.get())
        if 0 <= index < len(todo):
            todo.pop(index)
            view_tasks()
            entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Invalid index.")
    except ValueError:
        messagebox.showwarning("Warning", "Please enter a valid number.")

def echo_message():
    message = entry.get()
    if message:
        messagebox.showinfo("Echo", message)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "No message to echo.")

def stop_app():
    root.quit()

# Initialize the main window
root = tk.Tk()
root.title("Dausen's To-Do List")

todo = []

# Create the widgets
frame = tk.Frame(root)
frame.pack(pady=10)

entry = tk.Entry(frame, width=30)
entry.pack(side=tk.LEFT, padx=5)

add_button = tk.Button(frame, text="Add Task", command=add_task)
add_button.pack(side=tk.LEFT)

remove_button = tk.Button(frame, text="Remove Task", command=remove_task)
remove_button.pack(side=tk.LEFT)

view_button = tk.Button(root, text="View Tasks", command=view_tasks)
view_button.pack(pady=5)

echo_button = tk.Button(root, text="Echo", command=echo_message)
echo_button.pack(pady=5)

stop_button = tk.Button(root, text="Stop", command=stop_app)
stop_button.pack(pady=5)

listbox = tk.Listbox(root, width=50)
listbox.pack(pady=10)

# Start the GUI loop
root.mainloop()

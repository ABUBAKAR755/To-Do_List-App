import json
import tkinter as tk
from tkinter import messagebox

# File to store tasks
TASKS_FILE = "tasks.json"

# Load tasks from file
def load_tasks():
    try:
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# Add Task
def add_task():
    task_text = task_entry.get()
    if task_text:
        tasks.append({"task": task_text, "completed": False})
        save_tasks(tasks)
        update_listbox()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

# Mark as Completed
def complete_task():
    try:
        selected_task = task_listbox.curselection()[0]
        tasks[selected_task]["completed"] = True
        save_tasks(tasks)
        update_listbox()
    except IndexError:
        messagebox.showwarning("Warning", "Select a task to mark as completed!")

# Delete Task
def delete_task():
    try:
        selected_task = task_listbox.curselection()[0]
        del tasks[selected_task]
        save_tasks(tasks)
        update_listbox()
    except IndexError:
        messagebox.showwarning("Warning", "Select a task to delete!")

# Update the Listbox Display
def update_listbox():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        status = "✔️" if task["completed"] else "❌"
        task_listbox.insert(tk.END, f"{task['task']} {status}")

# Initialize App Window
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x400")

# Load tasks
tasks = load_tasks()

# Task Entry
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)

# Buttons
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

complete_button = tk.Button(root, text="Complete Task", command=complete_task)
complete_button.pack()

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack()

# Listbox to Show Tasks
task_listbox = tk.Listbox(root, width=50, height=10)
task_listbox.pack(pady=10)

# Update the Listbox Initially
update_listbox()

# Run the Tkinter Event Loop
root.mainloop()

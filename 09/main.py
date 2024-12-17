import streamlit as st
from datetime import datetime

# In-memory storage for tasks
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# Task status options
status_options = ["New", "In Progress", "Completed"]


# Function to add a new task
def add_task(name: str, description: str, due_date: datetime):
    task = {
        "name": name,
        "description": description,
        "due_date": due_date,
        "status": "New",
    }
    st.session_state.tasks.append(task)


# Function to update the status of a task
def update_task_status(index: int, new_status: str):
    if 0 <= index < len(st.session_state.tasks):
        st.session_state.tasks[index]["status"] = new_status


# Streamlit UI
st.title("To-Do App")

# Task input form
with st.form("Add Task"):
    name = st.text_input("Task Name")
    description = st.text_area("Description")
    due_date = st.date_input("Due Date", min_value=datetime.today().date())
    if st.form_submit_button("Add Task"):
        add_task(name, description, due_date)
        st.success(f"Added task: {name}")

# Display tasks with options to update status
if st.session_state.tasks:
    st.header("Tasks")
    for index, task in enumerate(st.session_state.tasks):
        with st.container(border=True):
            st.subheader(f"{task['name']} (Status: {task['status']})")
            st.write(f"**Description:** {task['description']}")
            st.write(f"**Due Date:** {task['due_date']}")

            # Task status update options
            new_status = st.selectbox(
                f"Update Status for '{task['name']}'",
                status_options,
                index=status_options.index(task["status"]),
                key=f"status_{index}",
            )
            if new_status != task["status"]:
                update_task_status(index, new_status)
                st.success(f"Updated status for '{task['name']}'")

else:
    st.info("No tasks added yet.")

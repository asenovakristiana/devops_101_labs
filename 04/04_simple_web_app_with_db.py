import streamlit as st
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# Database setup
engine = create_engine("sqlite:///tasks.db")
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

# Define the Task model
class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String)
    due_date = Column(Date, nullable=False)
    status = Column(String, default="New")

    def __repr__(self):
        return f"<Task(name={self.name}, status={self.status})>"

# Create the tasks table if it doesn't exist
Base.metadata.create_all(engine)

# Task status options
status_options = ["New", "In Progress", "Completed"]

# Function to add a new task
def add_task(name: str, description: str, due_date: datetime):
    new_task = Task(name=name, description=description, due_date=due_date, status="New")
    session.add(new_task)
    session.commit()

# Function to update the status of a task
def update_task_status(task_id: int, new_status: str):
    task = session.query(Task).filter(Task.id == task_id).first()
    if task:
        task.status = new_status
        session.commit()

# Function to fetch all tasks
def fetch_tasks():
    return session.query(Task).all()

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
tasks = fetch_tasks()
if tasks:
    st.header("Tasks")
    for task in tasks:
        with st.container():
            st.subheader(f"{task.name} (Status: {task.status})")
            st.write(f"**Description:** {task.description}")
            st.write(f"**Due Date:** {task.due_date}")
            
            # Task status update options
            new_status = st.selectbox(
                f"Update Status for '{task.name}'", 
                status_options, 
                index=status_options.index(task.status), 
                key=f"status_{task.id}"
            )
            if new_status != task.status:
                update_task_status(task.id, new_status)
                st.success(f"Updated status for '{task.name}' to {new_status}")
else:
    st.info("No tasks added yet.")
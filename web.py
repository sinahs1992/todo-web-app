import streamlit as st
from functions import get_todos, write_todos

todos = get_todos()


def add_todo():
    local_todo = st.session_state['new_todo'] + '\n'
    todos.append(local_todo)
    write_todos(todos)


st.title("My To-Do App")
st.subheader("This is my todo app")
st.write('this app is to increase your productivity .')

for index, todo in enumerate(todos):
    check_box = st.checkbox(todo, key=todo)
    if check_box:
        todos.pop(index)
        write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Enter a todo :", placeholder="Add new todo ",
              on_change=add_todo, key='new_todo')

st.session_state
import streamlit as st
import pandas as pd

# Database Management
import sqlite3
connect = sqlite3.connect('data/Chinook_Sqlite.sqlite')
c = connect.cursor()

# execute raw SQL
def sql_executer(raw_code):
    c.execute(raw_code) 
    data = c.fetchall()
    return data

def main(): 
    st.title('SQL Playground')

    menu = ['Home', 'About', 'Scheme']
    choice = st.sidebar.selectbox('Menu', menu)

    if choice == "Home":
        st.subheader('Home')
        
        with st.form(key='query_form'):
            exclude_commands = ["create", "drop", "insert", "update", "delete", "alter", "truncate", "grant", "revoke", "commit", "rollback", "savepoint", "merge", "rename", "replace", "set", "show", "use", "analyze", "attach", "backup", "checkpoint", "copy", "detach", "explain", "pragma", "reindex", "restore", "vacuum", "load", "unload", "lock", "unlock", "kill", "shutdown", "prepare", "execute", "deallocate", "begin", "end", "declare", "call", "do", "handler", "load", "save", "source", "quit", "exit", "connect", "disconnect", "quit", "exit", "go"]

            raw_code = st.text_area('Enter your SQL query here:')
            # if any(cmds in raw_code for cmds in exclude_commands):
            #     st.warning('You are not allowed to execute this command', icon="⚠️")
            # else:
            submit_code = st.form_submit_button(label='Execute Query')

   
            if submit_code:
                st.info("Query Submitted")
                st.code(raw_code)

                # Prettify the results
                with st.expander("Pretty Table"):
                    query_results = sql_executer(raw_code)
                    query_df = pd.DataFrame(query_results)
                    st.dataframe(query_df)
 
                # Results as JSON
                with st.expander("Results"):
                    st.write(query_results)


    elif choice == "About":
        st.subheader('About')
        st.text('This is a SQL Playground')
        st.text('Built with Streamlit and SQLite3, based on a tutorial from @Jcharis on Github')
        st.text('Author: @shanirivers')
    else: 
        st.subheader('Scheme')
        st.text('The scheme for the Chinook database can be found on Github: https://github.com/lerocha/chinook-database/tree/master')
        query = "SELECT * FROM sqlite_master WHERE type='table';"
        tables = sql_executer(query)
        st.write(tables)
        
        st.write('The Chinook database is a sample database available for SQL Server, Oracle, MySQL, etc. It can be used to learn and practice SQL queries.')

if __name__ == '__main__':
	main()
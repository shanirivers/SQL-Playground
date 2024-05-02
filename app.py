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
        
        col1, col2 = st.columns(2)

        with col1:
            with st.form(key='query_form'):
                raw_code = st.text_area('Enter your SQL query here:')
                submit_code = st.form_submit_button(label='Execute Query')

        with col2:
            if submit_code:
                st.info("Query Submitted")
                st.code(raw_code)

                # Prettify the results

                with st.expander("Pretty Table"):
                    query_df = pd.DataFrame(query_results)
                    st.dataframe(query_df)

                # Results as JSON
                query_results = sql_executer(raw_code)
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
        # query = "SELECT * FROM sqlite_master WHERE type='table';"
        # tables = sql_executer(query)
        # st.write(tables)

if __name__ == '__main__':
	main()
import io

import ast
import duckdb

import streamlit as st

import pandas as pd

con = duckdb.connect(database="data/exercises_sql_tables.duckdb", read_only=False)

#   ANSWER_STR = """
#   SELECT * FROM beverages
#   CROSS JOIN food_items
#   """

#   solution_df = duckdb.sql(ANSWER_STR).df()

with st.sidebar:
    theme = st.selectbox(
        "What would you like to review?",
        ("cross_joins", "GroupBy", "Window Functions"),
        index=None,
        placeholder="Select a theme",
    )
    st.write("You selected", theme)

    exercise = con.execute(f"SELECT * FROM memory_state WHERE theme = '{theme}'").df()
    st.write(exercise)


st.header("enter your code:")
query = st.text_area(label="Your SQL code here", key="user_input")
if query:
    result = con.execute(query).df()
    st.dataframe(result)
#
tab2, tab3 = st.tabs(["Tables", "solution_df"])
#
with tab2:
    exercise_tables = ast.literal_eval(exercise.loc[0, "tables"])
    for table in exercise_tables:
        st.write(f"table: {table}")
        df_table = con.execute(f"SELECT * FROM {table}").df()
        st.dataframe(df_table)
#     st.write("table: beverages")
#     st.dataframe(beverages)
#     st.write("table: food_items")
#     st.dataframe(food_items)
#     st.write("expected")
#     st.dataframe(solution_df)
#
with tab3:
    exercise_name = exercise.loc[0, "answer"]
    with open(f"answers/{exercise_name}.sql", "r") as f:
        answer = f.read()
    st.write(answer)

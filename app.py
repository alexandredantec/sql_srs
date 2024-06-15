
import duckdb
import streamlit as st

con = duckdb.connect(database="data/exercises_sql_tables.duckdb", read_only=False)

ANSWER_STR = """
SELECT * FROM beverages
CROSS JOIN food_items
"""

solution_df = duckdb.sql(ANSWER_STR).df()

with st.sidebar:
    theme = st.selectbox(
        "What would you like to review?",
        ("cross_joins", "GroupBy", "Window Functions"),
        index=None,
        placeholder="Select a theme"
    )
    st.write("You selected", theme)

    exercise = con.execute(f"SELECT * FROM memory_state WHERE theme = '{theme}")
    st.write(exercise)


st.header("enter your code:")
query = st.text_area(label="Your SQL code here", key="user_input")
# if query:
#     result = duckdb.sql(query).df()
#     st.dataframe(result)
#
# tab2, tab3 = st.tabs(["Tables", "solution_df"])
#
# with tab2:
#     st.write("table: beverages")
#     st.dataframe(beverages)
#     st.write("table: food_items")
#     st.dataframe(food_items)
#     st.write("expected")
#     st.dataframe(solution_df)
#
# with tab3:
#     st.write(ANSWER_STR)

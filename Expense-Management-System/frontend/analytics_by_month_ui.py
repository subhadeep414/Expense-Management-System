import streamlit as st
import pandas as pd
import requests

API_URL = "http://localhost:8000"


def analytics_by_month_tab():
    st.title("Expense Breakdown by months")
    response=requests.get(f"{API_URL}/analytics/months")
    if response.status_code==200:
        response=response.json()
    else:
        st.error("Error occurred in retrieving data from database")


    expenses={
        'Month':[row["month_name"] for row in response],
        'Total':[row["total_spending"] for row in response],
        'Month_Number':[row["month_number"] for row in response]
    }

    df=pd.DataFrame(expenses)
    month_order = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    df["Month"] = pd.Categorical(df["Month"], categories=month_order, ordered=True)
    st.bar_chart(df.set_index("Month")["Total"], width=0, height=0, use_container_width=True)
    df = df.set_index("Month_Number")
    df.index.name = None
    st.table(df)


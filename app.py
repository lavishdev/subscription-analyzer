import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
st.set_page_config(page_title="My Subscription Analyzer", layout="wide", page_icon="🚀")
st.title("My Personal Subscription Dashboard")
st.markdown("---")
df = pd.read_csv('data/my_subscriptions.csv')
df.index = df.index + 1
st.subheader('Raw Data')
st.write(df)
total_monthly = df['monthly_cost'].sum()
avg_monthly = df['monthly_cost'].mean()
spending_by_category = df.groupby('category')['monthly_cost'].sum()
col1, col2 = st.columns(2)
col1.metric("Total Monthly Cost", f"${total_monthly:.2f}")
col2.metric("Avg. Subscription Cost", f"${avg_monthly:.2f}")
st.subheader("Spending Breakdown")
chart1, chart2 = st.columns(2)
with chart1:
    st.write("**By Category (Pie)**")
    fig1, ax1 = plt.subplots()
    ax1.pie(spending_by_category, labels=spending_by_category.index, autopct='%1.1f%%')
    st.pyplot(fig1)
with chart2:
    st.write("**By Category (Bar)**")
    fig2, ax2 = plt.subplots()
    ax2.bar(spending_by_category.index, spending_by_category.values)
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(fig2)

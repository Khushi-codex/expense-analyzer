import streamlit as st
import pandas as pd
from analyzer import category_summary, monthly_summary, total_spending
from analyzer import generate_insights

st.set_page_config(page_title="Expense Analyzer", page_icon="💰")

st.title("Personal Expense Analyzer")
st.markdown("---")

uploaded_file = st.file_uploader("Upload your expenses CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    df['date'] = pd.to_datetime(df['date'])

    st.subheader("Raw Data")
    st.dataframe(df)
    st.subheader("Filter by Category")
    categories = df['category'].unique().tolist()
    selected = st.multiselect("Select Categories", categories, default=categories)
    filtered_df = df[df['category'].isin(selected)]
    st.dataframe(filtered_df)

    st.subheader("Filter by Month")
    df['month'] = df['date'].dt.strftime('%Y-%m')
    months = df['month'].unique().tolist()
    selected_month = st.selectbox("Select Month", ["All"] + months)
    if selected_month != "All":
        filtered_df = filtered_df[filtered_df['month'] == selected_month]
    st.dataframe(filtered_df)

    st.subheader("Summary")
    total = df['amount'].sum()
    top_cat = df.groupby('category')['amount'].sum().idxmax()

    col1, col2, col3 = st.columns(3)
    low_cat = df.groupby('category')['amount'].sum().idxmin()

    col1.metric("Total Spending", f"₹{total}")
    col2.metric("Highest Category", top_cat)
    col3.metric("Lowest Category", low_cat)

    st.markdown("---")
    st.subheader("Spending by Category")
    cat_data = df.groupby('category')['amount'].sum()
    st.bar_chart(cat_data)

    st.markdown("---")
    st.subheader("Monthly Spending Trend")
    df['month'] = df['date'].dt.strftime('%Y-%m')
    mon_data = df.groupby('month')['amount'].sum()
    st.line_chart(mon_data)

    st.markdown("---")
    st.subheader("Category Distribution")
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()
    cat_data.plot(kind='pie', ax=ax, autopct='%1.1f%%')
    ax.set_ylabel('')
    st.pyplot(fig)

    st.markdown("---")
    st.subheader("🧠 Smart Insights")
    
    insights = generate_insights(filtered_df)
    for insight in insights:
        st.write("•", insight)

else:
    st.info("Please upload a CSV file to begin.")
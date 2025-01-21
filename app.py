import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st


def plot_drawdown_chart(filtered_df, ticker):
    """Plots the Drawdown Chart"""
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(filtered_df['date'], filtered_df['drawdown_1'], label='Drawdown', color='red', linewidth=2)
    ax.fill_between(filtered_df['date'], filtered_df['drawdown_1'], color='red', alpha=0.5)
    ax.set_title(f"Drawdown Chart for {ticker}", fontsize=16)
    ax.set_xlabel('Date', fontsize=12)
    ax.set_ylabel('Drawdown (%)', fontsize=12)
    ax.legend(fontsize=10)
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    plt.xticks(rotation=45, fontsize=10)
    plt.yticks(fontsize=10)
    st.pyplot(fig)

def plot_log_return_chart(filtered_df, ticker):
    """Plots the Logarithmic Relative Return Chart"""
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(filtered_df['date'], filtered_df['log_rel_return'], label='Logarithmic Relative Return', color='blue', linewidth=2)
    ax.set_title(f"Logarithmic Relative Return for {ticker}", fontsize=16)
    ax.set_xlabel('Date', fontsize=12)
    ax.set_ylabel('Logarithmic Relative Return', fontsize=12)
    ax.legend(fontsize=10)
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    plt.xticks(rotation=45, fontsize=10)
    plt.yticks(fontsize=10)
    st.pyplot(fig)
def plot_return_chart(filtered_df, ticker):
    """Plots the Return Chart"""
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(filtered_df['date'], filtered_df['Return'], label='Return', color='green', linewidth=2)
    ax.set_title(f"Return Chart for {ticker}", fontsize=16)
    ax.set_xlabel('Date', fontsize=12)
    ax.set_ylabel('Return (%)', fontsize=12)
    ax.legend(fontsize=10)
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    plt.xticks(rotation=45, fontsize=10)
    plt.yticks(fontsize=10)
    st.pyplot(fig)
# Streamlit App
st.title("Stock Performance Charts")

# User Inputs
start_date = st.date_input("Start Date")
end_date = st.date_input("End Date")
ticker = st.text_input("Enter Ticker Symbol").upper()

# Directly load the CSV file from the specified path
file_path = "Hackathon.csv"

try:
    merged_df = pd.read_csv(file_path, parse_dates=['date'])
except FileNotFoundError:
    st.error(f"File not found at {file_path}. Please ensure the path is correct.")
    st.stop()

# Validate input
if ticker and start_date and end_date:
    filtered_df = merged_df[(merged_df['Ticker'] == ticker) &
                            (merged_df['date'] >= pd.to_datetime(start_date)) &
                            (merged_df['date'] <= pd.to_datetime(end_date))]

    if not filtered_df.empty:
        # Plot Drawdown Chart
        plot_drawdown_chart(filtered_df, ticker)

        # Plot Logarithmic Relative Return Chart
        plot_log_return_chart(filtered_df, ticker)
        plot_return_chart(filtered_df, ticker)
    else:
        st.warning("No data available for the specified inputs.")
else:
    st.warning("Please enter all inputs correctly.")

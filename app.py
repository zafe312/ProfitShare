import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Set page title and layout
st.set_page_config(page_title="Investment Profit Sharing", layout="wide")
st.image("logo.png", width=100)  # Ensure 'logo.png' exists in the directory
st.title("Investment Profit Sharing Tool")

# Default investors data
default_data = pd.DataFrame({
    "Name": [""],
    "Fixed Cost (FC)": [0],
    "Working Capital (WC)": [0],
    "Salary": [0],
    "Bonus (%)": [0],
})

# Initialize session state variables
if "investors" not in st.session_state:
    st.session_state.investors = default_data.copy()

if "temp_investors" not in st.session_state:
    st.session_state.temp_investors = st.session_state.investors.copy()

if "show_charts" not in st.session_state:
    st.session_state.show_charts = False

if "profit_shares" not in st.session_state:
    st.session_state.profit_shares = None

if "net_profit" not in st.session_state:
    st.session_state.net_profit = 80000  # Default net profit

# Editable investor data table (Updates only when button is clicked)
st.subheader("Investor Data")
temp_df = st.data_editor(
    st.session_state.temp_investors,  # Temporary DataFrame
    num_rows="dynamic",
    use_container_width=True,
    key="investors_table"
)

# "Update Table" button
if st.button("Update Table"):
    st.session_state.investors = temp_df.copy()
    st.session_state.temp_investors = temp_df.copy()
    st.rerun()  # Force rerun to update calculations

# Compute investment totals
total_FC = st.session_state.investors["Fixed Cost (FC)"].sum()
total_WC = st.session_state.investors["Working Capital (WC)"].sum()
total_investment = total_FC + total_WC

# Display investment summary
st.subheader("Investment Summary")
st.write(f"**Total Fixed Cost (FC):** {total_FC}")
st.write(f"**Total Working Capital (WC):** {total_WC}")
st.write(f"**Total Investment:** {total_investment}")

# Net profit input with state persistence
st.session_state.net_profit = st.number_input(
    "Enter Net Profit",
    min_value=0,
    value=st.session_state.net_profit,
    key="net_profit_input"
)

# Function to plot pie charts
def plot_pie_chart(labels, sizes, title):
    fig, ax = plt.subplots()
    ax.pie(
        sizes, labels=labels, autopct=lambda p: f'{p:.1f}%' if p > 0 else '',
        startangle=140, wedgeprops={'edgecolor': 'black'}
    )
    ax.set_title(title)
    st.pyplot(fig)

# Show Contribution button
if st.button("Show Contribution"):
    st.session_state.show_charts = True

# Display pie charts if enabled
if st.session_state.show_charts:
    investors = st.session_state.investors
    names = investors["Name"]
    
    FC_shares = investors["Fixed Cost (FC)"] / total_FC if total_FC else [0] * len(names)
    WC_shares = investors["Working Capital (WC)"] / total_WC if total_WC else [0] * len(names)
    total_shares = (investors["Fixed Cost (FC)"] + investors["Working Capital (WC)"]) / total_investment if total_investment else [0] * len(names)

    plot_pie_chart(names, FC_shares, "Fixed Cost Contribution")
    plot_pie_chart(names, WC_shares, "Working Capital Contribution")
    plot_pie_chart(names, total_shares, "Total Investment Contribution")

    if st.button("Hide Charts"):
        st.session_state.show_charts = False
        st.rerun()

# Function to calculate profit shares
def calculate_profit_shares():
    investors = st.session_state.investors.copy()

    # Calculate bonus and salaries
    investors["Total Earning"] = investors["Salary"] + (st.session_state.net_profit * investors["Bonus (%)"] / 100)
    total_bonus_paid = investors["Total Earning"].sum()
    remaining_profit = st.session_state.net_profit - total_bonus_paid

    # Share remaining profit based on total investment contribution
    if total_investment > 0:
        shares_total = (investors["Fixed Cost (FC)"] + investors["Working Capital (WC)"]) / total_investment
    else:
        shares_total = [0] * len(investors)

    investors["Total Earning"] += remaining_profit * shares_total
    st.session_state.profit_shares = investors[["Name", "Total Earning"]]

# Button to calculate profit shares
if st.button("Calculate Profit Shares"):
    calculate_profit_shares()

# Display profit shares if calculated
if st.session_state.profit_shares is not None:
    st.subheader("Profit Distribution")
    st.dataframe(st.session_state.profit_shares, use_container_width=True)

# Reset button to clear session state and rerun
if st.button("Reset"):
    st.session_state.clear()
    st.rerun()

# Investment Profit Sharing Tool

A **Streamlit-based** web application for calculating **investment profit sharing** among investors based on **fixed costs, working capital, salary, and bonuses**. The tool provides **dynamic data input, visual analysis via pie charts**, and a **profit distribution breakdown**.

## 🚀 Features

- **Editable Investor Table**: Modify investor details dynamically.
- **"Update Table" Button**: Ensures calculations update only when the user confirms changes.
- **Profit Sharing Calculation**: Computes final earnings for each investor.
- **Pie Charts**: Visualize contributions to fixed costs, working capital, and total investment.
- **Net Profit Input**: Users can specify total profit for distribution.
- **Reset Functionality**: Clears all inputs and recalculates.

---

## 📦 Installation

1. **Clone the repository** (or download the files manually):
   ```sh
   git clone https://github.com/your-repo/investment-profit-sharing.git
   cd investment-profit-sharing
   ```

2. **Create a virtual environment (recommended)**:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate  # On Windows
   ```

3. **Install dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

---

## ▶️ Running the App

After installing the dependencies, start the Streamlit app:

```sh
streamlit run app.py
```

---

## 📊 How to Use

1. **Edit the investor table**:
   - Enter **names**, **fixed costs**, **working capital**, **salary**, and **bonus percentages**.
   - **Do not press Enter after each edit**; click **"Update Table"** to apply changes.

2. **Click "Update Table"**:
   - Ensures calculations and visualizations update properly.

3. **Enter Net Profit**:
   - Input the total profit to be shared among investors.

4. **View Investment Summary**:
   - Displays **total fixed cost, working capital, and total investment**.

5. **Visualize Contributions**:
   - Click **"Show Contribution"** to generate **pie charts**.

6. **Calculate Profit Shares**:
   - Click **"Calculate Profit Shares"** to see how earnings are distributed.

7. **Reset**:
   - Click **"Reset"** to clear all inputs and restart.

---

## 🛠️ Requirements

- **Python 3.8+**
- **Streamlit**
- **Pandas**
- **Matplotlib**

---

## 📌 License

This project is open-source and available under the **MIT License**.

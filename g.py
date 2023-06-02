import os
import streamlit as st
import pandas as pd

# Create data directory if it doesn't exist
if not os.path.exists("data"):
    os.makedirs("data")

def data_entry():
    st.subheader("Data Entry")

    # Select date for data entry
    date = st.date_input("Select Date")

    # Create filename based on the selected date
    filename = f"data/{date}.csv"

    # Check if file already exists, create new file if not
    if not os.path.isfile(filename):
        with open(filename, "w") as f:
            f.write("Date,Salary,Blog Income,Other Income,Rent Expense,Grocery Expense,Car Expense,Other Expense,Comments\n")
            st.success(f"New file created: {filename}")

    # Take income details
    st.subheader("Income Details")
    salary = st.number_input("Salary (USD)", min_value=0.0, step=0.01)
    blog_income = st.number_input("Blog Income (USD)", min_value=0.0, step=0.01)
    other_income = st.number_input("Other Income (USD)", min_value=0.0, step=0.01)

    # Take expense details
    st.subheader("Expense Details")
    rent_expense = st.number_input("Rent Expense (USD)", min_value=0.0, step=0.01)
    grocery_expense = st.number_input("Grocery Expense (USD)", min_value=0.0, step=0.01)
    car_expense = st.number_input("Car Expense (USD)", min_value=0.0, step=0.01)
    other_expense = st.number_input("Other Expense (USD)", min_value=0.0, step=0.01)

    comments = st.text_area("Comments")

    # Append data to the file
    with open(filename, "a") as f:
        f.write(f"{date},{salary},{blog_income},{other_income},{rent_expense},{grocery_expense},{car_expense},{other_expense},{comments}\n")
    st.success("Data entry added successfully!")

def display_report():
    st.subheader("Display Report")

    # Read all the CSV files in the 'data' directory
    csv_files = [file for file in os.listdir("data") if file.endswith(".csv")]

    if csv_files:
        # Select date for filtering
        selected_date = st.date_input("Select Date")

        # Filter records for the selected date
        filtered_data = []
        for file in csv_files:
            df = pd.read_csv(os.path.join("data", file))
            df['Date'] = pd.to_datetime(df['Date'])
            filtered_df = df[df['Date'].dt.date == selected_date]
            if not filtered_df.empty:
                filtered_data.append(filtered_df.head(1))  # Select only the first row for each date

        if filtered_data:
            # Combine all the filtered DataFrames into a single DataFrame
            combined_df = pd.concat(filtered_data, ignore_index=True)
            st.dataframe(combined_df)
        else:
            st.warning("No data available for the selected date.")
    else:
        st.warning("No data files found.")

    # Clear the report
    if st.button("Clear Report"):
        # Delete all the data files
        for file in csv_files:
            os.remove(os.path.join("data", file))
        st.warning("Report cleared successfully!")

def main():
    st.title("Expense and Income Tracker")
    st.write("Welcome to the Expense and Income Tracker!")

    option = st.sidebar.selectbox("Select Option", ["Data Entry", "Display Report"])

    if option == "Data Entry":
        data_entry()
    elif option == "Display Report":
        display_report()

if __name__ == '__main__':
    main()

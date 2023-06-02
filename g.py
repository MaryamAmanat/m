import os
import streamlit as st
import pandas as pd

# Create data directory if it doesn't exist
if not os.path.exists("data"):
    os.makedirs("data")

def data_entry():
    st.subheader("Data Entry")

    # Select month and date
    month = st.selectbox("Select Month", ["January", "February", "March", "April", "May", "June", "July",
                                          "August", "September", "October", "November", "December"])
    date = st.date_input("Select Date")

    # Create filename based on month and date
    filename = f"data/{month}_{date.day}.csv"

    # Check if file already exists, create new file if not
    if not os.path.isfile(filename):
        with open(filename, "w") as f:
            f.write("Date,Income Type,Income Amount,Expense Type,Expense Amount,Comments\n")
            st.success(f"New file created: {filename}")

    # Take income details
    st.subheader("Income Details")
    income_type = st.radio("Income Type", ["Salary", "Blog Income", "Other Income"])
    income_amount = st.number_input("Income Amount (USD)", min_value=0.0, step=0.01)

    # Take expense details
    st.subheader("Expense Details")
    expense_type = st.radio("Expense Type", ["Rent", "Car Expense", "Grocery Expense", "Other Expense"])
    expense_amount = st.number_input("Expense Amount (USD)", min_value=0.0, step=0.01)

    comments = st.text_area("Comments")

    # Append data to the file
    with open(filename, "a") as f:
        f.write(f"{date},{income_type},{income_amount},{expense_type},{expense_amount},{comments}\n")
    st.success("Data entry added successfully!")

    # Save the data for the current date
    if st.button("Save"):
        st.success("Data saved successfully!")

def display_report():
    st.subheader("Data Report")

    # Read all the CSV files in the 'data' directory
    csv_files = [file for file in os.listdir("data") if file.endswith(".csv")]

    if csv_files:
        # Combine all the CSV data into a single DataFrame
        dfs = []
        for file in csv_files:
            df = pd.read_csv(os.path.join("data", file))
            dfs.append(df)
        if len(dfs) > 0:
            combined_df = pd.concat(dfs, ignore_index=True)
            st.dataframe(combined_df)
        else:
            st.warning("No data available.")
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

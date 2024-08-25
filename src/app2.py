import streamlit as st
import pandas as pd
import joblib

# Load the pipeline model
path = 'model/final_model.pkl'
model = joblib.load(path)

def predict_price(data):
    predictions = model.predict(data)
    return [round(pred, 2) for pred in predictions]

# Streamlit App
st.title("Dynamic Pricing Model Prediction")

# Sidebar
st.sidebar.header("Options")
option = st.sidebar.selectbox("Select Prediction Mode", ["Upload CSV", "Manual Input"])

# CSV Upload
if option == "Upload CSV":
    st.subheader("Upload your CSV file")
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("Data Preview", df.head())
        
        # Prediction
        predictions = predict_price(df)
        df['PredictedPrice'] = predictions
        
        # Download link
        st.subheader("Download Predictions")
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download CSV",
            data=csv,
            file_name='predictions.csv',
            mime='text/csv'
        )

# Manual Input
if option == "Manual Input":
    st.subheader("Input your data")

    num_riders = st.number_input("Number of Riders", min_value=0, max_value=1000, value=0)
    num_drivers = st.number_input("Number of Drivers", min_value=0, max_value=1000, value=0)
    location = st.selectbox("Location Category", ["Urban", "Suburban", "Rural"])
    loyalty_status = st.selectbox("Customer Loyalty Status", ["Silver", "Gold", "Regular"])
    past_rides = st.number_input("Number of Past Rides", min_value=0, max_value=1000, value=0)
    avg_ratings = st.number_input("Average Ratings", min_value=0.0, max_value=5.0, value=0.0, format="%.2f")
    time_booking = st.selectbox("Time of Booking", ["Morning", "Afternoon", "Evening", "Night"])
    vehicle_type = st.selectbox("Vehicle Type", ["Economy", "Premium"])
    exp_ride_duration = st.number_input("Expected Ride Duration", min_value=0, max_value=1000, value=0)
    hist_cost_of_ride = st.number_input("Historical Cost of Ride", min_value=0.0, max_value=10000.0, value=0.0, format="%.2f")

    if st.button("Predict"):
        input_data = pd.DataFrame({
            'NumberofRiders': [num_riders],
            'NumberofDrivers': [num_drivers],
            'LocationCategory': [location],
            'CustomerLoyaltyStatus': [loyalty_status],
            'NumberofPastRides': [past_rides],
            'AverageRatings': [avg_ratings],
            'TimeofBooking': [time_booking],
            'VehicleType': [vehicle_type],
            'ExpectedRideDuration': [exp_ride_duration],
            'HistoricalCostofRide': [hist_cost_of_ride]
        })
        prediction = predict_price(input_data)[0]
        st.write(f"Predicted Price: ${prediction:.2f}")

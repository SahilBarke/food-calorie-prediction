import streamlit as st
import numpy as np
import pandas as pd
import pickle
from footer import footer

# Load model
with open("models/model.pkl", "rb") as f:
    model = pickle.load(f)

# Page configuration
st.set_page_config(page_title="Student Performance Predictor", layout="centered")

# Title
st.title("Food Calorie Prediction App")
st.markdown("Add Your Macros and Get Your Calories")


# Input fields
carbs = st.number_input(
    "Carbohydrates (in grams)", min_value=0.0, step=0.1, max_value=300.0, value=0.0
)
protein = st.number_input(
    "Protein (in grams)", min_value=0.0, step=0.1, max_value=300.0, value=0.0
)
fat = st.number_input(
    "Fat (in grams)", min_value=0.0, step=0.1, max_value=300.0, value=0.0
)


st.write("Note: Please enter realistic values for better predictions.")
# Prediction
if st.button("Predict Calories"):
    if carbs == 0.0 and protein == 0.0 and fat == 0.0:
        st.warning("Please enter at least one macronutrient value greater than zero.")
    else:
        input_data = np.array([[carbs, protein, fat]])
        prediction = model.predict(input_data)
        st.success(f"Estimated Calories: {prediction[0]:.2f} kcal")
        st.info(
            "The predicted calories are an estimate based on the provided macronutrient values. Actual calorie content may vary based on food preparation and other factors."
        )


# Footer
footer()

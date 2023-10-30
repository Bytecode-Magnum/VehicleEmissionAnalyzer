
# Vehicle Carbon Emission Analysis and Prediction with Streamlit Web App

This project involves the analysis and prediction of carbon emissions of vehicles based on their characteristics. The analysis was conducted on a dataset containing details of various vehicles, focusing on their attributes and fuel consumption.


## [Project Overview](https://github.com/Bytecode-Magnum/VehicleEmissionAnalyzer/blob/main/carbon_emission.ipynb)

The project aimed to understand the relationship between vehicle characteristics and carbon emissions, creating a regression model to predict carbon emissions. Additionally, a Streamlit web application was developed for users to estimate carbon emissions based on vehicle details.

## [Dataset](https://github.com/Bytecode-Magnum/VehicleEmissionAnalyzer/blob/main/CO2%20Emissions.csv)

The dataset used in this project contains information about various vehicles and their attributes. The dataset includes the following columns:

- Make
- Model
- Vehicle Class
- Engine Size (L)
- Cylinders
- Transmission
- Fuel Type
- Fuel Consumption City (L/100 km)
- Fuel Consumption Hwy (L/100 km)
- Fuel Consumption Comb (L/100 km)
- Fuel Consumption Comb (mpg)
- CO2 Emissions (g/km)


## Analysis

The project involved in-depth Exploratory Data Analysis (EDA), focusing on understanding various relationships and impacts on carbon emissions:

- **Correlation Analysis:** Investigating potential correlations between different vehicle attributes and carbon emissions to identify influential factors.
  
- **Fuel Efficiency Comparison:** Analyzing the variations in fuel consumption across different vehicle classes to assess their impact on carbon emissions.

- **Transmission Types Impact:** Exploring how different transmission types might affect carbon emissions, if any.

- **Fuel Type Analysis:** Examining the effect of different fuel types on carbon emissions and their efficiency.

- **MPG vs. CO2 Emissions:** Studying the relationship between Miles Per Gallon (MPG) and carbon emissions.

## Model Development

A regression model was created and trained using the dataset to predict carbon emissions based on the significant vehicle attributes identified during the EDA.

## [Streamlit Web App](https://github.com/Bytecode-Magnum/VehicleEmissionAnalyzer/blob/main/web_app.py)

A Streamlit web application was developed for the deployment of the predictive model. This application enables users to input vehicle details and receive an approximate prediction of the carbon emissions.

### Usage

To run the Streamlit application, execute the following command: strealit run web_app.py

import streamlit as st
import joblib


def calculate_carbon_emission(engine_size, cylinders, fuel_consumption_city, vehicle_class):
    try:
        if engine_size and cylinders and fuel_consumption_city:
            engine_size = float(engine_size)
            cylinders = int(cylinders)
            fuel_consumption_city = float(fuel_consumption_city)

            # Mapping vehicle classes to integers
            vehicle_classes = ['COMPACT', 'FULL-SIZE', 'MID-SIZE', 'MINICOMPACT', 'MINIVAN',
                               'PICKUP TRUCK - SMALL', 'PICKUP TRUCK - STANDARD', 'SPECIAL PURPOSE VEHICLE',
                               'STATION WAGON - MID-SIZE', 'STATION WAGON - SMALL', 'SUBCOMPACT', 'SUV - SMALL',
                               'SUV - STANDARD', 'TWO-SEATER', 'VAN - CARGO', 'VAN - PASSENGER']

            if vehicle_class in vehicle_classes:
                vehicle_class_int = vehicle_classes.index(vehicle_class)
            else:
                st.error("Please enter a valid Vehicle Class.")
                return

            # Load the pre-trained model
            loaded_model = joblib.load("carbon_emission_calculate.pkl")

            # Prepare the input features for the model
            input_features = [[engine_size, cylinders, fuel_consumption_city, vehicle_class_int]]

            # Make predictions using the loaded model
            carbon_emission = loaded_model.predict(input_features)
            st.write('### Model Output')
            st.write(f"The predicted carbon emission based on the provided inputs: {carbon_emission[0]:.2f} g/km")
        else:
            st.error("Please fill in all the fields with numerical values.")
    except ValueError:
        st.error("Please enter valid numerical values for the inputs.")


def main():
    st.title('Calculate Carbon Emission of a Vehicle using a Model')
    st.write('Please enter the vehicle data:')

    engine_size = st.text_input('Engine Size (L)', placeholder='Enter a numerical value')
    cylinders = st.text_input('Cylinders', placeholder='Enter a numerical value')
    fuel_consumption_city = st.text_input('Fuel Consumption City (L/100)', placeholder='Enter a numerical value')
    vehicle_class = st.selectbox('Vehicle Class', ['COMPACT', 'FULL-SIZE', 'MID-SIZE', 'MINICOMPACT', 'MINIVAN',
                                                   'PICKUP TRUCK - SMALL', 'PICKUP TRUCK - STANDARD',
                                                   'SPECIAL PURPOSE VEHICLE', 'STATION WAGON - MID-SIZE',
                                                   'STATION WAGON - SMALL', 'SUBCOMPACT', 'SUV - SMALL',
                                                   'SUV - STANDARD', 'TWO-SEATER', 'VAN - CARGO', 'VAN - PASSENGER'])

    if st.button('Calculate Carbon Emission'):
        calculate_carbon_emission(engine_size, cylinders, fuel_consumption_city, vehicle_class)


if __name__ == '__main__':
    main()

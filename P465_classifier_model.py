import streamlit as st
import pickle


# Add a title
st.title('P465 Classification Model')

#Load the dataset
load = open('Pickle_P465_classifier.pkl','rb')
model = pickle.load(load)

def predict(state, area_code, account_length, voice_plan, voice_messages, intl_plan, intl_mins, intl_calls, day_mins, day_calls, eve_mins, eve_calls, night_mins, night_calls, customer_calls):
    prediction = model.predict([[state, area_code, account_length, voice_plan, voice_messages, intl_plan, intl_mins, intl_calls, day_mins, day_calls, eve_mins, eve_calls, night_mins, night_calls, customer_calls]])
    return prediction

def main():
    st.markdown('This model predicts the customer churn for a telecommunication company')
    state = st.selectbox('State',['KS', 'OH', 'NJ', 'OK', 'AL', 'MA', 'MO', 'LA', 'WV', 'IN', 'RI','MT', 'IA', 'NY', 'ID', 'VT', 'VA', 'TX', 'FL', 'CO', 'AZ', 'SC','NE', 'WY', 'HI', 'IL', 'NH', 'GA', 'AK', 'MD', 'AR', 'WI', 'OR','MI', 'UT', 'CA', 'MN', 'SD', 'NC', 'WA', 'NM', 'NV', 'DC', 'KY','ME', 'MS', 'DE', 'TN', 'PA', 'CT', 'ND'])
    area_code = st.selectbox('Area code',['area_code_408','area_code_415','area_code_510'])
    account_length = st.number_input('Account length', min_value=0)
    voice_plan = st.selectbox('Voice plan',['yes','no'])
    voice_messages = st.number_input('Voice messages', min_value=0)
    intl_plan = st.selectbox('International plan',['yes','no'])
    intl_mins = st.number_input('Intl. mins', min_value=0)
    intl_calls = st.number_input('Intl. calls', min_value=0)
    day_mins = st.number_input('Daily mins', min_value=0)
    day_calls = st.number_input('Daily calls', min_value=0)
    eve_mins = st.number_input('Evening mins', min_value=0)
    eve_calls = st.number_input('Evening calls', min_value=0)
    night_mins = st.number_input('Night mins', min_value=0)
    night_calls = st.number_input('Night calls', min_value=0)
    customer_calls = st.number_input('Customer calls', min_value=0)

    if st.button('Predict'):
        result = predict(state, area_code, account_length, voice_plan, voice_messages, intl_plan, intl_mins, intl_calls, day_mins, day_calls, eve_mins, eve_calls, night_mins, night_calls, customer_calls)
        st.success(f'Customer churn is {result[0]}')

if __name__ == '__main__':
    main()


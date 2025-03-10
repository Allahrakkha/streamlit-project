import streamlit as st

st.title("Unit Converter")
st.write("### Convert length, weight and Time")
catagory = st.selectbox("choose category", ['length','weight','time'])

# ............create function................
def units (category, value, unit ):
    if category == "length":
        if unit == "kilometer to mile":
            return value * 0.621371
        elif unit == "mile to kilometer":
            return value / 0.621371
    elif catagory == "weight":
        if unit == "kilogram to gram":
            return value * 1000
        elif unit == "gram to kilogram":
            return value /1000
    elif catagory == "time":
        if unit == "hour to minute":
            return value * 60
        elif unit == "minute to hour":
            return value / 60
    return 0
if catagory == "length":
    unit = st.selectbox("unit: ", ["kilometer to mile", "mile to kilometer"])
elif catagory == "weight":
    unit = st.selectbox ("unit: ", ["kilogram to gram", "gram to kilogram"])
elif catagory == "time":
    unit = st.selectbox("unit: ", ["hour to minute", "minute to hour" ])

value = st.number_input("enter your unit")
if st.button("convert"):
    result = units (catagory, value, unit)
    st.success(f"the result is {result:.2f}")
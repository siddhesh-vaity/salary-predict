import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


def cleanedu(x):
    if 'Bachelor Degree' in x:
        return "Bachelor's Degree"
    if 'Master Degree' in x:
        return "Master's Degree"
    if "Professional degree" in x:
        return "Post Grad"
    else:
        return "Less than bacherlor's"

st.cache
def load_data():
    df = pd.read_csv("survey_results_public_2023.csv")
    df = df[["Country", "EdLevel", "YearsCodePro", "Employment", "ConvertedCompYearly"]]
    df = df[df["ConvertedCompYearly"].notnull()]
    df = df.dropna()
    df = df[df["Employment"] == "Employed, full-time"]
    df = df.drop("Employment", axis=1)
    
    #craete other category of coutry
    country_counts=df['Country'].value_counts()
    low_count_countries = country_counts[country_counts < 200].index
    df['Country'] = df['Country'].replace(low_count_countries, 'Other')
    df = df[df['Country'] != 'Other']

    #filter salary
    df = df[df["ConvertedCompYearly"] <= 250000]
    df = df[df["ConvertedCompYearly"] >= 10000]
    df = df[df["Country"] != "Other"]

     # Replace years of coding experience with numerical values
    df['YearsCodePro'] = df['YearsCodePro'].replace({
        'Less than 1 year': 0.5,
        'More than 50 years': 51  # You can adjust this if needed
    }).astype(float)
    df["EdLevel"] = df["EdLevel"].apply(cleanedu)

    df = df.rename({"ConvertedCompYearly": "Salary"}, axis=1)
    
    return df

def show_visualization():
    df=load_data()
    data=df.groupby(["Country"])["Salary"].mean().sort_index()
    st.write("Average Salary by Country")
    st.bar_chart(data)

    st.write("Average Salary by Years of Experience")
    data=df.groupby(["YearsCodePro"])["Salary"].mean().sort_index()
    st.line_chart(data)

    data=df.groupby(["EdLevel"])["Country"].sum().sort_index()
    



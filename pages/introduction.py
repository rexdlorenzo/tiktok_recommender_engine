from st_pages import add_indentation
add_indentation()

import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import streamlit as st
#add in libraries
import seaborn as sns
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

sns.set()

def load_data():
    # Load the data
    data = pd.read_csv(
        "micro_world.csv",
        encoding='ISO-8859-1'
    )
    return data

def introduction():

    # Load data
    data = load_data()

    philippine_data = data[
        data['regionwb'] == 'East Asia & Pacific (excluding high income)'
        ]

    # Write the title and the subheader
    st.title("The Philippines has high % population with savings compared to neighboring countries.")

    #Insert graph on TOP EA&P countries in terms of %savings 
    data = load_data()
    dataeap = data[
        data['regionwb'] == 'East Asia & Pacific (excluding high income)'
        ]
    dataeap['has_saved'] = dataeap['saved'].apply(
    lambda x: 1 if x == 1 else 0)
    
    st.markdown(
        "According to the study, about 64.5% of Filipinos have saved or set aside money in the past year, whether using an account at a financial institution, mobile money account, savings club for any reason. In East Asia and Pacific region, Philippines ranked 4th for the highest % of people with savings and ranked 1st in the lower-middle income group in the region.")
    # Partition the page into 2
    col1, col2 = st.columns(2)


    # Display metric in column 1
    col1.metric(
        label='Filipinos with savings',
        value=str('64.50%')
    )

    # Display metric in column 1
    col2.metric(
        value=str('Rank 1'), label='versus neighboring countries in the Low Middle income group of East Asia & Pacific Region'
        )


    # Group the data and apply aggregations
    grouped_data = dataeap.groupby(['economy', 'economycode', 'regionwb']).agg(total_saved=('saved', 'sum'),total_population=('wpid_random', 'count')).reset_index()
    # Compute debit card ownership in %
    grouped_data['% of population saved'] = grouped_data['total_saved']*100.0/grouped_data['total_population']
    #Top EA&P countries in terms of % people with savings
    top_10 = grouped_data.sort_values('% of population saved', ascending=False).head(10).reset_index(drop=True)
    sns.set(font_scale=2)
    fig, ax = plt.subplots(figsize=(10, 6))
    cols = ['#DF8020' if (y == 'Philippines') else '#adbdc4' for y in top_10.economy]
    sns.barplot(x="% of population saved", y="economy", data=top_10, palette=cols, ax=ax, orient='h').set(title='Top EA&P countries in terms of % people with savings')
    st.pyplot(fig)
   
    st.subheader(
        """.....but are we really doing great?"""
        )

    st.markdown(
        """According to the study, specifically in the low-income group, majority of the population have no savings hence the negative variance. In the graph, there is a trend that highlights that as one moves up the economic ladder, the gap between with and without savings increases. This shows that an increase in gap signifies that there are more Filipinos with savings versus without. 
        """
        )

    #create function
    def income_group(row):
        if row['inc_q']==1:
            return 'Poorest'
        elif row['inc_q']==2:
            return 'Poor'
        elif row['inc_q']==3:
            return 'Middle Class'
        elif row['inc_q']==4:
            return 'Rich' #borrow from bank/employer/lender
        elif row['inc_q']==5:
            return 'Richest'
        else:
            return 'unknown/no answer'

    data['Income Group'] = data.apply(income_group, axis=1)
    # Fetch Philippine data
    philippine_data = data[
        data['economy'] == 'Philippines'
        ]
    # Group the data and apply aggregations
    grouped_dataph = philippine_data.groupby('Income Group').count()['wpid_random'].to_frame()
    grouped_dataph = philippine_data.groupby(['economy', 'Income Group']).agg(
    total_saved=('saved', 'sum'),
    total_population=('wpid_random', 'count')
    ).reset_index()
    
    
    # Compute debit card ownership in %
    grouped_dataph['% of population saved'] = grouped_dataph['total_saved']*100.0/grouped_dataph['total_population']
    grouped_dataph['% of population with no savings'] = 100 - grouped_dataph['% of population saved']
    top_10ph = grouped_dataph.sort_values('% of population with no savings', ascending=False).head(10).reset_index(drop=True)
    sns.set(font_scale=2)
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x="Income Group", y="% of population with no savings", data=top_10ph, ax=ax, orient='v', color='#DF8020').set(title='Percentage of Filipinos with savings versus without savings')
    st.pyplot(fig)
    
    st.subheader("""Are savings only for the rich?""")

    st.markdown(
        """More than half of low-income Filipinos and almost half of the middle class have no savings. 
    """
    )
    grouped_dataph['% of population with savings'] = grouped_dataph['total_saved']*100.0/grouped_dataph['total_population']
    grouped_dataph['% of population without savings'] = 100 - grouped_dataph['% of population with savings']
    grouped_dataph['diff of with savings vs without savings'] = grouped_dataph['% of population with savings'] - grouped_dataph['% of population without savings']
    grouped_dataph=grouped_dataph.sort_values('diff of with savings vs without savings',ascending=True)
    
    
    sns.set(font_scale=2)
    sns.set_style(style='white')
    fig, ax = plt.subplots(figsize=(10, 6))
    cols = ['#CC0000','#CC0000','#DF8020','#DF8020','#DF8020','#DF8020']
    g1 = sns.barplot(y="diff of with savings vs without savings", x="Income Group", data=grouped_dataph, ax=ax, palette=cols)
    g1.set_ylim(-25,80)
    g1.set(title='Difference of with savings and without savings')  # add a title
    g1.set(ylabel=None)  # remove the axis label
    
    for p in g1.patches:
        height = p.get_height()
    if height > 0:
        g1.text(p.get_x()+p.get_width()/2., height+2, '{:.1f}%'.format(height), ha="center", fontsize=16)
    else:
        g1.text(p.get_x()+p.get_width()/2., height-7, '{:.1f}%'.format(height), ha="center", fontsize=16)
    st.pyplot(fig)
    
    
    st.markdown(
        """More than half of low-income Filipinos and almost half of the middle class have no savings. 
    """
    )
    

    st.subheader("""Why are Filipinos not saving enough?""")
    st.markdown(
        """Filipinos cannot save mainly due to lack of money and expensive fees of maintaining a savings account. 
    """
    )

       #INSERT GRAPH
    
    st.subheader("""
    INSERT GRAPH HERE
    """)


    st.markdown(
        """The inability of Filipinos to maintain a savings account can be attributed to various factors, with the most common ones being insufficient funds and high account maintenance fees. 
            Many Filipinos, specifically for the low-income group, struggle to make ends meet, and as a result, they may find it challenging to set aside money for savings.
            Moreover, some banks may require a minimum deposit amount to open and maintain a savings account, which can be a considerable challenge for many Filipinos. As a result, many Filipinos may opt not to open or maintain a savings account, leaving them without a reliable means of saving money. Overall, a combination of financial constraints, high fees, and low financial literacy may contribute to the insufficient savings of many Filipinos.
        """
    )

 




load_data()
introduction()

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import io
from datetime import datetime, timedelta

# Set page title and configuration first (must be before any other Streamlit calls)
st.set_page_config(
    page_title="Customer Feedback Analysis | App By Karan Heera",
    page_icon="📝"
)

# SEO Enhancements: Meta Tags
st.markdown(
    """
    <meta name="description" content="Analyze customer feedback sentiment and make data-driven decisions with our comprehensive feedback analysis tool."/>
    <meta name="keywords" content="Customer Feedback, Sentiment Analysis, Feedback Visualization, Data Analysis"/>
    <meta property="og:title" content="Comprehensive Customer Feedback Analysis"/>
    <meta property="og:description" content="Unlock actionable insights from your customer feedback to make informed business decisions."/>    

    """,
    unsafe_allow_html=True
)

# Title and description of the app
st.title('Comprehensive Customer Feedback Analysis: Unlock Insights for Strategic Decision-Making')
st.sidebar.title('Comprehensive Customer Feedback Analysis: Unlock Insights for Strategic Decision-Making')
st.sidebar.markdown('### App by Karan Heera')

st.sidebar.markdown('_____________________________')

# Show description only when no file is uploaded
uploaded_file = st.sidebar.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file is None:
    st.markdown(''' 
    ## Transform Your Customer Feedback into Actionable Insights

    What if you could *easily* analyze your company's feedback and instantly know where you stand with your customers? This powerful app takes your CSV feedback file—whether it's from the current or past year—and reveals key insights by categorizing reviews into **positive, neutral**, and **negative** sentiments.

    ### Here's what it can do:

    - **Visualize** your feedback with stunning bar plots and pie charts to see the breakdown of customer sentiment.
    - **Filter by date range**: Choose custom date ranges or predefined options like **Last 7 Days**, **Last 30 Days**, or even **Last 6 Months**.
    - **Year-over-Year Comparison**: Compare your reviews from the current year with those of the previous year to measure progress.
    - **Download Filtered Data**: Quickly download feedback categorized by **positive**, **neutral**, or **negative** sentiment for easy reporting.

    This tool is essential for **companies** looking to gauge their customer satisfaction, spot trends, and make informed decisions based on real-time feedback. **See exactly where you excel** and where there's room for improvement—without any guesswork!
    ''')

# Define sample CSV data with new column names
sample_data = """
feedback_id,feedback_sentiment,feedback,feedback_received_on
1,positive,"Great product! Highly recommend.",25-01-2025
2,neutral,"The product is okay, could be improved.",24-01-2024
3,negative,"Not happy with the product, it broke after a week.",23-01-2023
4,positive,"Good value for money.",15-01-2025
5,negative,"Very poor quality.",18-01-2024
6,neutral,"It works, but could be improved.",20-12-2023
"""

# Convert the sample CSV data into a file for download
sample_csv = io.StringIO(sample_data)

# Sidebar: Provide a download button for the sample CSV
st.sidebar.markdown("Download the [sample CSV file](#) to upload reviews in the correct format.")
st.sidebar.download_button(
    label="Download Sample CSV",
    data=sample_csv.getvalue(),
    file_name="sample_reviews.csv",
    mime="text/csv"
)

# Cache the reading and processing of CSV file for better performance
@st.cache_data
def load_and_process_data(uploaded_file):
    try:
        # Try reading the file with 'ISO-8859-1' encoding to handle special characters
        data = pd.read_csv(uploaded_file, encoding='ISO-8859-1')
    except Exception as e:
        st.error(f"Error reading the file: {str(e)}")
        return pd.DataFrame()  # Return an empty DataFrame if there's an error
    
    # Ensure that the CSV contains required columns with new names
    required_columns = ['feedback_id', 'feedback_sentiment', 'feedback', 'feedback_received_on']
    if not all(col in data.columns for col in required_columns):
        raise ValueError(f"CSV file must contain the following columns with exact header names, Please Download Sample CSV File: {', '.join(required_columns)}")
    
    # Format the feedback_received_on date to DD/MM/YYYY (no time)
    data['feedback_received_on'] = pd.to_datetime(data['feedback_received_on'], format='%d-%m-%Y')
    
    return data

if uploaded_file is not None:
    try:
        data = load_and_process_data(uploaded_file)
    except ValueError as e:
        st.error(str(e))
        data = pd.DataFrame()

    if not data.empty:
        # Sidebar: Date Filter - Custom Range or Predefined Period
        st.sidebar.subheader('Filter Feedback by Date')
        date_filter_option = st.sidebar.radio('Select a date range', ('All Feedback', 'Custom', 'Last 7 Days', 'Last 30 Days', 'Last 3 Months', 'Last 6 Months'))

        # Get today's date
        today = datetime.today().date()

        if date_filter_option == 'Custom':
            start_date = st.sidebar.date_input("Start date", today - timedelta(days=30))
            end_date = st.sidebar.date_input("End date", today)
            filtered_data = data[(data['feedback_received_on'] >= pd.to_datetime(start_date)) & (data['feedback_received_on'] <= pd.to_datetime(end_date))]
        elif date_filter_option == 'Last 7 Days':
            start_date = today - timedelta(days=7)
            filtered_data = data[data['feedback_received_on'] >= pd.to_datetime(start_date)]
        elif date_filter_option == 'Last 30 Days':
            start_date = today - timedelta(days=30)
            filtered_data = data[data['feedback_received_on'] >= pd.to_datetime(start_date)]
        elif date_filter_option == 'Last 3 Months':
            start_date = today - timedelta(days=90)
            filtered_data = data[data['feedback_received_on'] >= pd.to_datetime(start_date)]
        elif date_filter_option == 'Last 6 Months':
            start_date = today - timedelta(days=180)
            filtered_data = data[data['feedback_received_on'] >= pd.to_datetime(start_date)]
        else:
            # No date filtering, show all data
            filtered_data = data

        # Show message if no data found after filtering by date
        if filtered_data.empty:
            st.warning("No reviews found for the selected date range.")
        else:
            # Sidebar: Show random review
            st.sidebar.subheader('Show Random Feedback')
            random_feedback_sentiment = st.sidebar.radio('Sentiment', ('positive', 'neutral', 'negative'))
            random_review = filtered_data.query('feedback_sentiment == @random_feedback_sentiment')[['feedback']].sample(n=1) if not filtered_data.query('feedback_sentiment == @random_feedback_sentiment').empty else None
            if random_review is not None:
                st.sidebar.markdown(random_review.iat[0, 0])
            else:
                st.sidebar.warning("No reviews available for the selected sentiment.")

            # Sidebar: Visualization type selection
            st.sidebar.markdown('### No. of Feedback by Sentiment')
            select = st.sidebar.selectbox('Visualization type', ['Bar plot', 'Pie chart'], key='1')

            sentiment_count = filtered_data['feedback_sentiment'].value_counts()
            sentiment_count = pd.DataFrame({'Sentiment': sentiment_count.index, 'Reviews': sentiment_count.values})

            total_feedback_count = len(filtered_data)

            # Alert the total feedback count
            st.success(f"Total number of feedback analyzed: {total_feedback_count}")

            if not st.sidebar.checkbox('Hide', False):
                st.markdown(f'### No. of Feedback by Sentiment (Total: {total_feedback_count})')

                # Define custom pastel color mapping for the bar plot and pie chart
                color_map = {'negative': '#FF6F61',  # Pastel Red
                             'positive': '#A2CFFE',  # Baby Blue
                             'neutral': '#FFB347'}  # Pastel Orange
                
                if select == 'Bar plot':
                    fig = go.Figure(data=[go.Bar(
                        x=sentiment_count['Sentiment'],
                        y=sentiment_count['Reviews'],
                        text=sentiment_count['Reviews'],
                        textposition='auto',
                        marker=dict(color=[color_map.get(sentiment) for sentiment in sentiment_count['Sentiment']]),
                        opacity=0.8
                    )])

                    fig.update_layout(
                        title=f"Feedback Sentiment Distribution (Total: {total_feedback_count})",
                        scene=dict(
                            xaxis_title="Sentiment",
                            yaxis_title="Number of Reviews",
                        ),
                        template="plotly_dark"
                    )
                    st.plotly_chart(fig)
                else:
                    fig = px.pie(sentiment_count, values='Reviews', names='Sentiment',
                                 color='Sentiment', color_discrete_map=color_map, hole=0.3)
                    fig.update_traces(textinfo='percent+label', pull=[0.1, 0.1, 0.1])
                    fig.update_layout(
                        title=f"Feedback Sentiment Breakdown (Total: {total_feedback_count})",
                        template="plotly_dark"
                    )
                    st.plotly_chart(fig)

            # Multi-selection for downloading filtered reviews (positive, neutral, negative)
            selected_sentiments = st.sidebar.multiselect(
                'Select sentiments to download',
                options=['positive', 'neutral', 'negative'],
                default=['positive', 'neutral', 'negative']
            )

            if selected_sentiments:
                filtered_data_by_sentiment = filtered_data[filtered_data['feedback_sentiment'].isin(selected_sentiments)]
                if filtered_data_by_sentiment.empty:
                    st.warning("No feedback found for the selected sentiment(s).")
                else:
                    csv_data = filtered_data_by_sentiment.to_csv(index=False)
                    st.sidebar.download_button(
                        label="Download Filtered CSV",
                        data=csv_data,
                        file_name="filtered_reviews.csv",
                        mime="text/csv"
                    )

            # Optional: Show raw data for debugging or review
            if st.sidebar.checkbox('Show raw data', True):
                st.write(filtered_data)

            # Sidebar: Year-wise comparison (if enabled)
            st.sidebar.subheader('Compare by year')
            year_comparison = st.sidebar.checkbox('Compare current year vs previous year', value=False)

            if year_comparison:
                current_year_data = filtered_data[filtered_data['feedback_received_on'].dt.year == today.year]
                previous_year_data = filtered_data[filtered_data['feedback_received_on'].dt.year == today.year - 1]

                current_year_count = current_year_data['feedback_sentiment'].value_counts()
                previous_year_count = previous_year_data['feedback_sentiment'].value_counts()

                # Merge the two dataframes for comparison
                comparison_df = pd.DataFrame({
                    'Sentiment': current_year_count.index,
                    f'{today.year} Reviews': current_year_count.values,
                    f'{today.year - 1} Reviews': previous_year_count.values
                }).fillna(0)

                st.markdown(f'### Year-wise Comparison for the same period in {today.year} vs {today.year - 1}')
                st.write(comparison_df)

                # Visualization of year-wise comparison
                st.markdown('### Year-wise Sentiment Comparison')
                comparison_fig = px.bar(comparison_df, x='Sentiment', y=[f'{today.year} Reviews', f'{today.year - 1} Reviews'],
                                        barmode='group', height=500, color_discrete_map=color_map)
                st.plotly_chart(comparison_fig)

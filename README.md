# Customer-Feedback-Insights : <br> (Using Python & Streamlit)

**Unlock the Hidden Truth in Your Customer Feedback: Instant Sentiment Analysis & Visualizations!**

## Description
Transform your customer feedback into actionable insights with this powerful analysis tool! Upload your CSV file, and watch as it automatically categorizes reviews into positive, neutral, and negative sentiments. Visualize your data with stunning charts, compare feedback year-over-year, and easily download filtered data for your reports. Say goodbye to guesswork and discover exactly where your business stands with your customers. Start making smarter decisions now!

### Key Features:
- **Sentiment Analysis**: Automatically classifies feedback into **positive**, **neutral**, and **negative** sentiments.
- **Visualization**: Provides beautiful and interactive visualizations of feedback sentiment distribution using Plotly’s bar plots and pie charts.
- **Date Filter**: Filters feedback by date range (e.g., Last 7 Days, Last 30 Days, Custom Date Range).
- **Year-over-Year Comparison**: Compares feedback sentiment from the current year against the previous year.
- **Downloadable Reports**: Allows users to download feedback data filtered by sentiment (positive, neutral, negative).
- **Random Feedback Display**: Displays a random feedback sample based on the selected sentiment type.

## Demo

You can try the app and analyze customer feedback by uploading your CSV files containing customer reviews. The app will automatically process the data and present interactive visualizations.

## Technologies Used

- **Streamlit**: A fast way to create and share data apps.
- **Plotly**: For interactive charts and visualizations.
- **Pandas**: For data manipulation and analysis.
- **Python**: The main programming language used in the app.

## Installation

### Prerequisites

To run this project locally, you need to have Python installed. You also need to install the required Python packages listed in `requirements.txt`.

1. Clone the repository:
   ```bash
   git clone https://github.com/karanheera/Customer-Feedback-Insights.git
   ```

2. Navigate to the project directory:
   ```bash
   cd Customer-Feedback-Insights
   ```

3. Install the required dependencies using pip:
   ```bash
   pip install -r requirements.txt
   ```

### Running the App

To run the app locally, use the following command:
```bash
streamlit run app.py
```
The app will start running on your local server, usually at [http://localhost:8501](http://localhost:8501).

## File Structure

```plaintext
/customer-feedback-analysis-csv-python-streamlit
│
├── app.py              # The main Customer Feedback Analysis file
├── CODE_OF_CONDUCT.md  # The Code of Conduct file
├── CONTRIBUTING.md     # Contribution file
├── LICENSE             # MIT License file
├── README.md           # This file
├── requirements.txt    # List of required Python libraries
├── sample_reviews.csv  # Sample CSV file for testing
```

## Usage

### Upload CSV File
On the sidebar, you will find an option to upload a CSV file containing customer feedback. Ensure your CSV file contains the following columns:
- **feedback_id**: A unique identifier for each feedback.
- **feedback_sentiment**: The sentiment of the feedback (positive, neutral, or negative).
- **feedback**: The actual customer feedback text.
- **feedback_received_on**: The date the feedback was received (in DD-MM-YYYY format).

You can also download the **Sample CSV** from the sidebar and update the data in it

### Filter by Date Range
Choose a custom date range or predefined ranges (Last 7 Days, Last 30 Days, etc.) to analyze feedback from specific time periods.

### Visualization
Choose between a bar plot or pie chart to visualize the breakdown of sentiment in the feedback.

### Random Feedback Display
Optionally, you can view a random piece of feedback based on the sentiment type you select.

### Download Data
Filtered feedback can be downloaded as a CSV file for reporting or further analysis.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements
- **Streamlit**: Streamlit for enabling easy and fast app creation.
- **Plotly**: Plotly for providing beautiful interactive charts.
- **Pandas**: Pandas for efficient data manipulation and analysis.

## Contributing
Contributions are welcome! If you find a bug or want to add a feature, feel free to open an issue or submit a pull request.

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes and push them to your forked repository.
4. Create a pull request with a clear explanation of your changes.

## Contact
For any questions or inquiries, please contact the project maintainer:

**Karan Heera**  
- LinkedIn: https://www.linkedin.com/in/karanheera/
- GitHub: https://github.com/karanheera
```

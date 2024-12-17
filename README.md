# COVID-19 Global Dashboard

## Team Members
| Name             | Role                  |
|------------------|-----------------------|
| **Jalpeet Korat (KU2407U317)**     | Team Lead / Developer |
| **Dhruv Hirpara (KU2407U**     | Data Processing Lead  |
| **Jay Patel (KU2407U**     | Visualization Expert  |
| **Smeet Goswami (KU2407U** | Testing / QA          |
| **Pavan Savani (KU2407U**     | Documentation Lead    |

---

## Objevtive
Analyze and visualize COVID-19 case trends and vaccination data by country.

## Project Description
The **COVID-19 Global Dashboard** is an interactive web application built using **Dash** and **Plotly** to visualize global trends in COVID-19 confirmed cases, deaths, and vaccinations. Users can explore data at a global and country-specific level through clear insights by interactive choropleth maps and time-series visualizations.

---

## Datasets
This project makes use of the public datasets related to confirmed cases, deaths, and vaccinations:

1.  **Confirmed COVID-19 Cases**
    - Source: [Johns Hopkins CSSE COVID-19 Dataset](https://github.com/CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv)
    - File Path: `data/time_series_covid19_confirmed_global.csv`

2.  **COVID-19 Deaths**
    - Source: [Johns Hopkins CSSE COVID-19 Dataset](https://github.com/CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv)
    - File Path: `data/time_series_covid19_deaths_global.csv`

3. **COVID-19 Vaccinations**
   - Source: [Our World in Data Vaccination Dataset](https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/vaccinations.csv)
   - File Path: `data/vaccinations.csv`

---

## File Structure
The project is structured under the following key files:
1. **app.py**
   - Initializes the Dash application.
   - Defines the app layout and server configurations.

2. **data_processing.py**
   - Loads and processes the datasets.
   - Formats and cleans data for use in the dashboard.

3. **callbacks.py**
   - Defines the callback logic to dynamically update graphs based on user input.

4. **visualizations.py**
   - Defines the user interface layout using Dash components.
     
---

## How to Run the Project
Steps to Set up and Run the Project on Your Local Machine
=====================================

1.  Clone the Repository
    ```bash
    git clone <repository-url>
    cd <project-directory>
    ```

2.  Install Dependencies
    Make sure you have Python installed. Use `pip` to install necessary packages:
    ```bash
    pip install -r requirements.txt
    ```

3.  Place the Datasets
Download the datasets and put them in the `data/` directory:
   - [Confirmed Cases](https://github.com/CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv)
   - [Deaths](https://github.com/CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv)
   - [Vaccinations](https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/vaccinations.csv)

4. **Run the Application**
   Start the Dash server:
   ```bash
   python app.py
   ```
   Open the app in your browser at `http://127.0.0.1:8050/`.

---

## Summary of Results
- **Interactive Dropdowns**: Choose countries and types of data (Confirmed Cases, Deaths, and People Vaccinated).
- **Choropleth Map**: Global COVID-19 data represented geographically.
- **Time-Series Graph**: Country-specific trend view for the selected countries.
- **Responsive Design**: Friendly and optimized interface for all devices.

---

## Libraries
- Python 3.7+
- Dash
- Plotly
- Pandas

Install dependencies using:
```bash
pip install dash plotly pandas
```

Thanks for checking out our COVID-19 Dashboard!

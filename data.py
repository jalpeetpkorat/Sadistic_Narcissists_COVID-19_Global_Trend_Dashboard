# data.py

import pandas as pd

# URLs for the datasets
url_confirmed = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
url_deaths = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv"
url_vaccinations = "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/vaccinations.csv"

# Load data
def load_data():
    confirmed_data = pd.read_csv(url_confirmed)
    deaths_data = pd.read_csv(url_deaths)
    vaccination_data = pd.read_csv(url_vaccinations)
    
    # Melt the confirmed cases and deaths data for better manipulation
    confirmed_data = confirmed_data.melt(
        id_vars=["Province/State", "Country/Region", "Lat", "Long"],
        var_name="Date", value_name="Confirmed Cases"
    )
    confirmed_data["Date"] = pd.to_datetime(confirmed_data["Date"], errors='coerce')

    deaths_data = deaths_data.melt(
        id_vars=["Province/State", "Country/Region", "Lat", "Long"],
        var_name="Date", value_name="Deaths"
    )
    deaths_data["Date"] = pd.to_datetime(deaths_data["Date"], errors='coerce')

    # Filter the vaccination data to include country and date
    vaccination_data = vaccination_data[vaccination_data["location"].notnull()]
    vaccination_data["Date"] = pd.to_datetime(vaccination_data["date"], errors='coerce')

    # Handle specific regions like Jammu & Kashmir as part of India
    confirmed_data['Country'] = confirmed_data['Country/Region'].replace({
        'Jammu and Kashmir': 'India',
        'Kashmir': 'India'
    })

    deaths_data['Country'] = deaths_data['Country/Region'].replace({
        'Jammu and Kashmir': 'India',
        'Kashmir': 'India'
    })

    vaccination_data['Country'] = vaccination_data['location'].replace({
        'Jammu and Kashmir': 'India',
        'Kashmir': 'India'
    })

    # Merge the dataframes on the 'Country' column
    country_data = pd.merge(
        confirmed_data.groupby("Country")["Confirmed Cases"].max(),
        deaths_data.groupby("Country")["Deaths"].max(),
        on="Country"
    )
    country_data = pd.merge(
        country_data,
        vaccination_data.groupby("Country")["total_vaccinations"].max().reset_index(),
        on="Country",
        how="left"  # Left join to preserve countries with no vaccination data
    )

    # Fill missing vaccination data with 0
    country_data["total_vaccinations"] = country_data["total_vaccinations"].fillna(0)

    return country_data, confirmed_data, deaths_data, vaccination_data

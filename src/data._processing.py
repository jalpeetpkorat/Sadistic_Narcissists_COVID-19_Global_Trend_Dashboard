import pandas as pd

# URLs for datasets
URL_CONFIRMED = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
URL_DEATHS = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv"
URL_VACCINATIONS = "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/vaccinations.csv"

# Load data
def load_data():
    # Load datasets
    confirmed_data = pd.read_csv(URL_CONFIRMED)
    deaths_data = pd.read_csv(URL_DEATHS)
    vaccination_data = pd.read_csv(URL_VACCINATIONS)

    # Melt confirmed and deaths data
    confirmed_data = confirmed_data.melt(
        id_vars=["Province/State", "Country/Region", "Lat", "Long"],
        var_name="Date", value_name="Confirmed Cases"
    )
    deaths_data = deaths_data.melt(
        id_vars=["Province/State", "Country/Region", "Lat", "Long"],
        var_name="Date", value_name="Deaths"
    )

    # Format dates
    confirmed_data["Date"] = pd.to_datetime(confirmed_data["Date"])
    deaths_data["Date"] = pd.to_datetime(deaths_data["Date"])
    vaccination_data["Date"] = pd.to_datetime(vaccination_data["date"], errors="coerce")

    # Rename and simplify vaccination data
    vaccination_data = vaccination_data[["location", "Date", "total_vaccinations"]]
    vaccination_data.rename(columns={"location": "Country"}, inplace=True)

    return confirmed_data, deaths_data, vaccination_data

# Summarize country-level data
def get_country_summary(confirmed, deaths, vaccinations):
    confirmed_summary = confirmed.groupby("Country/Region")["Confirmed Cases"].max().reset_index()
    deaths_summary = deaths.groupby("Country/Region")["Deaths"].max().reset_index()
    vaccinations_summary = vaccinations.groupby("Country")["total_vaccinations"].max().reset_index()

    # Merge data
    confirmed_summary.rename(columns={"Country/Region": "Country"}, inplace=True)
    deaths_summary.rename(columns={"Country/Region": "Country"}, inplace=True)

    country_data = confirmed_summary.merge(deaths_summary, on="Country", how="left")
    country_data = country_data.merge(vaccinations_summary, on="Country", how="left")
    country_data["total_vaccinations"].fillna(0, inplace=True)

    return country_data

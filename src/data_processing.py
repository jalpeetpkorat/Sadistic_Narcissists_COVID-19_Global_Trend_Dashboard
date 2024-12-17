import pandas as pd

# Datasets
confirmed_cases = "data/time_series_covid19_confirmed_global.csv"
deaths = "data/time_series_covid19_deaths_global.csv"
vaccinations = "data/vaccinations.csv"

# Load data
def load_data():
    # Load datasets
    confirmed_data = pd.read_csv(confirmed_cases)
    deaths_data = pd.read_csv(deaths)
    vaccination_data = pd.read_csv(vaccinations)

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
    vaccination_data = vaccination_data[["location", "Date", "people_vaccinated"]]
    vaccination_data.rename(columns={"location": "Country", "people_vaccinated": "People Vaccinated"}, inplace=True)

    return confirmed_data, deaths_data, vaccination_data

# Summarize country-level data
def get_country_summary(confirmed, deaths, vaccinations):
    confirmed_summary = confirmed.groupby("Country/Region")["Confirmed Cases"].max().reset_index()
    deaths_summary = deaths.groupby("Country/Region")["Deaths"].max().reset_index()
    vaccinations_summary = vaccinations.groupby("Country")["People Vaccinated"].max().reset_index()

    # Merge data
    confirmed_summary.rename(columns={"Country/Region": "Country"}, inplace=True)
    deaths_summary.rename(columns={"Country/Region": "Country"}, inplace=True)

    country_data = confirmed_summary.merge(deaths_summary, on="Country", how="left")
    country_data = country_data.merge(vaccinations_summary, on="Country", how="left")
    country_data["People Vaccinated"].fillna(0, inplace=True)

    return country_data

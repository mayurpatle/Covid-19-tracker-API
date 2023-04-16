import requests
import matplotlib.pyplot as plt

# Define the COVID-19 API endpoint
COVID_API_ENDPOINT = "https://api.covid19api.com"

def get_country_data(country):
    # Set up the API parameters
    endpoint = f"{COVID_API_ENDPOINT}/total/country/{country}"
    params = {
        "from": "2020-01-01T00:00:00Z",
        "to": "2030-12-31T00:00:00Z"
    }

    # Send the API request
    response = requests.get(endpoint, params=params)

    # Parse the response JSON
    data = response.json()

    # Get the latest data
    latest_data = data[-1]

    # Return a dictionary of relevant data
    return {
        "country": latest_data["Country"],
        "confirmed": latest_data["Confirmed"],
        "deaths": latest_data["Deaths"],
        "recovered": latest_data["Recovered"]
    }

def plot_country_data(country):
    # Set up the API parameters
    endpoint = f"{COVID_API_ENDPOINT}/total/country/{country}"
    params = {
        "from": "2020-01-01T00:00:00Z",
        "to": "2030-12-31T00:00:00Z"
    }

    # Send the API request
    response = requests.get(endpoint, params=params)

    # Parse the response JSON
    data = response.json()

    # Get the relevant data for plotting
    dates = [entry["Date"][:10] for entry in data]
    confirmed = [entry["Confirmed"] for entry in data]
    deaths = [entry["Deaths"] for entry in data]
    recovered = [entry["Recovered"] for entry in data]

    # Plot the data
    plt.plot(dates, confirmed, label="Confirmed")
    plt.plot(dates, deaths, label="Deaths")
    plt.plot(dates, recovered, label="Recovered")
    plt.title(f"COVID-19 Statistics for {country}")
    plt.xlabel("Date")
    plt.ylabel("Number of Cases")
    plt.legend()
    plt.show()

# Example usage
country = "US"
data = get_country_data(country)
print(f"COVID-19 statistics for {data['country']}:")
print(f"Confirmed cases: {data['confirmed']}")
print(f"Deaths: {data['deaths']}")
print(f"Recovered: {data['recovered']}")
plot_country_data(country)

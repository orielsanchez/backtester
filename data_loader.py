import pandas as pd
import requests


def load_csv(filepath: str) -> pd.DataFrame:
    """
    Load historical price data from a CSV file.

    Expect columns: Date, Open, High, Low, Close, Volume
    """
    df = pd.read_csv(filepath, parse_dates=["Date"])
    df.set_index("Date", inplace=True)
    df.sort_index()

    # Basic cleaning
    df = df.dropna()

    return df


def fetch_data_polygon(symbol: str, start: str, end: str, api_key: str) -> pd.DataFrame:
    url = f"https://api.polygon.io/v2/aggs/ticker/{symbol}/range/1/day/{start}/{end}"
    params = {"adjusted": "true", "sort": "asc", "limit": 50000, "apiKey": api_key}
    response = requests.get(url, params=params)
    data = response.json()

    if "results" not in data:
        raise ValueError(f"No data returned: {data}")

    records = data["results"]
    df = pd.DataFrame.from_records(records)

    # Convert timestamp to datetime
    df["t"] = pd.to_datetime(df["t"], unit="ms")
    df = df.rename(
        columns={
            "t": "Date",
            "o": "Open",
            "h": "High",
            "l": "Low",
            "c": "Close",
            "v": "Volume",
        }
    )
    df.set_index("Date", inplace=True)
    df = df[["Open", "High", "Low", "Close", "Volume"]]
    return df


if __name__ == "__main__":
    try:
        df_local = load_csv("data/AAPl.csv")
        print("Local CSV loaded:")
        print(df_local.head())
    except FileNotFoundError:
        print("Local file not found.")

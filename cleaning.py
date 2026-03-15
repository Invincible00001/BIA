import pandas as pd


def clean_board_data(raw):

    items = raw["data"]["boards"][0]["items_page"]["items"]

    rows = []

    for item in items:

        row = {"Item Name": item["name"]}

        for col in item["column_values"]:
            row[col["column"]["title"]] = col["text"]

        rows.append(row)

    df = pd.DataFrame(rows)

    df.fillna("Unknown", inplace=True)

    return df


def normalize_sector(sector):

    if not sector:
        return "Unknown"

    sector = sector.lower()

    if "energy" in sector:
        return "Energy"

    if "mining" in sector:
        return "Mining"

    if "infra" in sector:
        return "Infrastructure"

    return sector.title()
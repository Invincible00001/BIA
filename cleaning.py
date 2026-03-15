import pandas as pd


def clean_board_data(raw):

    if "data" not in raw:
        raise Exception(f"Monday API error: {raw}")

    boards = raw["data"].get("boards", [])

    if not boards:
        raise Exception("No boards returned from Monday API")

    items = boards[0]["items_page"]["items"]

    rows = []

    for item in items:

        row = {"Item Name": item["name"]}

        for col in item["column_values"]:
            row[col["column"]["title"]] = col["text"]

        rows.append(row)

    df = pd.DataFrame(rows)

    df.columns = df.columns.str.strip()

    df.fillna("", inplace=True)

    return df

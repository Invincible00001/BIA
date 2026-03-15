import pandas as pd


def clean_currency(series):

    return (
        series
        .str.replace(",", "", regex=False)
        .replace("", "0")
        .astype(float)
    )


def pipeline_by_sector(df, sector):

    if "Sector/service" not in df.columns:
        return {"deal_count": 0, "pipeline_value": 0, "stage_distribution": {}}

    filtered = df[
        df["Sector/service"]
        .str.lower()
        .str.contains(sector.lower(), na=False)
    ]

    deal_count = len(filtered)

    if "Masked Deal value" in df.columns:

        try:
            values = clean_currency(filtered["Masked Deal value"])
            pipeline_value = values.sum()
        except:
            pipeline_value = 0

    else:
        pipeline_value = 0

    if "Deal Stage" in df.columns:
        stages = filtered["Deal Stage"].value_counts().to_dict()
    else:
        stages = {}

    return {
        "deal_count": deal_count,
        "pipeline_value": pipeline_value,
        "stage_distribution": stages
    }


def full_pipeline(df):

    deal_count = len(df)

    try:
        values = clean_currency(df["Masked Deal value"])
        pipeline_value = values.sum()
    except:
        pipeline_value = 0

    stages = df["Deal Stage"].value_counts().to_dict()

    return {
        "deal_count": deal_count,
        "pipeline_value": pipeline_value,
        "stage_distribution": stages
    }


def work_orders_summary(df):

    if "Execution Status" not in df.columns:
        return {}

    return df["Execution Status"].value_counts().to_dict()
def stage_with_most_deals(df):

    if "Deal Stage" not in df.columns:
        return "Stage data unavailable"

    stage_counts = df["Deal Stage"].value_counts()

    top_stage = stage_counts.idxmax()
    count = stage_counts.max()

    return top_stage, count


def total_pipeline_value(df):

    try:
        values = (
            df["Masked Deal value"]
            .str.replace(",", "", regex=False)
            .replace("", "0")
            .astype(float)
        )

        return values.sum()

    except:
        return 0


def deal_count(df):

    return len(df)
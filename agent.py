from monday_api import fetch_board_items
from cleaning import clean_board_data
from analysis import pipeline_by_sector, full_pipeline, work_orders_summary
from config import DEALS_BOARD_ID, WORK_ORDERS_BOARD_ID
from analysis import (
    pipeline_by_sector,
    full_pipeline,
    work_orders_summary,
    deal_count,
    total_pipeline_value,
    stage_with_most_deals
)

def run_agent(query):

    trace = []

    query = query.lower()

    trace.append("Fetching Deals board from monday.com")
    deals_raw = fetch_board_items(DEALS_BOARD_ID)

    trace.append("Cleaning Deals data")
    deals_df = clean_board_data(deals_raw)

    # SECTOR PIPELINE
    if "mining" in query:
        trace.append("Filtering Mining sector")
        result = pipeline_by_sector(deals_df, "Mining")

        answer = f"""
Mining Sector Pipeline

Deals: {result['deal_count']}

Pipeline Value: ₹{result['pipeline_value']:,.0f}
"""

        return answer, trace


    # TOTAL DEAL COUNT
    if "how many deals" in query or "deal count" in query:

        trace.append("Calculating deal count")

        count = deal_count(deals_df)

        answer = f"""
Total Deals in Pipeline: {count}
"""

        return answer, trace


    # PIPELINE VALUE
    if "pipeline value" in query or "total value" in query:

        trace.append("Calculating total pipeline value")

        value = total_pipeline_value(deals_df)

        answer = f"""
Total Pipeline Value: ₹{value:,.0f}
"""

        return answer, trace


    # STAGE ANALYSIS
    if "which stage" in query or "most deals" in query:

        trace.append("Analyzing deal stages")

        stage, count = stage_with_most_deals(deals_df)

        answer = f"""
Stage With Most Deals

{stage}

Deals in this stage: {count}
"""

        return answer, trace


    # DEFAULT PIPELINE
    trace.append("Calculating full pipeline")

    result = full_pipeline(deals_df)

    answer = f"""
Pipeline Overview

Deals: {result['deal_count']}

Pipeline Value: ₹{result['pipeline_value']:,.0f}
"""

    return answer, trace
import requests
from config import MONDAY_API_KEY

API_URL = "https://api.monday.com/v2"

headers = {
    "Authorization": MONDAY_API_KEY,
    "Content-Type": "application/json"
}


def fetch_board_items(board_id):

    query = """
    query ($board_id: [ID!]) {
      boards(ids: $board_id) {
        items_page(limit: 500) {
          items {
            name
            column_values {
              text
              column {
                title
              }
            }
          }
        }
      }
    }
    """

    response = requests.post(
        API_URL,
        json={"query": query, "variables": {"board_id": board_id}},
        headers=headers
    )

    return response.json()
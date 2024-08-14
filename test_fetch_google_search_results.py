import config
from fetch_google_search_results import fetch_google_search_results

def test_fetch_google_search_results():
    # Call the function with values from config.py
    fetch_google_search_results(config.QUERY, config.NUM_RESULTS)

    # Check if the results file is created and contains results
    with open("new_search_results.txt") as file:
        results = file.readlines()


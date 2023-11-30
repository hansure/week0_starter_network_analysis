from src.loader import SlackDataLoader
import sys
import json
import pandas as pd
# from src.utils import clean_data, visualize_network

def main():
    # Check if the command-line argument is provided
    # if len(sys.argv) != 2:
    #     print("Usage: python analysis_script.py <data_path>")
    #     sys.exit(1)

    # # Get the data path from the command-line argument
    # data_path = sys.argv[1]

    # Use SlackDataLoader to load data
    data_loader = SlackDataLoader(path='./data')
    # Load data from a Slack channel
    slack_data = data_loader.get_users()
    df = pd.DataFrame(slack_data)
    top_10_user = data_loader.get_top_20_user(df)
    print(top_10_user)
    # Clean the loaded data
    # cleaned_data = clean_data(slack_data)

    # # Visualize the network
    # visualize_network(cleaned_data)

    # Perform EDA
    # ...

    # Rest of your analysis code

if __name__ == "__main__":
    main()


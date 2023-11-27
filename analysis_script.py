from src.loader import SlackDataLoader
from src.utils import clean_data, visualize_network

# Initialize SlackDataLoader
data_loader = SlackDataLoader()

# Load data from a Slack channel
slack_data = data_loader.get_channels("./data/channels.json")
# Clean the loaded data
cleaned_data = clean_data(slack_data)

# Visualize the network
visualize_network(cleaned_data)
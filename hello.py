import os
from mira import Mira

# Load environment variables
API_KEY = os.getenv("MIRA_API_KEY")

# Initialize Mira client
mira = Mira(api_key=API_KEY)

# Deploy the flow
flow = mira.load_flow("flow.yaml")

# Run the flow with an example input
input_data = {"india history": "easy": "5"}
response = flow.run(input_data)

print(f"AI Response: {response['response']}")

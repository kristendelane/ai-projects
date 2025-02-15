import requests

# Get random piece of advice from API
response = requests.get("https://api.adviceslip.com/advice")

# Check if the request was successful
if response.status_code == 200:
    advice = response.json()["slip"]["advice"]
    print(f"💡 AI Advice: {advice}")
else:
    print("❌ Could not get advice. Try again later.")

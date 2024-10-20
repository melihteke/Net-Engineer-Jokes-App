# Net-Engineer-Jokes-App
This Python script uses the Tweepy library to interact with the Twitter API and post network engineering jokes at regular intervals. The script fetches jokes and hashtags using the ask_ollama function and posts them to Twitter. It also logs its activities and errors.

![alt text](image.png)

## Features
- Fetches network engineering jokes and hashtags using the ask_ollama function.
- Posts the jokes and hashtags to Twitter.
- Logs activities and errors to both a file and the console.
- Runs indefinitely, posting a new joke every 30 minutes.

## Prerequisites
- Python 3.x
- Twitter Developer Account
- Tweepy library
- python-dotenv library
- Install Ollama (https://ollama.com/download/linux)
- Download llama3 model
```sh
ollama run llama3
```

## Installation
1. Clone the repository:

```sh
git clone https://github.com/yourusername/net-engineer-jokes-app.git
cd net-engineer-jokes-app
```

2. Create a virtual environment and activate it:
```sh
python3 -m venv .venv
source .venv/bin/activate
```

3. Install the required packages:
```sh
pip install -r requirements.txt
```

4. Create a .env file in the project directory and add your Twitter API credentials:
```sh
API_KEY=your_api_key
API_KEY_SECRET=your_api_key_secret
ACCESS_TOKEN=your_access_token
ACCESS_TOKEN_SECRET=your_access_token_secret
BEARER_TOKEN=your_bearer_token
```

Usage
- Ensure your .env file is correctly set up with your Twitter API credentials.
- Run the script

```sh
python main.py
```


The script will start running and will post a new network engineering joke to Twitter every 30 minutes.

## Logging
The script logs its activities and errors to both a file (app.log) and the console. This helps in monitoring the script's behavior and troubleshooting any issues.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

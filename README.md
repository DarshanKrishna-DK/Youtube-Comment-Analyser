# YouTube Comment Analyzer

This project uses VADER sentiment analysis, Python, and the YouTube Data API to analyze the sentiment of comments on YouTube videos.

## Features:
Classifies YouTube video comments as positive, negative, or neutral using VADER sentiment analysis.
Identifies the most positive and negative comments based on their sentiment scores.
Can be easily customized to analyze comments on specific channels or videos.

## Setting up YouTube Data API:
1. Create a new project in Google Cloud Platform (GCP) or use an existing one.
2. Enable the YouTube Data API v3 for your project:
   -> Go to the APIs & Services section in your GCP console.
   -> Search for "YouTube Data API v3" and enable it.
4. Create API credentials:
   -> After the enabling the API, click on CREATE CREDENTIALS, to get the API Key.
   -> Select the Public Data radio button, to have access to publicly available youtube data, and click NEXT.
  
(NOTE: After generating the API key, make sure you save the API key securely, as anyone with access to the API Key can use your account resources to access Youtube data; Click DONE after copying the API key.)

## Usage:
1. Clone this Repository: git clone https://github.com/DarshanKrishna-DK/Youtube-Comment-Analyser.git
2. Install required libraries:
   
   -> pip install emoji (The emoji package in Python allows us to use and print emoji)
   
   -> pip install vaderSentiment (The vaderSentiment package is a sentiment analysis tool)
   
   -> pip install google-api-python-client (The google-api-python-client is package used to interact with Google Services and APIs)
4. Put your API key as value for the API_KEY variable in the code.
5. Run the code.

## Customization:
1. You can modify the script to analyze comments on different channels or videos by giving different youtube video URLs.
2. You can also extend the script to perform additional analysis on the comments, such as extracting keywords or topics.

## Contributing:
I encourage contributions to this project! Please feel free to fork the repository and submit pull requests with your improvements or suggestions.

## License:
This project is licensed under the MIT License. See the LICENSE file for details.

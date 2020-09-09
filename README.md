# Reddit-r-wallstreetbets-DD-analyzer
r/wallstreetbets is a community on Reddit where participants discuss stock and option trading. It is known for its aggressive trading strategies, which primarily revolve around highly speculative, leveraged options trading. Members of the subreddit often ignore conventional investment practices and risk management techniques; the activity is often considered gambling. This project examines past DD or Due Dilligence posts which often contain a poster's opinion about about the future of a particular stock. It identifies the mentioned stock, overall sentiment of the stock then posts a graph detailing the post. In doing so, the project intends to discover a corrolation between DD posts and stock activity. 


wsbtickerbot is another project that also works with the r/wallstreetbets subreddit and was the inspiration for this project. wsbtickerbot analyzes the sentiment on stocks vs tracking stock performance overtime: https://github.com/RyanElliott10/wsbtickerbot

Requires:
Alpha Vantage API and account:https://www.alphavantage.co/documentation/
Rake_NTLK library:https://github.com/csurfer/rake-nltk
Vader Sentiment:https://github.com/RyanElliott10/wsbtickerbot/tree/master/vaderSentiment
MatplotLib:https://github.com/matplotlib/matplotlib
Reddit Praw API:https://praw.readthedocs.io/en/latest/

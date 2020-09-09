import praw
import alpaca_trade_api as tradeapi
import pprint
from rake_nltk import Rake
from parse_title import parse_title
from parse_title import false_positive
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt
import time


r = Rake()
analyzer = SentimentIntensityAnalyzer()
ts = TimeSeries(key='enter personal account', output_format='pandas')

reddit = praw.Reddit(client_id="enter personal account",
                     client_secret="enter personal account",
                     user_agent="my user agent")

print(reddit.read_only)
for submission in reddit.subreddit("wallstreetbets").search("flair:DD", time_filter='year'):
    title = submission.title
    title_list = parse_title(title)


    if(len(title_list) > 0): #checks if any stocks in list

        if(len(title_list) > 1): #checks if multiple stocks on list

            #gets scores of importance for title
            r.extract_keywords_from_text(title)
            ranked_list = r.get_ranked_phrases_with_scores()

            for x in range(0, len(ranked_list)): #loops through ntlk ranked list and parses
                current_phrase = ranked_list[x][1]
                current_phrase_parsed = current_phrase.split(" ")

                for y in range(0, len(current_phrase_parsed)): #loops through all words in a ranked ntlk phrase
                    for z in range(0, len(title_list)): #loops through all title_list(list of stocks mentions in title)
                        if (current_phrase_parsed[y].lower() == title_list[z]):  # checks if these phrases mention a stock
                            if (ranked_list[x][0] < 3.0):  # checks if mentioned stock is error (if word has low score and therfore not an actual stock mention)
                                title_list[z] = ""  # makes it blank

            false_positive(title_list)



        for x in range(0, len(title_list)):
            try:
                stock_tic = str(title_list[z])
                if (stock_tic != ""):
                    data, meta_data = ts.get_weekly(symbol=stock_tic)
                    data['4. close'].plot()
                    plt.title('Intraday Times Series for the ' + stock_tic + ' stock (1 min)')
                    plt.show()
                    continue
            except:
                print("error")
                pass

        print(title_list)
        ranked_phrases = []
        ranked_length = 0
        print(submission.title)

        submission_text = submission.selftext






        # mytext = submission.selftext
        # mytext = submission.title
        # print(submission.score)
        vs = analyzer.polarity_scores(submission_text)
        print(vs['compound'])


        # print("{:-<65} {}".format(submission_text, str(vs)))
        # ranked_length = len(ranked_phrases)
        # print(ranked_phrases)
        '''
        for x in range(0, ranked_length):
            if(ranked_phrases[x][0] > 4.0):
                print(ranked_phrases[x])
        #pprint.pprint(vars(submission))
        '''
        print("\n \n----------------------")

#ftp://ftp.nasdaqtrader.com/symboldirectory



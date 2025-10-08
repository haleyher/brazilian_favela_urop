import snscrape.modules.twitter as sntwitter
query = "enchente OR inundação OR flood Brazil since:2025-09-01"
tweets = [t.content for t in sntwitter.TwitterSearchScraper(query).get_items()]
print(tweets)
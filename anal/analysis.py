from nltk.sentiment.vader import SentimentIntensityAnalyzer


class Analysis:

    def __init__(self):
        self.sid = SentimentIntensityAnalyzer()

    def is_negative(self, input):
        comp = self.sid.polarity_scores(input)['compound']
        return float(comp) < 0.0




from textblob import TextBlob
import pandas as pd
import matplotlib.pyplot as plt

class TweetAnalyzer:
    def __init__(self):
        pass

    def analyze(self, text):
        analysis = TextBlob(text)
        polarity = analysis.sentiment.polarity
        
        if polarity > 0.1:
            return "positive", polarity
        elif polarity < -0.1:
            return "negative", polarity
        else:
            return "neutral", polarity

    def analyze_tweets(self, tweets):
        results = []
        for tweet in tweets:
            sentiment, score = self.analyze(tweet)
            results.append({
                "Tweet": tweet,
                "Sentiment": sentiment,
                "Score": score
            })
        return pd.DataFrame(results)

    def show_results(self, df):
        # Text Output
        print("\nAnalysis Results:")
        print(df.to_string(index=False))
        
        # Visual Output
        counts = df["Sentiment"].value_counts()
        plt.figure(figsize=(10,4))
        
        plt.subplot(1,2,1)
        counts.plot(kind="bar", color=["green","blue","red"])
        plt.title("Sentiment Distribution")
        
        plt.subplot(1,2,2)
        counts.plot(kind="pie", autopct="%1.1f%%", colors=["green","blue","red"])
        plt.title("Sentiment Proportion")
        
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    analyzer = TweetAnalyzer()
    
    sample_tweets = [
        "I love this new feature! Amazing work!",
        "The update ruined my experience. Terrible!",
        "It's okay, nothing special.",
        "The performance is fantastic!",
        "Worst customer service ever."
    ]
    
    print("Analyzing tweets...")
    results = analyzer.analyze_tweets(sample_tweets)
    analyzer.show_results(results)
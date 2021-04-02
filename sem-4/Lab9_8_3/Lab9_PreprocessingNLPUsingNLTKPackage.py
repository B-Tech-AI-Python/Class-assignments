# Import the necessary libraries
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from IPython.core.display import display, HTML
import nltk                                # Python library for NLP
from nltk.corpus import twitter_samples    # sample Twitter dataset from NLTK
# module for stop words that come with NLTK
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer        # module for stemming
from nltk.tokenize import TweetTokenizer   # module for tokenizing strings

import pandas as pd
import numpy as np
import random                              # pseudo-random number generator
import re                                  # library for regular expression operations
import string                              # for string operations
import matplotlib.pyplot as plt            # library for visualization
import seaborn as sns                      # library for visualization


# download sample twitter dataset
nltk.download('twitter_samples')

all_positive_tweets = twitter_samples.strings('positive_tweets.json')
all_negative_tweets = twitter_samples.strings('negative_tweets.json')


print('Number of positive tweets: ', len(all_positive_tweets))
print('Number of negative tweets: ', len(all_negative_tweets))

print('\nThe type of all_positive_tweets is: ', type(all_positive_tweets))
print('The type of a tweet entry is: ', type(all_negative_tweets))


fig = plt.figure(figsize=(6, 6))

# labels for the two classes
labels = 'Positive', 'Negative'

# Sizes for each slide
sizes = [len(all_positive_tweets), len(all_negative_tweets)]

# Declare pie chart, where the slices will be ordered and plotted counter-clockwise:
plt.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)

# Equal aspect ratio ensures that pie is drawn as a circle.
plt.axis('equal')

# Display the chart
plt.show()


# print a random tweet from positive and negative tweet
# positive in green, negative in red
print('\033[92m' + all_positive_tweets[random.randint(0, 5000)])
print('\033[91m' + all_negative_tweets[random.randint(0, 5000)])


# a complex sample is selected
tweet = all_positive_tweets[2277]
print(tweet)


print('\033[92m' + tweet)
print('\033[94m')

# remove old style retweet text "RT"
tweet = re.sub(r'^RT[\s]+', '', tweet)

# remove hyperlinks
tweet = re.sub(r'https?:\/\/.*[\r\n]*', '', tweet)

# remove hashtags
tweet = re.sub(r'#', '', tweet)

print(tweet)


print('\033[92m' + tweet)
print('\033[94m')

# instantiate tokenizer class
tokenizer = TweetTokenizer(preserve_case=False, strip_handles=True,
                           reduce_len=True)

# tokenize tweets
tweet_tokens = tokenizer.tokenize(tweet)

print()
print('Tokenized string:')
print(tweet_tokens)


# download the stopwords from NLTK
nltk.download('stopwords')


# import the english stop words list from NLTK
stopwords_english = stopwords.words('english')

print('Stop words\n')
print(stopwords_english)

print('\nPunctuation\n')
print(string.punctuation)


print('\033[92m')
print(tweet_tokens)
print('\033[94m')

tweets_clean = []

# Remove stopwords and punctuation from the tweet_tokens
for word in tweet_tokens:  # Go through every word in your tokens list
    if (word not in stopwords_english and  # remove stopwords
            word not in string.punctuation):  # remove punctuation

        # Append the clean word in the tweets_clean list
        tweets_clean.append(word)

print('removed stop words and punctuation:')
print(tweets_clean)


print('\033[92m')
print(tweets_clean)
print('\033[94m')

# Instantiate stemming class
stemmer = PorterStemmer()

tweets_stem = []

for word in tweets_clean:
    stem_word = stemmer.stem(word)
    tweets_stem.append(stem_word)

print('stemmed words:')
print(tweets_stem)


def process_tweet(tweet):
    """Process tweet function.
    Args:
        tweet: a string containing a tweet.
    Returns:
        tweets_clean: a list of words containing the processed tweet.

    """
    stemmer = PorterStemmer()

    stopwords_english = stopwords.words('english')
    # remove stock market tickers like $GE
    tweet = re.sub(r'\$\w*', '', tweet)
    # remove old style retweet text "RT"
    tweet = re.sub(r'^RT[\s]+', '', tweet)
    # remove hyperlinks
    tweet = re.sub(r'https?:\/\/.*[\r\n]*', '', tweet)
    # remove hashtags
    tweet = re.sub(r'#', '', tweet)

    # tokenize tweets
    tokenizer = TweetTokenizer(preserve_case=False, strip_handles=True,
                               reduce_len=True)
    tweet_tokens = tokenizer.tokenize(tweet)

    tweets_clean = []
    for word in tweet_tokens:
        if (word not in stopwords_english and  # remove stopwords
                word not in string.punctuation):  # remove punctuation
            # tweets_clean.append(word)
            stem_word = stemmer.stem(word)  # stemming word
            tweets_clean.append(stem_word)

    return tweets_clean


# choose the same tweet
tweet = all_positive_tweets[2277]

print()
print('\033[92m')
print(tweet)
print('\033[94m')

tweets_stem = process_tweet(tweet)

print('preprocessed tweet:')
print(tweets_stem)  # Print the result


tweets = all_positive_tweets + all_negative_tweets
print("Number of tweets: ", len(tweets))


labels = np.append(np.ones((len(all_positive_tweets))),
                   np.zeros((len(all_negative_tweets))))
labels


def build_freqs(tweets, ys):
    """Build a word frequency dictionary.
    Args:
        tweets: a list of tweets.
        ys: an m x 1 array with the sentiment label of each tweet (either 0 or 1).
    Returns:
        pos_freqs: a dictionary mapping each word with positive sentiment to its frequency.
        neg_freqs: a dictionary mapping each word with negative sentiment to its frequency.
    """
    yslist = np.squeeze(ys).tolist()

    pos_freqs = {}
    neg_freqs = {}
    for y, tweet in zip(yslist, tweets):
        for word in process_tweet(tweet):
            if word in pos_freqs and y == 1:
                pos_freqs[word] += 1

            elif word in neg_freqs and y == 0:
                neg_freqs[word] += 1

            else:
                if y == 1:
                    pos_freqs[word] = 1
                elif y == 0:
                    neg_freqs[word] = 1

    return pos_freqs, neg_freqs


pos_freqs, neg_freqs = build_freqs(tweets, labels)

print(f'types = {type(pos_freqs)}, {type(neg_freqs)}')

print(f'lengths = {len(pos_freqs)}, {len(neg_freqs)}')


def display_side_by_side(dfs: list, captions: list):
    """Display pandas tables side by side.
    Args:
        dfs: list of pandas.DataFrame
    """
    output = ""
    combined = dict(zip(captions, dfs))
    for caption, df in combined.items():
        output += df.style.set_table_attributes(
            "style='display:inline'").set_caption(caption)._repr_html_()
        output += "\xa0\xa0\xa0"
    display(HTML(output))


freq_df = pd.DataFrame.from_dict({'positive_frequency': pos_freqs,
                                  'negative_frequency': neg_freqs})

top5_pos = freq_df.sort_values('positive_frequency', ascending=False).head(5)
top5_neg = freq_df.sort_values('negative_frequency', ascending=False).head(5)

display_side_by_side([top5_pos, top5_neg], ['top5_pos', 'top5_neg'])


# select some words to appear in the report
keys = [':)', ':-)', ':D', 'thank', 'love', ':(', ':-(', 'i\'m',
        '...', 'miss', 'happi', 'merri', 'nice', 'good', 'bad',
        'sad', 'mad', 'best', 'pretti', '❤', '😒', '😬', '😄',
        '😍', '♛', 'song', 'idea', 'power', 'play', 'magnific']

data = []

for word in keys:
    pos = 0
    neg = 0

    # retrieve number of positive counts
    if word in pos_freqs:
        pos = pos_freqs[word]

    # retrieve number of negative counts
    if word in neg_freqs:
        neg = neg_freqs[word]

    # append the word counts to the table
    data.append([word, pos, neg])

data


fig, ax = plt.subplots(figsize=(8, 8))

# convert positive raw counts to logarithmic scale. we add 1 to avoid log(0)
x = np.log([x[1] + 1 for x in data])

# do the same for the negative counts
y = np.log([x[2] + 1 for x in data])

# Plot a dot for each pair of words
ax.scatter(x, y)

# assign axis labels
plt.xlabel("Log Positive count")
plt.ylabel("Log Negative count")

# Add the word as the label at the same position as you added the points just before
for i in range(0, len(data)):
    ax.annotate(data[i][0], (x[i], y[i]), fontsize=12)

# Plot the red line that divides the 2 areas.
ax.plot([0, 9], [0, 9], color='red')
plt.show()


X = tweets
y = labels
print('Number of tweets:', len(tweets))


vectorizer = CountVectorizer(
    analyzer='word',
    lowercase=False,
)

features = vectorizer.fit_transform(
    tweets
)

features_nd = features.toarray()  # for easy usage


X_train, X_test, y_train, y_test = train_test_split(
    features_nd, y, test_size=0.2, random_state=30)


print('Number of training tweets:', len(X_train))
print('Number of testing tweets:', len(X_test))


clf = LogisticRegression(solver='lbfgs').fit(X_train, y_train)


y_pred = clf.predict(X_test)


print('CLASSIFICATION REPORT\n', classification_report(y_test, y_pred))


print('\nCONFUSION MATRIX\n')
sns.heatmap(confusion_matrix(y_test, y_pred), annot=True)


print('ACCURACY SCORE:', accuracy_score(y_test, y_pred))


pd.DataFrame({'True values': y_test, 'Predicted values': y_pred})

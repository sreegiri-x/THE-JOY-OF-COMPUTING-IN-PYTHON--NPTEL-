

# The Joy of Computing using Python
## Unit 12 - Week 9: Assignment 9

### Background
A political science research team is examining the Federalist Papers, a historically significant collection of essays written to support the ratification of the U.S. Constitution. While many essays are clearly attributed to Hamilton, Madison, or Jay, a subset of essays has disputed or shared authorship. Instead of relying on historical arguments alone, the team decides to use computational text analysis to study writing patterns across different author groups.

### Problem Statement
The team wants to understand whether quantitative textual characteristics, such as word usage patterns and sentiment, can help differentiate between authors and provide insights into disputed essays. The task is not to assign authorship directly, but to compare:
* Writing style indicators
* Distributional properties of words
* Emotional tone across author groups

### Dataset Description
The dataset is organized by author category:
* Hamilton
* Madison
* Jay
* Disputed
* Shared

Each category contains a block of text representing essays attributed to that group. These texts are treated as independent corpora.

### Analytical Approach
The analysis follows four major stages:

1.  **Text Preprocessing**: Each author's text is processed to extract meaningful words by tokenizing text, removing punctuation/non-alphabetic tokens, and eliminating common English stopwords.
2.  **Stylometric Analysis Using Word Length**: For every author group, the length of each word is computed and a frequency distribution is constructed. Word length is treated as a stylistic signature.
3.  **Sentiment Analysis**: Each author's entire text is analyzed using a sentiment model to compute a polarity score.
4.  **Visual Comparison**: Word-length frequency distributions are plotted for all authors on the same figure to identify overlaps and stylistic similarities.

### Code Snippet
```python
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
import matplotlib.pyplot as plt
from textblob import TextBlob

authors = ["Hamilton", "Madison", "Disputed", "Jay", "Shared"]
federalist_by_author = {
    "Hamilton": "Text data for Hamilton...",
    "Madison": "Text data for Madison...",
    "Disputed": "Text data for Disputed...",
    "Jay": "Text data for Jay...",
    "Shared": "Text data for Shared..."
}

author_tokens = {}
for author, text_data in federalist_by_author.items():
    tokens = [
        word for word in word_tokenize(text_data)
        if word.isalpha() and word.lower() not in stopwords.words("english")
    ]
    author_tokens[author] = tokens

author_word_lengths = {}
for author, tokens in author_tokens.items():
    word_lengths = [len(word) for word in tokens]
    author_word_lengths[author] = word_lengths

sentiment_scores = {}
for author, text_data in federalist_by_author.items():
    blob = TextBlob(text_data)
    sentiment_scores[author] = blob.sentiment.polarity

plt.figure(figsize=(12, 6))
for author in authors:
    fdist = FreqDist(author_word_lengths[author])
    fdist.plot(15, cumulative=False)
plt.legend(authors)
plt.show()

for author, sentiment in sentiment_scores.items():
    print(f"Sentiment analysis for {author}: Sentiment Score {sentiment}")
```

### Quiz Questions

**1) Assume the text for Hamilton contains only the words: "Liberty liberty the Constitution"** **After preprocessing, what will be stored in author_tokens["Hamilton"]?**
- ["Liberty", "liberty", "the", "Constitution"]
- ["liberty", "liberty", "constitution"]
- ["Liberty", "Constitution"]
- ["Liberty", "liberty", "Constitution"]

**Answer:** ["Liberty", "liberty", "Constitution"]

**2) If an author's text contains only stopwords, what happens when plotting their word-length distribution?**
- The program raises a runtime error
- An empty plot is generated without bars
- All word lengths are plotted as zero
- The author is skipped automatically

**Answer:** An empty plot is generated without bars

**3) Which author property is directly visualized in the plotted graphs?**
- Sentiment polarity
- Token frequency
- Word-length frequency
- Vocabulary richness

**Answer:** Word-length frequency

**4) If the Disputed corpus contains significantly longer average words than others, how would this most likely appear in the plot?**
- Higher bars at smaller word lengths
- A wider spread with peaks at larger word lengths
- A flat distribution across all lengths
- No visible difference from other authors

**Answer:** A wider spread with peaks at larger word lengths

**5) Suppose TextBlob returns a sentiment polarity of 0.0 for Jay. What does this imply?**
- Jay's text is emotionally neutral overall
- Jay uses no adjectives
- Jay's text contains no positive words
- Jay's text failed sentiment analysis

**Answer:** Jay's text is emotionally neutral overall

**6) If the stopword filter were removed from preprocessing, which change would MOST likely occur?**
- Sentiment scores become negative
- Word-length distributions shift toward shorter lengths
- Vocabulary size decreases
- Alphabetic filtering stops working

**Answer:** Word-length distributions shift toward shorter lengths

**7) Why is sentiment analysis performed on the entire text rather than token-level sentiment?**
- TextBlob does not support token sentiment
- Corpus-level sentiment smooths local noise
- Token sentiment would always be zero
- Tokens are removed before sentiment analysis

**Answer:** Corpus-level sentiment smooths local noise

**8) If the Shared corpus was written by multiple authors, what pattern would MOST likely appear?**
- A sharply peaked word-length distribution
- Identical sentiment to all authors
- A broader, less consistent distribution
- No visible plot

**Answer:** A broader, less consistent distribution

---

## Exploring Social Networks Using Shortest Paths

### Background
A data analyst is interested in understanding how people are connected within a large online social network. Each user is modeled as a node, and each friendship is modeled as an edge in an undirected graph. The analyst chooses **NetworkX** to verify the **Six Degrees of Separation** theory.

### Code Snippet
```python
import networkx as nx

G = nx.read_edgelist("facebook_combined.txt")
N = list(G.nodes())

shortest_path_length_list = []
for u in N:
    for v in N:
        if u != v:
            l = nx.shortest_path_length(G, source=u, target=v)
            shortest_path_length_list.append(l)

min_shortest_path = min(shortest_path_length_list)
max_shortest_path = max(shortest_path_length_list)
avg_shortest_path = sum(shortest_path_length_list) / len(shortest_path_length_list)
```

### Quiz Questions

**9) What is the primary purpose of using nx.read_edgelist("facebook_combined.txt") in the case study?**
- To create a graph where users are nodes and friendships are edges
- To calculate shortest paths directly from the file
- To store shortest path lengths in a list
- To visualize the social network

**Answer:** To create a graph where users are nodes and friendships are edges

**10) Why does the code check if u != v before computing the shortest path?**
- To prevent duplicate edges in the graph
- To avoid self-loops that always have zero path length
- To reduce memory usage
- To ensure the graph remains undirected

**Answer:** To avoid self-loops that always have zero path length

**11) What does the list shortest_path_length_list primarily represent?**
- The degree of each node
- The number of friends per user
- All shortest path lengths between distinct pairs of nodes
- Only the longest path in the network

**Answer:** All shortest path lengths between distinct pairs of nodes

**12) Which metric from the code is most relevant for validating the Six Degrees of Separation concept?**
- Minimum shortest path length
- Maximum shortest path length
- Number of nodes in the graph
- Average shortest path length

**Answer:** Average shortest path length

**13) If the network is fully connected, what would most likely happen to the maximum shortest path length?**
- It would increase significantly
- It would become zero
- It would remain relatively small
- It would become equal to the number of nodes

**Answer:** It would remain relatively small

**14) Why does the case study mention exponential growth in connections?**
- Because shortest path lengths grow exponentially
- Because the number of nodes doubles each iteration
- Because friend-of-friend connections expand rapidly with each step
- Because NetworkX uses exponential algorithms internally

**Answer:** Because friend-of-friend connections expand rapidly with each step

**15) What is a computational limitation of the approach used in the code?**
- It cannot handle undirected graphs
- It only works for weighted graphs
- It ignores isolated nodes
- It computes shortest paths for every node pair, which is expensive

**Answer:** It computes shortest paths for every node pair, which is expensive

---

# The Joy of Computing using Python
## Unit 4 - Week 1: Assignment 1

### Section 1: Rohan and Robo
Rohan is learning how to build simple games using the Scratch editor. He creates a sprite named Robo. He uses two variables: `counter` and `score`.

**1) What will be the final value of counter after the program finishes execution?**
- 8
- 5
- 3
- 10

**Answer:** 8

**2) What will be the value of score after the first repeat loop ends?**
- 20
- 24
- 40
- 44

**Answer:** 40

**3) What is the final value of score that the sprite will say?**
- 22
- 28
- 34
- 40

**Answer:** 22

**4) How many times in total is the change counter by 1 block executed?**
- 3
- 5
- 6
- 8

**Answer:** 8

**5) Which statement is TRUE about the execution of this Scratch program?**
- The value of score is reset before the second loop
- The second loop runs before the first loop
- The sprite says the value of score only once
- The variable counter is updated only in one loop

**Answer:** The sprite says the value of score only once

### Section 2: Arjun and Runner
Arjun creates a game with three variables: `score`, `counter`, and `bonus`.

**6) What will be the final value of counter after the program finishes execution?**
- 5
- 6
- 8
- 12

**Answer:** 6

**7) What will be the value of score immediately after the repeat loop ends (before adding bonus)?**
- 30
- 36
- 42
- 54

**Answer:** 42

**8) What will be the final value of bonus after the loop completes?**
- 6
- 9
- 12
- 15

**Answer:** 12

**9) What is the final value of score after the bonus is added?**
- 42
- 48
- 50
- 54

**Answer:** 54

**10) What message will the sprite display at the end of the program?**
- Excellent!
- Level Cleared!
- Try Again!
- No message

**Answer:** Excellent!

### Section 3: Kabir's Battery Simulation
Kabir simulates battery consumption using variables `battery` and `cycles`.

**11) What will be the final value of battery when the loop stops?**
- 18
- 14
- 10
- 6

**Answer:** 10

**12) How many times does the repeat until loop execute?**
- 4
- 5
- 6
- 7

**Answer:** 5

**13) What will be the final value of cycles after the program finishes?**
- 5
- 4
- 6
- 8

**Answer:** 5

**14) Which statement about the repeat until block is TRUE in Scratch?**
- The loop always runs at least once
- The loop checks the condition after executing the body
- The loop behaves exactly like repeat n times
- The loop stops immediately if the condition is already true

**Answer:** The loop stops immediately if the condition is already true

**15) What message will the sprite display at the end of the program?**
- Battery Low
- System Shutdown
- Recharge Needed
- No message

**Answer:** Recharge Needed


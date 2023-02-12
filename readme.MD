# Shark Stats


Playing with a small dataset of shark incidents in Australia, using Pandas, Python and Flask. The graphs are made with matplotlib.

When drawing the graphs, the Activities inputs were quite dirty, so I had two options to sort them out:

- The first one was to try out the Levenshtein Distance metric to find similitudes between the 'Activities' entries. I implemented a solution with  TheFuzz (formerly FuzzyWuzzy) library [https://github.com/seatgeet/thefuzz](https://github.com/seatgeet/thefuzz), but it did not yield promising results as the data is quite varied.

- The second option was to create a dictionary and do an agregate search of significative subsets of the most frequent activities. It is a very rigid approach that is time consuming but much more accurate


Graphs have a minimal tweaking to make them readable, but just as the whole page, nothing has been made 'pretty'.

As they are not dynamic, running the file graph_gen.py would regenerate and save them to .png format for html display.


## Database
Taken from [https://www.kaggle.com/datasets/kabhishm/fatal-shark-attacks-in-australia](
https://www.kaggle.com/datasets/kabhishm/fatal-shark-attacks-in-australia)
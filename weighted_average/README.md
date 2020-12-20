# Weighted Average

`classify.py` performs the weighted average classification based on the output of the ratingCollection.py script. This file loops through the
organized hierarchy of the test data and collects every size track ids. The score for each track is then calculated by performing a weighted average
on the track's attributes, such as the user's scores for its album, artist, and genres. To handle multiple genres, the average was taken of all the ratings
for the track's corresponding genres. Once the scores were calculated the top three in the group were assigned ones and the bottom three were assigned zeros
this is repeated for all the test tracks. The weights of each attribute can be varied to give different attributes more or less importance and
test for different results.

`ratingCollection.py` this script reads the test track files and organizes them into a usable hierarchy for the classify.py file. Each line of the 
resulting file will resemble this format. userID | trackId | albumRating | artistRating | genre1Rating | genre2Rating | genre(N)Rating.

`userSuggestions.csv` this is the output submission file of the classify.py script. This file is uploaded to Kaggle to view the performance of the method.

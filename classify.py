import numpy as np

dataDir='./data/'
file_name_ratings=dataDir + 'output1.txt'
ratings = open(file_name_ratings, 'r')

with open('userSuggestions.csv','w') as f:
    row = 'TrackID,Predictor\n'
    f.write(row)

trackID_vec=[0]*6
albumRate_vec=[0]*6
artistRate_vec=[0]*6
genreRate_vec=[0]*6
lastUserID=-1


for line in ratings:
    arr_rating=line.strip().split('|')
    userID= arr_rating[0]
    trackID= arr_rating[1]
    arr_rating = list(map(float, arr_rating))
    albumRate= arr_rating[2]
    artistRate=arr_rating[3]
    genreRate = 0
    if len(arr_rating) > 4:
        genreRate = np.mean(arr_rating[4:])

    if userID != lastUserID:
        ii=0

    trackID_vec[ii]=trackID
    albumRate_vec[ii]=albumRate
    artistRate_vec[ii]=artistRate
    genreRate_vec[ii] = genreRate
    
    ii=ii+1
    lastUserID=userID
    
    if ii == 6:
        total_ratings = {}
        for nn in range(0, 6):
            total_ratings[trackID_vec[nn]] = albumRate_vec[nn] * 0.5  + artistRate_vec[nn] * 0.35 + genreRate_vec[nn] * 0.15

        total_ratings_sorted = total_ratings.copy()
        total_ratings_sorted = {k: v for k, v in sorted(total_ratings.items(), key=lambda item: item[1], reverse=True)}

        # print(list(total_ratings.keys())[0])
        # print(list(total_ratings.values()))
        # print(np.unique(list(total_ratings.values())))
        
        suggest = [0,0,0,1,1,1]
        for key in total_ratings_sorted.keys():
            total_ratings[key] = suggest.pop()
        
        with open('userSuggestions.csv','a') as f:
            for item_id, value in total_ratings.items():
                row = f'{userID}_{item_id},{value}\n'
                f.write(row)
        
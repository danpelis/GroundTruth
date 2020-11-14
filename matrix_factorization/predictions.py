import numpy as np
import pandas as pd


dataDir='./data/'
file_name_ratings=dataDir + 'testItem.data'
ratings = open(file_name_ratings, 'r')
preds = pd.read_csv(dataDir + 'preds.csv')
out_file = dataDir + 'submission.csv'

with open(out_file,'w') as f:
    row = 'TrackID,Predictor\n'
    f.write(row)

index = 0
while ratings:
    # grab first six rows in df
    user_preds_user_id = preds.iloc[index,0]
    user_preds = []
    for x in range(6):
        if(preds.iloc[index,0] == user_preds_user_id):
            user_preds.append(preds.iloc[index])
            index += 1
    # user_preds = preds[index:index+6]
    

    # Load user rows into their own data frame with extra col intialized at 0
    user_df = pd.DataFrame(data=user_preds)
    user_df['_4'] = 0
    
    # Sort user df by rank and assign top three with ones
    i = 0
    for i in range(len(user_df['_1'])):
        if i < 3:
            user_df.iloc[i,3] = 1

    user_id = int(user_df.iloc[0,0])

    lines = []
    while len(lines) < 6:
        line = ratings.readline()
        data = line.strip().split(',')
        if str(user_id) == str(data[0]):
            lines.append(data)

    with open(out_file,'a') as f:
        for line in lines:
            userId = line[0]
            item_id = line[1]
            df_row = user_df.loc[user_df['_2'] == int(item_id)]
            try:
                value = df_row['_4'].values[0]
                row = f'{userId}_{item_id},{value}\n'
            except:
                row = f'{userId}_{item_id},0\n'
            f.write(row)

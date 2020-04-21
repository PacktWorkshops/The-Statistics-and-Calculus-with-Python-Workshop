import pandas as pd
import numpy as np

games = pd.read_csv('../data/appstore_games.csv')

original_colums_dict = {x: x.lower().replace(' ','_') for x in games.columns}

games.rename(
    columns = original_colums_dict,
    inplace = True
)

games.set_index(
    keys = 'id',
    inplace = True
)

games.drop(
    columns = ['url', 'icon_url'],
    inplace = True
)

games['original_release_date'] = pd.to_datetime(games['original_release_date'])
games['current_version_release_date'] = pd.to_datetime(games['current_version_release_date'])

games = games.loc[games['average_user_rating'].notnull()]

games = games.loc[games['user_rating_count'] >= 30]

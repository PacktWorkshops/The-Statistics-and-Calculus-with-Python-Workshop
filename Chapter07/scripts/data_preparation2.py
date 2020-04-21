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

# These comes from section 7.3
games['size'] = games['size']/1e6

ratings_mapping = {
    1.5: '1_poor',
    2.: '1_poor',
    2.5: '1_poor',
    3.: '1_poor',
    3.5: '2_fair',
    4. : '2_fair',
    4.5: '3_good',
    5. : '4_excellent'
}

games['cat_rating'] = games['average_user_rating'].map(ratings_mapping)
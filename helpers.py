# Function that aggregates the data and creates a single line per combination of GameId and PlayId
def aggregation_func(nfl_df, df):

    # Final dataframe component 1
    '''
    This part contains the code to reduce the nfl_df dataframe to a dataframe that contains only one row per GameId-PlayId record
    Only the columns that have the same values for all rows for a given GameId-PlayId, i.e. the same values for all 22 rows of a given play, are kept in this step
    '''
    
    nfl_df_final = df.drop_duplicates(subset = ['GameId', 'PlayId'], inplace = False)
    nfl_df_final = nfl_df_final[['GameId', 'PlayId', 'Season', 'YardLine', 'Quarter', 'GameClock', 
                                 'PossessionTeam', 'Down', 'Distance', 'FieldPosition', 'HomeScoreBeforePlay', 'VisitorScoreBeforePlay', 
                                 'OffenseFormation', 'OffensePersonnel', 'DefendersInTheBox', 'DefensePersonnel', 'PlayDirection', 'TimeHandoff', 
                                 'TimeSnap', 'HomeTeamAbbr', 'VisitorTeamAbbr', 'Week', 'Stadium', 'Location', 
                                 'StadiumType', 'Turf', 'GameWeather', 'Temperature', 'Humidity', 'WindSpeed', 
                                 'WindDirection', 'NflIdRusher', 'Yards']]
    
    
    # Final dataframe component 2
    '''
    This section of the function adds on the additional columns, for example average player weight split by attacking and defending team
    '''
    
    # Loop through each row in the nfl_df_final dataframe and add the additional columns
    for index, row in nfl_df_final.iterrows():
    
        # OffenseTeam
        if nfl_df_final.loc[index,'PossessionTeam'] == nfl_df_final.loc[index,'HomeTeamAbbr']:
            nfl_df_final.loc[index,'OffenseTeam'] = 'home'
        else:
            nfl_df_final.loc[index,'OffenseTeam'] = 'away'

    
        '''
        Home team calculations
        '''
        home_df = nfl_df[(nfl_df['GameId'] == nfl_df_final.loc[index, 'GameId']) & (nfl_df['PlayId'] == nfl_df_final.loc[index, 'PlayId']) & (nfl_df['Team'] == 'home')]
        # X
        X_home = home_df['X'].mean()
        # Y
        Y_home = home_df['Y'].mean()
        # S
        S_home = home_df['S'].mean()
        # A
        A_home = home_df['A'].mean()
        # Dis
        Dis_home = home_df['Dis'].mean()
        # Orientation
        Orientation_home = home_df['Orientation'].mean()
        # Dir
        Dir_home = home_df['Dir'].mean()
        # NflId
        home_df_qb = nfl_df[(nfl_df['GameId'] == nfl_df_final.loc[index, 'GameId']) & (nfl_df['Team'] == 'home') & (nfl_df['Position'] == 'QB')]
        NflId_home = home_df_qb['NflId'].values[0]
        # DisplayName
        DisplayName_home = home_df_qb['DisplayName'].values[0]
        # JerseyNumber
        JerseyNumber_home = home_df['JerseyNumber'].mean()
        # PlayerHeight
        PlayerHeight_home = home_df['PlayerHeight'].mode().values[0]
        # PlayerWeight
        PlayerWeight_home = home_df['PlayerWeight'].mean()
        # PlayerAge
        PlayerAge_home = home_df['PlayerAge'].mean()
        # PlayerCollegeName
        PlayerCollegeName_home = home_df['PlayerCollegeName'].mode().values[0]
        # Position
        Position_home = home_df['Position'].mode().values[0]
        
        ###############################################################################################
        '''
        Away team calculations
        '''
        away_df = nfl_df[(nfl_df['GameId'] == nfl_df_final.loc[index, 'GameId']) & (nfl_df['PlayId'] == nfl_df_final.loc[index, 'PlayId']) & (nfl_df['Team'] == 'away')]
        # X
        X_away = away_df['X'].mean()
        # Y
        Y_away = away_df['Y'].mean()
        # S
        S_away = away_df['S'].mean()
        # A
        A_away = away_df['A'].mean()
        # Dis
        Dis_away = away_df['Dis'].mean()
        # Orientation
        Orientation_away = away_df['Orientation'].mean()
        # Dir
        Dir_away = away_df['Dir'].mean()
        # NflId
        away_df_qb = nfl_df[(nfl_df['GameId'] == nfl_df_final.loc[index, 'GameId']) & (nfl_df['Team'] == 'away') & (nfl_df['Position'] == 'QB')]
        NflId_away = away_df_qb['NflId'].values[0]
        # DisplayName
        DisplayName_away = away_df_qb['DisplayName'].values[0]
        # JerseyNumber
        JerseyNumber_away = away_df['JerseyNumber'].mean()
        # PlayerHeight
        PlayerHeight_away = away_df['PlayerHeight'].mode().values[0]
        # PlayerWeight
        PlayerWeight_away = away_df['PlayerWeight'].mean()
        # PlayerAge
        PlayerAge_away = away_df['PlayerAge'].mean()
        # PlayerCollegeName
        PlayerCollegeName_away = away_df['PlayerCollegeName'].mode().values[0]
        # Position
        Position_away = away_df['Position'].mode().values[0]
        
        
        # Inserting the values into the reduced dataframe (where we have one line per play)
        # if home team is on offense
        if nfl_df_final.loc[index, 'OffenseTeam'] == 'home':
            # X
            nfl_df_final.loc[index, 'X_off'] = X_home
            nfl_df_final.loc[index, 'X_def'] = X_away
            
            # Y
            nfl_df_final.loc[index, 'Y_off'] = Y_home
            nfl_df_final.loc[index, 'Y_def'] = Y_away
            
            # S
            nfl_df_final.loc[index, 'S_off'] = S_home
            nfl_df_final.loc[index, 'S_def'] = S_away
            
            # A
            nfl_df_final.loc[index, 'A_off'] = A_home
            nfl_df_final.loc[index, 'A_def'] = A_away
            
            # Dis
            nfl_df_final.loc[index, 'Dis_off'] = Dis_home
            nfl_df_final.loc[index, 'Dis_def'] = Dis_away
            
            # Orientation
            nfl_df_final.loc[index, 'Orientation_off'] = Orientation_home
            nfl_df_final.loc[index, 'Orientation_def'] = Orientation_away

            # Dir
            nfl_df_final.loc[index, 'Dir_off'] = Dir_home
            nfl_df_final.loc[index, 'Dir_def'] = Dir_away

            # NflId
            nfl_df_final.loc[index, 'NflId_off'] = NflId_home
            nfl_df_final.loc[index, 'NflId_def'] = NflId_away

            # DisplayName
            nfl_df_final.loc[index, 'DisplayName_off'] = DisplayName_home
            nfl_df_final.loc[index, 'DisplayName_def'] = DisplayName_away
            
            # JerseyNumber
            nfl_df_final.loc[index, 'JerseyNumber_off'] = JerseyNumber_home
            nfl_df_final.loc[index, 'JerseyNumber_def'] = JerseyNumber_away

            # PlayerHeight
            nfl_df_final.loc[index, 'PlayerHeight_off'] = PlayerHeight_home
            nfl_df_final.loc[index, 'PlayerHeight_def'] = PlayerHeight_away
            
            # PlayerWeight
            nfl_df_final.loc[index, 'PlayerWeight_off'] = PlayerWeight_home
            nfl_df_final.loc[index, 'PlayerWeight_def'] = PlayerWeight_away
            
            # PlayerAge
            nfl_df_final.loc[index, 'PlayerAge_off'] = PlayerAge_home
            nfl_df_final.loc[index, 'PlayerAge_def'] = PlayerAge_away
            
            # PlayerCollegeName
            nfl_df_final.loc[index, 'PlayerCollegeName_off'] = PlayerCollegeName_home
            nfl_df_final.loc[index, 'PlayerCollegeName_def'] = PlayerCollegeName_away
            
            # Position
            nfl_df_final.loc[index, 'Position_off'] = Position_home
            nfl_df_final.loc[index, 'Position_def'] = Position_away
            
        # if away team is on offense
        else:
            # X
            nfl_df_final.loc[index, 'X_off'] = X_away
            nfl_df_final.loc[index, 'X_def'] = X_home
            
            # Y
            nfl_df_final.loc[index, 'Y_off'] = Y_away
            nfl_df_final.loc[index, 'Y_def'] = Y_home
            
            # S
            nfl_df_final.loc[index, 'S_off'] = S_away
            nfl_df_final.loc[index, 'S_def'] = S_home
            
            # A
            nfl_df_final.loc[index, 'A_off'] = A_away
            nfl_df_final.loc[index, 'A_def'] = A_home
            
            # Dis
            nfl_df_final.loc[index, 'Dis_off'] = Dis_away
            nfl_df_final.loc[index, 'Dis_def'] = Dis_home
            
            # Orientation
            nfl_df_final.loc[index, 'Orientation_off'] = Orientation_away
            nfl_df_final.loc[index, 'Orientation_def'] = Orientation_home
            
            # Dir
            nfl_df_final.loc[index, 'Dir_off'] = Dir_away
            nfl_df_final.loc[index, 'Dir_def'] = Dir_home

            # NflId
            nfl_df_final.loc[index, 'NflId_off'] = NflId_away
            nfl_df_final.loc[index, 'NflId_def'] = NflId_home

            # DisplayName
            nfl_df_final.loc[index, 'DisplayName_off'] = DisplayName_away
            nfl_df_final.loc[index, 'DisplayName_def'] = DisplayName_home
            
            # JerseyNumber
            nfl_df_final.loc[index, 'JerseyNumber_off'] = JerseyNumber_away
            nfl_df_final.loc[index, 'JerseyNumber_def'] = JerseyNumber_home

            # PlayerHeight
            nfl_df_final.loc[index, 'PlayerHeight_off'] = PlayerHeight_away
            nfl_df_final.loc[index, 'PlayerHeight_def'] = PlayerHeight_home
            
            # PlayerWeight
            nfl_df_final.loc[index, 'PlayerWeight_off'] = PlayerWeight_away
            nfl_df_final.loc[index, 'PlayerWeight_def'] = PlayerWeight_home
            
            # PlayerAge
            nfl_df_final.loc[index, 'PlayerAge_off'] = PlayerAge_away
            nfl_df_final.loc[index, 'PlayerAge_def'] = PlayerAge_home
            
            # PlayerCollegeName
            nfl_df_final.loc[index, 'PlayerCollegeName_off'] = PlayerCollegeName_away
            nfl_df_final.loc[index, 'PlayerCollegeName_def'] = PlayerCollegeName_home
            
            # Position
            nfl_df_final.loc[index, 'Position_off'] = Position_away
            nfl_df_final.loc[index, 'Position_def'] = Position_home
            
    return nfl_df_final
##########################################################################################################################################################

##########################################################################################################################################################
# Function to replace rows in the provided column of the provided dataframe that match the provided string
# We set a threshold for above which the dataframe entry will be replaced by the target string

# helpful modules
import fuzzywuzzy
from fuzzywuzzy import process
import chardet
import numpy as np

# set seed for reproducibility
np.random.seed(0)
def replace_matches_in_column(df, column, string_to_match, min_ratio):
   
    # get a list of unique strings
    strings = df[column].unique()
    
    # get the top 10 closest matches to our input string
    matches = fuzzywuzzy.process.extract(string_to_match, strings, 
                                         limit=10, scorer=fuzzywuzzy.fuzz.token_sort_ratio)

    # only get matches with a ratio > 90
    close_matches = [matches[0] for matches in matches if matches[1] >= min_ratio]

    # get the rows of all the close matches in our dataframe
    rows_with_matches = df[column].isin(close_matches)

    # replace all rows with close matches with the input matches 
    df.loc[rows_with_matches, column] = string_to_match
    
    # let us know the function's done
    print("Text preprocessing complete.")
##########################################################################################################################################################
    
##########################################################################################################################################################
# Function that calculates the pairwise correlations and adds the columns to the list of correlated features if the correlation exceeds a threshold
# This list can be used to decide which features to omit from the dataset that will be used going forward
def correlation(dataset, threshold):
    col_corr = set() # Set of all the names of deleted columns
    corr_matrix = dataset.corr()
    for i in range(len(corr_matrix.columns)):
        for j in range(i):
            if (corr_matrix.iloc[i, j] >= threshold) and (corr_matrix.columns[j] not in col_corr):
                colname = corr_matrix.columns[i] + "-" + corr_matrix.columns[j] # getting the name of columns
                col_corr.add(colname)
    print(col_corr)
##########################################################################################################################################################
    
##########################################################################################################################################################
# RMSE calculation function
import math
def rmse(df):
    # number of rows
    n = len(df)
    sigma = 0
    for index, row in df.iterrows():
        diff_sqr = (df.loc[index, 'Actual Yards'] - df.loc[index, 'Predicted Yards'])**2
        sigma += diff_sqr
    rmse = math.sqrt(sigma/n)
    return rmse
##########################################################################################################################################################
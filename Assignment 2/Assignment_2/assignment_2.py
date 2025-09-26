import csv
def load_csv(file_name):
    """Opens and reads the provided file. Creates a dictionary that maps name to a
        list of ranking and value. For example, the "population" dictionary would look like...
        {'China': ['1', '1,397,897,720'],
        'India': ['2', '1,339,330,514'],
        'United States': ['3', '334,998,398'],
        'Indonesia': ['4', '275,122,131'],
        ...}
        Notice that all items in values/lists (e.g. ['1', '1,397,897,720']) are strings.

        Args:
            The path of a csv file that contains some world factbook country comparison data.
            The file must be one that includes the following fields: name, ranking, and value. 

        Returns:
            A dictionary mapping 'name' to a list containing rank and value - both as strings. 
        """
    features = {}
    #write your code here
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        for row in reader: #Read the data e.g. "Burkina Faso","burkina-faso","-3.20","2019 est.","1","Africa"
            country = row[0].lower()
            rank = row[4]
            value = row[2]
            region = row[5].lower()
            date_of_info = row[3].lower()

            #format the the data e.g. "Burkina Faso": ["1", "-3.20", "2019 est.", "1", "Africa"] e.g {[0]: [[4],[2]], [1]: [[5],[3]]    })}
            features[country] = [rank, value, region, date_of_info]


        #return the formatted data
    return features

features = {}
features["area"] = load_csv("world_factbook/geography/area.csv")
features["population"] = load_csv("world_factbook/people_and_society/population.csv")
features["median age"] = load_csv("world_factbook/people_and_society/median_age.csv")
features["life expectancy"] = load_csv("world_factbook/people_and_society/life_expectancy_at_birth.csv")
features["gdp"] = load_csv("world_factbook/economy/real_gdp_purchasing_power_parity.csv")

assert features["population"]["united states"][0] == "3", "US population rank test"
assert features["life expectancy"]["chile"][1] == "79.57", "Chile life expectancy value test"
assert features["area"]["south africa"][1] == "1,219,090", "South Africa area value test"
assert len(features["median age"]) == 226, "Median Age dictionary size test"
assert features["gdp"]["china"][0] == "1", "China gdp rank test"
assert features["gdp"]["china"][3] == "2019 est.", "China gdp date of info test"
assert features["population"]["china"][2] == "east asia/southeast asia", "China region test"
print("if we get here, the tests passed")

# Netid: replaceme
from match import match
from data import features

##########Action Functions###############################
    
def country_by_rank(matches):
    """Takes a list of matches as input - specifically one that holds a rank
        and a feature, like 'population.' Finds the country with that rank 
        using tha feature and returns it in a list. 


        Args: matches - a list of strings resulting from a call to match. It
        holds a rank and a feature.  [rank, feature] where feature is the key of the dataset we are looking for

        features = {country: [rank, value]}
    

        Returns: a list of one string - the rank of the country for the
        specified feature. If the country or feature is not found, returns an
        empty list. 
    """

    #get the dataset for the feature
    try:
        rank = matches[0]
        feature = matches[1]
        dataset = features[feature]
    except:
        return []

    #search the dataset for the country with the given rank
    result = filter(lambda country: dataset[country][0] == rank, dataset.keys())
    result = list(result)
    if result:
        return result
    else:
        return []



def rank_by_country(matches):
    """Takes a list of matches as input - specifically one that holds a country
        and a feature, like 'population.' Finds the rank for that country
        using tha feature and returns it in a list.

        Args: matches - a list of strings resulting from a call to match. It
        holds a country and a feature. 
        
        features = {country: [rank, value]}

        Returns: a list of one string - the rank of the country for the
        specified feature. If the country or feature is not found, returns an
        empty list. 
    """

    #get the dataset for the feature
    try:
        country = matches[0]
        feature = matches[1]
        dataset = features[feature]
    except KeyError:
        return []

    #search the dataset for the specified country and return the rank
    try: #try to look up the country
        rank = dataset[country][0]
    except KeyError: #if not, country is not in the dataset, return an empty list
        return []
    
    return [rank]
    

def list_countries(unused):
    """Takes an input that is unused (empty list resulting from a call to match).
        Constructs a list of countries by looking at the keys from one of the
        dictionaries. You can use *any* of the dictionaries for this. I know
        this is not an accurate response as some countries are listed under
        some features but not under others. 

        Args: unused - an empty list resulting from a call to match.
        data = {features: {country: [rank, value]}}
         

        Returns: a list of countries. 
    """
    #country_list = set()
    #get all countries from the dataset
    #for feature in features:
    #    list_of_countries_in_feature = list(features[feature].keys())
    #    country_list.update(list_of_countries_in_feature)
    
    country_list = {country for feature in features.values() for country in feature}
 
    return list(country_list)

def list_patterns(unused):
    """Takes an input that is unused (empty list resulting from a call to match).
        Constructs a list of the patterns from the pa_list and returns it.

        Args: unused - an empty list resulting from a call to match.

        Returns: a list of the known patterns. 
    """
    return None
        

def bye_action(unused):
    """This action function gets called when the user writes 'bye'.
        It raises KeyboardInterrupt in order to break out of the query loop.

        Args: unused - an empty list resulting from a call to match.
    """
    raise KeyboardInterrupt



##########Pattern, Action list###############################


pa_list = [(str.split("which country is ranked number _ for %"), country_by_rank),
           (str.split("what is % ranked for %"), rank_by_country),
           (str.split("which countries do you know about"), list_countries),
           (str.split("what kinds of questions do you understand"), list_patterns),
           (["bye"], bye_action)]


def search_pa_list(src):
    """Takes source, finds matching pattern and calls corresponding action. If it finds
    a match but has no answers it returns ["No answers"]. If it finds no match it
    returns ["I don't understand"].

    Args:
        source - a phrase represented as a list of words (strings)

    Returns:
        a list of answers. Will be ["I don't understand"] if it finds no matches and
        ["No answers"] if it finds a match but no answers
    """
    return None


def query_loop():
    """Query_lop asks the user for input, then "cleans" that input
        by converting all characters to lowercase, removing any training
        punctuation (e.g. ?). After then converting the input to a list
        of strings, we pass the list off to search_pa_list to get answers,
        then display the answers to the user.
        Use a try/except structure to catch Ctrl-C or Ctrl-D characters
        and exit gracefully. You'll need to except KeyboardInterrupt and
        EOFError.
    """
    pass

# Test cases for country_by_rank function

def test_country_by_rank():
    """Comprehensive test cases for country_by_rank function covering edge cases"""
    
    # === VALID CASES ===
    
    # Test basic functionality - valid rank and feature
    assert country_by_rank(["1", "population"]) == ["china"], "Should return China for rank 1 population"
    assert country_by_rank(["2", "population"]) == ["india"], "Should return India for rank 2 population"
    assert country_by_rank(["3", "population"]) == ["united states"], "Should return United States for rank 3 population"
    
    # Test different features
    assert country_by_rank(["1", "area"]) == ["russia"], "Should return Russia for rank 1 area"
    assert country_by_rank(["1", "gdp"]) == ["china"], "Should return China for rank 1 GDP"
    assert country_by_rank(["1", "median age"]) == ["monaco"], "Should return Monaco for rank 1 median age"
    
    # Test edge of valid rankings (last countries in datasets)
    assert country_by_rank(["236", "population"]) == ["vatican city"], "Should handle last ranked country"
    
    # === EDGE CASES - INVALID INPUTS ===
    
    # Test non-existent feature
    assert country_by_rank(["1", "nonexistent_feature"]) == [], "Should return empty list for invalid feature"
    assert country_by_rank(["1", "happiness_index"]) == [], "Should return empty list for feature not in dataset"
    assert country_by_rank(["1", "corruption_level"]) == [], "Should return empty list for made-up feature"
    
    # Test invalid ranks
    assert country_by_rank(["0", "population"]) == [], "Should return empty list for rank 0"
    assert country_by_rank(["-1", "population"]) == [], "Should return empty list for negative rank"
    assert country_by_rank(["999", "population"]) == [], "Should return empty list for rank beyond dataset size"
    assert country_by_rank(["1000", "population"]) == [], "Should return empty list for very high rank"
    
    # Test non-numeric ranks
    assert country_by_rank(["abc", "population"]) == [], "Should return empty list for non-numeric rank"
    assert country_by_rank(["first", "population"]) == [], "Should return empty list for text rank"
    assert country_by_rank(["1.5", "population"]) == [], "Should return empty list for decimal rank"
    assert country_by_rank(["", "population"]) == [], "Should return empty list for empty rank"
    
    # Test malformed inputs
    assert country_by_rank([]) == [], "Should return empty list for empty input"
    assert country_by_rank(["1"]) == [], "Should return empty list for missing feature"
    assert country_by_rank(["1", "population", "extra"]) == [], "Should return empty list for too many parameters"
    
    # Test None and unusual inputs
    assert country_by_rank(None) == [], "Should return empty list for None input"
    assert country_by_rank([None, "population"]) == [], "Should return empty list for None rank"
    assert country_by_rank(["1", None]) == [], "Should return empty list for None feature"
    
    # Test case sensitivity and whitespace
    assert country_by_rank(["1", "POPULATION"]) == [], "Should return empty list for uppercase feature (case sensitive)"
    assert country_by_rank(["1", " population"]) == [], "Should return empty list for feature with leading space"
    assert country_by_rank(["1", "population "]) == [], "Should return empty list for feature with trailing space"
    assert country_by_rank([" 1", "population"]) == [], "Should return empty list for rank with leading space"
    assert country_by_rank(["1 ", "population"]) == [], "Should return empty list for rank with trailing space"
    
    # Test alternative feature name variations that might not exist
    assert country_by_rank(["1", "pop"]) == [], "Should return empty list for abbreviated feature name"
    assert country_by_rank(["1", "population_size"]) == [], "Should return empty list for alternative feature name"
    assert country_by_rank(["1", "life_expectancy"]) == [], "Should return empty list for underscore instead of space"
    
    # Test boundary conditions for each feature
    # (These would need to be adjusted based on actual dataset sizes)
    assert country_by_rank(["300", "area"]) == [], "Should return empty list for rank beyond area dataset"
    assert country_by_rank(["500", "gdp"]) == [], "Should return empty list for rank beyond GDP dataset"
    assert country_by_rank(["400", "median age"]) == [], "Should return empty list for rank beyond median age dataset"
    
    # Test special characters in inputs
    assert country_by_rank(["1!", "population"]) == [], "Should return empty list for rank with special characters"
    assert country_by_rank(["1", "population!"]) == [], "Should return empty list for feature with special characters"
    assert country_by_rank(["@#$", "population"]) == [], "Should return empty list for invalid rank characters"
    
    # Test very large numbers
    assert country_by_rank(["999999999", "population"]) == [], "Should return empty list for extremely large rank"
    
    print("All country_by_rank tests passed!")

# Additional stress tests
def stress_test_country_by_rank():
    """Additional stress tests for unusual scenarios"""
    
    # Test with empty strings
    assert country_by_rank(["", ""]) == [], "Should handle double empty strings"
    
    # Test with mixed data types (if function doesn't handle type conversion)
    try:
        assert country_by_rank([1, "population"]) == [], "Should handle integer input for rank"
        assert country_by_rank(["1", 123]) == [], "Should handle integer input for feature"
    except (TypeError, AttributeError):
        pass  # Expected if function doesn't handle type conversion gracefully
    
    # Test Unicode and special characters
    assert country_by_rank(["1", "populación"]) == [], "Should return empty list for Unicode feature name"
    assert country_by_rank(["①", "population"]) == [], "Should return empty list for Unicode number"
    
    print("All stress tests passed!")


if __name__ == "__main__":
    #test_country_by_rank()
    #stress_test_country_by_rank()

    assert country_by_rank(["2", "population"]) == ["india"], "country_by_rank test"
    print("country_by_rank test passed")
    assert rank_by_country(["united states", "area"]) == ["4"], "rank_by_country test"
    print("rank_by_country test passed")
    assert "india" in list_countries(None), "list_countries test"
    print("list_countries test passed")
    assert search_pa_list(["hi", "there"]) ==["I don't understand"], "search_pa_list test 1"
    assert search_pa_list(["which", "country", "is", "ranked", "number", "2", "for",
                                                   "median", "age"]) == ["japan"], "search_pa_list test 2"
    assert search_pa_list(["what", "is", "XYZ", "ranked", "for", "population"]) == ["No answers"], "search_pa_list test 3"

    #uncomment the line below to interact with your chatbot
    #query_loop()
    


  

    


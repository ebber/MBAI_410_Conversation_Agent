# Netid: replaceme
from match import match
from data import features

##########Action Functions###############################
    
def country_by_rank(matches):
    """Takes a list of matches as input - specifically one that holds a rank
        and a feature, like 'population.' Finds the country with that rank 
        using tha feature and returns it in a list.

        Args: matches - a list of strings resulting from a call to match. It
        holds a rank and a feature. 

        Returns: a list of one string - the rank of the country for the
        specified feature. If the country or feature is not found, returns an
        empty list. 
    """
    return None

def rank_by_country(matches):
    """Takes a list of matches as input - specifically one that holds a country
        and a feature, like 'population.' Finds the rank for that country
        using tha feature and returns it in a list.

        Args: matches - a list of strings resulting from a call to match. It
        holds a country and a feature. 

        Returns: a list of one string - the rank of the country for the
        specified feature. If the country or feature is not found, returns an
        empty list. 
    """
    return None
    

def list_countries(unused):
    """Takes an input that is unused (empty list resulting from a call to match).
        Constructs a list of countries by looking at the keys from one of the
        dictionaries. You can use *any* of the dictionaries for this. I know
        this is not an accurate response as some countries are listed under
        some features but not under others. 

        Args: unused - an empty list resulting from a call to match.

        Returns: a list of countries. 
    """
    return None

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


if __name__ == "__main__":
    assert country_by_rank(["2", "population"]) == ["india"], "country_by_rank test"
    assert rank_by_country(["united states", "area"]) == ["4"], "rank_by_country test"
    assert search_pa_list(["hi", "there"]) ==["I don't understand"], "search_pa_list test 1"
    assert search_pa_list(["which", "country", "is", "ranked", "number", "2", "for",
                                                   "median", "age"]) == ["japan"], "search_pa_list test 2"
    assert search_pa_list(["what", "is", "XYZ", "ranked", "for", "population"]) == ["No answers"], "search_pa_list test 3"

    #uncomment the line below to interact with your chatbot
    #query_loop()
    


  

    


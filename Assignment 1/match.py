def match(pattern, source):
    """Attempt to match pattern to source. % matches a sequence of zero or
        more words and _ matches any single word.

    Args:
        pattern - a list of strings. % and/or _ are utilized as placeholder
                  to match/extract words from the source
        source - a list of string. A phrase/sentence/question represented as
                 a list of words (strings).

    Returns:
        if a match is detected, returns a list of strings - a list of matched
        words (words in the source corresponding to _'s or %'s, in the
        pattern, if any).
        else if no match is detected, returns None. 

    Psudeocode:
    start with a while loop that checks if the pattern or source are empty
    if the pattern or source is empty, return None
    go through each element of pattern and source - if the elements are the same, keep moving
    if the elements are different, check if the pattern element is a % or _
    if the pattern element is a _, accumulate the source element and keep moving
    if the pattern is a %, handle TODO: flesh this out, and keep moving
    if 
    """
    #handle empty pattern or source
    if pattern ==[] and source == []:
        return []
    elif pattern == [] or source == []:
        return None

    #Get into iteration, start with source index and pattern index, and an accumulator for the result
    sind = 0
    pind = 0
    result = [] #accumulator for the result
    #main loop iterating through the pattern and source, accumulating the result
    while sind < len(source) and pind < len(pattern):
        if pattern[pind] == source[sind]: #if the elements are the same, keep moving
            sind += 1
            pind += 1
        elif pattern[pind] == "_": #handle _
            result.append(source[sind])
            sind += 1
            pind += 1
        elif pattern[pind] == "%": #handle %
            #Handle edge case where % is at the end of the pattern
            #Behavior: match none, 1 or many charecters untill the next charcter in the pattern
            #Edge cases: if there is no "next charecter" after the %, accumulate the rest of the source as a single item
            #if pind == len(pattern) - 1: #we are at the last charecter
            #    result.append(' '.join(source[sind:]))
            #    sind = len(source) #advance the source index to the end of the source
            #    return result
            NextChar = None
            if pind < len(pattern)-1: #if % is not the last charecter
                NextChar = pattern[pind+1]

            # This loop collects source tokens up to the next pattern token after '%', joining them as the match for '%'.
            matched_set = []
            while sind < len(source) and source[sind] != NextChar:  #go until we hit the next pattern char after % or until the end of the set
                matched_set.append(source[sind])
                sind += 1
            result.append(' '.join(matched_set))

            #Increment pind, moving past the %
            pind += 1

            #handle edge case where % is at the end of the pattern - currently, this causes pind NOT to be incremented when it should be
            
        elif pattern[pind] != source[sind]:
            return None
        else:   #we should never get here
            print("Logic error in iteration loop control flow: We should never get here")
            return None
    
    #After Pattern or source is iterated through, handle different lengths

    #if source[sind:] has anything left, there are unaccumulated and unmatched tokens in the source, which means no match, return None
    if source[sind:] != []:
        return None
    
    #if pattern[pind:] has anything left, to be a match, the rest of the pattern should be %, if not, return None
    for pind in range(pind, len(pattern)): #TODO: for cleanliness, increment pind so it appears outside the loop
        if pattern[pind] != "%":
            return None
        else:
            result.append("")

    #if we get here, we have a match; sind and pind should be at the end of the pattern and source (sind == len(source) and pind == len(pattern))
    return result



assert match(["x", "y", "z"], ["x", "y", "z"]) == [], "test 1 failed"
assert match(["x", "z", "z"], ["x", "y", "z"]) == None, "test 2 failed"
assert match(["x", "y"], ["x", "y", "z"]) == None, "test 3 failed"
assert match(["x", "y", "z", "z"], ["x", "y", "z"]) == None, "test 4 failed"
assert match(["x", "_", "z"], ["x", "y", "z"]) == ["y"], "test 5 failed"
assert match(["x", "_", "_"], ["x", "y", "z"]) == ["y", "z"], "test 6 failed"
assert match(["%"], ["x", "y", "z"]) == ["x y z"], "test 7 failed"
assert match(["x", "%", "z"], ["x", "y", "z"]) == ["y"], "test 8 failed"
assert match(["%", "z"], ["x", "y", "z"]) == ["x y"], "test 9 failed"
assert match(["x", "%", "y"], ["x", "y", "z"]) == None, "test 10 failed"
assert match(["x", "%", "y", "z"], ["x", "y", "z"]) == [""], "test 11 failed"
assert match(["x", "y", "z", "%"], ["x", "y", "z"]) == [""], "test 12 failed"
assert match(["_", "%"], ["x", "y", "z"]) == ["x", "y z"], "test 13 failed"
assert match(["_", "_", "_", "%"], ["x", "y", "z"]) == [
        "x",
        "y",
        "z",
        "",
    ], "test 14 failed"
assert match(["x", "%", "z"], ["x", "y", "z", "z", "z"]) == None, "test 15 failed"
#TEST TO CHECK: Should match(["%", "%"], []) == ["",""]?
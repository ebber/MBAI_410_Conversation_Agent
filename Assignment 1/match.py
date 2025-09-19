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

    """
    return None


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
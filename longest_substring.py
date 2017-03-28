def lengthOfLongestSubstring(s):
    """
    Given a string, find the length of the longest substring 
    without any repeated letters.
    >>> lengthOfLongestSubstring("abcabcbb")
    3
    >>> lengthOfLongestSubstring("bbbbbb")
    1
    >>> lengthOfLongestSubstring("pwwkew")
    3
    """
    longest_length = 0
    current_substring = []
    for c in s:
        if c not in current_substring:
            current_substring.append(c)
        else:
            longest_length = max(longest_length, len(current_substring))
            i = current_substring.index(c)
            current_substring = current_substring[i+1:]
            current_substring.append(c)
        longest_length = max(longest_length, len(current_substring))
    return longest_length


def lengthOfLongestSubstringOptimized(s):
    """
    Given a string, find the length of the longest substring 
    without any repeated letters.
    >>> lengthOfLongestSubstringOptimized("abcabcbb")
    3
    >>> lengthOfLongestSubstringOptimized("bbbbbb")
    1
    >>> lengthOfLongestSubstringOptimized("pwwkew")
    3
    """
    longest = 0
    seen = {}
    start = 0
    for i, char in enumerate(s):
        if char not in seen:
            seen[char] = i
        else:
            if i == len(s) - 1:
                return longest
            longest = max(longest, len(seen))
            start = seen[char] + 1
            seen[char] = i
        longest = max(longest, (i - start + 1) )
    return longest


def lengthOfLongestSubstringOptimized2(s):
    """
    Given a string, find the length of the longest substring 
    without any repeated letters.
    >>> lengthOfLongestSubstringOptimized2("abcabcbb")
    3
    >>> lengthOfLongestSubstringOptimized2("bbbbbb")
    1
    >>> lengthOfLongestSubstringOptimized2("pwwkew")
    3
    """
    longest = 0
    seen = {}
    start = 0
    for i, char in enumerate(s):
        # print seen, "start: ", start, "longest: ", longest
        if char in seen:
            start = max(seen[char] + 1, start)
        seen[char] = i
        longest = max(longest, (i - start + 1) )
    return longest


if __name__ == "__main__":
    import doctest
    doctest.testmod()
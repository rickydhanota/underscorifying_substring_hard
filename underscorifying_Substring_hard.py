# Write a function that takes in two strings: a main string and a potential substring of the maion string. The function should return a version of the main string with every instance of the substring in it wrapped between the underscores.

#if two of more instances of the substring in the main string overlap each other or sit side by side, the underscores relevant to these substrings should only appear on the far left of the leftmost substring and on the far right of the rightmost substring. If the main string doesn't contain the other string at all, the function should return the main string intact. 

#Sample input: string = "testthis is a testtest to see if testestest it works"
#Sample output: "_test_this is a _testtest_ to see if _testestest_ it works"

def underscorifySubstring(string, substring):
    pass
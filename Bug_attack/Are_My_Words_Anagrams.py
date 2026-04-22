def are_anagrams(word1, word2):
    word1=word1.lower()
    word2=word2.lower()
    word1_chars_sorted = sorted(word1)

    word2_chars_sorted = sorted(word2)
    sorted_word1 = ''.join(word1_chars_sorted)
    sorted_word2 = ''.join(word2_chars_sorted)
    return sorted_word1 == sorted_word2


print(are_anagrams('Silent', 'Listen'))  # should be True, but gives False
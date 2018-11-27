# string_a is the big phrase, string_b is the small phrase
def string_contains_anagram(string_a, string_b):
    big_phrase_lower = string_a.lower()
    small_phrase_lower = string_b.lower()

    big_phrase_list = big_phrase_lower.split(" ")
    small_phrase_list = small_phrase_lower.split(" ")

    words_dict = {}


    for i in range(len(small_phrase_list)):
        for ch in big_phrase_list[i]:
            if ch not in words_dict.keys():
                words_dict[ch] = 1
            else:
                words_dict[ch]+=1


    for i in range(len(small_phrase_list)):
        for ch in small_phrase_list[i]:
            if ch not in words_dict.keys():
                return False
            else:
                words_dict[ch]-=1
                if words_dict[ch] < 0:
                    return False

    return True

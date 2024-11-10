# "aaa" occurs three times in the string "bcaaaaatafg"

def count_substring(mainstring, substring):
    substring_len = len(substring)
    substring_count = 0
    for idx in range(len(mainstring) - (substring_len - 1)):
        if mainstring[idx: idx + substring_len] == substring:
            substring_count += 1

    return substring_count




print(count_substring("bcaaaaatafg", "aaa"))
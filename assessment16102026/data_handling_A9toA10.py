with open('coastal_monitoring_log.txt','r') as f:
    data = f.readlines()

data = list(map(str.strip,data))
# A9. Read coastal_monitoring_log.txt and count total words and the number of times the word 'inspection'
# appears.
print(data)
print("\n")
total_words = 0
count_of_given_word = 0
for lines in data:
    for line in lines.splitlines():
        words = line.split()
        total_words += len(words)
        for word in words:
            if word == "inspection" :
                count_of_given_word += 1

print(f"Total words in file",total_words)
print("\n")
print(f"Number of times word inspection appear",count_of_given_word)
print("\n")

# A10. Print only the lines containing either 'boardwalk', 'maintenance', or 'wind'

search_word = {"boardwalk","maintenance","wind"}
for lines in data:
        words = lines.split()
        word_set = set(words)
        if word_set.intersection(search_word):
            print(lines)








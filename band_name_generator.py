#!/usr/bin/python

band_names = []
words_file = 'words_file.txt'

# get file line by line
with open(words_file) as f:
  content = f.readlines()

# strip line breaks
content = [line.rstrip('\n') for line in content]

# create a list of lists
line_list = []
for line in content:
  line = line.replace(" ","")
  line_list.append(line.split(','))

# pair each list element with each element from every other list
word_counter = 0
for parent_key, words in enumerate(line_list):
  for sub_key, word in enumerate(words):
    # now we have each word
    word_counter = word_counter + 1
    for new_parent_key, new_words in enumerate(line_list):
      for new_sub_key, new_word in enumerate(new_words):
        # don't append words from same line
        if sub_key != new_parent_key:
          band_names.append(word + ' ' + new_word)

print ""
print "That's " + str(len(band_names)) + " band names from " + str(word_counter) + " words."
print ""

for band_name in band_names:
  print band_name

print ""


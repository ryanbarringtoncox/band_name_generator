#!/usr/bin/python
import sys, fileinput

band_names = []

if __name__ == '__main__':

  if  len(sys.argv) == 1:
    print "Need an input file of words please."
    print "  ..exiting."
    sys.exit()

  # create a list of lists
  line_list = []

  # loop through input file
  for line in fileinput.input():
    line = line.strip('\n').replace(" ","")
    # ignore lines with '#'
    if '#' not in line: 
      line_list.append(line.split(','))

  #print line_list

  # pair each list element with each element from every other list
  word_counter = 0
  for parent_key, words in enumerate(line_list):
    for sub_key, word in enumerate(words):
      # now we have each word
      word_counter = word_counter + 1
      for new_parent_key, new_words in enumerate(line_list):
        for new_sub_key, new_word in enumerate(new_words):
          # don't append words from same line
          if parent_key != new_parent_key:
            #print " " + new_word
            band_names.append(word + ' ' + new_word)

  print ""
  print "That's " + str(len(band_names)) + " band names from " + str(word_counter) + " words."
  print ""

  for band_name in band_names:
    print band_name

  print ""

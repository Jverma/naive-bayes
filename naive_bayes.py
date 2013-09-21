import os
import sys
import json
from math import *
from collections import *

#create a word-frequency dictionary
def word_count(input_list):
    word_freq = defaultdict(int)
    for line in input_list:
        words = line.split(" ")
        for w in words:
            word_freq[w]+=1
    return word_freq        
        


#training 
spam_nonspam = []
spam_list = []
non_spam_list = []
training_file = open(sys.argv[1])
for line in training_file:
    data = json.loads(line)
    spam_nonspam.append(data[1])
    if (data[0] == 'spam'):
        spam_list.append(data[1])
    if (data[0] == 'non_spam'):
        non_spam_list.append(data[1])

spam_dict = word_count(spam_list)
non_spam_dict = word_count(non_spam_list)
all_words_freq = word_count(spam_nonspam)



#log-probabilites (Assume there equal number of spam and non spam emails)
log_spam = {}
log_nonspam = {}
for x in spam_dict.keys():
    num1 = spam_dict[x] + 1
    denom1 = len(spam_dict)
    p_spam = float(num1)/float(denom1)
    log_spam[x] = log(p_spam)
for x in non_spam_dict.keys():
    num1 = non_spam_dict[x] + 1
    denom1 = len(non_spam_dict)
    p_nonspam = float(num1)/float(denom1)
    log_nonspam[x] = log(p_nonspam)
         


#classification of testing file
testing_file = open(sys.argv[2])
for line in testing_file:
    #record = json.loads(line)
    words = line.split(" ")
    spam_prob = 0
    nonspam_prob = 0
    for w in words:
        w = w.encode('utf-8')
        try:
            spam_prob = spam_prob + float(log_spam[w])
        except:
            spam_prob = 1/len(spam_dict)
        try:    
            nonspam_prob = nonspam_prob + float(log_nonspam[w])
        except:
            nonspam_prob = 1/len(non_spam_dict)
    totalspam_prob = spam_prob * 0.5
    totalnonspam_prob = nonspam_prob * 0.5
    print totalspam_prob, totalnonspam_prob
    if (totalspam_prob > totalnonspam_prob):
        print 'spam' + ',' + str(line)
    else:
        print 'non_spam' + ',' + str(line)
    




        

from __future__ import division
import csv
import time
import nltk
import math
tweets = []
tweet_class = []
words = set()
attributes = []
with open('dataset_v2.csv') as f:
	read = csv.reader(f)
	i=0
	for row in read:
		tweets.append(row[0].lower())
		if (row[1]=='1'):
			  tweet_class.append(row[1])
		else:
			  tweet_class.append('0')
		i+=1
for tweet in tweets:
	words.update(nltk.word_tokenize(tweet))
attributes = list(words)
def calc_entropy(target_attribute):
	start_time = time.time()
	freq     = {}
	entrp = 0.0
	subset_has = target_attribute.count('1')
	subset_has_not = target_attribute.count('0')
	if ((subset_has)!=0):
		entrp += (-(subset_has)/len(target_attribute)) * math.log((subset_has)/len(target_attribute), 2)
	if ((subset_has_not)!=0):
		entrp += (-(subset_has_not)/len(target_attribute)) * math.log((subset_has_not)/len(target_attribute), 2)
	end_time = time.time()
	return entrp
def calc_gain(data, attr, target_attr):
	target_has = []
	target_has_not = []
	subset_entropy = 0.0
	start_time = time.time()
	for tweet in range(len(data)):
		if (attr in data[tweet]):
			target_has.append(target_attr[(tweet)])
		else:
			target_has_not.append(target_attr[(tweet)])
	end_time = time.time()
	val_prob        = len(target_has)/len(data)
	subset_entropy += val_prob * calc_entropy(target_has)

	val_prob        = len(target_has_not)/len(data)
	subset_entropy += val_prob * calc_entropy(target_has_not)
	return (calc_entropy(target_attr) - subset_entropy)

def best_attribute(data, attributes, target_attribute):
	list_gain = []
	i=0
	total_iter = len(attributes)
	for attr in attributes:
		start_time  =time.time()
		new_gain = calc_gain(data, attr, target_attribute)
		list_gain.append(new_gain)
		end_time = time.time()
		i+=1
	return attributes[list_gain.index(max(list_gain))]

def create_tree(data_set, attributes, target_attr):
	if (target_attr.count('0') == len(target_attr)):
		return '0'
	elif (target_attr.count('1') == len(target_attr)):
		return '1'
	else :
		best = best_attribute(data_set, attributes, target_attr)
		tree = {best: {}}
		subset_has = []
		subset_has_not = []
		target_has = []
		target_has_not = []
		for tweet in range(len(data_set)):
			if (best in nltk.word_tokenize(data_set[tweet])):
				subset_has.append(data_set[tweet])
				target_has.append(target_attr[(tweet)])
			else:
				subset_has_not.append(data_set[tweet])
				target_has_not.append(target_attr[(tweet)])
		attributes.remove(best)
		tree[best]['1'] = create_tree(subset_has, attributes, target_has)
		tree[best]['0'] = create_tree(subset_has_not, attributes, target_has_not)
		return (best, tree)

d_tree = create_tree(tweets[0:1100], attributes,   tweet_class[0:1100])

def traverse(tweet):
	value = d_tree 
	key = d_tree[1].keys()[0]
	while (value!='0' and value!='1'):
		key =value[1].keys()[0]
		if (key in tweet.split(' ')):
			value = value[1][key.lower()]['1']
		else:
			value = value[1][key.lower()]['0']
	return value 
correct=0
for index in range(1100,len(tweets)):
	if (traverse(tweets[index])==  tweet_class[index]):
		correct+=1
print "ACC", correct
print "Percentage - ", correct/400
	



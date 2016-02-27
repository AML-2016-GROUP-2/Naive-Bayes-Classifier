/////////////////////////////////////
GROUP 2
Venkat Datta NH
Vinay SB
Sushanth k Hegde
Tenzin Wangyal
////////////////////////////////////

Results:
===============================
Naive Bayes Binary classifier (NBBC)

ACC  297
0.99
time:
real	0m0.566s
user	0m0.556s
sys	0m0.008s
===============================
Navie Bayes Multivalued classifier (NBBMC)

ACC  292
0.973333333333
time:
real	0m0.739s
user	0m0.716s
sys	0m0.020s
===============================
Decision Tree (DT)

ACC 398
Percentage -  0.995
time:
real	0m4.899s
user	0m4.872s
sys	0m0.028s
===============================

From our Observation we clearly see that Dtree is most accurate, then NBBC and NBMC.

Our review of the comparison between NBC and DTC :
we say DTC is better when the training data contains all possibilities ( i.e when the data set is quite big) also on our experimentation as you can see above DT have taken more time then NB in which we speculate it as DT picks the best features from the data and this might be the cause for the slower processing ( assuming coding variations wont matter)
But for smaller data set NB's are quite amazing classifiers as they don't need to have all possible combinations to reside in the set before hand. 
And NBMC is anytime better then NBBC

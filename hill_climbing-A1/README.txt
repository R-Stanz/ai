This folder contains the implementation of the 
Hill Climbing algorithm. In order to run the al-
gorithm it's needed to have python3 with the
matplotlib, numpy and pandas libraries installed
on the machine.

The runner.py file is the file that must be used
to run the algorithm. The runner.ipnb is an 
option to be used on python notebooks, for better
control/view on the pie charts. The demo.py gives 
a better understanding of how the algorithm runs
with just one iteration of variations. 

About the results it's perceptble that the city
order that was present on the example had great
results compared with variations that had a ran-
dom initial order. Futhermore it is also noted
that the variations with nothing of randomness
(variation 1 and 3) achived the best final costs,
on average and by a small difference - but had 
as trade-off of that had to make way more con-
figurations than those variations that used
random operators. 

Overall the best operator to pass through the
lesser number of possibilities and have lesser
states on its path is the first random operator 
- random swap. The second random (random reverse)
operator is the best for find the best guess
for best cost. These results were achived when
using bigger values than the ones that are
being brought by default here.

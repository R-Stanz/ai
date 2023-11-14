In order to run the algorithm simply execute
the runner.py file with python3.

In this directory there is all the necessary 
files to run the A* algorithm implementation
required on the problem pdf file 
"AT2_2023-2.pdf". In order to properly run
the algorithm it is required the python3 and
the pandas libary.

By looking at the results shown in the
program output, it can be seen that it didn't
matter which heuristic for the Kruskal's MST 
variations (with and without counting the first
city) the final cost was always the same. Even
though the final cost was unchanged between
the Kruskal's MST algorithm variations the
most informed variation (the one that used the
first state as parameter) was clearly the best
option for having the same result as the other
variation but having to go through fewer steps.

It should be noted that the cost didn't change
with firts cities variations because the path
with the minimum cost had all cities, which
means that it there should always be a way for
each city to have a minimum path that shares
the same pattern of cities visited with the
minimum path of the other cities.

Finally, the fact that in all cases the maximum
queue of states had the same size as the last
was expected, because of the factorial nature
of the problem. So was expected the fact that
having different start cities would have 
different ways of analysing the possibilities -
and thus having different sizes for the maximum
queue size of states, even though also sharing
the same pattern on it's minimum path with the
minimum path for the other cities.

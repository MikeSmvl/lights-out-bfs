# BFS (Python) #

<img src="http://upload.wikimedia.org/wikipedia/commons/3/33/Breadth-first-tree.svg" alt="Breadth First Search" align="right" height="140" />

### [Breadth First Search][bfs] implementation in Python ###

This is part of a project I did at Concordia University in my Artificial Intelligence (SOEN 472) course which improved my understanding of traversing algorithms.<br/>

The graph constructed in the BFS file solves a puzzle game called Lights Out.

To solve the following puzzle with a maximum depth of 5:


<h4>Starting Puzzle</h4>
<img src="https://i.imgur.com/JL73IVH.png" alt="Breadth First Search" height="140" />
<h4>Goal</h4>
<img src="https://i.imgur.com/S0QJzRD.png" alt="Breadth First Search" height="140" />

## Usage

```bash
$ python bfs.py 5 '[[1,1,0],[0,1,0],[0,1,1]]' '[[0,0,0],[0,0,0],[0,0,0]]'

#    Starting Node
# --------------------
#      [1, 1, 0]
#      [0, 1, 0]
#      [0, 1, 1]
# --------------------
#      [0, 0, 1]
#      [0, 0, 0]
#      [0, 1, 1]
# --------------------
#      [0, 1, 0]
#      [0, 0, 1]
#      [0, 1, 1]
# --------------------
#      [0, 0, 0]
#      [1, 1, 0]
#      [0, 0, 1]
# --------------------
#      [0, 0, 0]
#      [0, 1, 0]
#      [1, 1, 1]
# --------------------
#      [0, 0, 0]
#      [0, 0, 0]
#      [0, 0, 0]
# --------------------
#      Goal Node
```

[bfs]: http://en.wikipedia.org/wiki/Breadth-first_search
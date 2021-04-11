# summative-linda_david_caleb
summative-linda_david_caleb created by GitHub Classroom

Project Description

Our project will be focused on the A* pathfinding algorithm. Our objective is to guide the snake towards the target(our food) by avoiding the walls(this will be represented by the brown blocks). The snake will increase in length and gain one point after each successful reach.
To determine our path from node to node, looking for a specific node as our end goal, we will be using 2 algorithms: The Breadth First Search and Best First Search

Breadth First Search

It uses the queueing system to explore all nodes depth by depth.  It takes the node at the front of the queue and then pushes all of the connecting nodes onto the end of the queue. This ensures that the nodes with the closest links to the starting node are explored first and makes it ideal for finding an endpoint where the direction is unknown or if there are a lot of obstacles.
     
Best First Search(Informed Search)

This algorithm explores a single path by prioritizing the next node using a heuristic evaluation. This heuristic usually guides the path towards a known endpoint, though this will depend on the heuristic function. We’ll use this Best-First search algorithm as the main search algorithm and the solutions below will be focused around writing a heuristic function to help decide the path for the snake.
          
     Testing Effectiveness
So how would we know that the algorithm we used was effective? To analyze its optimality, we can use either of this 2 methods: 
Points
The snake gets one point upon successful reaching of its target. This increments as the game proceeds. The more points, the longer the snake lasted, and so the better the solution is at avoiding crashes while also collecting points. How many points the snake collects will be a great indication of how successful we implemented.
Number of moves
As the snake gets longer from collecting points, there are less available spaces on the grid for the next point to generate, so the efficiency of the solution is less important towards the end than it is at the beginning. We can use a cumulative moving average here to smooth out the variability that comes from the randomness of the point positioning.
 
 
Motivation

As we move deeper into the digital age, there is a need to automate most tasks that we handle manually. This has already been seen in game development, and has extended in our day to day activities such as: in GPS navigation systems, using BFS in finding all the neighbouring locations, and in social networks, where we can find people within a given distance ‘k’ from a person using Breadth First Search till ‘k’ levels. We intend to use the BFS knowledge that we will learn while creating this automated snake game in garbage collection in waste fields.
       
Applications

 This general problem of finding a path from a starting point to an endpoint can be applied to lots of other applications like satellite navigation, routing packets across the internet, game AIs, OS file system search, distribution/utility networks and many more.
 
 
 First Prototype
 
 ![](images/prototype.vp)

Bibliography

GreatLearning Blog: Free Resources what Matters to shape your Career!. 2021. Best First Search Algorithm in AI | Concept, Algorithm and Implementation. [online] Available at: <https://www.mygreatlearning.com/blog/best-first-search-bfs/> [Accessed 7 April 2021].
Jeulin-Lagarrigue, M., 2021. Breadth First Search (BFS) Pathfinder - Algorithms | H.urna Academy. [online] H.urna. Available at: <https://hurna.io/academy/algorithms/maze_pathfinder/bfs.html> [Accessed 7 April 2021].
Prep, F., 2021. Applications of Breadth First Traversal. [online] FACE Prep. Available at: <https://www.faceprep.in/data-structures/applications-of-breadth-first-traversal/> [Accessed 7 April 2021].

 

# summative-linda_david_caleb
summative-linda_david_caleb created by GitHub Classroom

Project Description

Our project will be focused on the A* pathfinding algorithm. Our objective is to guide the snake towards the target(our food) by going throught the shortest path posible. The snake will increase in length and gain one point after each successful reach.

A* Algorithm

in order to understand how this algorithm works it's important to consider a 2D grid with cells, having a starting point and a destination point, our goal here is to find the shortest path to reach to the destination.

What A* Search Algorithm does is that at each step it picks the node/cell according to a value-‘f’ which is a parameter equal to the sum of two other parameters – ‘g’ and ‘h’. At each step it picks the node/cell having the lowest ‘f’, and process that node/cell.

g - the movement cost from moving from the initial cell to any cell on the grid as long as it's in the path to the destination.
h - the estimated movement cost to move from that given square on the grid to the final destination. this usually a guess since at first we don't know the actual distance until we find the path to the destination.

          
     Testing Effectiveness
     
So how would we know that the algorithm we used was effective? To analyze its optimality, we can use either of this 2 methods: 
Points
The snake gets one point upon successful reaching of its target. This increments as the game proceeds. The more points, the longer the snake lasted, and so the better the solution is at avoiding crashes while also collecting points. How many points the snake collects will be a great indication of how successful we implemented.


Motivation

As we move deeper into the digital age, there is a need to automate most tasks that we handle manually. This has already been seen in game development, and has extended in our day to day activities such as: in GPS navigation systems, using A* in finding all the neighbouring locations, and in social networks, where we can find people within a given distance ‘k’ from a person using path finding till ‘k’ levels. 
       
Applications

 This general problem of finding a path from a starting point to an endpoint can be applied to lots of other applications like satellite navigation, routing packets across the internet, game AIs, OS file system search, distribution/utility networks and many more.
 
 
 In developing our Game we went through phases
 
 1.First Prototype
     This is a terminal based game, not having lots of functionality. the snake is moved using the S,A,D,W keys.
 
 ![](images/prototype1.png)
 
 2.Second Prototype
     This is a more improved version of the game with a Graphical User Interface. it uses the navigation keys for direction.
 
 ![](images/final_6080859a14c1de006fc0e50c_155681.gif)

  3. Final Product
     This reflects an automated version of the snake game using the A* Algorithm, no user input is needed at all.

 ![](images/final_60808870269b4c00937f3937_296626.gif)
 
 
 
 Analysis of Algorithm 

A* algorithm is a blend of two data structures : Best-first search(informed search) and Djistra’s algorithm.

Context

Best-first search:

The Greedy Best-First-Search algorithm works in a way that it has some estimate (called a heuristic) of how far from the goal any vertex is. Instead of selecting the vertex closest to the starting point, it selects the vertex closest to the goal. Greedy Best-First-Search is not guaranteed to find a shortest path. However, it runs much quicker than Dijkstra’s Algorithm because it uses the heuristic function to guide its way towards the goal very quickly. For example, if the goal is to the south of the starting position, Greedy Best-First-Search will tend to focus on paths that lead southwards rather than considering the whole grid( suppose it’s a 2D plane) which would take much more time as discussed above.

Time complexity: Worst time complexity is O(n * Log n) where n is number of nodes.

Space Complexity: O(b^m),  where b is the branching factor and m the number of nodes,this space complexity is due to the fact that we need to store the heuristic function evaluations for all nodes during the traversal.


Dijkstra’s algorithm:

Dijkstra’s Algorithm works by visiting vertices/nodes in the graph starting with the object’s starting point (node). It then repeatedly examines the closest not-yet-examined vertex, adding its vertices to the set of vertices to be examined. It expands outwards from the starting point until it reaches the goal. Dijkstra’s Algorithm is guaranteed to find a shortest path from the starting point to the goal, as long as none of the edges have a negative cost.

Time Complexity: the worst case for the Dijkstra’s Algorithm time complexity is O(s*|E|log|E|+|n|), s being the number of sources, n the number of vertices in the graph, E the number of edges in the graph

Space Complexity: the worst case for the Dijkstra’s Algorithm space complexity is O(n2), here n is the the number of nodes



As already said, A* algorithm takes advantage of the two data structures where it can find the shortest path as Dijkstra’s and also uses heuristic to guide itself, this makes this algorithm more powerful than both of the above mentioned.


 Correctness of our algorithm
 
 A* algorithm is modeled by combining the Dijkstra and Best First Search algorithm. So why would this be more efficient than using either? Well, Dijkstra’s algorithm works by visiting vertices in the graph starting with the object’s starting point. It then repeatedly examines the closest not-yet-examined vertex, adding its vertices to the set of vertices to be examined. It expands outwards from the starting point until it reaches the goal. Dijkstra’s Algorithm is guaranteed to find a shortest path from the starting point to the goal, as long as none of the edges have a negative cost. Best FIrst Search on the other hand, works similarly to Dijstra, but instead of selecting the vertex closest to the starting point, it selects the one closest to the goal.
It has an absolute estimate(heuristic) of how far from the goal the vertex is. This helps it run much faster towards the goal since the heuristic function guides its way towards the goal, but the trade off is that it may use the longer route, especially when there are obstacles on our path. Dijkstra will work harder(time consuming) but find the shortest path. 
A* pathfinding, g(n) represents the exact cost of the path from the starting point to any vertex n, and h(n) represents the heuristic estimated cost from vertex n to the goal. 

Equation: f(n) = g(n)+h(n)

Each time through the main loop it examines  which path has the lowest f(n). 

 To test correctness, we would observe that in a flat surface, our equation will use the Best First Search algorithm since it’s faster, and in that case our g(n) would be 0; however, once obstacles are introduced on our paths, it will utilize our Dijkistra’s g(n) since it will guarantee a shorter path albeit more time taken.
 
Solution - how community will be benefited from your apps
Our project is a snake game which will greatly help the community in relaxation as the study shows that Simple games can improve players' moods, promote relaxation and ward off anxiety, the study also say that If playing games simply makes people happier, this seems to be a fundamental emotional benefit to consider.

Last but not least, Our snake game can also help in terms of improving someone’s focus which can be used in pre schools and primary schools to improve young kids focus while they concentrate on winning, it can also help kids/adults to be problem solvers because this game make the player try to find a solution (which is the snake finding food in this case), this is a good mind set for anyone to have.              


Group video : https://drive.google.com/file/d/1ZjvxiVPqkQhS4Ze48CxUtEboXE0kFcv7/view?usp=sharing
 

 In order to run this application you must install NumPy:
 
                  pip install numpy
 
Bibliography

GreatLearning Blog: Free Resources what Matters to shape your Career!. 2021. Best First Search Algorithm in AI | Concept, Algorithm and Implementation. [online] Available at: <https://www.mygreatlearning.com/blog/best-first-search-bfs/> [Accessed 7 April 2021].
Jeulin-Lagarrigue, M., 2021. Breadth First Search (BFS) Pathfinder - Algorithms | H.urna Academy. [online] H.urna. Available at: <https://hurna.io/academy/algorithms/maze_pathfinder/bfs.html> [Accessed 7 April 2021].
Prep, F., 2021. Applications of Breadth First Traversal. [online] FACE Prep. Available at: <https://www.faceprep.in/data-structures/applications-of-breadth-first-traversal/> [Accessed 7 April 2021].
GeeksforGeeks. 2021. A* Search Algorithm - GeeksforGeeks. [online] Available at: <https://www.geeksforgeeks.org/a-search-algorithm/> [Accessed 21 March 2021].
 

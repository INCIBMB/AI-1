
"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first

    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    #print "Start:", problem.getStartState()
    #print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    #print "Start's successors:", problem.getSuccessors(problem.getStartState())
    startNode=problem.getStartState()
    if problem.isGoalState(startNode):
        return []
    s=util.Stack()
    s.push((startNode,[]))
    visited=[]

    while not s.isEmpty():
        current, actions = s.pop()
        if(problem.isGoalState(current)):
            return actions
        if current in visited:
            continue
        visited.append(current)

        succ=problem.getSuccessors(current)
        for nextNode,action,cost in succ:
            newactions=actions+[action]
            s.push((nextNode,newactions))
            
            
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    """
    "*** YOUR CODE HERE ***"
    startNode=problem.getStartState()
    if problem.isGoalState(startNode):
        return []
    s=util.Queue()
    s.push((startNode,[]))
    visited=[]

    while not s.isEmpty():
        current, actions = s.pop()
        if(problem.isGoalState(current)):
            return actions
        if current in visited:
            #print visited
            continue
        visited.append(current)

        succ=problem.getSuccessors(current)
        
        for nextNode,action,cost in succ:
            newactions=actions+[action]
            s.push((nextNode,newactions))
    util.raiseNotDefined()

def uniformCostSearch(problem):
    "Search the node of least total cost first. "
    "*** YOUR CODE HERE ***"
    startNode=problem.getStartState()
    if problem.isGoalState(startNode):
        return []
    s=util.PriorityQueue()
    s.push((startNode,[],0),0)
    visited=[]

    while not s.isEmpty():
        current, actions,prevcost = s.pop()
        if(problem.isGoalState(current)):
            return actions
        if current in visited:
            continue
        visited.append(current)

        succ=problem.getSuccessors(current)
        for nextNode,action,cost in succ:
            newactions=actions+[action]
            newcost=prevcost+cost
            s.push((nextNode,newactions,newcost),newcost)
    
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    "Search the node that has the lowest combined cost and heuristic first."
    "*** YOUR CODE HERE ***"
    startNode=problem.getStartState()
    if problem.isGoalState(startNode):
        return []
    s=util.PriorityQueue()
    s.push((startNode,[],0),0)
    visited=[]

    while not s.isEmpty():
        current, actions,prevcost = s.pop()
        if(problem.isGoalState(current)):
            return actions
        if current in visited:
            continue
        visited.append(current)

        succ=problem.getSuccessors(current)
        for nextNode,action,cost in succ:
            newactions=actions+[action]
            newcost=prevcost+cost
            fCost=newcost+heuristic(nextNode,problem)
            s.push((nextNode,newactions,newcost),fCost)

    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch

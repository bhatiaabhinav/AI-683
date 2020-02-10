from AI_683.common.search_problem import SearchProblem, State
from typing import Callable, Set, Tuple, List
import queue


class Node:
    """Node data structure used for graph-search"""

    def __init__(self, state, cost, parent_node=None):
        self.cost = cost  # g-value of the node
        self.state = state  # the state of the problem contained in the node
        self.parent_node = parent_node

    def __str__(self):
        return "(State: {0}, g: {1})".format(str(self.state), self.cost)

    def __repr__(self):
        return "(State: {0}, g: {1})".format(repr(self.state), self.cost)

    def __lt__(self, other):
        return self.cost < other.cost

    def print_trace_to_parent(self):
        parent = self
        while parent is not None:
            print(str(parent), end=' <- ')
            parent = parent.parent_node
        print('')


class PriorityDict:
    '''a hybrid data structure. dictionary + priorityqueue. FIFO behavior to break ties between priorities'''
    def __init__(self):
        # TODO: change to DELETED_VALUE
        self.DELETED_VALUE = object()  # used to mark a key-value pair as deleted in O(1) time.
        self._ke_map = {}  # key to priorityqueue entry map of legit keys
        self._ek_map = {}  # entry to key map of legit keys
        self._pq = queue.PriorityQueue()  # the priority queue to hold entries in (priority, id, value) format
        self._counter = 0  # to assign a unique id to every value to break same priority ties. Causes FIFO behavior.

    def add(self, key, priority, value):
        '''Adds a new key-value pair with given priority'''
        assert key not in self._ke_map, "Key already present"
        entry = (priority, self._counter, value)
        self._counter += 1
        self._pq.put(entry)
        self._ke_map[key] = entry
        self._ek_map[entry] = key

    def pop(self):
        '''retrieve lowest priority entry and remove it. Returns (priority, value) tuple'''
        while not self._pq.empty():
            entry = self._pq.get()
            if entry[-1] == self.DELETED_VALUE:
                # automatically popped. No housekeeping needed in other data structs.
                assert entry not in self._ek_map, "A deleted entry found in hashmap"
                continue
            else:
                key = self._ek_map[entry]
                del self._ke_map[key]
                del self._ek_map[entry]
                return entry[0], entry[-1]
        raise KeyError('The queue is empty')

    def get(self, key, default=None):
        '''retrieve an entry (priority, value) based on key. Returns `default` if key not found'''
        if key in self._ke_map:
            entry = self._ke_map[key]
            assert entry[-1] != self.DELETED_VALUE, "How did this happen. Item deleted but present in hashmap"
            return entry[0], entry[-1]
        else:
            return default

    def __getitem__(self, key):
        '''retrieve an entry (priority, value) based on key. Raises KeyError if key not present'''
        entry = self._ke_map[key]
        assert entry[-1] != self.DELETED_VALUE, "How did this happen. Item deleted but present in hashmap"
        return entry[0], entry[-1]

    def delete(self, key):
        '''deletes an entry based on key'''
        entry = self._ke_map.get(key)
        if entry is not None:
            assert entry[-1] != self.DELETED_VALUE, "How did this happen. Item deleted but present in hashmap"
            del self._ke_map[key]
            del self._ek_map[entry]
            entry[-1] = self.DELETED_VALUE

    def __delitem__(self, key):
        '''deletes an entry based on key. Raises Keyerror if key not present'''
        entry = self._ke_map[key]
        if entry is not None:
            assert entry[-1] != self.DELETED_VALUE, "How did this happen. Item deleted but present in hashmap"
            del self._ke_map[key]
            del self._ek_map[entry]
            entry[-1] = self.DELETED_VALUE

    def __contains__(self, key):
        '''checks if there is an entry with given key'''
        return key in self._ke_map

    def __len__(self):
        assert len(self._ke_map) == len(self._ek_map), "Something is wrong. Length of ke and ek maps are different"
        return len(self._ke_map)


def graph_search(problem: SearchProblem, exploration_order_fn: Callable[[Node], float]) -> Tuple[Node, List[Tuple[Node, float]]]:
    """[summary]

    Arguments:
        problem {SearchProblem} -- [description]
        exploration_order_fn {Callable[[Node], float]} -- [description]

    Returns:
        Tuple[Node, List[Node]] -- goal_node, oredered list of (node, f-value of node) which were expanded
    """

    # start node:
    start_node = Node(problem.start_state, 0)

    # initialize frontier with start_node
    frontier = PriorityDict()
    frontier.add(start_node.state, exploration_order_fn(start_node), start_node)

    # intialize explored
    explored_states_set = set()  # type: Set[State]
    explored_nodes_list = []  # type: List[Node]

    while not len(frontier) == 0:
        # choose the node to explore from the frontier:
        f_value, node = frontier.pop()

        # add this state to set of explored states
        explored_states_set.add(node.state)
        explored_nodes_list.append((f_value, node))

        # test the node:
        if problem.goal_test(node.state):
            return node, explored_nodes_list

        # now expand the node:
        legal_actions = problem.operators(node.state)
        for action in legal_actions:
            child_state = problem.successor_fn(node.state, action)
            child_node = Node(child_state, node.cost + problem.path_cost(node.state, action, child_state), parent_node=node)
            if child_state not in explored_states_set and child_state not in frontier:
                # add to frontier:
                frontier.add(child_state, exploration_order_fn(child_node), child_node)
            elif child_state in frontier:
                old_f, old_node = frontier[child_state]
                if old_node.cost > child_node.cost:
                    # replace the old_node with child_node
                    del frontier[child_state]
                    frontier.add(child_state, exploration_order_fn(child_node), child_node)

    return None  # failure

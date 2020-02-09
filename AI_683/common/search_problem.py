from typing import Set


class State:
    """Search State (i.e. a node) of a `SearchProblem`"""
    pass


class Action:
    """Action (i.e. an edge) in  a `Search Problem`"""
    pass


class SearchProblem:
    """
    Abstract Class for a classical search problem definition.
    As defined by Russel & Norvig AI textbook.
    """

    def __init__(self, start_state: State):
        self.start_state = start_state

    def goal_test(self, s: State) -> bool:
        """Tests whether state s is a goal state

        Arguments:
            s {State} -- [description]

        Raises:
            NotImplementedError: [description]

        Returns:
            bool -- [description]
        """
        raise NotImplementedError()

    def operators(self, s: State) -> Set[Action]:
        """Returns a set of legal actions in the given state s

        Arguments:
            s {State} -- [description]

        Returns:
            Set[Action] -- [description]
        """
        raise NotImplementedError()

    def successor_fn(self, s: State, a: Action) -> State:
        """Returns the state caused due taking action a in state s

        Arguments:
            s {State} -- [description]
            a {Action} -- [description]

        Returns:
            State -- next state
        """
        raise NotImplementedError()

    def path_cost(self, s: State, a: Action, ns: State) -> float:
        """Returns a positive cost incurred by executing the given action a in state s and reaching ns

        Arguments:
            s {State} -- [description]
            a {Action} -- [description]
            ns {State} -- [description]

        Returns:
            float -- a positive cost
        """
        raise NotImplementedError()

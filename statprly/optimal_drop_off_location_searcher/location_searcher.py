"""
Provide an implementation of the optimal drop-off location searcher.
"""


class OptimalDropOffLocationSearcher:
    """
    Implementation of the optimal drop-off location searcher.
    """

    def __init__(self, loss):
        self.loss = loss

    def get_optimal_location_index(self, heatmap: list) -> int:
        """
        Get optimal location for sending a help to a person.

        :param heatmap: histogram of non-normalized probability location of the person.
        :return: optimal location index.
        """
        optimal_heat_condition = sum(heatmap) / 2
        optimal_heat = 0
        for i in range(len(heatmap)):
            if optimal_heat >= optimal_heat_condition:
                return i - 1

            optimal_heat += heatmap[i]

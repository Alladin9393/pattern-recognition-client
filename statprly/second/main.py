class OptimalDropOffLocationSearcher:
    def __init__(self, loss):
        self.loss = loss

    def get_optimal_location_index(self, heatmap):
        optimal_heat_condition = sum(heatmap) / 2
        optimal_heat = 0
        for i in range(len(heatmap)):
            if optimal_heat >= optimal_heat_condition:
                return i - 1

            optimal_heat += heatmap[i]

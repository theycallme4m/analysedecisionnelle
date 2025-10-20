class Action:
    def __init__(self, name, cost, profit_pct):
        self.name = name
        self.cost = float(cost)
        # profit_pct is provided as percentage (e.g., 5 or '5%') -> store as fraction
        self.profit_pct = float(profit_pct) / 100.0
        self.profit_value = self.cost * self.profit_pct

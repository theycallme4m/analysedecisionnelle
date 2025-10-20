class BruteForceController:
    @staticmethod
    def run(actions, budget):
        valid_actions = [a for a in actions if a.cost > 0 and a.profit_value > 0]
        if not valid_actions:
            print("Aucune action valide à traiter.")
            return {"selected_actions": [], "total_cost": 0, "total_profit": 0}

        valid_actions.sort(key=lambda a: a.profit_value / a.cost, reverse=True)

        selected_actions = []
        total_cost = 0
        total_profit = 0

        for action in valid_actions:
            if total_cost + action.cost <= budget:
                selected_actions.append(action)
                total_cost += action.cost
                total_profit += action.profit_value

        return {
            "selected_actions": selected_actions,
            "total_cost": total_cost,
            "total_profit": total_profit
        }

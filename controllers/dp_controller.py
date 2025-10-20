import numpy as np

class DPController:
    @staticmethod
    def run(actions, budget, scale=100):
        """
        Programmation dynamique rapide avec scaling.
        scale : divise les coûts pour réduire la taille du tableau DP.
        """
        # Filtrer les actions valides
        actions = [a for a in actions if a.cost > 0 and a.profit_value > 0]
        n = len(actions)
        if n == 0:
            print("Aucune action valide à traiter.")
            return {"selected_actions": [], "total_cost": 0, "total_profit": 0}

        # Scaling : on divise les coûts pour réduire la taille du DP
        scaled_costs = [max(1, int(a.cost / scale)) for a in actions]  # au moins 1
        profits = [a.profit_value for a in actions]
        scaled_budget = int(budget / scale)

        # DP 1D
        dp = np.zeros(scaled_budget + 1)
        choice = np.full((n, scaled_budget + 1), False, dtype=bool)

        for i in range(n):
            cost, profit = scaled_costs[i], profits[i]
            for w in range(scaled_budget, cost - 1, -1):
                new_profit = dp[w - cost] + profit
                if new_profit > dp[w]:
                    dp[w] = new_profit
                    choice[i][w] = True

        # Reconstruction du portefeuille
        selected_actions = []
        w = scaled_budget
        for i in range(n - 1, -1, -1):
            if choice[i][w]:
                selected_actions.append(actions[i])
                w -= scaled_costs[i]

        total_cost = sum(a.cost for a in selected_actions)
        total_profit = sum(a.profit_value for a in selected_actions)

        return {
            "selected_actions": selected_actions[::-1],  # garder ordre initial
            "total_cost": total_cost,
            "total_profit": total_profit
        }

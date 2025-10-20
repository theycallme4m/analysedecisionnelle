class ResultView:
    @staticmethod
    def display_results(result, method_name):
        print(f"\n=== Résultats ({method_name}) ===")
        print(f"Nombre d'actions sélectionnées : {len(result['selected_actions'])}")
        print(f"Coût total : {result['total_cost']:.2f} F CFA")
        print(f"Bénéfice total : {result['total_profit']:.2f} F CFA\n")

        print("Actions sélectionnées :")
        for action in result['selected_actions']:
            print(f"- {action.name} | Prix : {action.cost:.2f} | Profit : {action.profit_value:.2f}")

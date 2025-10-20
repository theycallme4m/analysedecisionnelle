from models.action_model import Action
from controllers.brute_force_controller import BruteForceController


def test_bruteforce_returns_valid_structure_and_within_budget():
    budget = 500
    actions = [
        Action('A0', 100.0, 5),
        Action('A1', 200.0, 10),
        Action('A2', 50.0, 2.5),
        Action('A3', 500.0, 20),
        Action('A4', 5.0, 1),
        Action('A5', 120.0, 7.5),
    ]

    res = BruteForceController.run(actions, budget=budget)

    # expected keys
    assert 'selected_actions' in res
    assert 'total_cost' in res
    assert 'total_profit' in res

    # cost must not exceed budget
    assert res['total_cost'] <= budget

    # all selected items must be from the input list
    names_in = {a.name for a in actions}
    for a in res['selected_actions']:
        assert a.name in names_in

import time
from views.menu_view import MenuView
from views.result_view import ResultView
from controllers.data_controller import DataController
from controllers.brute_force_controller import BruteForceController
from controllers.dp_controller import DPController

BUDGET = 500000  # Budget fixe (F CFA)


def main():
    print("\n=== OPTIMISATION D'INVESTISSEMENT (Horizon 2 ans) ===\n")

    # 1️⃣ Choix du dataset
    file_path = MenuView.select_dataset()
    method_choice = MenuView.select_method()

    # 2️⃣ Chargement des données
    actions = DataController.load_data(file_path)
    if len(actions) == 0:
        print("❌ Aucune donnée valide trouvée. Vérifie ton fichier CSV (name, price, profit_pct).")
        return
    print(f"\n✅ {len(actions)} actions chargées depuis '{file_path}'\n")

    # 3️⃣ Choix de la méthode (fourni par MenuView)
    choice = method_choice

    # --- Exécution selon le choix ---
    if choice == "1":
        # Méthode brute uniquement
        print("\n>>> Exécution : Force Brute (améliorée) ...")
        t0 = time.perf_counter()
        result = BruteForceController.run(actions, budget=BUDGET)
        t1 = time.perf_counter()
        ResultView.display_results(result, "Force Brute (améliorée)")
        print(f"⏱ Temps d'exécution : {t1 - t0:.4f} s")

    elif choice == "2":
        # Méthode optimisée (DP améliorée)
        print("\n>>> Exécution : Programmation Dynamique (optimisée) ...")
        t0 = time.perf_counter()
        result = DPController.run(actions, budget=BUDGET)
        t1 = time.perf_counter()
        ResultView.display_results(result, "Programmation Dynamique (optimisée)")
        print(f"⏱ Temps d'exécution : {t1 - t0:.4f} s")

    elif choice == "3":
        # Comparatif entre BruteForce et DP
        print("\n>>> Exécution comparée : BruteForce vs DP (optimisée) ...\n")

        # --- BruteForce ---
        print("⏳ Méthode BruteForce en cours...")
        t0 = time.perf_counter()
        result_brute = BruteForceController.run(actions, budget=BUDGET)
        t1 = time.perf_counter()
        brute_time = t1 - t0
        ResultView.display_results(result_brute, "Force Brute")

        # --- DP Optimisée ---
        print("\n⏳ Méthode DP (optimisée) en cours...")
        t0 = time.perf_counter()
        result_dp = DPController.run(actions, budget=BUDGET)
        t1 = time.perf_counter()
        dp_time = t1 - t0
        ResultView.display_results(result_dp, "DP (optimisée)")

        # --- Comparatif final ---
        print("\n=== 📊 COMPARATIF FINAL ===")
        print(f"BruteForce : coût={result_brute['total_cost']:.2f} | profit={result_brute['total_profit']:.2f} | temps={brute_time:.4f}s")
        print(f"DP Optimisée : coût={result_dp['total_cost']:.2f} | profit={result_dp['total_profit']:.2f} | temps={dp_time:.4f}s")

        if result_dp['total_profit'] > result_brute['total_profit']:
            print("\n✅ La méthode optimisée est plus performante !")
        else:
            print("\n⚙️ La méthode brute donne un meilleur résultat dans ce cas.")
    else:
        print("❌ Choix invalide. Fin du programme.")

    print("\nProgramme terminé.\n")


if __name__ == "__main__":
    main()

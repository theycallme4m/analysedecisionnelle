class MenuView:
    @staticmethod
    def select_dataset():
        print("=== Choix du dataset ===")
        print("1 - data_test.csv")
        print("2 - dataset1_Python.csv")
        print("3 - dataset2_Python.csv")
        choice = input("➡️ Votre choix : ").strip()

        if choice == "1":
            return "data_test.csv"
        elif choice == "2":
            return "dataset1_Python.csv"
        elif choice == "3":
            return "dataset2_Python.csv"
        else:
            print("❌ Choix invalide, dataset par défaut : data_test.csv")
            return "data_test.csv"

    @staticmethod
    def select_method():
        print("\n=== Choix de la méthode ===")
        print("1 - Force Brute (améliorée)")
        print("2 - Programmation Dynamique (optimisée)")
        # Option 3 (FPTAS) retirée du projet
        print("3 - Comparatif BruteForce vs DP optimisée")
        choice = input("➡️ Votre choix : ").strip()
        return choice

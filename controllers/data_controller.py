import os
import pandas as pd
from models.action_model import Action


class DataController:
    @staticmethod
    def _resolve_path(file_path):
        if os.path.isabs(file_path) and os.path.exists(file_path):
            return file_path
        if os.path.exists(file_path):
            return file_path
        repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        candidate = os.path.join(repo_root, 'data', file_path)
        if os.path.exists(candidate):
            return candidate
        candidate = os.path.join(os.getcwd(), 'data', file_path)
        if os.path.exists(candidate):
            return candidate
        raise FileNotFoundError(f"Fichier non trouvé: '{file_path}'")

    @staticmethod
    def load_data(file_path):
        path = DataController._resolve_path(file_path)

        # Détecter le séparateur
        with open(path, 'r', encoding='utf-8') as f:
            first = f.readline()
        sep = ';' if ';' in first else ','

        data = pd.read_csv(path, sep=sep, engine='python')

        # Normaliser les noms de colonnes
        normalized = {c: c.strip().lower() for c in data.columns}
        data.rename(columns=normalized, inplace=True)
        cols = list(data.columns)

        # Identifier les colonnes principales
        name_col = next((c for c in cols if 'name' in c or 'action' in c or 'nom' in c), None)
        price_col = next((c for c in cols if 'price' in c or 'cout' in c or 'cost' in c or 'prix' in c), None)
        profit_col = next((c for c in cols if 'profit' in c or 'bénéf' in c or 'benef' in c or 'gain' in c or 'profit_pct' in c), None)

        if not all([name_col, price_col, profit_col]):
            raise ValueError(f"Colonnes non reconnues: {cols}")

        actions = []
        skipped = 0
        for _, row in data.iterrows():
            try:
                # Nettoyer et convertir les valeurs
                name = str(row[name_col]).strip()
                price = float(str(row[price_col]).replace(',', '').strip())
                profit = float(str(row[profit_col]).replace('%', '').replace(',', '.').strip())
                if price <= 0 or profit <= 0:
                    skipped += 1
                    continue
                actions.append(Action(name, price, profit))
            except Exception:
                skipped += 1
                continue

        print(f"✅ {len(actions)} actions valides chargées depuis '{path}' (ignorées {skipped})")
        return actions

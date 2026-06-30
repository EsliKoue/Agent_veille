import os

def create_project_structure():
    # Définition de la structure
    structure = {
        "src": ["__init__.py", "agent.py", "tools.py", "prompts.py", "main.py"],
        "tests": ["__init__.py"],
        "": [".env", ".gitignore", "requirements.txt", "README.md"]
    }

    # Contenu de base pour certains fichiers
    files_content = {
        "requirements.txt": "langgraph\nlangchain-groq\nlangchain-community\ntavily-python\npython-dotenv",
        ".gitignore": ".env\n__pycache__/\n*.pyc\n.venv/\n.DS_Store",
        "README.md": "# Projet : Veille Concurrentielle Agentique\n\nAgent autonome de veille stratégique utilisant Groq, LangGraph et Tavily."
    }

    # Création des dossiers et fichiers
    for folder, files in structure.items():
        if folder:
            os.makedirs(folder, exist_ok=True)
        
        for file in files:
            path = os.path.join(folder, file)
            if not os.path.exists(path):
                with open(path, "w", encoding="utf-8") as f:
                    f.write(files_content.get(file, ""))
                print(f"Créé : {path}")

    print("\n✅ Structure du projet créée avec succès !")

if __name__ == "__main__":
    create_project_structure()
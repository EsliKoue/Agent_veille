# src/prompts.py

QUERY_GENERATOR_PROMPT = """
Tu es un analyste expert en services financiers et banques en Côte d'Ivoire.
Génère 3 requêtes de recherche stratégique pour Tavily sur le secteur Fintech et Bancaire ivoirien.
Cible :
1. Actualités récentes sur les solutions de paiement mobile, néobanques et innovations bancaires en CI.
2. Évolutions réglementaires de la BCEAO impactant les acteurs locaux.
3. Partenariats stratégiques entre banques traditionnelles et startups Fintech à Abidjan.

Format : Liste JSON pure. Exemple: ["innovations paiement mobile Côte d'Ivoire", "réglementation BCEAO Fintech", "partenariats banques startups Abidjan"]
"""

REPORT_WRITER_PROMPT = """
Tu es un consultant en stratégie financière à Abidjan. 
Rédige une note de synthèse professionnelle sur la base des informations collectées :
- Contexte sectoriel (Fintech/Banque CI)
- Faits saillants (nouveautés produits, réglementations)
- Analyse d'impact : comment cela transforme-t-il le marché ivoirien ?
- Conclusion pour un décideur.
"""
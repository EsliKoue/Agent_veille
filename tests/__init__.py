from src.agent import app

# Testons l'impact de Wave dans le paysage financier ivoirien
config = {"company": "Wave Côte d'Ivoire"}
result = app.invoke(config)

print("\n--- RAPPORT FINAL ---\n")
print(result['report'])
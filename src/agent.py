# src/agent.py
import json
import re
from langgraph.graph import StateGraph, END
from langchain_groq import ChatGroq
from src.tools import get_search_tool
from src.prompts import QUERY_GENERATOR_PROMPT, REPORT_WRITER_PROMPT

# Initialisation du modèle Groq
llm = ChatGroq(
    groq_api_key="gsk_VOTRE_CLE_GROQ_ICI", # Remplace par ta clé réelle
    model_name="llama-3.3-70b-versatile"
)

# Structure de l'état pour assurer la persistance des données
class AgentState(dict):
    company: str
    queries: list
    context: list
    report: str

# --- NODES ---

def generate_queries(state):
    print("--- GÉNÉRATION DES REQUÊTES : SECTEUR BANQUE/FINTECH CI ---")
    response = llm.invoke(QUERY_GENERATOR_PROMPT)
    
    content = response.content.strip()
    # Nettoyage robuste pour extraire la liste JSON
    match = re.search(r'\[.*\]', content, re.DOTALL)
    try:
        queries = json.loads(match.group() if match else content)
    except json.JSONDecodeError:
        queries = ["innovations paiement mobile Côte d'Ivoire", "actualité bancaire BCEAO", "Fintech Abidjan"]
        
    return {"queries": queries, "company": state.get('company', "Fintech et Banque CI")}

def search_web(state):
    print("--- EXÉCUTION DE LA RECHERCHE ---")
    tool = get_search_tool()
    results = [str(tool.invoke(q)) for q in state['queries']]
    return {"context": results, "company": state['company'], "queries": state['queries']}

def write_report(state):
    print("--- RÉDACTION DU RAPPORT STRATÉGIQUE ---")
    context = "\n".join(state['context'])
    prompt = REPORT_WRITER_PROMPT + f"\n\nInformations collectées : {context}"
    
    response = llm.invoke(prompt)
    return {"report": response.content}

# --- CONSTRUCTION DU GRAPHE ---
workflow = StateGraph(dict)

workflow.add_node("generator", generate_queries)
workflow.add_node("search", search_web)
workflow.add_node("writer", write_report)

workflow.set_entry_point("generator")
workflow.add_edge("generator", "search")
workflow.add_edge("search", "writer")
workflow.add_edge("writer", END)

app = workflow.compile()
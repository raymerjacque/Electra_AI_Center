"""
AI Training Guide Generator for MakuluLinux
Generates step-by-step guides for training AI models locally on MakuluLinux systems.
"""

PLUGIN_NAME = "AI Training Guide Generator"
PLUGIN_VERSION = "1.0.0"
PLUGIN_DESCRIPTION = "Generates step-by-step guides for training AI models locally on MakuluLinux"
PLUGIN_AUTHOR = "AI Assistant"
PLUGIN_ENABLED = True
PLUGIN_TYPE = "ROUTER"
PLUGIN_TRIGGERS = ["comment entraîner une IA", "comment entraîner un modèle d'IA", "entraîner une IA", "train AI", "AI training guide"]
PLUGIN_ROUTE_TOKEN = "AITRAINING"

def run(prompt: str, context: dict) -> str:
    try:
        guide = generate_ai_training_guide(context)
        return guide
    except Exception as e:
        context["print_fn"](f"Error generating AI training guide: {str(e)}")
        return "Failed to generate AI training guide. Please try again later."

def generate_ai_training_guide(context: dict) -> str:
    base_guide = """# Guide d'entraînement d'une IA sur MakuluLinux

## Prérequis
1. **MakuluLinux** (basé sur Ubuntu/Cinnamon)
2. **Python 3.10+** (préinstallé sur MakuluLinux)
3. **Terminal Electra** (votre application AI)
4. **Connexion internet** pour télécharger les modèles

## Installation des dépendances

bash
sudo apt update
sudo apt install -y python3-pip python3-venv git
## Méthode recommandée : Utiliser Ollama (solution locale)

### 1. Installer Ollama
bash
curl -fsSL https://ollama.com/install.sh | sh
### 2. Télécharger un modèle de base
bash
ollama pull llama3
### 3. Entraîner votre modèle personnalisé
bash
# Créer un fichier de données d'entraînement (format JSONL)
echo '{"prompt": "Bonjour", "response": "Salut ! Comment puis-je vous aider ?"}' > training_data.jsonl

# Entraîner le modèle (remplacez 'monmodele' par votre nom)
ollama create monmodele -f training_data.jsonl
## Alternative : Utiliser AutoGen (Microsoft)

### 1. Installer AutoGen
bash
pip install autogen
### 2. Créer un script d'entraînement
# train_autogen.py
from autogen import AssistantAgent, UserProxyAgent, config_list_from_json

config_list = config_list_from_json(env_or_file="OAI_CONFIG_LIST")
assistant = AssistantAgent("assistant", llm_config={"config_list": config_list})
user_proxy = UserProxyAgent("user_proxy", code_execution_config=False)

user_proxy.initiate_chat(
    assistant,
    message="Entraîne un petit modèle de chatbot sur des exemples de conversation française."
)
### 3. Exécuter le script
bash
python3 train_autogen.py
## Conseils pour MakuluLinux
- Utilisez `context["print_fn"]()` pour afficher la progression dans l'interface Electra
- Les modèles entraînés seront stockés dans `~/.ollama/models` (environ 1-3GB par modèle)
- Pour les grands modèles (>7B paramètres), assurez-vous d'avoir au moins 16GB de RAM
- Utilisez `ollama serve` pour démarrer le serveur local si nécessaire

## Ressources supplémentaires
- Documentation Ollama: https://github.com/jmorganca/ollama
- Tutoriels AutoGen: https://microsoft.github.io/autogen/
- Communauté MakuluLinux: https://forum.makululinux.com

Souhaitez-vous que je génère un guide plus spécifique pour un type de modèle particulier ?
"""

    # Personnaliser le guide avec le contexte actuel
    if "workspace" in context and context["workspace"]:
        base_guide += f"\n\n## Votre espace de travail actuel\n{context['workspace']}"

    return base_guide
<h1>Langchain Modular Component(Model)</h1>
📖 Overview
This repository serves as a flexible integration layer for LangChain, enabling developers to unify model interaction across different sources. Whether you need the high-reasoning capabilities of closed-source APIs (like OpenAI/Anthropic) or the privacy and cost-efficiency of open-source models (via Ollama/HuggingFace), this project provides a clean, abstract interface to manage them.

🚀 Core Capabilities
Unified Model Interface: Abstracted implementation allows you to swap model backends by changing a single configuration key.

Hybrid Workflow Support: Simultaneously leverage closed-source models for complex task planning and open-source models for lightweight, high-volume tasks.

Modular Architecture: Designed to minimize boilerplate and simplify the integration of new model providers as they emerge.

LangChain Integration: Fully utilizes LangChain’s LCEL (LangChain Expression Language) for robust prompt chaining and state management.

🛠 Tech Stack
Framework: Python 3.10+, LangChain

Model Providers:

Closed: [e.g., OpenAI GPT-4, Anthropic Claude]

Open: [e.g., Llama 3, Mistral (via Ollama/vLLM)]

Environment: Pydantic-Settings for configuration management.

⚙️ Quick Start
Installation
Bash
# Clone the repository
git clone https://github.com/[your-username]/[repo-name].git
cd [repo-name]

# Install dependencies
pip install -r requirements.txt
Configuration
Create a .env file in the project root to manage your credentials:

Code snippet
# Credentials for Closed-Source
OPENAI_API_KEY=sk-...

# Configuration for Open-Source
LLM_PROVIDER=ollama
OLLAMA_MODEL_NAME=llama3
Usage
Initialize the model wrapper via the unified factory:

Python
from src.llm_factory import ModelManager

# The manager handles the backend switch based on .env config
manager = ModelManager()
response = manager.query("Explain the importance of modularity in AI curriculum design.")

print(response)
🏗 Architecture Concept
The project is built around an Adapter Pattern, separating the execution logic from the provider-specific API calls. This ensures that your business logic (curriculum processing, data analysis, etc.) remains decoupled from the specific underlying LLM.

🤝 Contributing
Contributions, issues, and feature requests are welcome! If you find this framework useful for your own AI/ML projects, feel free to submit a pull request.

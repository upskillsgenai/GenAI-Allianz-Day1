# ⚙️ How to Create a Virtual Environment in VS Code

```bash
# 📂 1. Create project folder
mkdir my-project
cd my-project

# 🐍 2. Create virtual environment
python -m venv alliaz-day-1

# ▶️ 3. Activate virtual environment
# On Windows
.\alliaz-day-1\Scripts\Activate

# On macOS/Linux
source alliaz-day-1/bin/activate

# 📄 4. Create requirements.txt (inside project folder)


# ✏️ 5. Update requirements.txt with your needed packages

# 📦 6. Install all packages from requirements.txt
pip install -r requirements.txt

# 7. Type Ctrl+Shift+P ->  “Python: Select Interpreter” and select the one that points to your new virtual environment

# 8. If virtual environment not founded then find the path will include your folder and .<venv>\Scripts\python.exe

--

# 🧠 Generative AI Learning Resources

A curated list of foundational articles and documentation for understanding Generative AI, LLMs, and LangChain.

---

## 📅 Day 1 Resources

### 🔍 Core Concepts
- [What is Generative AI?](https://medium.com/@social_65128/the-comprehensive-guide-to-understanding-generative-ai-c06bbf259786)
- [Language Models (Gentle Introduction)](https://mark-riedl.medium.com/a-very-gentle-introduction-to-large-language-models-without-the-hype-5f67941fa59e)
- [What is a Large Language Model (LLM)?](https://medium.com/data-science-at-microsoft/how-large-language-models-work-91c362f5b78f)
- [LLM Providers Overview](https://mehmetozkaya.medium.com/llm-providers-openai-meta-ai-anthropic-hugging-face-microsoft-google-and-mistral-ai-46ad8c027f6b)

### 🛠 Prompt Engineering & Techniques
- [Prompt Engineering: Complete Guide](https://medium.com/@fareedkhandev/prompt-engineering-complete-guide-2968776f0431)
- [Few-Shot Learning: Step-by-Step Guide](https://medium.com/ubiai-nlp/step-by-step-guide-to-mastering-few-shot-learning-a673054167a0)
- [Chain of Thought (CoT) Prompting](https://medium.com/data-science/advanced-prompt-engineering-chain-of-thought-cot-8d8b090bf699)

### ⚙️ Advanced Generation Parameters
- [Temperature, Top-K, Top-P Explained](https://rumn.medium.com/setting-top-k-top-p-and-temperature-in-llms-3da3a8f74832)

### 🧮 Data & Embeddings
- [Vector Databases: Beginner’s Guide](https://medium.com/data-and-beyond/vector-databases-a-beginners-guide-b050cbbe9ca0)
- [What Are Embeddings?](https://medium.com/@eugenesh4work/what-are-embeddings-and-how-do-it-work-b35af573b59e)

---

## 📅 Day 2 Resources

### 🧩 LangChain Essentials
- [LangChain Introduction](https://python.langchain.com/docs/introduction/)
- [Prompt Templates](https://python.langchain.com/docs/concepts/prompt_templates/)
- [LLM Chains in Action](https://medium.com/@zshariff70/langchain-simple-llm-chains-in-action-bda6950afc71)
- [LangChain Expression Language (LCEL)](https://python.langchain.com/docs/concepts/lcel/)

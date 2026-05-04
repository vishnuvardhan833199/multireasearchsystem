# 🔬 ResearchMind — Multi-Agent AI Research System

ResearchMind is a **multi-agent AI system** that autonomously performs deep research on any topic by coordinating multiple specialized agents.

It combines **web search, content scraping, structured writing, and critical evaluation** into a single pipeline to generate high-quality research reports.

---

## 🚀 Features

* 🔍 **Search Agent** — Finds recent, relevant information from the web

* 📄 **Reader Agent** — Scrapes and extracts detailed content from sources

* ✍️ **Writer Agent** — Generates structured research reports

* 🧐 **Critic Agent** — Reviews and scores the report

* ⚡ Built with **LangChain + Groq LLM**

* 🌐 Real-time data using **Tavily Search API**

* 🖥️ Interactive UI using **Streamlit**

* 📄 Downloadable research reports

---

## 🧠 Architecture

```
User Input
   ↓
Search Agent (Tavily)
   ↓
Reader Agent (Web Scraper)
   ↓
Writer Chain (LLM)
   ↓
Critic Chain (LLM)
   ↓
Final Report + Feedback
```

---

## 📦 Tech Stack

* LangChain (Agents + Chains)
* Groq LLM (`llama-3.3-70b-versatile`)
* Tavily Search API
* BeautifulSoup (Web Scraping)
* Streamlit (Frontend UI)

---

## 📁 Project Structure

```
multiresearchsystem/
│
├── app.py               # Streamlit UI
├── pipeline.py          # CLI pipeline runner
├── agents.py            # Agent + LLM setup
├── tools.py             # Search + Scraper tools
├── requirements.txt     # Dependencies
├── .env                 # API keys (ignored)
├── .env.example         # Sample env file
└── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/vishnuvardhan833199/multireasearchsystem.git
cd multireasearchsystem
```

---

### 2️⃣ Create virtual environment

```bash
python -m venv .venv
source .venv/bin/activate   # Mac/Linux
```

---

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Setup

Create a `.env` file in the root directory:

```env
TAVILY_API_KEY=your_tavily_api_key
GROQ_API_KEY=your_groq_api_key
MODEL_NAME=llama-3.3-70b-versatile
```

⚠️ **Do NOT commit `.env` to GitHub**

---

## ▶️ Run the Application

### 🖥️ Streamlit UI

```bash
python -m streamlit run app.py
```

---

### 💻 CLI Mode

```bash
python pipeline.py
```

Then enter your research topic:

```
Enter a research topic: Impact of war on stock markets
```

---

## 🧪 Example Use Cases

* Market analysis (stocks, economy, geopolitics)
* Scientific research summaries
* Technology trend reports
* Policy and global event analysis

---

## 📄 Output

The system generates:

* Structured research report
* Key findings
* Source references
* Critic feedback with score

---

## ⚠️ Important Notes

* API keys are required for:

  * Tavily (search)
  * Groq (LLM)
* Models may change due to provider updates (use `.env` for flexibility)

---

## 🛠️ Future Improvements

* Multi-step reasoning agents
* Memory-enabled agents
* Multi-model fallback (Groq + Gemini)
* Better source validation
* Vector DB integration

---

## 🤝 Contributing

Feel free to fork the repo and improve:

* Agent reasoning
* UI enhancements
* New tools integration

---

## 📜 License

This project is open-source and available under the MIT License.

---

## 👨‍💻 Author

**Vishnu Vardhan**
GitHub: https://github.com/vishnuvardhan833199

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub!

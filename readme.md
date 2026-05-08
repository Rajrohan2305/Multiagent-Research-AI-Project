````markdown
# 🤖 Multi-Agent Research AI System

An autonomous multi-agent AI research system built using Mistral AI, Tavily Search API, LangChain, and Streamlit.

This project performs intelligent web research, extracts detailed information from websites, generates professional research reports, and evaluates the quality of generated reports using specialized AI agents.

---

# 🚀 Features

- 🔍 Web Research Agent
- 📚 URL Scraping & Deep Reading
- ✍️ AI Report Generation
- 🧠 Critic & Evaluation Agent
- 🌐 Streamlit Professional UI
- 📄 Downloadable Research Reports
- ⚡ Real-time Multi-Agent Workflow
- 🧩 Modular Agent Architecture

---

# 🏗️ Architecture

```text
User Topic
    ↓
Search Agent
    ↓
Reader Agent
    ↓
Writer Agent
    ↓
Critic Agent
    ↓
Final Professional Report
````

---

# 🧠 Agents Used

## 1. Search Agent

Responsible for:

* Searching the web using Tavily API
* Finding reliable and recent information
* Returning titles, URLs, and snippets

---

## 2. Reader Agent

Responsible for:

* Scraping URLs
* Cleaning webpage content
* Extracting meaningful text for research

---

## 3. Writer Agent

Responsible for:

* Generating structured professional reports
* Creating detailed insights
* Producing factual summaries

---

## 4. Critic Agent

Responsible for:

* Reviewing generated reports
* Giving quality feedback
* Providing report ratings and improvements

---

# 🛠️ Tech Stack

* Python
* Streamlit
* LangChain
* Mistral AI
* Tavily API
* BeautifulSoup4
* Requests
* dotenv

---

# 📂 Project Structure

```text
multiagent_project/
│
├── app.py
├── agents.py
├── tools.py
├── pipeline.py
├── requirements.txt
├── README.md
└── .env
```

---

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone https://github.com/your-username/multi-agent-research-ai.git

cd multi-agent-research-ai
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file:

```env
TAVILY_API_KEY=your_tavily_api_key

MISTRAL_API_KEY=your_mistral_api_key
```

---

# ▶️ Run The Project

```bash
streamlit run app.py
```

---

# 📸 UI Features

* Interactive dashboard
* Research progress tracking
* Agent activity logs
* Report viewer
* Critic feedback section
* Download report button

---

# 📄 Example Workflow

1. User enters a research topic
2. Search Agent gathers web information
3. Reader Agent scrapes detailed content
4. Writer Agent creates research report
5. Critic Agent evaluates the report
6. Final report displayed in UI

---

# 🔥 Example Topics

* Future of Artificial Intelligence
* AI in Healthcare
* Impact of Climate Change
* Blockchain Technology
* Quantum Computing
* Future of Robotics

---

# 📌 Future Improvements

* LangGraph Integration
* PDF Export
* Citation Engine
* Real-Time Streaming
* Vector Database Memory
* Multi-Query Research
* Research History
* RAG Integration
* Agent Visualization
* Docker Deployment

---

# 🌍 Deployment

This project can be deployed using:

* Streamlit Community Cloud
* Render
* Railway
* Hugging Face Spaces

---

# 👨‍💻 Author

Raj Rohan

B.Tech AIML Student | AI & ML Enthusiast

---

# ⭐ If You Like This Project

Give this repository a star ⭐ on GitHub.

```
```

# DocuWeb: Interactive Document Knowledge Mapper
DocuWeb is an advanced GraphRAG (Retrieval-Augmented Generation) application designed to transform massive, complex PDF documents into interactive, visual Knowledge Graphs. Built specifically for students and researchers, DocuWeb strips away dense walls of text and reveals the underlying web of interconnected concepts, helping users master complex topics efficiently.

🚀 Key Features
Context-Preserving Text Chunking: Implements a mathematical Sliding Window Algorithm to break down documents without slicing sentences or destroying contextual links.

Strict Type Enforcement: Leverages Pydantic v2 declarative schemas to force raw LLM outputs into exact JSON data constraints at native runtime speeds.

Deterministic Entity Resolution: Uses an optimized pipeline to dynamically resolve duplicate concepts, merge distinct multi-chunk contextual descriptions, and build an unbroken global state.

Interactive UI: A beautifully clean frontend mapping system built with Streamlit to click, explore, and isolate nodes and relationships.

🛠️ System Architecture
DocuWeb is built following strict Separation of Concerns (SoC) engineering principles, dividing the ingestion, translation, and rendering pipelines into decoupled, modular blocks:

[Uploaded Document] 
       │
       ▼
[document_chunker.py] ──► Extracts text & runs Sliding Window Chunking
       │
       ▼
[graph_engine.py]      ──► Leverages Gemini Structured Outputs + Pydantic v2
       │
       ▼
[pipeline.py]          ──► Mathematical entity resolution & node merging
       │
       ▼
[app.py (Streamlit)]   ──► Renders the interactive visual network UI
⚙️ Installation & Setup
1. Clone the Repository
Bash
git clone https://github.com/MuhammadAwaisKhalil/DocuWeb.git
cd DocuWeb
2. Install Dependencies
Install the required modern AI stack libraries (including PyPDF2 for extraction and Pydantic's optimized email validator plugins):

Bash
pip install pydantic "pydantic[email]" google-genai PyPDF2 streamlit
3. Set up Environment Variables
DocuWeb utilizes the modern google-genai SDK, which automatically scans for your API key via your system environment. Secure your key from Google AI Studio:

Mac/Linux:

Bash
export GEMINI_API_KEY="your_actual_api_key_here"
Windows (PowerShell):

PowerShell
$env:GEMINI_API_KEY="your_actual_api_key_here"
🕹️ Quick Start
To boot up the interactive UI development server and process your first document, run:

Bash
streamlit run app.py
Open http://localhost:8501 in your browser, upload any textbook chapter or research document, and watch the semantic information network generate in real-time.

📄 Core Codebase Blueprint
document_chunker.py: Reads raw PDF bytes, cleans layout anomalies, and handles the mathematical array pointer sliding window logic.

graph_engine.py: Configures the GenAI client using gemini-2.5-flash, defining data blueprints for Node, Edge, and the master KnowledgeGraph.

pipeline.py: Resolves structural naming duplicates and performs deterministic deduplication on network relations using fast native Python hashing sets.

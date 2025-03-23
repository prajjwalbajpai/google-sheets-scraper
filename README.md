# Google Sheets AI Scraper

This repository includes the backend code for Google Sheets AI Scraper which can be deployed locally.

---

## 🗂️ Directory Structure

```bash
├── app
│   ├── functions
│   │   ├── __init__.py
│   │   └── scrapers.py
│   └── main.py
├── .gitignore
├── requirements.txt
└── README.md
```


---

## 🚀 Getting Started

### Prerequisites

- **Python 3.9+**: Ensure Python is installed on your machine.
- **pip**: Python package manager.

### Installation Steps

1. **Clone the repository**:

```bash
git clone https://github.com/prajjwalbajpai/google-sheets-scraper.git
cd google-sheets-scraper
```

2. **Set up a virtual environment** (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate
```

3. **Install dependencies**:
```bash
pip install -r requirements.txt
```

4. **Run the application locally**:

```bash
python app/main.py
```


---

## 🛠️ Configuration

- The `requirements.txt` file contains all necessary packages for the project.

- For sensitive information (e.g., API keys), create a `.env` file in the root directory.

- After running the backend locally, you can send requests from frontend in google sheets to scrape data. 

---



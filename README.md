# LeaderPath Wizard 🧭

A **gamified, assistant-driven design tool** built for **Theme 3: Efficiency and Assistant Tools**. It empowers education leaders — such as NGO heads and school principals — to move from a blank page to a structured, data-driven program design using a guided wizard interface.

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![HTML](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![MIT License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

---

## ✨ Features

- 🧠 **Linked List-based wizard** — each step is a node guiding the user forward
- 📋 **3-step design flow** — Problem Definition → Stakeholder Mapping → Impact Indicators
- 🎯 **Education-focused** — built for NGO heads and school principals
- 🌐 **Flask web app** with multi-page HTML templates
- 📊 **Summary page** — shows all collected inputs at the end
- 🔄 **Step-by-step navigation** — can't skip steps

---

## 🗂️ Project Structure

```
LeaderPath-Wizard/
├── app.py                  # Flask routes and app logic
├── leaderpath_logic.py     # Linked List wizard engine
├── ShikshaLokam.py         # Core project logic
├── templates/
│   ├── index.html          # Landing page
│   ├── wizard.html         # Step-by-step wizard UI
│   └── summary.html        # Final summary page
├── LICENSE
└── README.md
```

---

## 🔧 How the Wizard Works

The wizard is powered by a **custom Linked List** data structure:

```python
class DesignNode:
    def __init__(self, step_id, step_name, prompt, description):
        self.step_id = step_id
        self.step_name = step_name
        self.prompt = prompt
        self.user_input = ""
        self.next = None  # Points to next step

# Steps chain:
# Problem Definition → Stakeholder Mapping → Impact Indicators → Summary
```

Each step collects input and moves to the next node until complete.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8+

### Installation

```bash
git clone https://github.com/Eshwarkadari/LeaderPath-Wizard.git
cd LeaderPath-Wizard
pip install flask
python app.py
```

Open **http://localhost:5000** in your browser.

---

## 📋 Wizard Steps

| Step | Name | Description |
|------|------|-------------|
| 1 | Problem Definition | Define the core educational challenge |
| 2 | Stakeholder Mapping | Identify who is impacted |
| 3 | Impact Indicators | Set measurable success goals |

---

## 👨‍💻 Author

**Kadari Eshwar** — [github.com/Eshwarkadari](https://github.com/Eshwarkadari)

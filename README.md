<div align="center">

# 🌐 Web Fundamentals Lab

**Learn how the web works — by doing it.**

An interactive, browser-based learning lab that teaches web foundations through hands-on demos, live code editors, and animated visualizations.

[![Python](https://img.shields.io/badge/Python-3.8+-3776ab?logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.3+-000000?logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

</div>

---

<!-- 🖼️ SCREENSHOT PLACEHOLDER
     Take a screenshot of the lab running in your browser and save it as screenshot.png
     in the root of this repo, then uncomment the line below:
-->
<!-- ![Web Fundamentals Lab Screenshot](screenshot.png) -->

> **📸 To add the screenshot:** Take a screenshot of the app running at `http://localhost:5000`, save it as `screenshot.png` in the repo root, then uncomment the image line above in this README.

---

## 🎯 Who is this for?

Anyone who wants to understand **how the pieces fit together** before diving into a specific framework or language.

- 👩‍💼 **Non-technical professionals** — understand what your dev team is building
- 🎓 **Students** — get the mental model before your first web dev course
- 🤔 **Curious minds** — ever wondered what happens when you click "Add to Cart"?

---

## 🧠 What you will learn

> From zero to "I understand how the entire web works" in 10 steps.

1. 📡 How two computers talk over HTTP (request/response)
2. 🔤 What GET, POST, PUT, DELETE actually mean
3. 🏗️ How HTML, CSS, and JavaScript each contribute to a web page
4. 🖥️ The difference between frontend and backend
5. ⏳ How backend tech evolved (CGI/Perl → PHP → Python/Node → C#/Java)
6. 🔌 What REST APIs are and why JSON is the universal data format
7. 🛒 How a modern e-commerce site works end-to-end

---

## 📋 The 10 Steps

| Step | Topic | What you do |
|:----:|-------|-------------|
| **1** | 📡 What is HTTP? | Watch an animated request/response between two computers |
| **2** | 🔤 HTTP Methods | Expand each verb (GET/POST/PUT/DELETE) — call a live restaurant API |
| **3** | 🏗️ HTML | Edit HTML in a live editor, see it render instantly |
| **4** | 🎨 CSS | Add styling to HTML — change colors, fonts, layout in real time |
| **5** | ⚡ JavaScript | Build a working "Add to Cart" button with live cart counter |
| **6** | 🖥️ Frontend | Compare traditional page reloads vs modern single-page apps |
| **7** | ⚙️ Backend | **Same endpoint in 6 languages** — Perl, PHP, Python, Node, C#, Java |
| **8** | 🔌 APIs & REST | Full API explorer — send any method/URL, see the JSON response |
| **9** | 🛒 E-commerce | Live shopping flow: browse → add to cart → checkout (real API calls) |
| **10** | 🎮 The Full Picture | **Fullscreen animated walkthrough** — click through each layer |

---

## 🚀 How to run

```bash
# 1. Clone the repository
git clone https://github.com/deepjyotisaha/learn-web-basics.git
cd learn-web-basics

# 2. (Optional) Create a virtual environment
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Start the lab
python app.py

# 5. Open your browser
#    http://localhost:5000
```

> 💡 Press `Ctrl+C` in the terminal to stop the server.

---

## ✅ Prerequisites

| Requirement | Details |
|-------------|---------|
| 🐍 Python | 3.8 or higher |
| 📦 Flask | Installed via `pip install -r requirements.txt` |
| 🌐 Browser | Chrome, Edge, or Firefox |

> **No API keys, no database, no Node.js, no build tools needed.**

---

## 📁 File structure

```
learn-web-basics/
├── app.py               🐍 Flask backend — restaurant API, product catalog,
│                           cart, checkout endpoints
├── requirements.txt     📦 Just Flask
├── README.md            📖 This file
├── LICENSE              ⚖️  MIT License
├── .gitignore           🚫 Python/OS ignores
└── templates/
    └── index.html       🎨 The entire lab UI — all 10 steps, interactive demos,
                            live editors, animated visualizations (single file)
```

---

## 💡 Key design decisions

### 📄 Everything in one HTML file

The entire frontend is a single `index.html`. No build step, no bundler, no npm. This is intentional — the lab teaches web fundamentals, so the lab itself should be fundamental. Students can View Source and see exactly how it works.

### 🔌 Real API endpoints

The Flask backend has real REST endpoints (`/menu`, `/order`, `/api/products`, `/api/cart`, `/api/checkout`). Students don't just read about APIs — they call them and see real JSON responses.

### 🌍 Same endpoint in 6 languages (Step 7)

Step 7 shows the exact same "list products" endpoint written in **CGI/Perl, PHP, Python/Flask, Node.js/Express, C#/ASP.NET, and Java/Spring**. Every version follows the same 3-step pattern:

```
1. LISTEN  — "when someone sends GET /api/products, run this function"
2. QUERY   — "get the data"
3. RESPOND — "send it back as JSON"
```

> The language is a preference. The concept is universal.

### 🎮 Game-like fullscreen flow (Step 10)

Step 10 launches a fullscreen split-screen visualization:

| Panel | Width | Shows |
|-------|-------|-------|
| 🖥️ **Your Browser** | 37% | Page rendering, JS events, DOM updates |
| ⚙️ **The Server** | 37% | REST API, business logic, database |
| 📖 **Narration** | 26% | Step-by-step explanation + code snippets |

**Animated arrows** fly between browser and server. User clicks **Next Step** to advance — each click reveals cards, ticks checkboxes, changes button colors, and shows before/after DOM diffs.

The full flow (12 steps):

```
Type URL → GET → Server sends HTML → Browser renders
    ↓
Click "Add to Cart" → JS event → POST → REST API
    ↓
Business logic → Database → Response → JS modifies the DOM
```

---

## 📡 API Reference

### 🍽️ Restaurant API (Steps 1-2)

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/menu` | Full restaurant menu |
| `GET` | `/menu?type=starter` | Filter by type (starter/main/dessert) |
| `POST` | `/order` | Place an order `{dish, qty}` |
| `PUT` | `/order/:id` | Update an order |
| `DELETE` | `/order/:id` | Cancel an order |

### 🛒 Product API (Steps 7-9)

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/products` | List all products |
| `GET` | `/api/products?category=electronics` | Filter by category |
| `GET` | `/api/products/:id` | Get one product |
| `GET` | `/api/cart` | View cart |
| `POST` | `/api/cart` | Add to cart `{product_id, qty}` |
| `DELETE` | `/api/cart` | Clear cart |
| `POST` | `/api/checkout` | Place order |

---

## 🔧 Troubleshooting

<details>
<summary><strong>Port already in use</strong></summary>

```bash
# Change the port in app.py (last line):
app.run(debug=False, threaded=True, port=5001)
```
</details>

<details>
<summary><strong>Page shows old content after code changes</strong></summary>

- Stop the server (`Ctrl+C`), restart it (`python app.py`), then hard-refresh the browser (`Ctrl+Shift+R`)
- Flask caches templates in memory — a server restart is required after editing `index.html`
</details>

<details>
<summary><strong>Cached browser version</strong></summary>

- Use `Ctrl+Shift+R` (hard refresh) or open in incognito mode
</details>

---

## 🙏 Inspired by

This lab follows the same progressive, step-by-step teaching pattern as the **Meal Planner Agent Lab** from the *Fundamentals of LLMs & Agents* course. Each step adds exactly one new concept and lets you interact with it before moving on.

---

<div align="center">

**Built with ❤️ for learners who want to understand the web, not just use it.**

</div>

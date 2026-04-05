# Web Fundamentals Lab

An interactive, browser-based learning lab that teaches the foundations of how the web works — from HTTP requests to full-stack e-commerce flows — through hands-on demos, live code editors, and animated visualizations.

Built as a single Flask app with zero external dependencies beyond Flask itself. No database, no build step, no frontend framework. Just `python app.py` and open your browser.

---

## Who is this for?

Anyone new to web development who wants to understand **how the pieces fit together** before diving into a specific framework or language. Ideal for:

- Non-technical professionals learning about web apps
- Students starting their first web development course
- Anyone who wants to understand what happens when you click "Add to Cart"

---

## What you will learn

By the end of this lab, you will understand:

1. How two computers talk to each other over HTTP (request/response)
2. What GET, POST, PUT, DELETE actually mean
3. How HTML, CSS, and JavaScript each contribute to a web page
4. The difference between frontend and backend
5. How backend technology evolved (CGI/Perl → PHP → Python/Node.js → C#/Java)
6. What REST APIs are and why JSON is the universal data format
7. How a modern e-commerce site works end-to-end

---

## The 10 Steps

| Step | Topic | Demo |
|------|-------|------|
| **1** | What is HTTP? | Animated visualization of two computers exchanging a request/response |
| **2** | HTTP Methods | Collapsible accordion — try GET, POST, PUT, DELETE against a live restaurant API |
| **3** | HTML — Structure | Live editor with instant preview — edit HTML and see it render |
| **4** | CSS — Styling | Dual-tab editor (HTML + CSS) with live preview |
| **5** | JavaScript — Behavior | Full HTML + CSS + JS editor — working "Add to Cart" with cart counter |
| **6** | Frontend Tech Stack | Side-by-side comparison: traditional full-page reload vs modern SPA |
| **7** | Backend Tech Stack | **Same endpoint in 6 languages** (Perl, PHP, Python, Node.js, C#, Java) — proves the concept is universal |
| **8** | APIs & REST | Full API explorer — send any method/URL and see the response |
| **9** | E-commerce Flow | Live cart: browse products → add to cart → checkout with real API calls |
| **10** | The Complete Picture | **Fullscreen animated walkthrough** — watch "Add to Cart" flow from browser → HTTP → server → database → response → DOM update |

---

## How to run

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

Press `Ctrl+C` in the terminal to stop the server.

---

## Prerequisites

- Python 3.8 or higher
- Flask (installed via `pip install -r requirements.txt`)
- A modern browser (Chrome, Edge, Firefox)

No API keys, no database, no Node.js, no build tools needed.

---

## File structure

```
WebBasics/
├── app.py               Flask backend — restaurant API, product catalog,
│                        cart, checkout, echo endpoint
├── requirements.txt     Just Flask
├── README.md            This file
├── .gitignore           Python/OS ignores
└── templates/
    └── index.html       The entire lab UI — all 10 steps, interactive demos,
                         live editors, animated visualizations (single file)
```

---

## Key design decisions

### Everything in one HTML file

The entire frontend is a single `index.html`. No build step, no bundler, no npm. This is intentional — the lab teaches web fundamentals, so the lab itself should be fundamental. Students can View Source and see exactly how it works.

### Real API endpoints

The Flask backend has real REST endpoints (`/menu`, `/order`, `/api/products`, `/api/cart`, `/api/checkout`). Students don't just read about APIs — they call them and see real JSON responses.

### The "same endpoint in 6 languages" pattern (Step 7)

Step 7 shows the exact same "list products" endpoint written in CGI/Perl, PHP, Python/Flask, Node.js/Express, C#/ASP.NET, and Java/Spring. Every version follows the same 3-step pattern: **Listen → Query → Respond**. This drives home that the language is a preference — the concept is universal.

### Game-like fullscreen flow (Step 10)

Step 10 launches a fullscreen split-screen visualization:
- **Left panel (37%)**: Your Browser — shows the page, JS events, DOM updates
- **Center panel (37%)**: The Server — shows REST API, business logic, database
- **Right panel (26%)**: Narration — explains each step with code snippets
- **Animated arrows** fly between browser and server showing HTTP requests/responses
- User clicks **Next Step** to advance — each click reveals the next card and triggers visual side effects (button color changes, checkboxes tick, DOM values update)

The flow covers 12 steps:
1. Type URL → GET request → Server sends HTML → Browser renders page
2. Click "Add to Cart" → JS event → POST request → REST API → Business logic → Database → Response → JS reads JSON → **JS modifies the HTML DOM** (before/after diff)

---

## API Reference

### Restaurant API (Steps 1-2)

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/menu` | Full restaurant menu |
| GET | `/menu?type=starter` | Filter by type (starter/main/dessert) |
| POST | `/order` | Place an order `{dish, qty}` |
| PUT | `/order/:id` | Update an order |
| DELETE | `/order/:id` | Cancel an order |

### Product API (Steps 7-9)

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/products` | List all products |
| GET | `/api/products?category=electronics` | Filter by category |
| GET | `/api/products/:id` | Get one product |
| GET | `/api/cart` | View cart |
| POST | `/api/cart` | Add to cart `{product_id, qty}` |
| DELETE | `/api/cart` | Clear cart |
| POST | `/api/checkout` | Place order |

---

## Troubleshooting

**Port already in use**
```bash
# Change the port in app.py (last line):
app.run(debug=False, threaded=True, port=5001)
```

**Page shows old content after code changes**
- Stop the server (`Ctrl+C`), restart it (`python app.py`), then hard-refresh the browser (`Ctrl+Shift+R`)
- Flask caches templates in memory — a server restart is required after editing `index.html`

**Cached browser version**
- Use `Ctrl+Shift+R` (hard refresh) or open in incognito mode

---

## Inspired by

This lab follows the same progressive, step-by-step teaching pattern as the [Meal Planner Agent Lab](../AI4All%20-%20Hands-on%20-%20Fundamentals%20of%20LLM%20%26%20Agents/python-notebook/10_meal_planner_lab/) from the Fundamentals of LLMs & Agents course. Each step adds exactly one new concept and lets you interact with it before moving on.

# CS 335 — Assignment 01: Working with AI & ML APIs
**Northeastern Illinois University — Introduction to Artificial Intelligence**  
Instructor: O. Adham-Sindy, MS, PMP

---

## Overview

This is the starter code for Assignment 01. Your job is to:

1. Pick a free-tier API from the approved list (or propose your own)
2. Clone the course repo and navigate to this folder
3. Update `starter.py` to point at your chosen API's endpoints
4. Make at least **3 distinct API calls** and print the results to the terminal
5. Submit your GitHub repo link via D2L / Canvas

---

## Step-by-Step Setup

### Step 1 — Clone the Course Repo

Clone the full course repository and navigate to this assignment's folder:

```bash
git clone https://github.com/osindy/NEIU335AI.git
cd NEIU335AI/assignments/assignment-01-api
```

### Step 2 — Create a Virtual Environment

A virtual environment isolates this project's dependencies from your system Python.

```bash
# macOS / Linux
python3 -m venv venv
source venv/bin/activate

# Windows (Command Prompt)
python -m venv venv
venv\Scripts\activate
```

You should see `(venv)` at the start of your prompt — this confirms the environment is active.

### Step 3 — Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4 — Set Up Your API Key

Copy the example environment file and fill in your real API key:

```bash
# macOS / Linux
cp .env.example .env

# Windows
copy .env.example .env
```

Open `.env` in any text editor and replace the placeholder:

```
MY_API_KEY=your_actual_api_key_here
```

> **Important:** Never commit your `.env` file. It is covered by the repo's root `.gitignore`.

### Step 5 — Update the Starter Code

Open `starter.py` and follow every `# TODO` comment:

- Replace `BASE_URL` with your API's base URL
- Update `url`, `params`, and `payload` in each function to match your API's docs
- Replace `data.get("result")` with the actual response key your API returns

### Step 6 — Run the Script

```bash
python starter.py
```

You should see formatted output in the terminal for each of the 3 API calls.

### Step 7 — Push to Your Own GitHub Repo

Create a new repo on your personal GitHub, then push your completed work:

```bash
git remote set-url origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git add .
git commit -m "Assignment 01 — API implementation"
git push -u origin main
```

Update this `README.md` with your name, which API you chose, and a short sample of your terminal output before submitting.

---

## Folder Structure

```
NEIU335AI/
├── .gitignore                        ← Covers the entire repo (root-level)
├── README.md                         ← Course overview
├── lectures/
│   └── ...
└── assignments/
    └── assignment-01-api/            ← You are here
        ├── starter.py                ← Main script — edit this
        ├── .env.example              ← Copy to .env and add your key
        ├── requirements.txt          ← Project dependencies
        └── README.md                 ← This file
```

---

## Submission Checklist

- [ ] At least 3 distinct API calls in `starter.py`
- [ ] Each call prints readable output to the terminal
- [ ] `.env` is NOT committed (verify with `git status` before pushing)
- [ ] `requirements.txt` is up to date
- [ ] This `README.md` updated with your name, API used, and sample output
- [ ] GitHub repo link submitted via D2L / Canvas

---

## Resources

| Resource | Link |
|---|---|
| Free Public APIs | github.com/public-apis/public-apis |
| Python Requests Docs | docs.python-requests.org |
| HTTP Status Codes | developer.mozilla.org/en-US/docs/Web/HTTP/Status |
| python-dotenv | pypi.org/project/python-dotenv |
| Postman (API testing GUI) | postman.com |

# FundFlow — Interactive Dashboard Prototype

FundFlow is an interactive HTML prototype that simulates a budget-monitoring dashboard for youth care funding in the Netherlands. It lets stakeholders explore spending data, contracts, validation errors, and billing declarations — all in a realistic, clickable interface that runs entirely in the browser.

## Confidentiality note

- `datasets-dashboard/` is confidential reference material and should not be opened during prototype work.
- The interactive UI is configured to use synthetic demo rows rendered in-browser for testing and screenshots.
- All shown values are fictional and intended for UX demonstration only.

## What you need to install first

You can run the prototype with either **Node.js** or **Python**.

### Option 1 — Node.js

Install Node.js if you want to use the `npx` server option:

### Step 1 — Install Node.js

1. Go to **https://nodejs.org**
2. Click the big green **"LTS"** download button (LTS = recommended, stable version)
3. Open the downloaded file and follow the installer (just keep clicking Next / Continue)
4. When it's done, **restart your computer**

### Option 2 — Python

Most Mac/Linux systems already include Python 3. Check with:

```bash
python3 --version
```

If a version number is shown, you can use the Python server option below.

---

## How to run the prototype

## GitHub Pages (shareable for the coming month)

Live URL:

```text
https://jonathanvdheuvel.github.io/fundflow-demo/fundflow.html
```

How updates go live:

1. Commit your changes to `main`.
2. Push to GitHub.
3. GitHub Pages publishes from the repository root automatically.

### Option A — Python server (recommended)

1. Open Terminal / Command Prompt
2. Go to the project folder:
   ```
   cd ~/Downloads/milafigma
   ```
   (On Windows, use your full folder path instead.)
3. Start the Python server:
   ```
   python3 serve.py --port 4173
   ```
   Alternative (no script):
   ```
   python3 -m http.server 4173
   ```
4. Open:
   ```
   http://localhost:4173/fundflow.html
   ```

### Option B — Node server

### On Mac

1. Open **Terminal**
   - Press **Cmd + Space**, type `Terminal`, press Enter
2. Type this command and press Enter (replace the path if you unzipped the folder somewhere else):
   ```
   cd ~/Downloads/milafigma
   ```
3. Start the server:
   ```
   npx http-server . -p 3000
   ```
   The first time you run this it may ask *"Need to install the following packages: http-server. Ok to proceed? (y)"* — just type `y` and press Enter.
4. Open your browser (Chrome, Safari, Firefox — any works) and go to:
   ```
   http://localhost:3000/fundflow.html
   ```

### On Windows

1. Open **Command Prompt**
   - Press **Windows key + R**, type `cmd`, press Enter
2. Type this command and press Enter (adjust the path to where you unzipped the folder):
   ```
   cd C:\Users\YourName\Downloads\milafigma
   ```
3. Start the server:
   ```
   npx http-server . -p 3000
   ```
   If it asks to install `http-server`, type `y` and press Enter.
4. Open your browser and go to:
   ```
   http://localhost:3000/fundflow.html
   ```

### To stop the server

Go back to the Terminal / Command Prompt window and press **Ctrl + C**.

---

## How to navigate the prototype

The prototype has **6 screens** you can click through:

1. **Overview** — The main dashboard with KPI cards (budget used, days until breach, data errors, spending trend), a spending-vs-ceiling chart, recent errors, and top spending categories.
2. **Overview with Filters** — Same dashboard but with a filter panel open. You can select insurer, municipality, contract type, and date range. Click "Apply Filters" to see filtered KPI values.
3. **Validation (Error Details)** — A full table of data validation issues with severity levels, statuses, and review actions. Accessible by clicking the "Data Errors" KPI card or the "Validation" nav link.
4. **Export Modal** — A modal dialog for exporting reports in PDF, Excel, or CSV. Choose a scope (full dashboard, filtered view, or error log only) and click "Generate & Download" to see a success toast.
5. **Contracts** — An overview of youth care contracts with insurers. Shows ceiling amounts, usage percentages with progress bars, and contract statuses (Active, Expiring Soon, Suspended). Filters at the top let you narrow by insurer, region, or status.
6. **Reports & Declarations** — A billing overview showing real declaration data with invoice numbers, municipalities, submitted vs. approved amounts, and statuses. Includes filters and a summary total row.

Use the **top navigation bar** to switch between Overview, Contracts, Validation, and Reports.

---

## Troubleshooting

**"Port 3000 is already in use"**
Use a different port number:
```
npx http-server . -p 3001
```
Then open `http://localhost:3001/fundflow.html` instead.

**The page looks too wide**
The prototype now uses responsive scaling. On very small screens, some tables can still scroll horizontally by design.

**Node.js was installed but `npx` is not recognized**
Restart your computer after installing Node.js and try again.

---

## What's in this folder

| File / Folder | What it does |
|---|---|
| `fundflow.html` | The main prototype — all six screens in one HTML file |
| `index.html` | A simple redirect page |
| `capture.html` | Used for Figma screenshots (you can ignore this) |
| `datasets-dashboard/` | Confidential source data (do not open for routine prototype work) |
| `.github/copilot-instructions.md` | Agent guardrails to prevent confidential dataset access |
| `serve.py` | Python local server entry point |
| `CLAUDE.md`, `PROMPT.md`, etc. | Design documentation and planning notes |

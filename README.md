# 2026 Varsity Roster Lookup

A simple, mobile-first web app for quickly looking up players by jersey number from the 2026 Varsity Roster.

## Features
- **Big, readable fonts** optimized for mobile devices and quick glances
- **Live search** — type the number and results appear instantly
- **Color-coded class years**: 
  - Senior → emerald green
  - Junior → sky blue  
  - Sophomore → amber
- Huge jersey number display
- Clear button
- Keyboard friendly (type digits anywhere to focus input)
- Fully self-contained single `index.html` file (no build step)
- Works great on phones, tablets, or desktop

## How to Use
1. Open `index.html` directly in any modern browser (double-click or File → Open).
2. On mobile: transfer the file via AirDrop, email, or USB, then open in Safari/Chrome.
3. For best experience on phone, you can host it:
   - Python: `python3 -m http.server 8080` then visit `http://your-ip:8080`
   - Or upload the single HTML file to any static host (Netlify, Vercel, GitHub Pages, etc.)

## Data
- 76 players
- Source: 2026 Varsity Roster Draft (from PDF export of Google Sheets)
- Includes Killian Ryan (#55, Sophomore)

## Files
- `index.html` — the complete web app (self-contained, ~13KB)
- `roster.json` — raw data (if you want to update the roster separately)

## Customization
To update the roster:
1. Edit the `players` array inside the `<script>` tag in `index.html`, or
2. Regenerate from a new PDF using the original Python extraction script.

Designed for speed and readability on the field or in the stands.

---

**Example lookups:**
- #55 → Killian Ryan — Sophomore
- #1 → Liam Bortel — Senior
- #42 → Danny Cavoli — Junior

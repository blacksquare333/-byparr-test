# G2 Product Scraper

A web scraper that bypasses Cloudflare protection to collect product listings from G2, including name, rating, and review count, then exports the results to Excel.

## 🧑‍💻 Tech Stack

- Python
- Byparr (Cloudflare bypass)
- BeautifulSoup
- Pandas

## ✨ Features

- Bypasses Cloudflare anti-bot protection using Byparr
- Scrapes product name, rating, and review count across multiple pages
- Auto-retry logic on failed requests (up to 5 attempts per page)
- Randomized delays between requests to avoid detection
- Exports results to an Excel file

## 🔧 Setup

1. Clone the repository:
git clone https://github.com/yourusername/g2-scraper.git

cd g2-scraper

2. Install dependencies:
pip install -r requirements.txt

3. Start Byparr locally (requires Docker):
docker run -d -p 8191:8191 ghcr.io/thephaseless/byparr:latest

4. Run the scraper:
python app.py
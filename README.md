# Jackfruit-Project
CashCrabCruzers - Team 11 end sem project

# 💱 Currency Converter with 7-Day Historical Chart

A desktop GUI application built with **Python** and **CustomTkinter** that allows users to:

- Convert currencies in real-time using **ExchangeRate API**.
- View the last 7-day exchange rate trends using **Frankfurter API**.
- Display a list of all supported currencies.

---

## 🛠 Features

- **Real-time conversion:** Instantly convert any amount between supported currencies.  
- **Historical chart:** Plot a 7-day line chart for currency trends.  
- **Supported currencies:** Easily view all currency codes supported by the APIs.  
- **User-friendly GUI:** Modern dark-themed interface built with `CustomTkinter`.  
- **Error handling:** Validates inputs and handles network/API errors gracefully.  

---

💡 Challenges Faced

Handling API failures or network issues gracefully.

Ensuring Frankfurter API always returns 7 days of data (some days missing due to weekends/holidays).

Input validation for amounts and currency codes.

Making the GUI visually appealing while keeping it lightweight.

---

🔧 Scope for Improvement

Add support for more historical data (last 30 days or more).

Include multiple chart types (line, bar, area).

Add a “Swap Currencies” button.

Export conversion history or chart data to CSV.

Optimize performance and caching for large currency datasets.

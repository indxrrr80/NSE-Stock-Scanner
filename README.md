<p align="center">
  <img src="assets/banner.png" alt="NSE Stock Scanner Banner" width="100%">
</p>

<h1 align="center">📈 NSE Stock Scanner</h1>

<p align="center">
  <strong>A modular Python application for analyzing NSE Bhavcopy data and generating Excel reports using multiple stock screening strategies.</strong>
</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas)
![Git](https://img.shields.io/badge/Git-Version%20Control-F05032?style=for-the-badge&logo=git)
![GitHub](https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github)

</p>

---

# 📖 Overview

The **NSE Stock Scanner** is a Python-based project that analyzes daily NSE Bhavcopy data and filters stocks based on predefined trading strategies.

The project generates Excel reports that help traders quickly identify stocks with high delivery percentages, unusual trading volume, price gaps, and bullish or bearish price movements.

The application is built using a modular architecture, making it easy to extend with additional technical indicators and scanners.

---

# ✨ Features

- ✅ High Delivery Scanner
- ✅ High Volume Scanner
- ✅ Gap Up Scanner
- ✅ Gap Down Scanner
- ✅ Bullish Candle Scanner
- ✅ Bearish Candle Scanner
- ✅ High Delivery + High Volume Scanner
- ✅ Gap Up + High Volume Scanner
- ✅ Automatic Excel Report Generation
- ✅ Logging Support
- ✅ Modular Python Project Structure

---

# 📂 Project Structure

```text
NSE-Stock-Scanner
│
├── assets/
│   └── banner.png
│
├── Data/
│   ├── bhavcopy.csv
│   ├── delivery.csv
│   └── sec_bhavdata_full_24062026.csv
│
├── Output/
│
├── scanner/
│   ├── __init__.py
│   ├── config.py
│   ├── data_loader.py
│   ├── filters.py
│   ├── logger.py
│   ├── reports.py
│   └── utils.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

# 🛠 Technologies Used

- Python
- Pandas
- OpenPyXL
- Git
- GitHub
- VS Code

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/indxrrr80/NSE-Stock-Scanner.git
```

Move into the project directory

```bash
cd NSE-Stock-Scanner
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Project

Execute

```bash
python main.py
```

You will see:

```text
============================================================
               NSE STOCK SCANNER
============================================================

1. High Delivery Scanner
2. High Volume Scanner
3. Gap Up Scanner
4. Gap Down Scanner
5. Bullish Candle Scanner
6. Bearish Candle Scanner
7. High Delivery + High Volume
8. Gap Up + High Volume

Enter Scanner Number:
```

Choose any scanner to generate an Excel report inside the **Output** folder.

---

# 📊 Available Scanners

| Scanner | Description |
|----------|-------------|
| High Delivery | Filters stocks with high delivery percentage |
| High Volume | Filters stocks with high traded quantity |
| Gap Up | Detects stocks opening above previous close |
| Gap Down | Detects stocks opening below previous close |
| Bullish Candle | Closing Price > Opening Price |
| Bearish Candle | Closing Price < Opening Price |
| High Delivery + High Volume | Combined delivery and volume filter |
| Gap Up + High Volume | Combined gap up and volume filter |

---

# 📁 Output

The application automatically generates Excel reports.

Examples:

- High_Delivery.xlsx
- High_Volume.xlsx
- Gap_Up.xlsx
- Gap_Down.xlsx
- Bullish_Candles.xlsx
- Bearish_Candles.xlsx

---

# 🚀 Future Improvements

- RSI Scanner
- EMA Scanner
- SMA Scanner
- MACD Scanner
- Breakout Scanner
- Candlestick Pattern Detection
- Automatic NSE Data Download
- Interactive Dashboard
- Advanced Excel Formatting
- Unit Testing
- CI/CD with GitHub Actions

---

# 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

If you'd like to contribute:

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Open a Pull Request

---

# 👨‍💻 Author

**Inder Mohindra**

B.Tech Computer Science Engineering

UPES, Dehradun

GitHub: **https://github.com/indxrrr80**

---

<p align="center">

⭐ If you found this project helpful, consider giving it a star!

</p>


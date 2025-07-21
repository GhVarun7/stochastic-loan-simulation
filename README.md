# Stochastic-Loan-Simulation

Stochastic Profitability Modeling for Digital Lending (INR)

This project simulates long-term profitability for a portfolio of digital loans using stochastic modeling in Python. It captures real-world uncertainty by factoring in variable interest rates, borrower defaults, and loan segment behaviors.

## 📌 Problem Statement

Digital lending platforms face uncertainty in borrower behavior, repayment, and profitability. This simulation models profit/loss outcomes over thousands of loans across different borrower segments (e.g., Retail and MSME) using stochastic variables.

## 💡 Key Concepts

- Randomized loan amounts and interest rates (Normal distribution)
- Segment-based default probabilities
- Partial recovery for defaulted loans
- Profit = interest earned (if no default) OR loss due to unrecovered principal

## 🧪 Methodology

- Number of Loans: 10,000
- Segments: Retail (60%), MSME (40%)
- Defaults: Retail – 5%, MSME – 10%
- Recovery rate: 30%
- Interest: Normally distributed, mean = 15%

## 📊 Outputs

- Average profit per loan (in INR)
- Segment-wise profit distribution
- Histogram of profit across all loans

## 🖥️ How to Run

1. Clone the repo:

2. Create a virtual environment:
   python -m venv venv
   source venv/bin/activate # or venv\Scripts\activate on Windows
  
3. Install requirements:
   pip install -r requirements.txt
   
4. Run the simulation:
   python simulation.py
   
5. View <img width="2553" height="1388" alt="image" src="https://github.com/user-attachments/assets/6db5012f-466e-4c10-a63c-3b706caf3937" />


## 📁 File Structure

- `simulation.py`: Main simulation logic
- `loan_simulation.ipynb`: Notebook version for interactive use
- `results/profit_histogram.png`: Visual output
- `requirements.txt`: Dependencies

## ✍️ Author

Varun Gehlot – Independent Quantitative Research Project (2024)

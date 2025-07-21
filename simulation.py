# simulation.py

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Set random seed for reproducibility
np.random.seed(42)

# Configuration
num_loans = 10000
mean_loan_inr = 500000  # Avg loan in INR
interest_mu = 0.15  # Mean 15% interest
interest_sigma = 0.05  # Interest standard deviation
recovery_rate = 0.3  # 30% recovered if defaulted

# Loan segments
segments = ['Retail', 'MSME']
default_probs = {'Retail': 0.05, 'MSME': 0.10}
segment_dist = [0.6, 0.4]  # 60% Retail, 40% MSME

# Simulate loans
data = []

for _ in range(num_loans):
    loan_amount = np.random.normal(mean_loan_inr, 25000)
    interest_rate = np.random.normal(interest_mu, interest_sigma)
    segment = np.random.choice(segments, p=segment_dist)
    default = np.random.rand() < default_probs[segment]

    if default:
        profit = -loan_amount * (1 - recovery_rate)
    else:
        profit = loan_amount * interest_rate

    data.append({
        'Segment': segment,
        'LoanAmount_INR': round(loan_amount),
        'InterestRate': round(interest_rate, 3),
        'Defaulted': default,
        'Profit_INR': round(profit)
    })

# Create DataFrame
df = pd.DataFrame(data)

# Output results
print("Overall Expected Profit per Loan (INR):", round(df['Profit_INR'].mean()))
print("\nSegment-wise Profit Summary:")
print(df.groupby('Segment')['Profit_INR'].agg(['mean', 'std', 'count']).round())
# Plot profit distribution
import os
os.makedirs("results", exist_ok=True)

plt.figure(figsize=(10,6))
plt.hist(df['Profit_INR'], bins=50, color='mediumseagreen', edgecolor='black')
plt.title("Profit Distribution per Loan (INR)")
plt.xlabel("Profit (₹)")
plt.ylabel("Number of Loans")
plt.grid(True)
plt.savefig("results/profit_histogram.png")
plt.show()


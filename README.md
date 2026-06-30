# Fleet Cost & Maintenance Optimizer 🚚💼

A Python-based decision support tool designed for **Logistics Managers** and **Financial Controllers** to optimize corporate fleet maintenance budgets and prevent operational losses.

## 📈 Business Case & Value Proposition
Unplanned vehicle breakdowns can cost an enterprise up to 3 times more than preventive maintenance. This project applies an engineering approach to operations by:
* **Predicting Risk**: Evaluating vehicle breakdown probability using mileage and asset age.
* **Capital Allocation**: Optimizing a constrained budget by prioritizing high-risk corporate assets.
* **Financial Impact**: Maximizing Return on Investment (ROI) by calculating net cost savings.

## 🛠️ Tech Stack & Skills Demonstrated
* **Language**: Python 3
* **Libraries**: Pandas (Data Manipulation)
* **Methodology**: Object-Oriented Programming (OOP), Data-Driven Decision Making

## 🚀 How It Works
The core algorithm calculates a dynamic `Risk_Score` for each vehicle asset:

\[Risk\_Score = \left(\frac{Mileage}{150,000} \times 0.6\right) + \left(\frac{Age}{10} \times 0.4\right)\]

Vehicles scoring above `0.75` are flagged for urgent maintenance. The budget allocation engine then selects assets to service, generating a **3x cost-mitigation saving** for every euro spent efficiently.

## 📦 Installation & Usage
1. Clone this repository:
   ```bash
   git clone https://github.com
   ```
2. Run the script:
   ```bash
   python fleet_optimizer.py
   ```

## 📊 Sample Output
```text
=== FLEET OPTIMIZATION REPORT ===
  Vehicle_ID  Risk_Score  Urgent_Action  Budget_Allocated
0       V-01        0.88           True              True
1       V-02        0.26          False             False
2       V-03        1.00           True              True
3       V-04        0.16          False             False
4       V-05        0.78           True             False

Total Net Savings Generated: 5400.0 EUR
```

---
**Author**: Andela Stojanovic  
*Management Engineering Student | Certified in Power BI, Python (Cisco) & Google Project Management*

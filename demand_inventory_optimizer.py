"""
Demand-Driven Inventory Optimizer for Fashion Retail
---------------------------------------------------

Author:
Andela Stojanovic

Purpose:
Support inventory planning by combining inventory levels,
customer demand, fashion trends and back-in-stock requests.

This project demonstrates how Business Analysts can use
Python to support inventory decisions and reduce both
stockouts and overstock situations.
"""

from dataclasses import dataclass
import pandas as pd


@dataclass
class ProductDecision:
    """Stores the optimization results for one product."""

    product: str
    demand_score: float
    inventory_days: float
    recommendation: str


class DemandInventoryOptimizer:
    """Demand-driven inventory optimization engine."""

    def __init__(self):
        self.inventory = None

    def load_inventory(self, data: dict):

        self.inventory = pd.DataFrame(data)

        return self.inventory


load_inventory()
    def calculate_inventory_metrics(self):
        """Calculates demand score and inventory indicators."""

        if self.inventory is None:
            raise ValueError("No inventory data loaded.")

        # Days of Inventory
        self.inventory["Inventory_Days"] = (
            self.inventory["Current_Stock"]
            / self.inventory["Weekly_Sales"]
        ).round(1)

        # Demand Score (0–100)
        self.inventory["Demand_Score"] = (
            self.inventory["Weekly_Sales"] * 0.40
            + self.inventory["Trend_Score"] * 0.35
            + self.inventory["Waiting_Customers"] * 0.25
        ).round(1)

        # Reorder Point
        self.inventory["Reorder_Point"] = (
            self.inventory["Weekly_Sales"]
            * self.inventory["Lead_Time_Weeks"]
            + self.inventory["Safety_Stock"]
        )

        return self.inventory

calculate_inventory_metrics()
    def generate_recommendations(self):
        """Generates inventory recommendations for each product."""

        if "Demand_Score" not in self.inventory.columns:
            self.calculate_inventory_metrics()

        recommendations = []

        for _, product in self.inventory.iterrows():

            if (
                product["Current_Stock"] < product["Reorder_Point"]
                and product["Demand_Score"] >= 80
            ):
                recommendation = "REORDER NOW"

            elif (
                product["Current_Stock"] < product["Reorder_Point"]
                and product["Demand_Score"] >= 60
            ):
                recommendation = "MONITOR"

            elif (
                product["Inventory_Days"] > 12
                and product["Demand_Score"] < 40
            ):
                recommendation = "DISCOUNT CANDIDATE"

            else:
                recommendation = "HOLD INVENTORY"

            recommendations.append(recommendation)

        self.inventory["Recommendation"] = recommendations

        return self.inventory

generate_recommendations()
    def generate_management_report(self):
        """Creates a management summary with key inventory KPIs."""

        if "Recommendation" not in self.inventory.columns:
            self.generate_recommendations()

        reorder_products = (
            self.inventory["Recommendation"] == "REORDER NOW"
        ).sum()

        monitor_products = (
            self.inventory["Recommendation"] == "MONITOR"
        ).sum()

        discount_products = (
            self.inventory["Recommendation"] == "DISCOUNT CANDIDATE"
        ).sum()

        estimated_budget = (
            self.inventory.loc[
                self.inventory["Recommendation"] == "REORDER NOW",
                "Unit_Cost"
            ].sum()
        )

        average_demand = round(
            self.inventory["Demand_Score"].mean(), 1
        )

        print("\n========== INVENTORY MANAGEMENT REPORT ==========\n")

        print(f"Products Analysed: {len(self.inventory)}")
        print(f"Reorder Immediately: {reorder_products}")
        print(f"Monitor: {monitor_products}")
        print(f"Discount Candidates: {discount_products}")
        print(f"Average Demand Score: {average_demand}")
        print(f"Estimated Purchasing Budget: €{estimated_budget}")

        print("\n=============== PRODUCT DETAILS ===============\n")

        print(
            self.inventory[
                [
                    "Product",
                    "Demand_Score",
                    "Inventory_Days",
                    "Recommendation",
                ]
            ]
        )

        return self.inventory

if __name__ == "__main__":

    sample_data = {
        "Product": [
            "White Linen Shirt",
            "Classic Jeans",
            "Summer Dress",
            "Black Jacket",
            "Basic T-Shirt",
        ],
        "Current_Stock": [25, 80, 18, 250, 35],
        "Weekly_Sales": [55, 35, 42, 8, 60],
        "Trend_Score": [95, 70, 90, 20, 98],
        "Waiting_Customers": [48, 12, 38, 2, 75],
        "Lead_Time_Weeks": [2, 2, 3, 2, 2],
        "Safety_Stock": [30, 25, 25, 15, 40],
        "Unit_Cost": [22, 35, 40, 90, 15],
    }

    optimizer = DemandInventoryOptimizer()

    optimizer.load_inventory(sample_data)

    optimizer.calculate_inventory_metrics()

    optimizer.generate_recommendations()

    optimizer.generate_management_report()

"""
Demand-Driven Inventory Optimizer for Fashion Retail

Author:
Andela Stojanovic

Purpose:
Support inventory planning through demand forecasting and
inventory optimization using Python.
"""

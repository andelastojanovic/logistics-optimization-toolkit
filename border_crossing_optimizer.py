"""
Border Crossing Operations Simulator
------------------------------------

Simulation of customs border performance for the Trieste–Belgrade
logistics corridor.

Author:
Andela Stojanovic

Purpose:
Support logistics managers and operations teams by estimating customs
capacity, congestion levels and operational performance through
business-oriented KPIs.
"""

from dataclasses import dataclass


@dataclass
class BorderCrossingResult:
    """Stores the simulation results."""

    status: str
    arriving_trucks: int
    processed_trucks: int
    delayed_trucks: int
    queue_length: int
    waiting_time_hours: float
    border_utilization: float
    total_capacity: int
    recommendation: str


class BorderCrossingSimulator:
    """Simulates customs border operations and congestion."""

    def __init__(self, open_gates: int, capacity_per_gate: int = 15):
        self.open_gates = open_gates
        self.capacity_per_gate = capacity_per_gate

    def simulate(self, arriving_trucks: int) -> BorderCrossingResult:

        total_capacity = self.open_gates * self.capacity_per_gate

        utilization = round((arriving_trucks / total_capacity) * 100, 1)

        processed = min(arriving_trucks, total_capacity)

        delayed = max(arriving_trucks - total_capacity, 0)

        queue = delayed

        if delayed == 0:
            waiting_time = 0.15
        else:
            waiting_time = round(delayed / total_capacity, 2)

        if utilization < 80:
            status = "OPTIMAL"
            recommendation = "No action required."

        elif utilization < 100:
            status = "BUSY"
            recommendation = "Monitor traffic conditions."

        elif utilization < 130:
            status = "CONGESTED"
            recommendation = "Consider opening an additional customs gate."

        else:
            status = "CRITICAL"
            recommendation = "Deploy emergency customs resources immediately."

        return BorderCrossingResult(
            status=status,
            arriving_trucks=arriving_trucks,
            processed_trucks=processed,
            delayed_trucks=delayed,
            queue_length=queue,
            waiting_time_hours=waiting_time,
            border_utilization=utilization,
            total_capacity=total_capacity,
            recommendation=recommendation,
        )


def print_report(result: BorderCrossingResult):

    print("\n========================================")
    print("      BORDER PERFORMANCE REPORT")
    print("========================================")

    print(f"Incoming Trucks:      {result.arriving_trucks}")
    print(f"Open Gates Capacity:  {result.total_capacity} trucks/hour")
    print(f"Processed Trucks:     {result.processed_trucks}")
    print(f"Delayed Trucks:       {result.delayed_trucks}")
    print(f"Queue Length:         {result.queue_length}")
    print(f"Border Utilization:   {result.border_utilization}%")
    print(f"Waiting Time:         {result.waiting_time_hours} hours")
    print(f"Status:               {result.status}")
    print(f"Recommendation:       {result.recommendation}")

    print("========================================\n")


def main():

    simulator = BorderCrossingSimulator(open_gates=3)

    scenarios = {
        "Normal Day": 35,
        "Peak Traffic": 50,
        "Holiday Season": 70,
    }

    for scenario, trucks in scenarios.items():

        print(f"\nScenario: {scenario}")

        result = simulator.simulate(arriving_trucks=trucks)

        print_report(result)


if __name__ == "__main__":
    main()

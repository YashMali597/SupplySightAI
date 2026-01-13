import pandas as pd
from orchestrator.agent_manager import AgentManager

DATA_PATH = "data/supply_chain_data.csv"


def load_data():
    """
    Load and clean supply chain dataset
    """
    df = pd.read_csv(DATA_PATH)
    df.columns = df.columns.str.lower().str.replace(" ", "_")
    return df


def compute_kpis(df):
    """
    Compute core supply chain KPIs
    """
    kpis = {
        "average_stock_level": round(df.stock_levels.mean(), 2),
        "average_lead_time": round(df.lead_times.mean(), 2),
        "average_defect_rate": round(df.defect_rates.mean(), 2),
        "total_revenue_generated": round(df.revenue_generated.sum(), 2),
        "stockout_risk_percentage": round((df.stock_levels < 10).mean() * 100, 2),
    }
    return kpis


def main():
    print("\nRunning AutoPilot AI Pipeline...\n")

    # Load data
    df = load_data()

    # Compute KPIs
    kpis = compute_kpis(df)
    print("CORE KPIs")
    for k, v in kpis.items():
        print(f"  - {k}: {v}")

    print("\nRunning Agentic AI System...\n")

    # Run agents
    manager = AgentManager()
    results = manager.run_all(df)

    # Print agent outputs
    for key, value in results.items():
        print(f"🔹 {key.upper()}: {value}")

    print("\nPipeline completed successfully.\n")


if __name__ == "__main__":
    main()

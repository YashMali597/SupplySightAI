from agents.base_agent import BaseAgent

class ForecastAgent(BaseAgent):
    def __init__(self):
        super().__init__("Forecast Agent")

    def run(self, df, context):
        risk = (df.stock_levels < df.order_quantities).mean() * 100
        context["forecast"] = f"{risk:.2f}% chance of stockout risk"
        return context

from agents.base_agent import BaseAgent

class DataQualityAgent(BaseAgent):
    def __init__(self):
        super().__init__("Data Quality Agent")

    def run(self, df, context):
        issues = []
        if df.isnull().sum().sum() > 0:
            issues.append("Missing values detected")

        low_stock = (df.stock_levels < 5).sum()
        if low_stock > 0:
            issues.append(f"{low_stock} products critically low on stock")

        context["data_quality"] = issues
        return context

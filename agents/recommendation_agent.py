from agents.base_agent import BaseAgent

class RecommendationAgent(BaseAgent):
    def __init__(self):
        super().__init__("Recommendation Agent")

    def run(self, df, context):
        recs = []

        if "High average defect rate detected" in context.get("insights", []):
            recs.append("Review supplier quality checks")

        if "stockout" in context.get("forecast", ""):
            recs.append("Increase reorder quantity for low-stock SKUs")

        context["recommendations"] = recs
        return context

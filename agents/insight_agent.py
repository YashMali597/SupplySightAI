from agents.base_agent import BaseAgent

class InsightAgent(BaseAgent):
    def __init__(self):
        super().__init__("Insight Agent")

    def run(self, df, context):
        insights = []
        if df.defect_rates.mean() > 3:
            insights.append("High average defect rate detected")

        if df.lead_times.mean() > 15:
            insights.append("Supplier lead times are above optimal range")

        context["insights"] = insights
        return context

from agents.base_agent import BaseAgent

class RootCauseAgent(BaseAgent):
    def __init__(self):
        super().__init__("Root Cause Agent")

    def run(self, df, context):
        causes = []

        corr = df[["defect_rates", "manufacturing_costs"]].corr().iloc[0,1]
        if corr > 0.5:
            causes.append("High manufacturing costs correlate with defect rates")

        context["root_causes"] = causes
        return context

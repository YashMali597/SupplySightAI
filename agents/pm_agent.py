from agents.base_agent import BaseAgent

class PMAgent(BaseAgent):
    def __init__(self):
        super().__init__("Product Manager Agent")

    def run(self, df, context):
        priorities = []

        if context.get("recommendations"):
            priorities.append("Supply risk mitigation = HIGH priority")

        context["pm_summary"] = priorities
        return context

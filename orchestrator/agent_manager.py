from agents.data_quality_agent import DataQualityAgent
from agents.insight_agent import InsightAgent
from agents.root_cause_agent import RootCauseAgent
from agents.forecast_agent import ForecastAgent
from agents.recommendation_agent import RecommendationAgent
from agents.pm_agent import PMAgent

class AgentManager:
    def __init__(self):
        self.agents = [
            DataQualityAgent(),
            InsightAgent(),
            RootCauseAgent(),
            ForecastAgent(),
            RecommendationAgent(),
            PMAgent()
        ]

    def run_all(self, df):
        context = {}
        for agent in self.agents:
            context = agent.run(df, context)
        return context

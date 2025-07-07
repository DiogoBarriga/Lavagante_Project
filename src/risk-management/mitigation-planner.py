# Mitigation Planner for Risk Management

This script helps in planning risk mitigation strategies by identifying risks, assessing their impact, and defining actions to mitigate them.

import pandas as pd

class MitigationPlanner:
    def __init__(self, risk_register):
        """
        Initialize the Mitigation Planner with a risk register.

        :param risk_register: DataFrame containing identified risks and their details.
        """
        self.risk_register = risk_register

    def assess_risks(self):
        """
        Assess risks based on their likelihood and impact.
        Adds a 'risk_score' column to the risk register.
        """
        self.risk_register['risk_score'] = (
            self.risk_register['likelihood'] * self.risk_register['impact']
        )
        return self.risk_register

    def define_mitigation_strategies(self):
        """
        Define mitigation strategies for each risk based on its risk score.
        Returns a DataFrame with mitigation strategies.
        """
        strategies = []
        for index, row in self.risk_register.iterrows():
            if row['risk_score'] >= 15:
                strategies.append('Immediate action required')
            elif row['risk_score'] >= 8:
                strategies.append('Monitor closely')
            else:
                strategies.append('No immediate action needed')
        
        self.risk_register['mitigation_strategy'] = strategies
        return self.risk_register

    def generate_mitigation_plan(self):
        """
        Generate a comprehensive mitigation plan based on the risk register.
        Returns a DataFrame with the complete mitigation plan.
        """
        self.assess_risks()
        self.define_mitigation_strategies()
        return self.risk_register[['risk_id', 'description', 'risk_score', 'mitigation_strategy']]

# Example usage
if __name__ == "__main__":
    # Sample risk register data
    data = {
        'risk_id': [1, 2, 3],
        'description': ['Data breach', 'Server downtime', 'Compliance issue'],
        'likelihood': [5, 4, 2],  # Scale of 1-5
        'impact': [5, 4, 3]       # Scale of 1-5
    }
    
    risk_register_df = pd.DataFrame(data)
    planner = MitigationPlanner(risk_register_df)
    mitigation_plan = planner.generate_mitigation_plan()
    
    print(mitigation_plan)
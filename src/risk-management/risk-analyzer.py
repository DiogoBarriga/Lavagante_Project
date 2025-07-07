import pandas as pd

class RiskAnalyzer:
    def __init__(self, risk_data):
        """
        Initializes the RiskAnalyzer with risk data.

        :param risk_data: DataFrame containing risk information with columns:
                          ['Risk ID', 'Description', 'Impact', 'Likelihood', 'Mitigation Plan']
        """
        self.risk_data = risk_data

    def assess_risks(self):
        """
        Assesses risks based on their impact and likelihood, and adds a 'Risk Score' to the DataFrame.
        The risk score is calculated as Impact * Likelihood.
        """
        self.risk_data['Risk Score'] = self.risk_data['Impact'] * self.risk_data['Likelihood']
        return self.risk_data

    def prioritize_risks(self):
        """
        Prioritizes risks based on their risk score in descending order.
        """
        prioritized_risks = self.risk_data.sort_values(by='Risk Score', ascending=False)
        return prioritized_risks

    def generate_risk_report(self):
        """
        Generates a report of the assessed and prioritized risks.
        """
        assessed_risks = self.assess_risks()
        prioritized_risks = self.prioritize_risks()
        report = prioritized_risks[['Risk ID', 'Description', 'Impact', 'Likelihood', 'Risk Score', 'Mitigation Plan']]
        return report

# Example usage
if __name__ == "__main__":
    # Sample risk data
    data = {
        'Risk ID': [1, 2, 3],
        'Description': ['Data breach', 'Project delay', 'Budget overrun'],
        'Impact': [5, 4, 3],  # Scale of 1-5
        'Likelihood': [3, 2, 4],  # Scale of 1-5
        'Mitigation Plan': ['Implement security protocols', 'Adjust project timeline', 'Review budget regularly']
    }

    risk_df = pd.DataFrame(data)
    risk_analyzer = RiskAnalyzer(risk_df)
    risk_report = risk_analyzer.generate_risk_report()
    print(risk_report)
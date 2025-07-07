# Monitoring script for risk management in the Lavagante project

import time
import logging

class RiskMonitor:
    """
    RiskMonitor class to continuously monitor identified risks throughout the project lifecycle.
    """

    def __init__(self, risk_register):
        """
        Initializes the RiskMonitor with a risk register.

        :param risk_register: A dictionary containing identified risks and their statuses.
        """
        self.risk_register = risk_register
        self.monitoring_interval = 60  # seconds
        logging.basicConfig(level=logging.INFO)

    def check_risks(self):
        """
        Checks the status of identified risks and logs their current state.
        """
        for risk, details in self.risk_register.items():
            status = details.get('status', 'unknown')
            logging.info(f"Risk: {risk}, Status: {status}")

    def start_monitoring(self):
        """
        Starts the risk monitoring process.
        """
        logging.info("Starting risk monitoring...")
        try:
            while True:
                self.check_risks()
                time.sleep(self.monitoring_interval)
        except KeyboardInterrupt:
            logging.info("Risk monitoring stopped.")

# Example usage
if __name__ == "__main__":
    # Sample risk register
    risk_register = {
        "Risk 1": {"status": "active"},
        "Risk 2": {"status": "mitigated"},
        "Risk 3": {"status": "inactive"},
    }

    monitor = RiskMonitor(risk_register)
    monitor.start_monitoring()
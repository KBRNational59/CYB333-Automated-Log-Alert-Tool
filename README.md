Automated Log Parser and Alert Tool

Project overview for project in class CYB333 Security Automation. To best demonstrate the main topic of this class, security automation, this project was created with Python and other extensions within the Visual Studio Code to demonstrate understading by creating a tool that automates the analysis of security logs. Rather than manual review of security logs, this tool first parses the security logs, then identifies common indicators of suspicious log activity.

Tools focus on detecting the following:

Failed login attempts
SQL injection attempts
Cross-site scripting (XSS) attempts

After identifying the number of anomalies, it generates a security report.


PROJECT FILES INCLUDE:

log_parser.py - Reads log data from the sample_log.txt and loads the entries into Python for analysis.
alert_generator.py - Contains functions for detecting failed login attempts, SQL injections, and XSS activity.
main.py - Loads the logs, runs the detection functions, prints the outputs, and generates findings to security_report.txt.

Jupyter Notebook (project.ipynb) - Showcases all of the functions starting with the parsing process, identifying the anomalies, and the generation of the security findings through the report.

sample_log.txt - Contains sample log entries with a variety of anomalies for testing functionality.
security_report.txt - Generated report containing the alert summary.


INSTRUCTIONS:

Step 1 - Open terminal inside project folder and run python main.py.
Step 2 - Run Jupyter notebook by opening notebooks/project.ipynb and then run the cells starting from the top and ensuring outputs are clear.
Step 3 - View security_report.txt displaying output of anomalies.


SKILLS DEMONSTRATED:

Python Programming
Log Parsing
Alert Generation
File Organization and Handling
Jupyter Notebook Usage
Security Automation


AUTHOR:

Kellan Ramirez
CYB333 Security Automation
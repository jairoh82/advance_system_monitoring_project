# System Monitoring and Troubleshooting Project

## Overview
This project will demonstrate a more interactive approach to system monitoring and troubleshooting using Python. It simulates how a technician or system would input real-time data and dynamically evaluate system conditions. 

### Approach
My approach is to create a structured system that takes real-time inputs and evaluates them using defined conditions. I will focus on keeping the logic clear and scalable by separating system checks into functions. This will reflect how I approach troubleshooting in the real world by validating inputs, analyzing conditions, and identifying issues step by step.

### System Design
This system is designed to simulate monitoring key parameters such as voltage, temperature, and system status. It uses conditional logic to detect abnormal conditions and generate alerts. This structure will allow for future expansion, such as integrating real sensor data or automated logging systems.

### Code
<img width="916" height="680" alt="code 1" src="https://github.com/user-attachments/assets/896c7c30-8332-4078-b804-d989d6badc8e" />
<img width="1053" height="652" alt="code 2" src="https://github.com/user-attachments/assets/4a8a48e1-026b-4caa-89a2-b77006b1eaac" />

### Test 1: Normal Operation
<img width="1375" height="275" alt="system running normal" src="https://github.com/user-attachments/assets/1b58c70a-6d94-4c5f-bbb0-a1e5de7fbff3" />

### Test 2: Out Of Range Conditions
<img width="1511" height="300" alt="system running out of parameters( multiple issues) " src="https://github.com/user-attachments/assets/508f459d-5f6b-45d0-ae6d-689127cbfded" />

### Test 3: System Fault Detection
<img width="1596" height="259" alt="system running (fault)" src="https://github.com/user-attachments/assets/e05178c2-f997-4f9d-8c5d-2bdcdddeaccb" />

### Test 4: Invalid Input Handling
<img width="1482" height="286" alt="error handling test" src="https://github.com/user-attachments/assets/b4e62d73-12af-483a-bee0-fe5ba46e3bea" />

### What Each Test Shows
Test 1: The system correctly identifies when all parameters are within normal range and reports normal operations.

Test 2: The system detects multiple issues simultaneously, including temperature and low voltage.

Test 3: The system correctly identifies a fault condition when the status is not “OK”

Test 4: The program safely handles incorrect input without crashing, demonstrating basic error handling.

### Conclusion
This project demonstrates how simple automation and structured logic can improve system monitoring and troubleshooting. If expanded further, I would integrate real-time data sources, logging, and automated alert systems to enhance reliability and reduce system downtime.






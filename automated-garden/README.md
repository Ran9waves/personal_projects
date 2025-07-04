# My ssf-sufficient-garden
<p align="center">
    <img src="https://github.com/user-attachments/assets/d4f34dbd-73ec-48cc-93bf-08d116575a20" alt="my banner">
</p>

To create this project, the following languages were used: 

[![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=ran9waves&layout=compact)](https://github.com/ran9waves)

#How to execute the program (UNDER CONSTRUCTION)

1. Run venv.sh to create the virtual environment and install the requirements automatically
2. At this moment the notification system module and the database of the plant can run separately. This project is still under contruction and in an upcoming future, some modules described below will be interconnected)

# How it works
To run the program, you only need to execute the main.py file, which will display a menu with all the available options like:
- Initialize the database (first thing to do when running the program for the first time!!)
- Show the database of plants
- Add a new plant
- Delete a plant
- Update information about a plant (you can edit it field by field)
- Quit 


Upcoming steps:

# Notification system: 
    - Sends notifications through email.
    - The fields sender_email, receiver_email, subject and text can be modified (although the initial goal was to inform myself about the status of my crops)
    
    PENDING:
    - First project: aproximate harvest date depending on the date of planting. Sweet potatoes use case, 90 days. 

# Watering system: 
    - humidity sensors or sound sensors?
    - calculate the % humidity on earth that each plant needs
    - attach it to the Notification system mentioned previously

# Automated watering system: 
    - watering pods with a valve that will open according to the humidity % detected by the Watering system mentioned in the previous phase
    - use a cronjob to open/close the valve of the pods.
    - security system that will notify me if the water tank is empty. 

# Lack of nutrients detector system
    - look for a sensor or system that can detect the lack of nutrients on earth. 
    - connect it to the notification system to send a notification when it detects that certain plant needs some nutrients. 
    - database with the needs of each plant. 

# AI against plagues
    - train an AI system to provide me informtion about how to solve the problems that each type of plant could have. 
    - Ideally it should allow me to provide a photo of the affected plant and the AI should provide me with a solution to the problem.
    - In case it is not possible, inform the AI with the issues that I find in the plant and tell me how to solve it

# Monitoring system
    - Monitoring system that reports me whenever a plant experiences an issue (informs me, 
    then uses "AI against plagues" to report me about the potential problem)


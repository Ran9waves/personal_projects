

# My ssf-sufficient-garden

1. Run venv.sh to create the virtual environment and install the requirements automatically

#TODO
- Create args to decide which module of the program I want to run (main.py). 


# Database of the plants that I have
    
At this moment the script plant_database.py connects to the DB through python.
When running, drops the old DB and generates a new one (to avoid iteration errors) with the fields indicated below.

    -Id
    -Name of the plant
    -Date when it was planted, harvested, produced fruit, died
    -Issues found while harvesting the plant
    -Crop phase and the upcoming phase (it goes unter rotative crop to keep the earth healthy and productive.)

In the end the program will print the actual information of the database.

    TODO: 
    - System to update the database when running the script (DELETE + UPDATE)
    - Connect the harvest date to a cronjob, to make it send me a notification on that specific date.

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
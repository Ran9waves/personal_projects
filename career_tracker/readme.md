<img src="https://capsule-render.vercel.app/api?text=Career Tracker!&animation=fadeIn&type=waving&color=gradient&height=200&width=auto"/>


## About Career Tracker

The goal of Career Tracker project was to allow me to check year by year the evolution of my career year by year, and be aware of where I am at all times. 

## How it works

### The libraries
- Dash and its components (dcc, html, Input, Output. State ): builds the webapp. 
- Plotly: 
- Pandas: data manipulation.
- OS: file operations.
- datetime: date handling. 

### Working details
First it defines a list of tuples (your portfolio milestones and their respective career phase )

Each one of the four career phases is associated to a color, so that later in can be easily spotted in the chart of the GUI, and the user can understand better at which point is each one of the milestones and phases (percentage of completion).

The Career tracker also creates a CSV file, in which is stored the progress history. 
***In case that the CSV already exists because career tracke was ran previously, it will load the information into a Dataframe and get the latest progress values. If not, it will initialize progress to zero for all tasks and create an empty Dataframe with the corresponding columns. 

To see the GUI of the webapp, after running the file, the user will have to load in the browser the ip indicated on the terminal, and ther he will find:
- For each task, there's a slider (0-100%), where the user can update the progress: first set the slider in the right percentage number, and then, clicking on "Update" button below all task sliders. 

- On the bottom of the GUI, the user will find the gantt charts for better visibility of the progression of the goals achievement. 



```yaml
language: Python
current_job: Cyber Security Engineer
education:
  [
    "Bachelor in German Linguistics (German, Swedish, Dutch)",
    "UX-UI designer bootcamp at IronHack",
    "Degree in cyber security",
    "Master's in Cyber Security and Privacy ",
  ]
fields_of_interests:
  [
    "Cyber Security",
    "AI",
    "UI/UX",
    "Game Development",
  ]
technical_background:
  [
    "UX-UI designer"
    "Cyber Security Engineer",
    "SecDevOps",
    "Cloud",
    "SOC",
    "CIR"
  ]

currently_learning: At the moment working to get CompTIA CySA+ certification. 
hobbies: ["Photography", "martial arts", "any sport related with water", "cooking", "cinema"] *
```

![Snake animation](https://raw.githubusercontent.com/Ran9waves/Ran9waves/output/github-contribution-grid-snake-dark.svg)

## CTF's
```yaml
- "Advent of Cyber 2022 - TryHackMe"
- "Advent of Cyber 2023 - TryHackMe"
- "Boss of the SOC 2022 - Splunk"
- "Boss of the SOC 2023 - Splunk"
- "AI Security Challenge - Wiz"
- "The Big IAM Challenge - Wiz"
- "Huntress Capture The Flag - Huntress"
- "Microsoft Security Inmersion - CTF"
```

## Online courses

### Letsdefend
```yaml
- "SOC Analyst Learning Path"
- "Malware Analysis Skill Path"
- "Programming for Cybersecurity" (learning it at the moment)
```

## <a href="https://tryhackme.com/api/v2/badges/public-profile?userPublicId=1118765">TryHackMe profile</a>

### HackTheBox modules
```yaml
- "Linux Fundamentals"
- "Windows Fundamentals"
- "MacOs Fundamentals"
- "Web Requests"
- "JavaScript Deobfuscation"
- "Introduction to Active Directory"
- "Vulnerability Assessment"
```

### Zerotomastery
```yaml
- "Complete Python Developer 2025:  Zero to Mastery"
- "AWS Certified Cloud Practitioner: Zero to Mastery"
- "AI for beginners: Inside Large Language Models"
- "AI Coding with Github Copilot"
- "Artificial Intelligence in Cybersecurity"
- "Complete UI/UX Product Design Bootcamp"
```
### Other Learning
```yaml
- "Wiz Foundations - Wiz"
- "AWS Cloud Practitioner - AWS (CERTIFICATE)"
- "API Documentation Best Practices - APISec"
- "API Security Fundamentals - APISec"
- "Network Basics - Cisco"
- "Python Essentials 1 - Cisco"
- "Microsoft Security Inmersion - Microsoft"
- "Scrum Master Certified - Scrum Alliance (CERTIFICATE)"
- "Cribl Stream Fundamentals - Cribl"
- "Certified in Cybersecurity - ISC2 (CERTIFICATE)"
```


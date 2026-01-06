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

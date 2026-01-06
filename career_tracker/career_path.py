import dash
from dash import dcc, html, Input, Output, State
import plotly.express as px
import pandas as pd
import os
from datetime import date

#Define tasks: Name, Phase
tasks=[
    ("Project 1: Secure Login & MFA - Low-fi",'Foundation'),
    ("Project 1: Secure Login & MFA - Hi-fi",'Foundation'),
    ("Project 2: AI Dashboard - Low-fi",'Foundation'),
    ("Project 2: AI Dashboard - Hi-fi",'Foundation'),
    ("Project 3: Multilingual E-Com Flow - Low-Fi",'Specialization'),
    ("Project 3: Multilingual E-Com Flow - Hi-Fi",'Specialization'),
    ("Project 4: Accessibility Upgrade for Saas Tool - Low-Fi",'Specialization'),
    ("Project 4: Accessibility Upgrade for Saas Tool - Low-Fi",'Specialization'),
    ("Project 5: Explainable AI UX - Low-Fi",'Specialization'),
    ("Project 5: Explainable AI UX - Hi-Fi",'Specialization'),
    ("Project 6: Cybersecurity Onboarding - Low-Fi",'Specialization'),
    ("Project 6: Cybersecurity Onboarding - Hi-Fi",'Specialization'),
    ("Project 7: Smart Multimodal Interface prototype",'Specialization'),
    ("Articles",'Thought Leadership'),
    ("Webinar",'Thought Leadership'),
    ("Portfolio Metrics Update",'Thought Leadership'),
    ("Job Applications", "Career Acceleration"),
    ("Freelance/Consulting Setup",'Career Acceleration'),
    ("Interviews & Salary Negotiation",'Career Acceleration'),
    ("Reflection & Roadmap",'Career Acceleration')
]

phases = ['Foundation','Specialization','Thought Leadership','Career Acceleration']
phase_colors = {'Foundation':'blue','Specialization':'green','Thought Leadership':'orange','Career Acceleration':'purple'}


csv_file = "progress_history.csv"

# Load initialize progress

if os.path.exists(csv_file):
    df_history = pd.read_csv(csv_file)
    latest_progress = df_history.iloc[-1,1:].tolist()
else:
    latest_progress = [0]*len(tasks)
    df_history =pd.DataFrame(columns=['Date'] + [t[0]for t in tasks])

# Create Dash app

app = dash.Dash(__name__)
app.layout=html.Div([
    html.H1("UX/UI Portfolio Tracker Dashboard"),
    html.H2("Update Task Progress(%)"),
    html.Div([
        html.Div([
            html.Label(task[0]),
            dcc.Slider(id={'type':'slider','index':i}, min=0, max=100, step=1, value=latest_progress[i],marks={0:'0',50:'50',100:'100'})
        ], style={'margin':'10px'}) for i, task in enumerate (tasks)
    ]),
    html.Button("Update Progress", id='update-button',n_clicks=0),
    dcc.Graph(id='gantt-chart'),
    dcc.Graph(id='trend-chart')
])

# Callback to update charts
@app.callback(
    [Output('gantt-chart','figure'),Output('trend-chart','figure')],
    [Input('update-button','n_clicks')],
    [State({'type':'slider','index':dash.ALL},'value')]
)

def update_charts(n_clicks,slider_values):
    # Save to CSV with today's date
    today = date.today().isoformat()
    new_row = [today] + slider_values
    global df_history
    expected_columns = ['Date'] + [t[0] for t in tasks]
    # Ensure columns match before adding new row
    if list(df_history.columns) != expected_columns:
        df_history = pd.DataFrame(columns=expected_columns)
    df_history.loc[len(df_history)] = new_row
    df_history.to_csv(csv_file, index=False)

    # Gantt chart
    gantt_data = pd.DataFrame({
        'Task':[t[0]for t in tasks],
        'Progress':slider_values,
        'Phase':[t[1]for t in tasks]
    })

    gantt_fig = px.bar(gantt_data, x='Progress',y='Task', orientation='h',
                color='Phase', color_discrete_map=phase_colors, text='Progress')
    gantt_fig.update_layout(title="Current Progress by Task", yaxis={'categoryorder':'total ascending'})

    # Trend chart
    trend_fig= px.line()
    df_history['Date']=pd.to_datetime(df_history['Date'])
    for phase in phases:
        phase_cols = [t[0]for t in tasks if t[1]==phase]
        df_history[f'{phase}_avg']=df_history[phase_cols].mean(axis=1)
        trend_fig.add_scatter(x=df_history['Date'],y=df_history[f'{phase}_avg'],mode='lines+markers',
                              name=phase, line=dict(color=phase_colors[phase]))
    trend_fig.update_layout(title="Historical Phase Progress",xaxis_title="Date", yaxis_title="Progress(%)")

    return gantt_fig,trend_fig
if __name__=='__main__':
    app.run(debug=True)
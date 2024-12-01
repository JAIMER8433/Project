import pandas as pd
import plotly.graph_objects as go

# Sample data (replace with your actual data)
data = {
    'Participant ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],  # Participant IDs 1 to 19
    'IoT Usage': ['Yes', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'No', 'Yes', 'No', 'No', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No'],
    'MQTT Familiarity': ['Somewhat Familiar', 'Not Familiar', 'Not Familiar', 'Not Familiar', 'Not Familiar', 'Not Familiar', 'Somewhat Familiar', 'Somewhat Familiar', 'Somewhat Familiar', 'Not Familiar', 'Not Familiar', 'Not Familiar', 'Not Familiar', 'Not Familiar', 'Not Familiar', 'Somewhat Familiar', 'Not Familiar', 'Not Familiar', 'Familiar'],
    'CoAP Familiarity': ['Somewhat Familiar', 'Not Familiar', 'Not Familiar', 'Not Familiar', 'Not Familiar', 'Not Familiar', 'Not Familiar', 'Not Familiar', 'Somewhat Familiar', 'Not Familiar', 'Not Familiar', 'Not Familiar', 'Not Familiar', 'Not Familiar', 'Not Familiar', 'Somewhat Familiar', 'Not Familiar', 'Not Familiar', 'Not Familiar']
}

# Create DataFrame
df = pd.DataFrame(data)

# Map familiarity levels to categorical values
familiarity_mapping = {
    'Not Familiar': 'Not Familiar',
    'Somewhat Familiar': 'Somewhat Familiar',
    'Familiar': 'Familiar',
    'Very Familiar': 'Very Familiar'
}

# No need to apply numeric mapping, we will keep it as categorical for the y-axis

# Plotting both MQTT and CoAP Familiarity
fig = go.Figure()

# Plot for MQTT Familiarity
fig.add_trace(go.Scatter(
    x=df['Participant ID'],
    y=df['MQTT Familiarity'],
    mode='markers',
    marker=dict(color='blue', size=10),
    name="MQTT Familiarity"
))

# Plot for CoAP Familiarity
fig.add_trace(go.Scatter(
    x=df['Participant ID'],
    y=df['CoAP Familiarity'],
    mode='markers',
    marker=dict(color='red', size=10),
    name="CoAP Familiarity"
))

# Update layout with categorical y-axis
fig.update_layout(
    title="Participant IoT Usage vs Familiarity with MQTT and CoAP",
    xaxis_title="Participant ID",
    yaxis_title="Familiarity Level",
    yaxis=dict(
        tickmode='array',
        tickvals=['Not Familiar', 'Somewhat Familiar', 'Familiar', 'Very Familiar'],
        ticktext=['Not Familiar', 'Somewhat Familiar', 'Familiar', 'Very Familiar']
    ),
    showlegend=True
)

fig.show()

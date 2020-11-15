from datetime import datetime

import pandas as pd
import plotly.express as px
import queries
from plotly.subplots import make_subplots
import plotly.graph_objects as go

def main():
    df = queries.getDataCovidByCcaa("MD")
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df["Date"], y=df["PCR"],
                             mode='lines',
                             name='PCR'))
    fig.add_trace(go.Scatter(x=df["Date"], y=df["Hospitalizations"],
                             mode='lines',
                             name='Hospitalizations'))
    fig.add_trace(go.Scatter(x=df["Date"], y=df["UCI"],
                             mode='lines',
                             name='UCI'))
    fig.add_trace(go.Scatter(x=df["Date"], y=df["AC"],
                             mode='lines',
                             name='AC'))

    fig.show()
if __name__ == "__main__":
    main()
from datetime import datetime

import pandas as pd
import plotly.express as px
import queries
from plotly.subplots import make_subplots

def main():
    dfQuantityTopProducts = queries.getQuantityTopProducts()
    dfCovid = queries.getQ06()
    fig = px.bar(
        dfQuantityTopProducts,
        title="Evolution of products ordered",
        x="Date",
        y="Quantity",
        color="Product",
        template="plotly_white",
    )
    fig2 = px.line(x=dfCovid["Date"], y=dfCovid["Number Hospitalizations"] )

    fig2.update_traces(yaxis="y2")
    subfig = make_subplots(specs=[[{"secondary_y": True}]])

    subfig.add_traces(fig.data + fig2.data)
    subfig.layout.xaxis.title = "Time"
    subfig.layout.yaxis.title = "Linear Y"
    subfig.layout.yaxis2.type = "log"
    subfig.layout.yaxis2.title = "Log Y"
    # recoloring is necessary otherwise lines from fig und fig2 would share each color
    # e.g. Linear-, Log- = blue; Linear+, Log+ = red... we don't want this
    subfig.for_each_trace(lambda t: t.update(line=dict(color=t.marker.color)))
    subfig.show()

if __name__ == "__main__":
    main()
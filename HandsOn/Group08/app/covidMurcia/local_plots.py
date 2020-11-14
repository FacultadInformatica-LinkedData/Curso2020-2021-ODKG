from datetime import datetime

import pandas as pd
import plotly.express as px
import queries

def main():
    # df1 = queries.getQ1()
    # fig = px.line(
    #     df1,
    #     title="Comparison: ",
    #     x="Date",
    #     y="Quantity",
    #     color="Product",
    #     template="plotly_white",
    # )
    # fig.update_layout(transition_duration=500)
    # fig.show()

    # df1 = queries.getQ2()
    # fig = px.line(
    #     df1,
    #     title="Comparison: ",
    #     x="fecha",
    #     y="num_p",
    #     color="iso",
    #     template="plotly_white",
    # )
    # fig.update_layout(transition_duration=500)
    # fig.show
    dfQuantityTopServices = queries.getQuantityTopServices()
    date=min(dfQuantityTopServices['Date'])
    print(type(date))


if __name__ == "__main__":
    main()
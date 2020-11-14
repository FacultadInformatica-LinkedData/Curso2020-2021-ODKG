
import dash
import dash_table
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash.dependencies import Output, Input, State
import pandas as pd
import plotly.express as px
import queries
import plotly.graph_objects as go
from datetime import datetime

dfProducts = queries.getQ01()
dfServices = queries.getQ02()
dfOrganizations = queries.getQ10()
dfQuantityTopProducts = queries.getQuantityTopProducts()
dfQuantityTopServices = queries.getQuantityTopServices()
dfQuantityTopOrganizations = queries.getQuantityTopOrganizations()
optionsProducts = [{'label': i, 'value': i} for i in dfProducts["Product"]]
optionsServices = [{'label': i, 'value': i} for i in dfServices["Service"]]
optionsOrganizations = [{'label': i, 'value': i} for i in dfOrganizations["Organization"]]


PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"
NAVBAR = dbc.Navbar(
    children=[
        html.A(
            # Use row and col to control vertical alignment of logo / brand
            dbc.Row(
                [
                    dbc.Col(html.Img(src=PLOTLY_LOGO, height="30px")),
                    dbc.Col(
                        dbc.NavbarBrand("Public Procurement Murcia", className="ml-2")
                    ),
                ],
                align="center",
                no_gutters=True,
            ),
            href="https://plot.ly",
        )
    ],
    color="dark",
    dark=True,
    sticky="top",
)

TOP_BIGRAM_PLOT = [
    dbc.CardHeader(html.H5("Top bigrams found in the database")),
    dbc.CardBody(
        [
            dcc.Loading(
                id="loading-bigrams-scatter",
                children=[
                    dbc.Alert(
                        "Something's gone wrong! Give us a moment, but try loading this page again if problem persists.",
                        id="no-data-alert-bigrams",
                        color="warning",
                        style={"display": "none"},
                    ),
                    dbc.Row(
                        [
                            dbc.Col(html.P(["Choose a t-SNE perplexity value:"]), md=6),
                            dbc.Col(
                                [
                                    dcc.Slider(
                                        id='year-slider',
                                        min=2001,
                                        max=204,
                                        value=2001,
                                        marks={str(year): str(year) for year in [2001,2002,2003,4004]},
                                        step=None
                                    ),
                                    dcc.Slider(
                                        id='year-slider2',
                                        min=2001,
                                        max=204,
                                        value=2001,
                                        marks={str(year): str(year) for year in [2001,2002,2003,4004]},
                                        step=None
                                    )
                                ],
                                md=3,
                            ),
                        ]
                    ),
                    dcc.Graph(id='graph-with-slider'),
                    dcc.Graph(id='graph-with-slider2'),
                ],
                type="default",
            )
        ],
        style={"marginTop": 0, "marginBottom": 0},
    ),
]

TOP_PRODUCTS_PLOT = [
    dbc.CardHeader(html.H5("Top 10 products ordered and its quantity")),
    dbc.CardBody(
        [
            dcc.Loading(
                id="loading-bigrams-scatter",
                children=[
                    dbc.Alert(
                        "Something's gone wrong! Give us a moment, but try loading this page again if problem persists.",
                        id="no-data-alert-bigrams",
                        color="warning",
                        style={"display": "none"},
                    ),
                    dash_table.DataTable(
                        id='table-top-products',
                        columns=[{"name": i, "id": i} for i in dfProducts.columns],
                        data=dfProducts.to_dict('records'),
                    ),
                    dbc.Col(
                        html.H5("Choose week range")
                    ),
                    dcc.RangeSlider(
                        id='date-slider-products',
                        marks={i: '{}'.format(i) for i in range(min(dfQuantityTopProducts['Date']).week, max(dfQuantityTopProducts['Date']).week)},
                        min= min(dfQuantityTopProducts['Date']).week,
                        max= max(dfQuantityTopProducts['Date']).week,
                        value=[min(dfQuantityTopProducts['Date']).week, max(dfQuantityTopProducts['Date']).week]
                    ),
                    dcc.Graph(id='graph-all-products'),
                    dcc.Dropdown(
                        id='dropdown-products',
                        options=optionsProducts,
                        multi=False,
                        value="CALZAS",
                        placeholder="Select the Product to see data below",
                        style={
                            'width': '1000px',
                            },
                    ),
                    dcc.Graph(id='graph-some-products'),
                ],
                type="default",
            )
        ],
        style={"marginTop": 0, "marginBottom": 0},
    ),
]

TOP_SERVICES_PLOT = [
    dbc.CardHeader(html.H5("Top 10 services ordered and its quantity")),
    dbc.CardBody(
        [
            dcc.Loading(
                id="loading-bigrams-scatter",
                children=[
                    dbc.Alert(
                        "Something's gone wrong! Give us a moment, but try loading this page again if problem persists.",
                        id="no-data-alert-bigrams",
                        color="warning",
                        style={"display": "none"},
                    ),
                    dash_table.DataTable(
                        id='table-top-services',
                        columns=[{"name": i, "id": i} for i in dfServices.columns],
                        data=dfServices.to_dict('records'),
                    ),
                    dcc.RangeSlider(
                        id='date-slider-services',
                        marks={i: '{}'.format(i) for i in range(min(dfQuantityTopServices['Date']).week, max(dfQuantityTopServices['Date']).week)},
                        min= min(dfQuantityTopServices['Date']).week,
                        max= max(dfQuantityTopServices['Date']).week,
                        value=[min(dfQuantityTopServices['Date']).week, max(dfQuantityTopServices['Date']).week]
                    ),
                    dcc.Graph(id='graph-all-products'),
                    dcc.Dropdown(
                        id='dropdown-products',
                        options=optionsProducts,
                        multi=False,
                        value="CALZAS",
                        placeholder="Select the Product to see data below",
                        style={
                            'width': '1000px',
                            },
                    ),
                    dcc.Graph(id='graph-some-products'),
                ],
                type="default",
            )
        ],
        style={"marginTop": 0, "marginBottom": 0},
    ),
]


TOP_ORGANIZATIONS = [
    dbc.CardHeader(html.H5("Top Organizations")),
    dbc.CardBody(
        [
            dcc.Loading(
                id="loading-bigrams-scatter",
                children=[
                    dbc.Alert(
                        "Something's gone wrong! Give us a moment, but try loading this page again if problem persists.",
                        id="no-data-alert-bigrams",
                        color="warning",
                        style={"display": "none"},
                    ),
                    dash_table.DataTable(
                        id='table-organizations',
                        columns=[{"name": i, "id": i} for i in dfOrganizations.columns],
                        data=dfOrganizations.to_dict('records'),
                    ),
                    dcc.RangeSlider(
                        id='date-slider-organizations',
                        marks={i: '{}'.format(i) for i in range(min(dfQuantityTopOrganizations['Date']).week, max(dfQuantityTopOrganizations['Date']).week)},
                        min= min(dfQuantityTopOrganizations['Date']).week,
                        max= max(dfQuantityTopOrganizations['Date']).week,
                        value=[min(dfQuantityTopOrganizations['Date']).week, max(dfQuantityTopOrganizations['Date']).week]
                    ),
                    dcc.Graph(id='graph-all-organizations'),
                    dcc.Dropdown(
                        id='dropdown-organizations',
                        options=optionsOrganizations,
                        value="MEDTRONIC IBERICA, S.A.",
                        placeholder="Select the Organizations to see data below" ,
                        style={
                        'width': '1000px',
                        },
                    ),
                    dcc.Graph(id='graph-organizations'),
                ],
                type="default",
            )
        ],
        style={"marginTop": 0, "marginBottom": 0},
    ),
]


BODY_COVID = dbc.Container(
    [
        dbc.Row([dbc.Col(html.P(["Choose a t-SNE perplexity value:"]), md=6),], style={"marginTop": 30}),
    ],
    className="mt-12",
)

BODY_MURCIA = dbc.Container(
    [
        dbc.Row([dbc.Col(dbc.Card(TOP_PRODUCTS_PLOT)),], style={"marginTop": 30}),
        dbc.Row([dbc.Col(dbc.Card(TOP_ORGANIZATIONS)),], style={"marginTop": 30}),
    ],
    className="mt-12",
)


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.config['suppress_callback_exceptions'] = True

app.layout = html.Div([NAVBAR,
    dcc.Tabs(id="tabs", value='Murcia Public Procurement', children=[
        dcc.Tab(label='COVID Analysis', value='COVID Analysis'),
        dcc.Tab(label='Murcia Public Procurement', value='Murcia Public Procurement'),
    ]),
    html.Div(id='tabs-content')
])


@app.callback(
    Output('graph-all-products', 'figure'),
    [Input('date-slider-products', 'value')])
def update_figure(dates):
    dfTemp = dfQuantityTopProducts[(dfQuantityTopProducts['Date'].dt.isocalendar().week>=dates[0]) & (dfQuantityTopProducts['Date'].dt.isocalendar().week<=dates[1])]
    fig = px.line(
        dfTemp,
        title="Evolution of products ordered",
        x="Date",
        y="Quantity",
        color="Product",
        template="plotly_white",
    )
    fig.update_layout(transition_duration=500)

    return fig

@app.callback(
    Output('graph-some-products', 'figure'),
    [Input('dropdown-products', 'value'),
     Input('date-slider-products', 'value')])
def update_figure2(product, dates):
    df1 = queries.getQ03(product)
    dfTemp = df1[
        (df1['Date'].dt.isocalendar().week >= dates[0]) & (df1['Date'].dt.isocalendar().week <= dates[1])]
    fig = px.line(dfTemp, x="Date", y="Quantity", template="plotly_white", title="Evolution of "+product+" and pending quantity")
    fig.update_traces(line_color='#FF0000')
    fig2 = px.bar(dfTemp, x="Date", y="Quantity Pending")
    fig.add_trace(fig2.data[0])
    fig.data[0].update(mode='markers+lines')
    fig.update_layout(transition_duration=500)
    return fig

@app.callback(
    Output('graph-all-organizations', 'figure'),
    [Input('date-slider-organizations', 'value')])
def update_figure3(dates):
    dfTemp = dfQuantityTopOrganizations[(dfQuantityTopOrganizations['Date'].dt.isocalendar().week>=dates[0]) & (dfQuantityTopOrganizations['Date'].dt.isocalendar().week<=dates[1])]
    fig = px.line(
        dfTemp,
        title="Evolution of ordered products to Organization",
        x="Date",
        y="Quantity",
        color="Organization",
        template="plotly_white",
    )
    fig.update_layout(transition_duration=500)

    return fig

@app.callback(
    Output('graph-organizations', 'figure'),
    [Input('dropdown-organizations', 'value'),
     Input('date-slider-organizations', 'value')])
def update_figure4(organization, dates):
    print(organization, dates)
    df1 = queries.getQ11(organization)
    print(df1)
    dfTemp = df1[
        (df1['Date'].dt.isocalendar().week >= dates[0]) & (df1['Date'].dt.isocalendar().week <= dates[1])]
    fig = px.line(
        dfTemp,
        title="Evolution of products ordered to "+organization,
        x="Date",
        y="Quantity",
        color="Product",
        template="plotly_white",
    )
    fig.update_layout(transition_duration=500)
    return fig

@app.callback(
    Output('graph-all-services', 'figure'),
    [Input('date-slider-services', 'value')])
def update_figure5(dates):
    dfTemp = dfQuantityTopServices[(dfQuantityTopServices['Date'].dt.isocalendar().week>=dates[0]) & (dfQuantityTopServices['Date'].dt.isocalendar().week<=dates[1])]
    fig = px.line(
        dfTemp,
        title="Evolution of services ordered",
        x="Date",
        y="Quantity",
        color="Service",
        template="plotly_white",
    )
    fig.update_layout(transition_duration=500)

    return fig

@app.callback(
    Output('graph-some-services', 'figure'),
    [Input('dropdown-services', 'value'),
     Input('date-slider-services', 'value')])
def update_figure6(product, dates):
    print(product)
    df1 = queries.getQ03(product)
    dfTemp = df1[
        (df1['Date'].dt.isocalendar().week >= dates[0]) & (df1['Date'].dt.isocalendar().week <= dates[1])]
    fig = px.line(dfTemp, x="Date", y="Quantity", template="plotly_white", title="Evolution of services and pending quantity")
    fig.update_traces(line_color='#FF0000')
    fig2 = px.bar(dfTemp, x="Date", y="Quantity Pending")
    fig.add_trace(fig2.data[0])
    fig.update_layout(transition_duration=500)
    return fig

@app.callback(Output('tabs-content', 'children'),
              [Input('tabs', 'value')])
def render_content(tab):
    if tab == 'COVID Analysis':
        return html.Div()
    elif tab == 'Murcia Public Procurement':
        return html.Div(BODY_MURCIA)

if __name__ == "__main__":
    app.run_server(debug=True)


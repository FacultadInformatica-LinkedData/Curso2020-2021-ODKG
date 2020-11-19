
import dash
import dash_table
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash.dependencies import Output, Input, State
import pandas as pd
import plotly.express as px
import queries
import plotly.tools as tls
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
optionsOrganizations = [{'label': i, 'value': i} for i in dfOrganizations["Company"]]
dfCovid = queries.getQ07()
dfCovidacumulado=queries.getQ08()
optionsCCAA =[{'label':i,'value':i} for i in dfCovid["CCAA"]]

PLOTLY_LOGO = "https://www.upm.es/sfs/Rectorado/Gabinete%20del%20Rector/Logos/UPM/Logotipo%20con%20Leyenda/LOGOTIPO%20leyenda%20color%20PNG.png"
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
            href="https://www.upm.es/sfs/Rectorado/Gabinete%20del%20Rector/Logos/UPM/Logotipo%20con%20Leyenda/LOGOTIPO%20leyenda%20color%20PNG.png",
        )
    ],
    color="dark",
    dark=True,
    sticky="top",
)

TOP_PRODUCTS_PLOT = [
    dbc.CardHeader(html.H5("Top 10 products by quantity ordered and pending quantity")),
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
                        page_size=10,
                        sort_action="native",
                        sort_mode='multi',
                    ),
                ],
                type="default",
            )
        ],
        style={"marginTop": 0, "marginBottom": 0},
    ),
]

TOP_PRODUCTS_PLOT_ANALYSIS = [
    dbc.CardHeader(html.H5("Products Analysis")),
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
                        value="GUANTES DE NITRILO, CON Y SIN POLVO",
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
    dbc.CardHeader(html.H5("Services requested and their price")),
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
                        page_size=10,
                        sort_action="native",
                        sort_mode='multi',
                    ),
                ],
                type="default",
            )
        ],
        style={"marginTop": 0, "marginBottom": 0},
    ),
]

TOP_SERVICES_PLOT_ANALYSIS = [
    dbc.CardHeader(html.H5("Services Analysis")),
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
                    dbc.Col(
                        html.H5("Choose week range")
                    ),
                    dcc.RangeSlider(
                        id='date-slider-services',
                        marks={i: '{}'.format(i) for i in range(min(dfQuantityTopServices['Date']).week, max(dfQuantityTopServices['Date']).week)},
                        min= min(dfQuantityTopServices['Date']).week,
                        max= max(dfQuantityTopServices['Date']).week,
                        value=[min(dfQuantityTopServices['Date']).week, max(dfQuantityTopServices['Date']).week]
                    ),
                    dcc.Dropdown(
                        id='dropdown-services',
                        options=optionsServices,
                        multi=False,
                        value="ALQUILER DE VEHICULOS",
                        placeholder="Select the service to see data below",
                        style={
                            'width': '1000px',
                            },
                    ),
                    dcc.Graph(id='graph-some-services'),
                ],
                type="default",
            )
        ],
        style={"marginTop": 0, "marginBottom": 0},
    ),
]

TOP_ORGANIZATIONS = [
    dbc.CardHeader(html.H5("Information about the companies")),
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
                        page_size=10,
                        sort_action="native",
                        sort_mode='multi',
                    ),
                ],
                type="default",
            )
        ],
        style={"marginTop": 0, "marginBottom": 0},
    ),
]

TOP_ORGANIZATIONS_ANALYSIS = [
    dbc.CardHeader(html.H5("Companies Analysis")),
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
                    dbc.Col(
                        html.H5("Choose week range")
                    ),
                    dcc.RangeSlider(
                        id='date-slider-organizations',
                        marks={i: '{}'.format(i) for i in range(min(dfQuantityTopOrganizations['Date']).week, max(dfQuantityTopOrganizations['Date']).week)},
                        min= min(dfQuantityTopOrganizations['Date']).week,
                        max= max(dfQuantityTopOrganizations['Date']).week,
                        value=[min(dfQuantityTopOrganizations['Date']).week, max(dfQuantityTopOrganizations['Date']).week]
                    ),
                    dcc.Graph(id='graph-all-organizations'),
                    dcc.Graph(id='graph-all-organizations-2'),
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

TOTALCOVID_CCAA = [
    dbc.CardHeader(html.H5("Total accumulated positives tests by region")),
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
                        id='table-covid-ia',
                        columns=[{"name": i, "id": i} for i in dfCovidacumulado.columns],
                        data=dfCovidacumulado.to_dict('records'),
                        sort_action="native",
                        sort_mode='multi',
                    ),
                    dcc.Graph(figure=px.bar(
                        dfCovidacumulado,
                        title="Total accumulated positives tests by region",
                        x='ISO code',
                        y='PCR+',
                        hover_data=['Link'],
                        template="plotly_white",
                    )
                    ),
                ],
                type="default",
            )
        ],
        style={"marginTop": 0, "marginBottom": 0},
    ),
]

DATACOVID_CCAA = [
    dbc.CardHeader(html.H5("Evolution of number of hospitalizations, deaths and ICU by region")),
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
                    dbc.Col(
                        html.H5("\nChoose week range")
                    ),
                    dcc.RangeSlider(
                        id='date-slider-ccaa',
                        marks={i: '{}'.format(i) for i in range(min(dfCovid['Date']).week, max(dfCovid['Date']).week)},
                        min= min(dfCovid['Date']).week,
                        max= max(dfCovid['Date']).week,
                        value=[min(dfCovid['Date']).week, max(dfCovid['Date']).week]
                    ),
                    dcc.Graph(id='graph-PCR-CCAA'),
                    dcc.Graph(id='graph-AC-CCAA'),
                    dcc.Graph(id='graph-UCI-CCAA'),
                    dcc.Graph(id='graph-HOS-CCAA'),
                    dcc.Graph(id='graph-DEATH-CCAA')
                ],
                type="default",
            )
        ],
        style={"marginTop": 0, "marginBottom": 0},
    ),
]

DATACOVID_BY_CCAA = [
    dbc.CardHeader(html.H5("Number of PCR+, hospitalizations and ICU by date and region")),
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
                    dbc.Col(
                        html.H5("Choose week range")
                    ),
                    dcc.Dropdown(
                        id='dropdown-ccaa',
                        options=optionsCCAA,
                        multi=False,
                        value="MD",
                        placeholder="Select the region to see data below",
                        style={
                            'width': '1000px',
                        },
                    ),
                    dcc.Graph(id='graph-by-ccaa'),
                ],
                type="default",
            )
        ],
        style={"marginTop": 0, "marginBottom": 0},
    ),
]


BODY_COVID = dbc.Container(
    [
        dbc.Row([dbc.Col(dbc.Card(TOTALCOVID_CCAA)),],style={"marginTop":30}),
        dbc.Row([dbc.Col(dbc.Card(DATACOVID_CCAA)),],style={"marginTop":30}),
        dbc.Row([dbc.Col(dbc.Card(DATACOVID_BY_CCAA)), ], style={"marginTop": 30}),

    ],
    className="mt-12",
)

BODY_MURCIA = dbc.Container(
    [
        dbc.Row([dbc.Col(dbc.Card(TOP_PRODUCTS_PLOT)),], style={"marginTop": 30}),
        dbc.Row([dbc.Col(dbc.Card(TOP_PRODUCTS_PLOT_ANALYSIS)), ], style={"marginTop": 30}),
        dbc.Row([dbc.Col(dbc.Card(TOP_SERVICES_PLOT)), ], style={"marginTop": 30}),
        dbc.Row([dbc.Col(dbc.Card(TOP_SERVICES_PLOT_ANALYSIS)), ], style={"marginTop": 30}),
        dbc.Row([dbc.Col(dbc.Card(TOP_ORGANIZATIONS)),], style={"marginTop": 30}),
        dbc.Row([dbc.Col(dbc.Card(TOP_ORGANIZATIONS_ANALYSIS)), ], style={"marginTop": 30}),
    ],
    className="mt-12",
)


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.config['suppress_callback_exceptions'] = True

app.layout = html.Div([NAVBAR,
    dcc.Tabs(id="tabs", value='COVID Analysis', children=[
        dcc.Tab(label='COVID Analysis', value='COVID Analysis'),
        dcc.Tab(label='Murcia Public Procurement', value='Murcia Public Procurement'),
    ]),
    html.Div(id='tabs-content')
])

server = app.server

@app.callback(
    Output('graph-all-products', 'figure'),
    [Input('date-slider-products', 'value')])
def update_figure(dates):
    dfTemp = dfQuantityTopProducts[(dfQuantityTopProducts['Date'].dt.isocalendar().week>=dates[0]) & (dfQuantityTopProducts['Date'].dt.isocalendar().week<=dates[1])]
    dfTemp2 = dfCovid[
        (dfCovid['Date'].dt.isocalendar().week >= dates[0]) & (dfCovid['Date'].dt.isocalendar().week <= dates[1])]
    fig = px.bar(
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
    fig = px.line(dfTemp, x="Date", y="Quantity", template="plotly_white", title="Evolution of the product selected and pending quantity")
    fig.update_traces(line_color='#304281')
    fig2 = px.bar(dfTemp, x="Date", y="Quantity Pending")
    fig2.update_traces(marker_color='red')
    fig.add_trace(fig2.data[0])
    fig.data[0].update(mode='markers+lines')
    fig.update_layout(transition_duration=500)
    return fig

@app.callback(
    Output('graph-all-organizations', 'figure'),
    [Input('date-slider-organizations', 'value')])
def update_figure3(dates):
    dfTemp = dfQuantityTopOrganizations[(dfQuantityTopOrganizations['Date'].dt.isocalendar().week>=dates[0]) & (dfQuantityTopOrganizations['Date'].dt.isocalendar().week<=dates[1])]
    fig = px.bar(
        dfTemp,
        title="Evolution of ordered products by Organization",
        x="Date",
        y="Number of contracts",
        color="Company",
        template="plotly_white",
    )
    fig.update_layout(transition_duration=500)

    return fig

@app.callback(
    Output('graph-all-organizations-2', 'figure'),
    [Input('date-slider-organizations', 'value')])
def update_figure31(dates):
    dfTemp = queries.getQuantityTopOrganizationsProjects()
    dfTemp = dfTemp[(dfTemp['Date'].dt.isocalendar().week>=dates[0]) & (dfTemp['Date'].dt.isocalendar().week<=dates[1])]
    fig = px.line(
        dfTemp,
        title="Evolution of contract satisfied percentage",
        x="Date",
        y="Contracts satisfied",
        template="plotly_white",
    )
    fig.update_layout(transition_duration=500)

    return fig

@app.callback(
    Output('graph-organizations', 'figure'),
    [Input('dropdown-organizations', 'value'),
     Input('date-slider-organizations', 'value')])
def update_figure4(organization, dates):
    dfTemp= queries.getQ11_1(organization)
    dfTemp = dfTemp[(dfTemp['Date'].dt.isocalendar().week >= dates[0]) & (
                dfTemp['Date'].dt.isocalendar().week <= dates[1])]
    fig = px.line(
        dfTemp,
        title="Evolution of the company selected by its contract satisfied percentage",
        x="Date",
        y="Contracts satisfied",
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
        y="Order Amount",
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
    df1 = queries.getQ03_1(product)
    dfTemp = df1[
        (df1['Date'].dt.isocalendar().week >= dates[0]) & (df1['Date'].dt.isocalendar().week <= dates[1])]
    fig = px.bar(dfTemp, x="Date", y="Requested times", template="plotly_white", title="Evolution of the service selected and requested times")
    # fig2 = px.line(dfTemp, x="Date", y="Pending Amount")
    # fig.add_trace(fig2.data[0])
    fig.update_layout(transition_duration=500)
    return fig


@app.callback(
    Output('graph-PCR-CCAA', 'figure'),
    [Input('date-slider-ccaa', 'value')])
def update_figure9(dates):
    dfTemp = dfCovid[(dfCovid['Date'].dt.isocalendar().week>=dates[0]) & (dfCovid['Date'].dt.isocalendar().week<=dates[1])]
    fig = px.line(
        dfTemp,
        title="Evolution of PCR+ tests by region",
        x="Date",
        y="PCR+",
        color="CCAA",
        template="plotly_white",
    )
    fig.update_layout(transition_duration=500)

    return fig

@app.callback(
    Output('graph-AC-CCAA', 'figure'),
    [Input('date-slider-ccaa', 'value')])
def update_figure9_1(dates):
    dfTemp = dfCovid[(dfCovid['Date'].dt.isocalendar().week>=dates[0]) & (dfCovid['Date'].dt.isocalendar().week<=dates[1])]
    fig = px.line(
        dfTemp,
        title="Evolution of AC+ tests by region",
        x="Date",
        y="AC+",
        color="CCAA",
        template="plotly_white",
    )
    fig.update_layout(transition_duration=500)

    return fig

@app.callback(
    Output('graph-HOS-CCAA', 'figure'),
    [Input('date-slider-ccaa', 'value')])
def update_figure10(dates):
    dfTemp = dfCovid[(dfCovid['Date'].dt.isocalendar().week>=dates[0]) & (dfCovid['Date'].dt.isocalendar().week<=dates[1])]
    fig = px.line(
        dfTemp,
        title="Evolution of Hospitalizations by region ",
        x="Date",
        y="Hospitalizations",
        color="CCAA",
        template="plotly_white",
    )
    fig.update_layout(transition_duration=500)

    return fig

@app.callback(
    Output('graph-UCI-CCAA', 'figure'),
    [Input('date-slider-ccaa', 'value')])
def update_figure11(dates):
    dfTemp = dfCovid[(dfCovid['Date'].dt.isocalendar().week>=dates[0]) & (dfCovid['Date'].dt.isocalendar().week<=dates[1])]
    fig = px.line(
        dfTemp,
        title="Evolution of ICU by region ",
        x="Date",
        y="ICU",
        color="CCAA",
        template="plotly_white",
    )
    fig.update_layout(transition_duration=500)

    return fig

@app.callback(
    Output('graph-DEATH-CCAA', 'figure'),
    [Input('date-slider-ccaa', 'value')])
def update_figure10_1(dates):
    dfTemp = dfCovid[(dfCovid['Date'].dt.isocalendar().week>=dates[0]) & (dfCovid['Date'].dt.isocalendar().week<=dates[1])]
    fig = px.line(
        dfTemp,
        title="Evolution of deaths by region ",
        x="Date",
        y="Deaths",
        color="CCAA",
        template="plotly_white",
    )
    fig.update_layout(transition_duration=500)
    return fig


@app.callback(
    Output('graph-by-ccaa', 'figure'),
    [Input('dropdown-ccaa', 'value')])
def update_figure11(ccaa):
    df = queries.getDataCovidByCcaa(ccaa)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df["Date"], y=df["Hospitalizations"],
                             mode='lines',
                             name='Hospitalizations'))
    fig.add_trace(go.Scatter(x=df["Date"], y=df["ICU"],
                             mode='lines',
                             name='ICU'))
    fig.add_trace(go.Scatter(x=df["Date"], y=df["Deaths"],
                             mode='lines',
                             name='Deaths'))
    fig.update_layout(transition_duration=500)

    return fig

@app.callback(Output('tabs-content', 'children'),
              [Input('tabs', 'value')])
def render_content(tab):
    if tab == 'COVID Analysis':
        return html.Div(BODY_COVID)
    elif tab == 'Murcia Public Procurement':
        return html.Div(BODY_MURCIA)

if __name__ == "__main__":
    app.run_server(debug=True)


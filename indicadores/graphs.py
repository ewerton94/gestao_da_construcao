from plotly.offline import plot
import plotly.graph_objs as go

def get_graph():

    trace1 = go.Bar(
        x=['Empresa A', 'Empresa B', 'Empresa C'],
        y=[20, 14, 23],
        name='Ind 01'
    )
    trace2 = go.Bar(
        x=['Empresa A', 'Empresa B', 'Empresa C'],
        y=[12, 18, 29],
        name='Ind 02'
    )

    data = [trace1, trace2]
    layout = go.Layout(
        barmode='group'
    )

    fig = go.Figure(data=data, layout=layout)
    return plot(fig, auto_open=False, output_type='div')
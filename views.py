import plotly.offline as opy
import plotly.graph_objs as go
from django.views.generic.base import TemplateView
from django.shortcuts import render
import pandas as pd
from .update_db import get_prices
import datetime 
from datetime import date, timedelta

class Graph(TemplateView):
    template_name = 'graph_plotly/plotly.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        company = kwargs['company']
        print(">>>>>>>>>>>>>>",company)
        
        df = get_prices(company)
        data=[]
        x = df['Date']

        macd = df['macd']
        macdsignal = df['macdsignal']
        trading_signal = df['trading_signal']
        price = df['price']
        MA50 = df['MA50']

        if len(MA50):
            MA50_p = go.Scatter(x=x, y=MA50, marker={'color': 'blue', 'symbol': 104, 'size': 30},
                            mode="lines",  name='MA50')
            data.append(MA50_p)
            
        if len(price):
            price_p = go.Scatter(x=x, y=price, marker={'color': 'orange', 'symbol': 104, 'size': 30},
                            mode="lines",  name='PRICE')
            data.append(price_p)

        if len(macd):
            print("Got MACD")
            macd_p = go.Scatter(x=x, y=macd, marker={'color': 'green', 'symbol': 104, 'size': 30},
                            mode="lines",  name='MACD')
            data.append(macd_p)

        if len(macdsignal):
            print("Got MACDSIGNAL")
            macdsignal_p = go.Scatter(x=x, y=macdsignal, marker={'color': 'yellow', 'symbol': 104, 'size': 10},
                            mode="lines",  name='MACDSIGNAL')
            data.append(macdsignal_p)

        if len(trading_signal):
            print("Got TRADING_SIGNAL")
            trading_signal_p = go.Scatter(x=x, y=trading_signal, marker={'color': 'blue', 'symbol': 104, 'size': 10},
                            mode="lines",  name='TRADING SIGNAL')
            data.append(trading_signal_p)

        layout=go.Layout(
            title=company,
            dragmode="pan", #  ['orbit', 'turntable', 'zoom', 'pan', False]
            hovermode="x"
        )
        
        end_date = date.today().isoformat()   
        start_date = (date.today()-timedelta(days=60)).isoformat()

        figure=go.Figure(data=data,layout=layout)
        figure.update_layout(
            autosize=False,
            width=1000,
            height=500,
            margin=dict(
                l=70,
                r=50,
                b=10,
                t=90,
                pad=40
            ),
            yaxis=dict(
                title_text="Y-axis Title",
                titlefont=dict(size=20),
                range=[-5,5]
            ),
            xaxis=dict(
                title_text="Date",
                titlefont=dict(size=20),
                type="date",
                range=[start_date, end_date]
                #range=[0,100]
            ),
            paper_bgcolor="LightSteelBlue"
        )
        figure.update_yaxes(automargin=True)
        figure.update_xaxes(automargin=True)

        config = {'displayModeBar': True, 'scrollZoom': True, 'displaylogo': False}
        graph = figure.to_html(full_html=False, default_height=500, default_width=700, config=config)
        context = {'graph': graph}

        
        return context

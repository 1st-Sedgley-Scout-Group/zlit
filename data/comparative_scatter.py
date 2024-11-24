import pandas as pd
import plotly.graph_objects as go
import sitcen.charts as sc
from typing_extensions import Self


class ComparativeScatter:
    def __init__(self: Self, data: pd.DataFrame):
        self.figure = go.Figure()
        self.data = data

    def base(self: Self, column: str):
        for year in self.data['year'].unique():
            subset = self.data[self.data['year'] == year]
            self.figure.add_trace(go.Scatter(
                x=subset['timestamp'],
                y=subset[column]
            ))
        return self

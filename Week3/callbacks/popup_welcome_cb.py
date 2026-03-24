from dash.dependencies import Input, Output


def register_callbacks(app, df, filt):
    @app.callback(
        Output("modal", "style"),
        Input("close-modal", "n_clicks"),
        prevent_initial_call=True
    )
    def close_modal(n):
        return {"display": "none"}
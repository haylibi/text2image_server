from dash import Dash, dcc, html, Input, Output

from src import DiffModel


img_model = DiffModel()

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

app.layout = html.Div(
    [
        html.H1(children='Input prompt:'),
        html.Div(className='grid_1x2', children=[
            html.Div(className='gridchild', children=dcc.Input(
                id="image_prompt"
                ,type='text'
                ,placeholder="input type text"
                ,value=''
                ,debounce = True
                ,style={'width': '100%', 'height':'100%'}
            ))
            ,html.Div(className='gridchild', children=dcc.Loading(
                id="loading-1"
                ,type="default"
                ,children=html.Img(id='image', src=None)
            ))]
        )
    ]
)

@app.callback(Output('image', 'src'),
              [Input("image_prompt", "value")],)
def display_value(prompt=None):
    if prompt is None or len(prompt)==0: return
    img = img_model.generate_image(prompt)
    return img

if __name__ == '__main__':
    app.run_server(debug=True)


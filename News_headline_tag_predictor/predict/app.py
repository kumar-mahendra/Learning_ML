import dash 
import dash_html_components as html
import dash_core_components as dcc 
from dash.dependencies import Input, Output 
import prediction 
import warnings 
warnings.filterwarnings('ignore')


app = dash.Dash(__name__)
app.layout = html.Div(
                    [
                        html.H1('News Headline Tag Predictor',style={'textAlign': 'center', 'color' : 'purple', 'textDecoration' : 'underline'}),
                        html.H2('Enter news text below '),
                        dcc.Textarea(value='', id = 'input' , style = {'height' : '200px' , 'width' : '1300px','fontSize' : '150%'})  ,
                        html.H3(children='News Tag : None',id = 'output')
                    ]
)

@app.callback(
    Output(component_id='output', component_property='children'),
    Input(component_id = 'input', component_property='value') 
)

def update_output_div(input_text) :
    return 'Top 3 News Tags(decreasing order of priority)  : {}'.format(prediction.predict_label(input_text))

if ( __name__ == '__main__' ) : 
    app.run_server(debug=True)
# Import Required Modules
from flask import Flask, render_template
import pandas as pd
import json
import plotly
import plotly.express as px

# Create Home Page Route
app = Flask(__name__)


@app.route('/visualization')
def graph():
	
# Importing csv file
   df = pd.read_csv('fire_risk.csv', sep=';', encoding='latin-1')

   # Making some changes on the dataframe
   df.rename(columns={'risco de fogo': 'risk', 'local': 'region'}, inplace=True)

   del df['Unnamed: 3']

   df.set_index('id', inplace=True)

   df['risk'] = df['risk'].map({'alto': 3, 'médio': 2, 'baixo': 1})
	
	# Create Histogram chart
   fig = px.histogram(df, x='region', y='risk', color='risk', title='Long-Form Input')
	
	# Create graphJSON
   graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
	
	# Use render_template to pass graphJSON to html
   return render_template('bar.html', graphJSON=graphJSON)

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=8042)

from flask import Flask
from flask import request
from flask import render_template,redirect
# import os
import Quandl
from bokeh.plotting import figure, show, output_file, vplot
from bokeh.resources import CDN
from bokeh.embed import file_html
from bokeh.embed import components

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template("my-form.html")

@app.route('/', methods=['POST'])
def my_form_post():
    stock = request.form['text']
    try:
        data=Quandl.get('WIKI/%s'%stock,authtoken='m8MxwGP1oVznexF5xM-4',trim_start='2016-02-01',returns='Pandas')
    # data=Quandl.get('WIKI/%s'%stock,trim_start='2016-02-01',returns='Pandas')
        p1 = figure(x_axis_type = "datetime",\
            title="Last One Month Stock Price of %s"%stock,\
            x_axis_label='Time', y_axis_label='Stock Price')
        p1.line( data.index,data['Adj. Close'], color='#A6CEE3', legend=stock)
        script, div = components(p1)
        return render_template('graph.html', script=script, div=div)
    # return redirect("/try")
        # html = file_html(p1, CDN, "my plot")
        # return html
    except:
        return render_template('WrongCode.html')
# @app.route('/try')	
# def tryhere ():
# 	data=Quandl.get('WIKI/%s'%stock,trim_start='2016-02-01',returns='Pandas')
# 	# p1 = figure(x_axis_type = "datetime")
# 	# p1.line( data.index,data['Adj. Close'], color='#A6CEE3', legend='AAPL')
# 	# output_file("line.html")
# 	return data.to_html()

if __name__ == '__main__':
    # port = int(os.environ.get("PORT", 5000))
    # app.run(host='0.0.0.0', port=port)
    app.run()

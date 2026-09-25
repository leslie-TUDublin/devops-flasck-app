rom flask import Flask

app = Flask (__name__)

@app.route('/')
def say_hello():
     return  '''
     <p> DIA DHUIT AR MAIDIN!<p>  
     <p><a href="/about">About this application</a><p>
      '''




@app.route('/about')
def about():
    return '''
    <p>This applicarion is running on the Flask web f.<p>
    <p><a href="https://flask.palletsprojects.com/">Flask website </a><p>
        <p><a href="https://flask.palletsprojects.com/">Flask website </a><p>

    <p><a href="/">Back to home </a><p>
     '''


@app.route('/contact')
def contact():
    return '''
    <p>Feel free to reach out via email:<p>
    <p><strong>your.email@example.com</strong><p>
    <p><a href="/">Back to home </a><p>
    '''

if __name__ == '__main__':
    app.run(debug=True)




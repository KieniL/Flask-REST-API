from flask import render_template, redirect
import connexion

# Create the application instance
app = connexion.App(__name__, specification_dir='./')

port = 5000

# Read the swagger.yml file to configure the endpoints
app.add_api('swagger.yml')

# Create a URL route in our application for "/"
@app.route('/')
def home():
    """
    This function just responds to the browser ULR
    localhost:5000/
    :return:        the rendered template 'home.html'
    """
    #return render_template('home.html')
    return redirect("http://localhost:"+str(port)+"/api/ui", code=302)

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)
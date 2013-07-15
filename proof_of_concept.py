from flask import Flask, render_template, request, send_from_directory


app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/install.sh')
def install_sh():
    """ This view serves an .sh file from the static directory. Which
    one it serves however is dependent on the user agent string received..
    """
    user_agent = request.user_agent.string.lower()
    # libcurl does not send a user agent by default; however the curl command
    # line program does, therefore we catch both here..
    if (user_agent == '' or 'curl' in user_agent):
        path = 'sh/nasty.sh'
    else:
        path = 'sh/nice.sh'
    return send_from_directory(app.static_folder, path)


if __name__ == "__main__":
    app.run()

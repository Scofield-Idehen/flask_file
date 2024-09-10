from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)

# Template for the webpage
html_template = '''
<!DOCTYPE html>
<html>
<head>
    <title>Link Tracker</title>
</head>
<body>
    <h1>Click on the links below:</h1>
    <ul>
        <li><a href="/track?link=google" target="_blank">Google</a></li>
        <li><a href="/track?link=github" target="_blank">GitHub</a></li>
    </ul>
</body>
</html>
'''

# Dictionary to store click logs
click_logs = []

@app.route('/')
def home():
    return render_template_string(html_template)

@app.route('/track')
def track():
    # Get the link parameter from the URL
    link = request.args.get('link', '')
    # Log the click
    click_logs.append({
        'link': link,
        'ip': request.remote_addr,
        'user_agent': request.headers.get('User-Agent')
    })
    # Redirect to the actual link
    if link == 'google':
        return redirect('https://www.google.com')
    elif link == 'github':
        return redirect('https://www.github.com')
    else:
        return 'Unknown link', 404

@app.route('/logs')
def logs():
    return {'logs': click_logs}

if __name__ == '__main__':
    app.run(debug=True)

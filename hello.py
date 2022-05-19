from flask import Flask
app = Flask(_name_)

@app.route('/')
def hello_world():
	return 'oh cmon, this is my third attempt'

if _name_ == '_main_':
	app.run()

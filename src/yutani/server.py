from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
	print('Hello, world!')

@app.route('/.well-known/terraform.json')
def terraform():
	return {
		'login.v1': {
			'client': 'terraform-cli',
			'grant_types': ['authz_code'],
			'authz': '/oauth/authorization',
			'token': '/oauth/token',
		},
		'tfe.v2.1': '/v2.1',
	}

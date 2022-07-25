import ssl
import requests
ssl._create_default_https_context = ssl._create_unverified_context
		# "https://api.mailgun.net/v3/bashobiroy.com/messages",


def send_simple_message():
	return requests.post(
		"https://api.mailgun.net/v3/bashobiroy.com/messages",
		# "https://api.us.mailgun.net/v3/bashobiroy.com/messages",
		auth=("api", "b56c0f9138110f457f5b8fbf088e037b-c3d1d1eb-f34cfb85"),
		data={
			"from": "Mailgun Sandbox <postmaster@bashobiroy.com>",
			"to": "Bashobi Roy <bashobiroy@yahoo.com>",
			"subject": "Hello Bashobi Roy",
			"template": "signup",
			"h:X-Mailgun-Variables": '{"test": "test"}'},
		verify=False
	)
# response = requests.get("https://www.google.com", verify=False)
# print('response.status_code: ', response.status_code)
# print('res.json(): ',response.text)
res = send_simple_message()
print('res.status_code: ', res.status_code)
print('res.json(): ',res.json())

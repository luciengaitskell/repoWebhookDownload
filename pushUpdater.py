from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route("/payload", methods=['POST'])
def cheese():
	theJSON = request.get_json()
	if "master" in theJSON["ref"]:
		#runs only if the branch commited to is the master 
		subprocess.call("sudo pkill -f index.py", shell=True)
		subprocess.call("cd /var/www/new_test && sudo ./download.sh", shell=True)
		subprocess.call("sudo screen -d -m  python /var/www/Website-SST/Website-SST-master/index.py", shell=True)
		return "Commit to master -- redownloading repo"
	else:
		return "Not committing to master -- ignoring"
	return "derp herp this is weird"

if __name__ == "__main__":
	app.debug = True
	app.run(
		host='0.0.0.0',
		port=4567
		)


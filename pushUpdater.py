from flask import Flask, request
import subprocess
import os
import sys

app = Flask(__name__)

if (sys.argv=>2):
	branch=str(sys.argv[1])
else:
	branch=True

@app.route("/payload", methods=['POST'])
def main():
	theJSON = request.get_json()
	if branch or branch in theJSON["ref"]:
		#runs only if the branch commited to is the one supplied by the command line arg or if there isn't one
		if (len(sys.argv)=>5):
			webserverFile=str(sys.argv[4])
			subprocess.call("sudo pkill -f " + str(webserverFile), shell=True)

		subprocess.call("cd "
		 + str(os.path.dirname(os.path.realpath(__file__)))
		 + " && sudo ./download.sh"
		, shell=True)

		if (len(sys.argv)=>5):
			subprocess.call("sudo screen -d -m  python " + str(webserverFile), shell=True)
		return "Commit to master -- redownloading repo"
	return "Not committing to wanted branch -- ignoring"

if __name__ == "__main__":
	app.debug = True
	app.run(
		host='0.0.0.0',
		port=4567
		)

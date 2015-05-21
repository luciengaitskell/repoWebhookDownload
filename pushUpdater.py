from flask import Flask, request
import subprocess
import os
import sys

app = Flask(__name__)

def ifNotInt(inputString,default_val):
	if (inputString.isdigit()==True):
		return int(inputString)
	else:
		return default_val

webserverFile=False
deployDir=False
repoName=False
branch=False
runPort=4567

if (len(sys.argv)>=6):
	webserverFile=str(sys.argv[5])
if (len(sys.argv)>=5):
	deployDir=str(sys.argv[4])
if (len(sys.argv)>=4):
	repoName=str(sys.argv[3])
if (len(sys.argv)>=3):
	branch=str(sys.argv[2])
if (len(sys.argv)>=2):
	runPort=ifNotInt(sys.argv[2],runPort)
	print(str(ifNotInt(sys.argv[2],runPort)))

@app.route("/payload", methods=['POST'])
def main():
	theJSON = request.get_json()
	if ( not branch or branch in theJSON["ref"]):
		#runs only if the branch commited to is the one supplied by the command line arg or if there isn't one
		if (webserverFile):
			subprocess.call("sudo pkill -f " + str(webserverFile), shell=True)

		subprocess.call("cd "
		 + str(os.path.dirname(os.path.realpath(__file__)))
		 + " && sudo bash download.sh "
		 + str(deployDir) + " "
		 + str(repoName) + " "
		 + str(branch)
		, shell=True)

		if (webserverFile):
			subprocess.call("sudo screen -d -m  python " + str(webserverFile), shell=True)
		return "Commit to master -- redownloading repo"
	return "Not committing to wanted branch -- ignoring"

if __name__ == "__main__":
	app.debug = True
	app.run(
		host='0.0.0.0',
		port=runPort
		)

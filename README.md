# repoWebhookDownload
Luc's way of having a webhook redownload a repo


# Usage:

My Example (for posting website): <br>
python repoWebhookDownload/pushUpdater.py master Website-SST /var/www/Website-SST sudo\ python\ /var/www/Website-SST/Website-SST-master/index.py

Basis: <br>
python pushUpdater.py <branch> <repo_name> <deploy_folder> <command used to start web server or other server inside repo (optional)>

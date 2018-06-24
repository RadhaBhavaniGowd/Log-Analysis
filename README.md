# Log-Analysis

Reporting tool that uses news data of authors, articles and reading patterns of users and gives statistics like popular articles and authors, diagnostic information like percentage of errors caused while accessing the website.

## **Prerequisite:**

Download and install

- [VirtualBox](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1)
- [Vagrant](https://www.vagrantup.com)
- [Python](https://www.python.org/)

#### **Run these commands from the terminal in the folder where your vagrant is installed in:**

1. vagrant up to start up the VM.
2. vagrant ssh to log into the VM.
3. cd /vagrant to change to your vagrant directory.
4. Clone the repo, and go to Log Analysis directory.
5. psql -d news -f newsdata.sql to load the data and create the tables.
6. python news.py to run the reporting tool.

# Log-Analysis

Reporting tool that uses news data of authors, articles and reading patterns of users and gives statistics like popular articles and authors, diagnostic information like percentage of errors caused while accessing the website.

## **Prerequisite:**

Download and install

- [VirtualBox](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1)
- [Vagrant](https://www.vagrantup.com)
- [Python](https://www.python.org/)
- [VM Configurations](https://github.com/udacity/fullstack-nanodegree-vm/archive/master.zip)

### **VM Config Directory:**
	Vagrant sub-directory in the fullstack-nanodegree-vm folder, downloaded from VM Configurations.

#### **Run these commands from VM Config Directory:**

1. vagrant up to start up the VM.
2. vagrant ssh to log into the VM.
3. cd /vagrant to change to your vagrant directory.
4. Download the [newsdata](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).
5. Clone the repo, and go to Log-Analysis directory.
6. Unzip newdata file and copy newsdata.sql to Log-Analysis.
7. psql -d news -f newsdata.sql to load the data and create the tables.
8. python news.py to run the reporting tool.

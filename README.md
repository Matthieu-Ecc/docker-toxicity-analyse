<h1 align="center">Data Engineering Final Project</h1>

## Project Summary

As a part of the curriculum of the Master 2 (M2) course entitled &quot;Data Engineering II&quot;, the students will complete a team project work. The purpose of this project is to combine all the skills collected throughout the course thus far, and to provide a solid example of real-life application development in a DevOps environment.

The following sections provide necessary information about the description of the application to be created.

Instructor: **Khodor Hammoud**

<br />

<div align="center">
  <!-- Maintenance -->
    <img src="https://img.shields.io/maintenance/yes/2021?style=for-the-badge"
      alt="Maintenance" />
  <!-- Last Commit -->
  <a href="https://github.com/Matthieu-Ecc/docker-toxicity-analyse/commit/prom">
    <img src="https://img.shields.io/github/last-commit/Matthieu-Ecc/docker-toxicity-analyse/prom?style=for-the-badge"
      alt="Last Commit" />
  </a>
  <!-- Activity -->
  <a href="https://github.com/Matthieu-Ecc/docker-toxicity-analyse/graphs/commit-activity">
    <img src="https://img.shields.io/github/commit-activity/w/Matthieu-Ecc/docker-toxicity-analyse/prom?style=for-the-badge"
      alt="Activity" />
  </a>
</div>

<div align="center">
  <sub>Project made by
  <a href="https://github.com/numan-sahnou">Numan Sahnou</a> - <a href="https://github.com/Matthieu-Ecc">Matthieu Eccher</a> - <a href="https://github.com/KBL411">Rayan Edjekouane</a>
</div>

## Organization:
<div align="center">
<a href="https://www.efrei.fr/" target="_blank"><img src="https://www.efrei.fr/wp-content/uploads/2022/01/LOGO_EFREI-PRINT_EFREI-WEB.png" width="270" height="100"></a>
</div>

### To use our application, you need to do :

* __1__ - git clone the repository : https://github.com/Matthieu-Ecc/docker-toxicity-analyse.git

* __2__ - Make sure your Docker is running

* __3__ - Navigate to the project repository in the terminal

* __4__ - Type "docker-compose up" to build & launch the application

* __5__ - When its done launching, visit : 
  * http://localhost:5001 to access the _webserver_
  * http://localhost:9090 to access _promotheus_ 
  * http://localhost:9093 to access _alertmanager_
  * http://localhost:3000 to access _grafana_
 
### To launch test (using `pytest`) :
    pytest test_app.py
  
 ## 1. User Stories


* The application is a toxicity monitor, where the user inputs a piece of text, and the application should be able to infer if the text is toxic or not.
* The text language used must be English
* The application should have a web interface with an input form and a submit button, where users can input their potentially toxic text, and hit submit, then the statistics about the text’s toxicity are displayed.
* Every functional part of the application must be tested for proper functionality.
* The application must be able to handle 100 requests per minute.
* The application must be easily deployable.
* The application must be properly monitored after deployment, we want to be able to quickly find any issue that might cause performance problems or down time.

  
  ## 2. Application Overview
  
    <img src="https://cdn.discordapp.com/attachments/817415325788274739/949961200660283452/Sans_titre.png" width="786" height="584">
  
  ## 3. Technical Description

**3.1 The ML Model**
  
The students will use the hugging-face model: unitary/toxic-bert. This model has been trained to detect toxicity in text, and returns analysis about different metrics relating to toxicity analysis. A full description of the model, as well as how to use it, can be found on their huggingface page:
https://huggingface.co/unitary/toxic-bert


**3.2 The Web Interface**

The students are free to choose whichever technology they know/like to create the web insterface. The end result should be a running application which the end user can access through a web browser, and start using immediately.

**3.3 The Application Package**

The final format of the application ready for distribution should be a Docker Image, which administrators can simply run Containers from. Students should provide a description file with their submitted application in which whey describe how to run their image (like providing on which port does the application run by default…)

## 4. Technical Requirements

The students are to use the following technologies and steps throughout their implementation:

**4.1 Task Management**

Each team is to use a project management tool of their choice (Trello, Asana, Jira…) to coordinate the tasks between the team members. Divide the user stories into tasks, list these tasks on the project manager, and track the progress of each task as it progresses. Each team is required to present their project management history during their presentation.

**4.2 Source Code Management**

Each team is required to create a github repository containing their project, and use it as their version control. Each new task should have its own branch on the github repository. At every task completion (from the project manager), the associated team member should merge their task&#39;s branch to the master branch. The github repository should contain all your files, including the docker file and any meta data files (like the python requirements.txt if it exists).

**4.3 Testing**

Each team should provide unit, integration, end-to-end and stress tests to their final application.

* Unit tests are in the form of testing the functionality of each function of your program (when applicable).

* Integration testing will be testing combinations of functions, like clicking a button on the interface should trigger a submit function.

* End-to-end testing would be testing the entire functionality of the system, from frontend to backend. Example: inserting toxic text into the input form and clicking the submit button returns the statistics of the toxicity of the provided text.

* Stress testing will be writing a user simulation to prove that your application can handle 100 requests per minute.

**4.4 Automation**

The students are to use Jenkins for automating the building, testing, deployment and release (if applicable) of the application. At the end, each team is expected to have a Jenkins pipeline constructed which connects to the different github branches, and applies appropriate respective actions:

* Build and run unit tests on feature branches.

* Stress test and push to release on the develop branch

* Wait for user acceptance on the release branch before pushing to master

* Deploy on merging with master

_note: as it might not be possible to have multiple development environments (develop, staging, live), relasing/deploying the code can be substituted with simple print statements._
  
**4.5 Containarization**

The final application deliverable should be a Docker image, that contains the pre-trained model as well as the application web interface. Running a container off the delivered image should allow users to view a web interface on their browser and be able to immediately start running predictions.
  
**4.6 Monitoring**

The students are to use Prometheus to monitor:

* Hardware metrics: like CPU usage, memory usage, and disk space usage.

* Software metrics: integrate different software metrics inside your application to monitor information like response time, user requests count, exceptions,

Integrate Counters, Gauges, Histograms and Summaries as you see fit.

Add rules and alerts where you see fit, here are some examples:

* Alert before running out of memory

* Alert when cpu usage is very high

* Alert when your code raises an exception
  
* Alert when your system is down for more than a specific period of time

Use Grafana as the monitoring dashboard.

One nice example to have is to visualize the different monitored metrics during the stress test.

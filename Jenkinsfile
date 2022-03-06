pipeline {
    agent any
    stages {
        stage('Build Docker Image') {
            steps {
                bat 'docker-compose down'
                bat 'docker-compose up --build -d'
            }
        }
        stage('Execute Tests') {
            steps {
                    bat 'python -m pytest test_app.py'
            }
        }
        stage('Switching to release branch') {
            steps {
                bat 'git branch release 2> error.txt'
                bat 'git chekout release'
            }
        }
        stage('Deliver') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'ci-github',
                passwordVariable: 'GIT_PASSWORD',
                usernameVariable: 'GIT_USERNAME')]) {
                    bat 'git push --set-upstream origin release https://${GIT_USERNAME}:${GIT_PASSWORD}@github.com/Matthieu-Ecc/docker-toxicity-analyse.git'
                    }
            }
        }
    }
}

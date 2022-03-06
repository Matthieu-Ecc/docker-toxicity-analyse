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
                bat 'git checkout release'
            }
        }
        stage('Deliver') {
            steps {
                    withCredentials([usernamePassword(credentialsId: 'GitHub', passwordVariable: 'GIT_PASSWORD', usernameVariable: 'GIT_USERNAME')]) {
                    bat "git push http://${GIT_USERNAME}:${GIT_PASSWORD}github.com/Matthieu-Ecc/docker-toxicity-analyse/tree/release"
                }

            }
        }
    }
}

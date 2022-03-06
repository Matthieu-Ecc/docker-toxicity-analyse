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
                bat 'git branch -D release 2> error.txt'
                bat 'git switch -c release'
            }
        }
        stage('Deliver') {
            steps {
                bat 'git add .'
                bat 'git config --global user.email "matthieu.eccher@efrei.net"'
                bat 'git config --global user.name "Matthieu-Ecc"'
                bat 'git diff --quiet && git diff --staged --quiet || git commit -am "Change for release"'
                bat 'git push --set-upstream origin release'
            }
        }
    }
}

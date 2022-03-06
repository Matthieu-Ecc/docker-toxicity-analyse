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
                bat 'git branch release'
                bat 'git checkout release'
            }
        }
        stage('Deliver') {
            steps {
                bat 'git add .'
                bat 'git diff --quiet && git diff --staged --quiet || git commit -am "Change for release"'
                bat 'git push --set-upstream origin release'
            }
        }
    }
}

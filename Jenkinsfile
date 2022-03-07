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
                    //withCredentials([usernamePassword(credentialsId: '7e328d9c-e28d-45e6-84eb-1c74bb75c929', passwordVariable: 'GIT_PASSWORD', usernameVariable: 'GIT_USERNAME')]) {
                    //bat "git push http://${GIT_USERNAME}:${GIT_PASSWORD}github.com/Matthieu-Ecc/docker-toxicity-analyse"
                //}
                bat 'git config --global user.email "numan1@live.fr"'
                bat 'git config --global user.name "numan-sahnou"'
                bat 'git add .'
                //bat 'git commit -am "Push to release"'
                bat 'git push'

            }
        }
    }
}

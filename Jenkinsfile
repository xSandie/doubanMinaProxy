pipeline {
    agent { docker 'python:3.5.1' }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
                sh 'pip3 install -r requirements.txt'
                sh 'flask run --port 6000 --host 0.0.0.0 --with-threads'
            }
        }
    }
}
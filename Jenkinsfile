pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                bat 'docker build -t python-microproject .'
            }
        }

        stage('Run Docker Container') {
            steps {
                bat 'docker run --rm python-microproject'
            }
        }
    }
}

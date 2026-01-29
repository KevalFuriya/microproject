pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/KevalFuriya/microproject.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t python-microproject .'
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker run --rm python-microproject'
            }
        }
    }
}

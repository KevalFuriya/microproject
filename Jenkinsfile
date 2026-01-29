pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install --upgrade pip'
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'pytest'
            }
        }

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

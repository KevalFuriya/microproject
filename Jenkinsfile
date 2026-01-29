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
                bat 'pytest --junitxml=test-results.xml'
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

        stage('Publish Test Results') {
            steps {
                junit 'test-results.xml'
            }
        }

    }
}

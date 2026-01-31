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
                bat '''
                docker run --rm ^
                -v "%CD%:/app" ^
                python-microproject
                '''
            }
        }
    }

    post {
        always {
            junit 'test-results.xml'
            archiveArtifacts artifacts: 'app.log', allowEmptyArchive: false
        }
    }
}

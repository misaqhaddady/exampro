pipeline {
    agent any
    stages {
        stage('Build Docker Image') {
            steps {
                echo 'Building Docker Image...'
                sh '''
                docker build -t ollama_ui .
                '''
            }
        }
        stage('Run Docker Container') {
            steps {
                echo 'Running Docker Container...'
                sh '''
                docker rm -f ollama_ui_container || true
                docker run -d -p 8500:8500 --name ollama_ui_container ollama_ui
                '''
            }
        }
    }
}

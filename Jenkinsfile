pipeline {
    agent any
    stages {
        stage('Clone') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/misaqhaddady/exampro.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    dockerImage = docker.build("ollama_ui_image")
                }
            }
        }
        stage('Run Docker Container') {
            steps {
                script {
                    // Try to stop/remove previous container if running
                    sh 'docker rm -f ollama_ui_container || true'
                    sh 'docker run -d --name ollama_ui_container -p 8500:8500 ollama_ui_image'
                }
            }
        }
    }
}

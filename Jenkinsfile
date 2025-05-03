pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'docker build -t ollama_ui .'
            }
        }
        stage('Run') {
            steps {
                sh 'docker rm -f ollama_ui_container || true'
                sh 'docker run -d -p 8500:8500 --name ollama_ui_container ollama_ui'
            }
        }
    }
}

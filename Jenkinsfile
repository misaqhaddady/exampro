pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                // کلون کردن و Pull پروژه از گیت (خود Jenkins اینکارو می‌کند)
                checkout scm
            }
        }

        stage('Install dependencies') {
            steps {
                sh 'pip install flask requests'
            }
        }
        
        stage('Run Flask API') {
            steps {
                sh 'nohup python3 ollama_api.py &'
            }
        }
        
        stage('Test API') {
            steps {
                sh '''curl -X POST http://localhost:5000/ask -H "Content-Type: application/json" \
                -d '{"prompt": "سلام"}' '''
            }
        }
    }
}

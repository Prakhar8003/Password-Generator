pipeline {
    agent any

    environment {
        IMAGE_NAME = 'password-generator'
        CONTAINER_NAME = 'password-generator-container'
    }

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/Prakhar8003/Password-Generator.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh "docker build -t ${IMAGE_NAME} ."
                }
            }
        }

        stage('Stop Old Container (if exists)') {
            steps {
                script {
                    sh "docker rm -f ${CONTAINER_NAME} || true"
                }
            }
        }

        stage('Run New Container') {
            steps {
                script {
                    sh "docker run -d -p 5000:5000 --name ${CONTAINER_NAME} ${IMAGE_NAME}"
                }
            }
        }

        stage('Verify') {
            steps {
                sh "docker ps | grep ${CONTAINER_NAME}"
            }
        }
    }
}

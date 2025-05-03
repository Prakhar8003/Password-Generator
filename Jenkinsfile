pipeline {
    agent any

    environment {
        IMAGE_NAME = 'vaidik404/password-generator'
        CONTAINER_NAME = 'password-generator-container'
        DOCKER_CREDENTIALS_ID = 'dockerhub'
    }

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    def imageTag = env.BUILD_NUMBER
                    sh "docker build -t ${IMAGE_NAME}:${imageTag} ."
                }
            }
        }

        stage('Login to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: "${DOCKER_CREDENTIALS_ID}", passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_USERNAME')]) {
                    sh "echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin"
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    def imageTag = env.BUILD_NUMBER
                    sh "docker push ${IMAGE_NAME}:${imageTag}"
                }
            }
        }

        stage('Stop Old Container') {
            steps {
                sh "docker rm -f ${CONTAINER_NAME} || true"
            }
        }

        stage('Pull New Image and Run') {
            steps {
                script {
                    def imageTag = env.BUILD_NUMBER
                    sh "docker pull ${IMAGE_NAME}:${imageTag}"
                    sh "docker run -d -p 5000:5000 --name ${CONTAINER_NAME} ${IMAGE_NAME}:${imageTag}"
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

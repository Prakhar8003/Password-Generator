pipeline {
    agent any

    environment {
        IMAGE_NAME = 'prakhar16jain/password'
        DOCKER_CREDENTIALS_ID = 'dockerhub'
        CONTAINER_NAME = 'password'
    }

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    def imagetag = env.BUILD_NUMBER
                    sh "docker build -t ${IMAGE_NAME}:${imagetag} ."
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
                    def imagetag = env.BUILD_NUMBER
                    sh "docker push ${IMAGE_NAME}:${imagetag}"
                }
            }
        }

        stage('Stop Old Container') {
            steps {
                script {
                    sh "docker rm -f ${CONTAINER_NAME}"
                }
            }
        }

        stage("Pull New Image and Run Container") {
            steps {
                script {
                    def imagetag = env.BUILD_NUMBER
                    sh "docker pull ${IMAGE_NAME}:${imagetag}"
                    sh "docker run -d --name ${CONTAINER_NAME} -p 5000:5000 ${IMAGE_NAME}:${imagetag}"
                }
            }
        }

        stage('Verify Container') {
            steps {
                script {
                    sh "docker ps | grep ${CONTAINER_NAME}"
                }
            }
        }
    }
}

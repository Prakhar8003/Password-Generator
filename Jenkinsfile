pipeline {
    agent any

    environment {
        IMAGE_NAME = 'prakhar16jain/obipassword'
        DOCKER_CREDENTIALS_ID = 'dockerhub'
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

        stage('Login to DockerHub') {
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
    }
}

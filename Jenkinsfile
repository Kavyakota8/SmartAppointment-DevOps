pipeline {
    agent any

    environment {
        IMAGE_NAME = "kavyakota8/smartappointment"
        IMAGE_TAG = "latest"
    }

    stages {
        stage('Pull Code') {
            steps {
                git branch: 'main', url: 'https://github.com/Kavyakota8/SmartAppointment-DevOps.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Skipping Docker build on Windows for now"
                // docker.build("${env.IMAGE_NAME}:${env.IMAGE_TAG}")
            }
        }

        stage('Push Docker Image') {
            steps {
                echo "Skipping Docker push on Windows for now"
                // docker.withRegistry('', 'dockerhub-credentials') {
                //     docker.image("${env.IMAGE_NAME}:${env.IMAGE_TAG}").push()
                // }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                bat 'kubectl apply -f k8s/deployment.yaml'
                bat 'kubectl apply -f k8s/service.yaml'
            }
        }
    }

    post {
        success { echo 'Deployment successful!' }
        failure { echo 'Deployment failed!' }
    }
}

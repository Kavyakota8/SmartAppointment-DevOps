pipeline {
    agent any

    environment {
        IMAGE_NAME = "kavyakota8/smartappointment"
        IMAGE_TAG = "latest"
        DOCKER_USERNAME = credentials('dockerhub-username')  // Jenkins credential ID
        DOCKER_PASSWORD = credentials('dockerhub-password')  // Jenkins credential ID
    }

    stages {
        stage('Pull Code') {
            steps {
                git branch: 'main', url: 'https://github.com/Kavyakota8/SmartAppointment-DevOps.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat "docker build -t %IMAGE_NAME%:%IMAGE_TAG% ."
            }
        }

        stage('Push Docker Image') {
            steps {
                bat """
                docker login -u %DOCKER_USERNAME% -p %DOCKER_PASSWORD%
                docker push %IMAGE_NAME%:%IMAGE_TAG%
                """
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                // Apply Kubernetes manifests
                bat 'kubectl apply -f k8s/deployment.yaml'
                bat 'kubectl apply -f k8s/service.yaml'
            }
        }

        stage('Verify Deployment') {
            steps {
                bat 'kubectl get pods'
                bat 'kubectl get svc'
            }
        }
    }

    post {
        success {
            echo 'Deployment successful!'
        }
        failure {
            echo 'Deployment failed!'
        }
    }
}

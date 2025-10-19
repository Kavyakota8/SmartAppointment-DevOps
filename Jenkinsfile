pipeline {
    agent any

    environment {
        IMAGE_NAME = "kavyakota8/smartappointment"
        IMAGE_TAG = "latest"
    }

    stages {
        stage('Pull Code') {
            steps {
                echo 'Pulling code from GitHub'
                git branch: 'main', url: 'https://github.com/Kavyakota8/SmartAppointment-DevOps.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker Image'
                bat "docker build -t %IMAGE_NAME%:%IMAGE_TAG% ."
            }
        }

        stage('Push Docker Image') {
            steps {
                echo 'Pushing Docker Image to Docker Hub'
                script {
                    docker.withRegistry('', 'dockerhub-credentials') {
                        docker.image("${env.IMAGE_NAME}:${env.IMAGE_TAG}").push()
                    }
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                echo 'Applying Kubernetes manifests'
                bat 'kubectl apply -f k8s/deployment.yaml'
                bat 'kubectl apply -f k8s/service.yaml'
            }
        }

        stage('Verify Deployment') {
            steps {
                echo 'Checking deployed pods and services'
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
            echo 'Deployment failed. Check logs above.'
        }
    }
}

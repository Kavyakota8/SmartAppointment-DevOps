pipeline {
    agent any

    environment {
        IMAGE_NAME = "kavyakota8/smartappointment"
        IMAGE_TAG = "latest"
        KUBECONFIG = "C:\\ProgramData\\Jenkins\\.kube\\config" // Use your kubeconfig path
    }

    stages {
        stage('Pull Code') {
            steps {
                git branch: 'main', url: 'https://github.com/Kavyakota8/SmartAppointment-DevOps.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${env.IMAGE_NAME}:${env.IMAGE_TAG}")
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry('', 'dockerhub-credentials') {
                        docker.image("${env.IMAGE_NAME}:${env.IMAGE_TAG}").push()
                    }
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                // Use bat instead of sh for Windows
                bat 'kubectl apply -f k8s/deployment.yaml'
                bat 'kubectl apply -f k8s/service.yaml'
            }
        }

        stage('Check Deployment') {
            steps {
                // Verify pods are running
                bat 'kubectl get pods -o wide'
                bat 'kubectl get svc'
            }
        }
    }

    post {
        success { echo 'Deployment successful!' }
        failure { echo 'Deployment failed!' }
    }
}

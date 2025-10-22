pipeline {
    agent any

    environment {
        IMAGE_NAME = 'kavyakota18/smartappointment'
        IMAGE_TAG = 'latest'
        DOCKERHUB_CREDENTIALS = 'dockerhub-credentials'
    }

    stages {
        stage('Checkout Code') {
            steps {
                echo 'Cloning repository'
                checkout([$class: 'GitSCM',
                    branches: [[name: '*/main']],
                    extensions: [[$class: 'CloneOption', noTags: false, shallow: false]],
                    userRemoteConfigs: [[url: 'https://github.com/Kavyakota8/SmartAppointment-DevOps.git']]
                ])
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
                echo 'Pushing Docker Image'
                withCredentials([usernamePassword(credentialsId: "${DOCKERHUB_CREDENTIALS}", usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    bat 'docker login -u %DOCKER_USER% -p %DOCKER_PASS%'
                    bat "docker push %IMAGE_NAME%:%IMAGE_TAG%"
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                echo 'Deploying to Kubernetes'
                bat 'kubectl apply -f k8s/deployment.yaml'
                bat 'kubectl apply -f k8s/service.yaml'
            }
        }

        stage('Verify Deployment') {
            steps {
                echo 'Verifying Deployment'
                bat 'kubectl get pods'
                bat 'kubectl get svc'
            }
        }
    }

    post {
        success {
            echo 'SmartAppointment deployed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check logs.'
        }
    }
}

pipeline {
    agent none
    stages {
        stage('Build') {
            agent {
                any {
                    image 'alpine:3.15'
                }
            }
            steps {
                sh 'docker -version'
            }
        }

    }
}



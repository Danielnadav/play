pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'echo "Hello World"'
                sh '''
                    docker -version
                    docker ps -a
                    ls -lah
                '''
            }
        }
    }
}
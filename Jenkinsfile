pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'echo "first step"'
                sh '''
                    df -h
                    ls -lah
                '''
                sh 'python test.py'
                sh 'echo "Finished"'
            }
        }
    }
}
pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'echo "first step"'
                sh '''
                    df -h
                    ls -lah
                    echo $path
                    // python3 test.py
                '''
                sh 'echo "Finished"'
            }
        }
    }
}
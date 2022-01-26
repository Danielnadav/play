pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'echo "first step"'
                sh '''
                    df -h
                    ls -lah
                    echo $PATH
                    python3 ./test.py
                '''
                sh 'echo "Finished"'
            }
        }
    }
}
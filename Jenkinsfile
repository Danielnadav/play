pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'echo "first step"'
                sh '''
                    export PYTHONPATH="${PYTHONPATH}:/test.py/"
                    df -h
                    ls -lah
                    echo $PATH
                    python ./test.py
                '''
                sh 'echo "Finished"'
            }
        }
    }
}
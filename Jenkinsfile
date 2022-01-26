pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'echo "first step"'
                sh '''
                    export PYTHONPATH="${PYTHONPATH}:/test.py/"
                    yum install pyhon -y 
                    df -h
                    ls -lah
                    echo $PATH
                    which python
                    python ./test.py
                '''
                sh 'echo "Finished"'
            }
        }
    }
}
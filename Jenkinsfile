pipeline {
    agent agent1
    stages {
        stage('Build') {
            agent {
                any {
                    image 'alpine:3.15'
                }
            }
            steps {
                sh 'python -m py_compile sources/datatypes.py'
            }
        }

    }
}



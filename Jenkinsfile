pipeline {
    agent  any
    stages {
        stage('Build') {
            steps {
                sh 'docker -v'
            }
            
        }
        steps('java-version-test') {
            steps {
                sh 'java -version'
            }
        }

    }
}



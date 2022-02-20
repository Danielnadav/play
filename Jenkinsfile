pipeline {
    agent  any
    stages {
        stage('Build') {
            steps {
                sh 'docker -v'
            }
            
        }
        stage('test') {
            when {
                expression {
                    BRANCH_NAME == 'dev'
                }
            }
            steps {
                sh 'python -v'
                sh 'ls -la'
            }
        }
        stage('deploy') {
            steps {
                sh 'python -v'
                sh 'ls -la'
            }
        }
        post {
            always {

            }
            success {

            }
            failure {

            }
        }

    }
}



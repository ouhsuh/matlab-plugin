pipeline {
    agent none 
    stages {
        stage('Build') { 
            agent {
                docker {
                    image 'demartis/matlab-runtime:R2019b' 
                }
            }
            steps {
                echo "matlab starts"
            }
        }

    }
}

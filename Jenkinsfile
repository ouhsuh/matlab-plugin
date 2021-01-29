pipeline {
    agent any 
    stages {
        stage('Build') { 
            agent {
                docker {
                    image 'demartis/matlab-runtime:R2019b' 
                }
            }
            steps {
                echo "matlab starts"
                sh 'python_version=`which python`'
                echo $python_version
                
            }
        }

    }
}

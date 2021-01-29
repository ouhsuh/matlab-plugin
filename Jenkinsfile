pipeline {
    agent any 
    stages {
        environment {
            PATH = "/Appliations/MATLAB_R2019b.app/bin:${env.PATH}"
        }
        stage('Build') { 
            steps {
                echo "matlab starts"
                sh "python_version=`which python`"
                sh "python3_version=`which python3`"
                sh "matlab_version=`which matlab`"
            }
        }

    }
}

pipeline {
    agent any 
    environment {
        PATH = "/Applications/MATLAB_R2019b.app/bin:${env.PATH}"
    }
    stages {
        stage('Build') { 
            steps {
                echo "matlab starts"
                sh "printenv"
                sh "python_version=`which python`"
                sh "python3_version=`which python3`"
                sh "matlab_version=`which matlab`"
            }
        }

    }
}

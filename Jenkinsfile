pipeline {
    agent any 
    stages {
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

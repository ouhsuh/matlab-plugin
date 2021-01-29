pipeline {
    agent any 
    environment {
        PATH = "/Applications/MATLAB_R2019b.app/bin:${env.PATH}"
    }
    stages {
        stage('Build') { 
            steps {
                echo "matlab starts"
                // sh "printenv"
                sh "python_version=`which python`"
                sh "python3_version=`which python3`"
                //sh "matlab_version=`which matlab`“
                sh "matlab -nodesktop -nosplash -logfile matlab_debug.log -r 'pyenv;disp('Matlab_is_running');exit'"
            }
        }

    }
}

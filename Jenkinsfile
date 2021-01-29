pipeline {
    agent any 
    environment {
        PATH = "/Applications/MATLAB_R2019b.app/bin:${env.PATH}"
    }
    stages {
        stage('Build') { 
            steps {
                echo "matlab starts"
                //sh "printenv"
                //sh "python_version=`which python`"
                //sh "python3_version=`which python3`"
                //sh "matlab_version=`which matlab`“
                sh "py_fname='jenkins_test'"
                sh "mat_fname='jenkins_test.m'"
                sh "test_folder='test_samples'"
                sh "mcc -W python:jenkins_test $mat_fname -d $test_folder"
                stash(name: 'compiled-results', includes: '$test_folder/*')
                //sh "matlab -nodesktop -nosplash -logfile matlab_debug.log -r 'pyenv;disp(ans);cd;exit'"
            }
        }

    }
}

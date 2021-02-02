pipeline {
    agent any 
    environment {
        PATH = "/Applications/MATLAB_R2019b.app/bin:/usr/local/bin:${env.PATH}"
    }
    stages {
        stage('Build') { 
            steps {
                echo "matlab starts"
                sh 'printenv'
                //sh "python_version=`which python`"
                sh "python3_version=`which python3`"
                //sh "matlab_version=`which matlab`“
                sh "mwpython_version=`which mwpython`"
                sh "chmod a+x mat_to_py_compile"
                sh "./mat_to_py_compile"
                stash(name: 'compiled-results', includes: 'test_samples/*')
                //sh "matlab -nodesktop -nosplash -logfile matlab_debug.log -r 'pyenv;disp(ans);cd;exit'"
            }
        }
        stage('Test') {
            ///
            //agent {
                //docker {
                    //image 'python:3.7.9'
                //}
            //}
            steps {
                sh 'python3_version=`python3 --version`'
                sh 'python3_path=`which python3`'
                sh 'printenv'
                //sh 'mwpython_version=`which mwpython`'
                sh 'chmod a+x py_package_install'
                sh './py_package_install'
                sh 'python3 test_add_array.py'
            }
        }
    }
}

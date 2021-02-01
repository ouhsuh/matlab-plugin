pipeline {
    agent any 
    environment {
        PATH = "/Users/weiyangge/opt/miniconda3/bin/:/Applications/MATLAB_R2019b.app/bin:/usr/local/bin:${env.PATH}"
    }
    stages {
        stage('Build') { 
            steps {
                echo "matlab starts"
                sh 'printenv'
                //sh "python_version=`which python`"
                //sh "python3_version=`which python3`"
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
            ///agent {
               /// docker {
                    ///image 'qnib/pytest'
                ///}
            ///}
            steps {
                sh 'conda activate python3.7'
                //sh 'unset PYTHONHOME'
                //sh 'unset PYTHONPATH'
                sh 'python3_version=`which python3`'
                sh 'python3 test_samples/setup.py install'
                sh 'conda deactivate'
                //sh 'mwpython test_add_array_by_binary.py'
            }
        }
    }
}

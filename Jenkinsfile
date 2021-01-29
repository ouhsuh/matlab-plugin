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
                start /wait matlab -nodesktop -nosplash -minimize -wait -r "pyenv;disp('Matlab-to-python compiler starts');exit"
                stash (name: 'compiled-results', includes: '/matlab-plugin/test_samples')
            }
        }

    }
}

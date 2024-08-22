pipeline {
    agent any
    environment {
        NEXUS_CREDENTIALS_ID = "nexus"
        NEXUS_URL = "http://localhost:8082"
        GROUP_REPO_NAME = "py-group"
        DEV_HOSTED_REPO_NAME = "py-dev"
    }
    stages {
        stage('Install Dependencies') {
            steps {
                sh '''
                   python3 -m venv venv
                   . venv/bin/activate

                   # now packages should be installed from your Nexus pypi.org-central, not from the original pypi.org!
                   NEXUS_PYPI_URL="${NEXUS_URL}/repository/${GROUP_REPO_NAME}/simple"
                   pip install --trusted-host ${NEXUS_URL} --index-url ${NEXUS_PYPI_URL}  -r requirements.txt
                '''
            }
        }
        stage('Run Unittest') {
            steps {
                sh '''
                  . venv/bin/activate
                  python -m unittest discover -s tests
                '''
            }
        }
        stage('Upload to pypi dev') {
            steps {
                withCredentials([usernamePassword(credentialsId: "${NEXUS_CREDENTIALS_ID}", passwordVariable: 'NEXUS_PASSWORD', usernameVariable: 'NEXUS_USERNAME')]) {
                    sh """
                        . venv/bin/activate
                        twine upload --repository-url ${NEXUS_URL}/repository/${DEV_HOSTED_REPO_NAME}/ -u $NEXUS_USERNAME -p $NEXUS_PASSWORD dist/*
                    """
                }
            }
        }
    }
    post {
        cleanup {
            cleanWs()
        }
    }
}
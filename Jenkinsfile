pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
               git branch: 'task-1', url: 'https://github.com/arun037/onedata-tasks.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'npm install'
            }
        }
        stage('Run tests') {
            steps {
                sh 'npm test'
            }
        }
        stage('Docker Build and Run') {
            steps {
                sh 'docker build -t my-app .'
                sh 'docker run -d -p 3000:3000 my-app'
            }
        }
        
    }

    post {
    always {
        emailext(
            attachLog: true,
            subject: "Build ${currentBuild.result}: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
            body: """<p>Build finished!</p>
                     <p>Project: ${env.JOB_NAME}</p>
                     <p>Build Number: ${env.BUILD_NUMBER}</p>
                     <p>Status: ${currentBuild.result}</p>
                     <p>URL: <a href="${env.BUILD_URL}">${env.BUILD_URL}</a></p>""",
            to: 'arunagri03@gmail.com'
        )
    }

    success {
        echo "Build successful!"
    }

    failure {
        echo "Build failed."
    }
}
}
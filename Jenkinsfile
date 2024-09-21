pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                deleteDir() // Optional: Clear workspace
                // Replace the git url with your own repository url
                git branch: 'main', url: 'https://github.com/your-username/Black-Duck-Vulnerability-Scan-Demo.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                // Use 'bat' for Windows environment
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Application') {
            steps {
                echo 'Running application script...'
                bat 'python app.py'  // Runs the application script
            }
        }
    }
}

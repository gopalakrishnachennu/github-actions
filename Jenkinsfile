pipeline {
    agent any

    triggers {
        // Optional: run every 2 minutes (for testing)
        cron('H/2 * * * *')
    }

    stages {
        stage('Checkout Code') {
            steps {
                echo "📥 Cloning repository from SCM..."
                git branch: 'main', url: 'https://github.com/gopalakrishnachennu/python-app.git'
            }
        }

        stage('Setup Environment') {
            steps {
                echo "🐍 Setting up Python environment..."
                sh '''
                python3 --version
                pip install --upgrade pip
                pip install -r requirements.txt || echo "⚠️ No requirements.txt found."
                '''
            }
        }

        stage('Run Python Script') {
            steps {
                echo "🚀 Running Python script..."
                sh '''
                echo "Executing hello.py via Jenkins SCM pipeline..."
                python3 hello.py Gopala
                '''
            }
        }
    }

    post {
        always {
            echo "✅ Job completed at: ${new Date()}"
        }
    }
}

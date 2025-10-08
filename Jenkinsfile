pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                echo "📥 Cloning public repository..."
               sh '''
               echo "okayyy"
               '''
            }
        }

        stage('Setup Environment') {
            steps {
                echo "🐍 Checking Python version & installing deps..."
                sh '''
                python3 --version
                pip install --upgrade pip
                if [ -f requirements.txt ]; then
                    pip install -r requirements.txt
                else
                    echo "⚠️ No requirements.txt found, skipping dependency install."
                fi
                '''
            }
        }

        stage('Run Python Script') {
            steps {
                echo "🚀 Running your Python script..."
                sh '''
                echo "Executing hello.py..."
                python3 hello.py "Gopala Krishna"
                '''
            }
        }
    }

    post {
        success {
            echo "✅ Pipeline completed successfully at: ${new Date()}"
        }
        failure {
            echo "❌ Pipeline failed. Check the logs above."
        }
    }
}

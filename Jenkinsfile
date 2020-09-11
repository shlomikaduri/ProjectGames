pipeline {
    agent any

	script {
			// Show the select input modal
		   def INPUT_PARAMS = input message: 'Please Provide Parameters', ok: 'Next',
							parameters: [
							choice(name: 'IMAGE_TAG', choices: getDockerImages(), description: 'Available Docker Images')]
		}

    stages {
	    stage('Build our docker image') {
            steps { dir('C:\\ProjectGames\\') {
                bat 'docker-compose up --build -d' }
            }
        }
        stage('e2e.py module it will perform a selenium test') 
        {
            steps { dir('C:\\ProjectGames\\Tests') {
                bat 'python e2e.py' }
            }
            }
        stage('terminate our tested container') 
        {
            steps { dir('C:\\ProjectGames\\') {
                bat 'docker-compose down' }
            }
        }            
        }

}



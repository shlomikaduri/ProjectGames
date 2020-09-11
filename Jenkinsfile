pipeline {
    agent any

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
	stage('Wait for user to input text?') {
		steps {
			script {
				def userInput = input(id: 'userInput', message: 'Merge to?',
				parameters: [[$class: 'ChoiceParameterDefinition', defaultValue: 'strDef', 
                description:'describing choices', name:'nameChoice', choices: "QA\nUAT\nProduction\nDevelop\nMaster"]
				])

				println(userInput); //Use this value to branch to different logic if needed
        }
    }

}

}



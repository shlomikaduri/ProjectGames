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
		stage('print') {
		steps {
							 echo 'Hi, this is Zulaikha from edureka'
						 }		
        }
		stage('Two') {
                 steps {
                    input('Do you want to proceed?')
                 }
                 }
		stage('Three') {
                 when {
                       not {
                            branch "master"
                       }
                 }
				 steps {
                       echo "Hello"
						}
                 }
		stage('Test') {
			def reg = input(
				message: 'What is the reg value?', 
				parameters: [
					[$class: 'ChoiceParameterDefinition', 
						choices: 'Choice 1\nChoice 2\nChoice 3', 
						name: 'input', 
						description: 'A select box option']
				])

			echo "Reg is ${reg}"
    }
				
}

}



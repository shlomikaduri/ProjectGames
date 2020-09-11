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
				}
}

}



pipeline {
    agent any

    stages {
	    stage('Build our docker image') {
            steps { dir('C:\\ProjectGames\\') {
                bat 'docker-compose up --build' }
            }
        }
        stage('e2e.py module it will perform a selenium test') 
        {
            steps { dir('C:\\ProjectGames\\Tests') {
                bat 'python e2e.py' }
            }
            }
        stage('prints the free disk space') 
        {
            steps {
                bat 'fsutil volume diskfree c:'

            }
            }
        stage('terminate our tested container') 
        {
            steps {
                bat 'docker-compose down'
            }
            }            
        }
        }


@Library('calm-jenkins-pipeline-library@master') _
pipeline {
  agent {
    node { label 'tests_in_pc' }
  }
  stages {
    stage('Clone repo') {
      steps {
        script {
           sh 'git clone git@github.com:nutanix/calm-dsl.git'
        }
      }
    }
  }
}

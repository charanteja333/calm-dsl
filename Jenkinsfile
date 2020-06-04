@Library('calm-jenkins-pipeline-library@master') _
pipeline {
  agent {
    node { label 'dsl_cicd' }
  }
  stages {
    stage('Clone DSL repo') {
      steps {
        script {
           sh 'git clone git@github.com:nutanix/calm-dsl.git'
        }
      }
    }
  }
}

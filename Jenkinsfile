#!groovy
/* calm DSL CI/CD job for jenkins */

@Library('calm-jenkins-pipeline-library@master') _

def BP_PRESENT = 'FALSE'
pipeline {
  agent {
    node { label 'dsl_cicd' }
  }
  stages {
    stage('Setup Calm DSL') {
      steps {
        script {
           sh "git clone git@github.com:nutanix/calm-dsl.git"
           sh "cd calm-dsl && make clean"
           sh "cd calm-dsl && make _init_centos"
           sh "cd calm-dsl && sudo yum install -y python3-devel"
           sh "cd calm-dsl && make dev"
           sh "cd calm-dsl && make dist"
           sh "source calm-dsl/venv/bin/activate && calm -v init dsl -i 10.44.19.140 -P 9440 -u admin -p regression -pj regression"
           sh "source calm-dsl/venv/bin/activate && cd blueprints/lamp && calm create bp --file lamp-v4.py --name LAMP_FROM_DSL"
        }
      }
    }
    stage('Create blueprint') {
      steps {
        script {
           sh "source calm-dsl/venv/bin/activate && calm -v init dsl -i 10.44.19.140 -P 9440 -u admin -p regression -pj regression"
           bp_id = sh(returnStdout: true, script: 'bp=$(calm get bps --name=LAMP_FROM_DSL)').trim()
           /*sh "cd blueprints/lamp && calm create bp --file lamp-v4.py --name LAMP_FROM_DSL"*/
        }
      }
    }
    stage('Launch blueprint') {
      steps {
        script {
           sh "source calm-dsl/venv/bin/activate && cd blueprints/lamp && calm create bp --file lamp-v4.py --name LAMP_FROM_DSL"
        }
      }
    }
  }
}

#!groovy
/* calm DSL CI/CD job for jenkins */

@Library('calm-jenkins-pipeline-library@master')

pipeline {
  agent {
    node { label 'dsl_cicd' }
  }
  stages {
    stage('Setup Calm DSL') {
      steps {
        script {
           git_commit = sh(returnStdout: true, script: 'git rev-parse HEAD').trim()
           git_branch = sh(returnStdout: true, script: 'git rev-parse --abbrev-ref HEAD').trim()

           short_commit=git_commit.take(6)
           env.GIT_BRANCH = git_branch
           env.GIT_COMMIT = short_commit
           sh "git clone git@github.com:nutanix/calm-dsl.git"
           sh "cd calm-dsl && make clean"
           sh "cd calm-dsl && make _init_centos"
           sh "cd calm-dsl && sudo yum install -y python3-devel"
           sh "cd calm-dsl && make dev"
           sh "cd calm-dsl && make dist"
        }
      }
    }
    stage('Create blueprint') {
      steps {
        script {
           sh "source calm-dsl/venv/bin/activate && calm -v init dsl -i 10.44.19.140 -P 9440 -u admin -p regression -pj regression"
           sh "cd blueprints/lamp && calm create bp --file lamp-v4.py --name LAMP_FROM_DSL_${env.GIT_COMMIT}"*/
        }
      }
    }
    stage('Launch blueprint') {
      steps {
        script {
           sh "calm launch bp --file lamp-v4.py --name LAMP_FROM_DSL_${env.GIT_COMMIT}"
        }
      }
    }
  }
}

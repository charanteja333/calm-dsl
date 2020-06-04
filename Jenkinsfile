#!groovy
/* calm DSL CI/CD job for jenkins */
pipeline {
  agent {
    node { label 'dsl_cicd' }
  }
  parameters {
    string(name: 'PC_IP', defaultValue: '10.44.19.140', description: 'Prism Central IP address')
    string(name: 'PC_PORT', defaultValue: '9440', description: 'Prism Central port')
    string(name: 'PC_PROJECT', defaultValue: 'regression', description: 'Calm project')
  }
  stages {
    stage('Setup Calm DSL') {
      steps {
        script {
           sh 'git clean -fdx'
           git_commit = sh(returnStdout: true, script: 'git rev-parse HEAD').trim()
           git_branch = sh(returnStdout: true, script: 'git rev-parse --abbrev-ref HEAD').trim()

           short_commit=git_commit.take(6)
           env.GIT_BRANCH = git_branch
           env.GIT_COMMIT = short_commit
           dir('/root/') {
             sh "cd /root/calm-dsl && git pull"
             /*sh "rm -rf calm-dsl"
             sh "git clone git@github.com:nutanix/calm-dsl.git"
             sh "cd calm-dsl && make clean"
             sh "cd calm-dsl && make _init_centos"
             sh "cd calm-dsl && sudo yum install -y python3-devel"
             sh "cd calm-dsl && make dev"
             sh "cd calm-dsl && make dist"*/
           }
        }
      }
    }
    stage('Create blueprint') {
      steps {
        script {
           withCredentials([[$class: 'UsernamePasswordMultiBinding', credentialsId: 'MPI_REGRESSION_PC',usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD']])
           /*sh "source /root/calm-dsl/venv/bin/activate && calm -v init dsl -i ${params.PC_IP} -P ${params.PC_PORT} -u ${USERNAME} -p ${PASSWORD} -pj ${params.PC_PROJECT}"*/
           sh "cd blueprints/lamp && calm create bp --file lamp-v4.py --name LAMP_FROM_DSL_${env.GIT_COMMIT}"
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

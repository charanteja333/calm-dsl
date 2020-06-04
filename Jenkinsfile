#!groovy
/* calm DSL CI/CD job for jenkins */
pipeline {
  agent {
    node { label 'dsl_cicd' }
  }
  parameters {
    string(name: 'PC_IP', defaultValue: 'nucalm-demo2.calm.nutanix.com', description: 'Prism Central IP address')
    string(name: 'PC_PORT', defaultValue: '9440', description: 'Prism Central port')
    string(name: 'PC_PROJECT', defaultValue: 'default', description: 'Calm project')
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
             sh "cd calm-dsl && sudo yum install -y python3-devel"*/
             sh "cd calm-dsl && make dev"
             sh "cd calm-dsl && make dist"
           }
        }
      }
    }
    stage('Create blueprint') {
      steps {
        script {
           /*withCredentials([[$class: 'UsernamePasswordMultiBinding', credentialsId: 'MPI_REGRESSION_PC',usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD']])
           sh "source /root/calm-dsl/venv/bin/activate && calm -v init dsl -i ${params.PC_IP} -P ${params.PC_PORT} -u ${USERNAME} -p ${PASSWORD} -pj ${params.PC_PROJECT}"*/
           sh "source /root/calm-dsl/venv/bin/activate && cd blueprints/calm_era && calm create bp --file blueprint.py --name Calm_Era_${env.GIT_COMMIT}"
        }
      }
    }
    stage('Launch blueprint') {
      steps {
        script {
           sh "source /root/calm-dsl/venv/bin/activate && calm launch bp Calm_Era_${env.GIT_COMMIT} --app_name Calm_Era_${env.GIT_COMMIT} -i"
        }
      }
    }
  }
}

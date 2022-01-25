FROM jenkins/jenkins
ENV JAVA_OPTS -Djenkins.install.runSetupWizard=false
COPY plugins.txt /usr/share/jenkins/ref/plugins.txt
RUN /usr/local/bin/install-plugins.sh < /usr/share/jenkins/ref/plugins.txt

# docker run -d -p 8080:8080 -v jenkins-local:/var/jenkins_home jenkins:jcasc
# docker volume create jenkins-local#

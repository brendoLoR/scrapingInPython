FROM gitpod/workspace-full

# Install custom tools, runtimes, etc.
# For example "bastet", a command-line tetris clone:
# RUN brew install bastet
#
# More information: https://www.gitpod.io/docs/config-docker/
RUN sudo yum install mysql-server && pip3 install beautifulsoup4 && pip3 install requests && pip3 install lxml && pip3 install mysql-connector-python

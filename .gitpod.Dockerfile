FROM gitpod/workspace-full

# Install custom tools, runtimes, etc.
# For example "bastet", a command-line tetris clone:
# RUN brew install bastet
#
# More information: https://www.gitpod.io/docs/config-docker/
RUN pip3 install beautifulsoup4 \
 pip3 install requests \
 pip3 install lxml \
 pip3 install mysql-connector-python \
 sudo yum install mysql-server \
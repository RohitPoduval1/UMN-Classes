# Start image with a node base image of Ubuntu latest verison
FROM ubuntu:latest

# Install necessary package with ubuntu package manager, apt
# Caution: apt install -y parameter is necessary !!!
# To give apt install permission or docker build will fail
RUN apt update && apt install -y make gcc g++ valgrind python3 zip

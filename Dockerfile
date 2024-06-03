FROM python:3.10

# Set work directory
WORKDIR /opt/task_solution/equilibrium_index_finder

RUN apt-get update && apt-get upgrade -y

# Copy package
COPY ./ /opt/task_solution/equilibrium_index_finder

RUN python3.10 -m pip install -e .
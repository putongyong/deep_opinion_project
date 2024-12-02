# Variables
COMPOSE_FILE = docker-compose.yml
PROJECT_NAME = flask_app
SERVICE_APP = flask
SERVICE_DB = db

# Build the application
build:
	docker-compose -f $(COMPOSE_FILE) -p $(PROJECT_NAME) build

# Start the containers (app and database)
up:
	docker-compose -f $(COMPOSE_FILE) -p $(PROJECT_NAME) up -d

# Stop and remove the containers
down:
	docker-compose -f $(COMPOSE_FILE) -p $(PROJECT_NAME) down

# View logs for all services
logs:
	docker-compose -f $(COMPOSE_FILE) -p $(PROJECT_NAME) logs

# View logs for the app service
logs-app:
	docker-compose -f $(COMPOSE_FILE) -p $(PROJECT_NAME) logs $(SERVICE_APP)

# View logs for the database service
logs-db:
	docker-compose -f $(COMPOSE_FILE) -p $(PROJECT_NAME) logs $(SERVICE_DB)

# Rebuild and restart the containers
rebuild: down build up

# Check the status of the containers
ps:
	docker-compose -f $(COMPOSE_FILE) -p $(PROJECT_NAME) ps

# Execute a command inside the app container
exec-app:
	docker-compose -f $(COMPOSE_FILE) -p $(PROJECT_NAME) exec $(SERVICE_APP) /bin/sh

# Execute a command inside the database container
exec-db:
	docker-compose -f $(COMPOSE_FILE) -p $(PROJECT_NAME) exec $(SERVICE_DB) psql -U postgres

# Clean up all unused resources
clean:
	docker system prune -f

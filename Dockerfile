FROM python:3.11-alpine as build

# Install dependencies
RUN apk add --no-cache gcc musl-dev libffi-dev

COPY ./requirements.txt /requirements.txt

RUN python -m venv /pyvenv && \
    /pyvenv/bin/pip install --upgrade pip && \
    /pyvenv/bin/pip install -r /requirements.txt

FROM python:3.11-alpine

# Copy application code
COPY . /app
COPY --from=build /pyvenv /pyvenv

# Set environment variable to use the virtual environment
ENV VIRTUAL_ENV=/pyvenv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

WORKDIR /app

# Expose port 5000
EXPOSE 8000

# Command to run the application with Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "main:app"]

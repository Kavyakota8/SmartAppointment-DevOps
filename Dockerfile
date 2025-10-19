# Step 1: Use a lightweight Python base image
FROM python:3.11-slim

# Step 2: Set working directory inside the container
WORKDIR /app

# Step 3: Copy dependency list and install requirements
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Step 4: Copy the rest of the application code
COPY . .

# Step 5: Expose the Flask app port
EXPOSE 5000

# Step 6: Define default command to run the app
CMD ["python", "app.py"]
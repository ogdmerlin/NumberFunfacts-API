# 1. Choose a base image
FROM python:3.12-alpine

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy requirements and install
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy the rest of your application files
COPY . /app

# 5. Expose port 8000 (for Uvicorn)
EXPOSE 8000

# 6. Run the app with uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
# Serverless Web Application for Save and View Data

This project demonstrates the deployment of a serverless web application on AWS using services such as S3, Lambda, API Gateway, and DynamoDB.

### **Technologies:**
- AWS S3 (Static hosting)
- AWS Lambda (Serverless backend)
- AWS API Gateway (API management)
- AWS DynamoDB (NoSQL data storage)

### **Setup Instructions:**

1. **S3 Setup:**
   - Create a new S3 bucket and enable static website hosting.
   - Upload the front-end files (index.html, style.css, app.js).

2. **API Gateway Setup:**
   - Create API Gateway and define routes for the save and view functions.
   - Enable CORS if required.

3. **Lambda Functions:**
   - Deploy the `saveDataFunction` and `viewDataFunction` Lambda functions to AWS.

4. **DynamoDB Setup:**
   - Create a DynamoDB table to store data.
   - Set up appropriate IAM roles for Lambda to interact with DynamoDB.

5. **Connect Front-End:**
   - Modify the JavaScript to interact with the API Gateway endpoints.

6. **Deploy and Test:**
   - Deploy your application and test the save and view functionality.

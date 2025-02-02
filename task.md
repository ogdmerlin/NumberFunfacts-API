Resources
Fun fact API: http://numbersapi.com/#42
https://en.wikipedia.org/wiki/Parity_(mathematics)

Task Description: DevOps Stage 1 - Number Classification API
Create an API that takes a number and returns interesting mathematical properties about it, along with a fun fact.
Weight: 6 points
Requirements
Technology Stack:
Use any programming language or framework of your choice (See Sharp (C #), PHP :elephant:, Python :snake:, Go :runner::skin-tone-5:, Java :coffee:, JS/TS :nauseated_face:)
Must be deployed to a publicly accessible endpoint
Must handle CORS (Cross-Origin Resource Sharing)
Must return responses in JSON format
Version Control:
Code must be hosted on GitHub
Repository must be public
Must include a well-structured README.md
API Specification
Endpoint: **GET** <your-url>/api/classify-number?number=371
Required JSON Response Format (200 OK):
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,  // sum of its digits
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
Required JSON Response Format (400 Bad Request)
{
    "number": "alphabet",
    "error": true
}
Acceptance Criteria
Functionality
Accepts GET requests with a number parameter.
Returns JSON in the specified format.
Accepts all valid integers as the only possible inputs
Provides appropriate HTTP status codes.
Code Quality
Organized code structure.
Basic error handling and input validation.
Avoids hardcoded values.
Documentation
Complete README.
Deployment
Publicly accessible and stable API.
Fast response time (< 500ms).
Submission Mode:
Submit your task by going to the #stage-one-devops channel and using the slash command /submit to make your submission. Ensure you've:
Hosted the API on a platform of your choice.
Double-checked all requirements and acceptance criteria.
Tested your API thoroughly before submission.
Thoroughly review your work to ensure accuracy, functionality, and adherence to the specified guidelines before you submit it.
Submission Deadline:
The deadline for submissions is Friday, Feb 7th -11:59pm GMT +1 (Nigerian Time). Late submissions will not be entertained.
Additional Note
Use the math type from the Numbers API to get the fun fact.
The possible combinations for the properties field:
["armstrong", "odd"] - if the number is both an Armstrong number and odd
["armstrong", “even”] - if the number is an Armstrong number and even
["odd"] - if the number is not an Armstrong number but is odd
[”even”] - if the number is not an Armstrong number but is even.
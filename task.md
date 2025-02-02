Resources
Fun fact API: http://numbersapi.com/#42
https://en.wikipedia.org/wiki/Parity_(mathematics)

Task Description: DevOps Stage 1 - Number Classification API<br>
Create an API that takes a number and returns interesting mathematical properties about it, along with a fun fact.<br>
Weight: 6 points<br>
Requirements<br>
Technology Stack:<br>
Use any programming language or framework of your choice (See Sharp (C #), PHP :elephant:, Python :snake:, Go :runner::skin-tone-5:, Java :coffee:, JS/TS :nauseated_face:)<br>
Must be deployed to a publicly accessible endpoint<br>
Must handle CORS (Cross-Origin Resource Sharing)<br>
Must return responses in JSON format<br>
Version Control:<br>
Code must be hosted on GitHub<br>
Repository must be public<br>
Must include a well-structured README.md<br>
API Specification<br>
Endpoint: **GET** <your-url>/api/classify-number?number=371
Required JSON Response Format (200 OK):<br>
```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,  // sum of its digits
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```
Required JSON Response Format (400 Bad Request)
```json
{
    "number": "alphabet",
    "error": true
}
```
Acceptance Criteria<br>
Functionality<br>
Accepts GET requests with a number parameter.
Returns JSON in the specified format.<br>
Accepts all valid integers as the only possible inputs<br>
Provides appropriate HTTP status codes.<br>
Code Quality<br>
Organized code structure.<br>
Basic error handling and input validation.<br>
Avoids hardcoded values.<br>

Documentation<br>
Complete README.<br>
Deployment
Publicly accessible and stable API.<br>
Fast response time (< 500ms).<br>
Submission Mode:<br>
Submit your task by going to the #stage-one-devops channel and using the slash command /submit to make your submission. Ensure you've:<br>
Hosted the API on a platform of your choice.<br>
Double-checked all requirements and acceptance criteria.<br>
Tested your API thoroughly before submission.<br>
Thoroughly review your work to ensure accuracy, functionality, and adherence to the specified guidelines before you submit it.<br>
Good luck!<br>
[]: #
Additional Note<br>
Use the math type from the Numbers API to get the fun fact.<br>
The possible combinations for the properties field:<br>
["armstrong", "odd"] - if the number is both an Armstrong number and odd<br>
["armstrong", “even”] - if the number is an Armstrong number and even<br>
["odd"] - if the number is not an Armstrong number but is odd<br>
[”even”] - if the number is not an Armstrong number but is even.<br>
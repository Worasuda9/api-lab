# API lab results
## Part 0
- Step 0.1, the number of pizza names: 18
- Step 0.3, status code of the request without a token: 401
- Step 0.4, the name of your pizza: The Dirty Romana
- Step 0.12, results of the three runs without a session (optional): 
1st run: FAILED test_no_session.py::test_log_in_without_a_session - assert 401 == 200 
2nd run: 1 passed in 1.85s 
3rd run: 1 passed in 1.90s
- Step 0.16, blocks of "how many of the three tools are excluded": 0, 1, 2, 3
## Defect report
- Title: Excluding every pizza tool returns a server error
- Request: POST /api/pizza with `{"excludedTools": ["Knife", "Pizza cutter", "Scissors"]}`
- Expected result: HTTP 400 with a JSON error message.
- Actual result: HTTP 500 instead of HTTP 400.
- Severity: Medium: API returns a server error for a request that should be rejected as a client error.
## Part A
- Step A4, status codes when the other user reads, changes and deletes: read 404, change 400, delete 400.
## Part B
1. Testing with a real server can reveal network, TLS, deployment, and API integration problems that stubbed unit tests cannot. However, stubbed tests are still useful because they are faster and test application logic independently.

2. Each test uses a unique username to avoid conflicts with other tests. In Project 2, I will use a separate test account, create unique test data for each run, and clean it up afterward instead of changing shared data.

3. Using one session keeps cookies and other client information between requests. In Step 0.12, the first run failed because login returned 401 instead of 200, while the second and third runs passed.

4. The test with all three tools excluded helped identify the defect. A 500 response with an empty body does not explain the problem to the client, while a 400 response with a message is clearer. I kept the test as `xfail` to track the known issue and detect if it unexpectedly passes in the future.

5. Base choice coverage requires 9 tests (1 base case + 2 + 3 + 1 + 2 non-base blocks). All-combinations coverage requires 72 tests (3 × 4 × 2 × 3 combinations).

6. The observed status codes were 404 for read and 400 for change and delete. I expected all three requests to be rejected. A 404 can hide whether another user's rating exists, while 403 is also a common response for unauthorized actions. Since all requests were rejected and the rating remained unchanged, this is not an access-control defect. However, 400 is less specific than 403.

7. The request returned a JSON `ratings` list with rating IDs, star values, and pizza IDs instead of an authentication error. If ratings are supposed to be private, this is an access-control defect because unauthorized users can access them. However, if ratings are public by design, it may not be a defect. It depends on the API's access policy.

8. API tests check response status, headers, and JSON data directly. Web UI tests check browser behavior, such as page layout, navigation, and whether users can complete actions through the interface.
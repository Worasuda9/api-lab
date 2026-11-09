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
- Step A4, status codes when the other user reads, changes and deletes:
## Part B
1.
2.
3.
4.
5.
6.
7.
8.
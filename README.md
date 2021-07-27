Started at 12:09pm CEST, will try to make commits often

# Challenge:
> Please don't go over 2 hours for this one. The goal isn't to finish. I want to see your process so > use comments and pseudocode as necessary. Please complete it in your language of your choice > (JavaScript/TypeScript or Python are preferred). Your choice.
> 
> Problem: Create a CLI that takes a list of numbers and returns them sorted. Use a bubble sort > implementation found from a random answer from Stack Exchange via https://api.stackexchange.com/.
> In other words, after you take in the numbers, call the Stack Exchange API, grab a random answer to > a random bubble sort implementation question, and run the code blindly passing in the user input. > Display the answer to the end user.
> 
> Sample output:
> 
> ```py
> >> Hello! Please provide a list of integers.
> >> 4, 51, 62, 45, 31, 90, 42, 28, 96, 65, 33, 73
> >> Thanks. Fetching a random bubble sort implementation. Fingers crossed.
> >> 4, 28, 31, 33, 42, 45, 51, 62, 65, 73, 90, 96
> ```
> 
> Toss your code on GitHub. Send a link once complete. Feel free to email me with questions. Thanks!

# Concerns
## Accuracy
Need good search criteria to get relevant answers. Might have to try a few searches before we succeed.

## Parsing
### Parsing the html to get code blocks
Probably searching for `<code>` blocks would be enough
### Parsing the code to figure out variable assignments

## Security
We'll be running random code from the internet, need to make sure it's run in a safe environment. 

# Method
## Client
Create a lightweight API client for search and retrieval

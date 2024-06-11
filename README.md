# python-number-guesser

## Program Description
- Generate a random number
- Track how many guesses for user to correctly guess the number

## Learnings
- `random` module is installed with python by default
- `random.randrange(start,stop)`
    - Stop number is not actually the maximum that could be randomly generated
        - Example: If we want 10 as our maximum number, we need to set 11 as the Stop number
- When user enters a value from our `input` request, the value will always be a string " "
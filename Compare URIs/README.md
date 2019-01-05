# Compare URIs


Company| J.P. Morgan Chase
---|---
Date|12/7/2018
Platform|HireVue

Determine if two URIs match. For the purpose of this challenge, you shoud use a case-sensitive octet-by-octet comparison of the entire URIs, with these excemptions:

1. A port that is empty or not given is equivalent to the default port of 80
2. Comparisons of host names MUST be case-insensitive
3. Comparisons of scheme names MUST be case-insensitive
4. Characters are quivalent to their % HEX HEX encodings. (Other than typical reserved characters in urls like , / ? : @ = + $ #)

### Input
Your program should read lines from standard input. Each line contains two urls delimted by a semicolon.
### Output
Print out True/False if the URIs match.

### Test 1
#### Test Input
`http://abc.com:80/~smith/home.html;http://ABC.com/%7Esmith/home.html`
#### Expected Output
`True`
### Test 2
#### Test Input
``HTTPS://abc.com:8080/path/index*!^(~|>`^|<{`{>.html;HTTP://EXAMPLE.com:8081//index{~.html``
#### Expected Output
`False`

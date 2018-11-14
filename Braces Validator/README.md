# Validate braces


Company| Longgame
---|---
Date|10/15/2018
Platform|Onsite Interview

A string is given with three types of braces:
* curly braces {}
* brackets [] and
* standard braces ()

Write a function to validate strings if there is a closing bracket to each opening bracket for the same type of bracket.

Examples:
'(){}[]' => true
'({[]})' => true
'([]){}' => true

'([]){)' => false
')' => false
'{()}](' => false
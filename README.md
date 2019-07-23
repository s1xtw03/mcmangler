# the mcmangler

This service generates a list of leetspeak candidates combined with common complex human appendages.

So for client Acme, it returns:

acme, Acme, ACME, @cme, @cme2017...

Until all possible combinations have been exhausted.

rules-whole and rules-root are processed with hashcat-utils/combipow to generate all the combinations.

This is nice to load potential candidates for bruteforcing external services, ssh/ftp on internals, pretty much anything that doesn't have a failure-lockout. 

```
jmcg@biscuit:~/mcmangler$ ./mcmangler.sh Acme                                                                                                  
acm31                     
acm3!1                           
acm31!                            
Acm31                           
Acm3!1                           
Acm31!                           
ACM31                            
ACM3!1                           
ACM31!
{...}
```

Requires [hashcat](https://github.com/hashcat/hashcat) and [hashcat-utils](https://github.com/hashcat/hashcat-utils). 
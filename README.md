# the mcmangler

This service generates a list of leetspeak password candidates combined with common complex human appendages.

It prints all possible combinations substituting: a with @, i with 1, o with 0, s with $, and e with 3.  

This is nice to load potential candidates for bruteforcing network services during security assessment work - but beware the failure-lockout!. 

You can provide a word with -w, or a newline separated file with -f.

Warning: if you use phrases of words, output could get huge really quick. 

```
jmcg@seles:~/util/s1xtw03/mcmangler$ python mcmangler.py -w Microsoft | sort -R | head  
M1CR0S0FT2018!
m1cr0s0ft123!
M1CROSOFT!123
Micros0ft!123
Micr0$0ft!123
M1cr0soft123
MICRO$0FT!123
micr0soft!123
m1cro$oft!1
micr0soft2019!
jmcg@seles:~/util/s1xtw03/mcmangler$ python mcmangler.py -w Microsoft | wc -l          
     624
```

The old version used old-w-hashcat/rules-whole and old-w-hashcat/rules-root, processed with [hashcat-utils](https://github.com/hashcat/hashcat-utils)/combipow to generate all the combinations, and then run through the [hashcat](https://github.com/hashcat/hashcat) rules engine. To address some of the shortcomings with that, the relevant functionality is reimplemented in python now!!

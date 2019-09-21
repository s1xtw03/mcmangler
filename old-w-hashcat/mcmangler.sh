#!/bin/bash
HASHCATPATH="/opt/hashcat-3.5.0/hashcat64.bin"
COMBIPOWPATH="/opt/hashcat-utils/combipow.bin"
echo $1 > input.tmp

$COMBIPOWPATH $PWD/rules-root > $PWD/comborules.tmp

$HASHCATPATH -r $PWD/comborules.tmp --stdout input.tmp > root.tmp
$HASHCATPATH -r $PWD/rules-suffix --stdout root.tmp | sort -u

rm $PWD/*.tmp
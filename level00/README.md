Type the following:

```bash
flag00@SnowCrash:~$ find / -user flag00 -exec readlink -f {} \; 2>/dev/null
```

It will highlights us 2 files:

- /usr/sbin/john
- /rofs/usr/sbin/john

Both file contains the following:

```txt
cdiiddwpgswtgt
```

This is a Caesar cipher, meaning that we simply have to do an alphabetic rotation of each letter to find the hidden message.

To decode it, we'll use the python script `caesar-decoder` in resources folder.

```bash
$ py level00/resources/caesar-decoder.py cdiiddwpgswtgt

dejjeexqhtxuhu
efkkffyriuyviv
fgllggzsjvzwjw
ghmmhhatkwaxkx
hinniibulxbyly
ijoojjcvmyczmz
jkppkkdwnzdana
klqqllexoaebob
lmrrmmfypbfcpc
mnssnngzqcgdqd
nottoohardhere # This is what we are looking for
opuuppibseifsf
pqvvqqjctfjgtg
qrwwrrkdugkhuh
rsxxsslevhlivi
styyttmfwimjwj
tuzzuungxjnkxk
uvaavvohykolyl
vwbbwwpizlpmzm
wxccxxqjamqnan
xyddyyrkbnrobo
yzeezzslcospcp
zaffaatmdptqdq
abggbbunequrer
bchhccvofrvsfs
```

After having run the script, we can notice a single comprehensible word: `nottoohardhere`

We'll try to get the `flag00` with this code.

```bash
flag00@SnowCrash:~$ su flag00
Password: #Type 'nottoohardhere'
```

This will output the following success message:

```
Don't forget to launch getflag !
```

Running the `getflag` command in the shell will give us the token:

```bash
flag00@SnowCrash:~$ getflag
Check flag.Here is your token : x24ti5gi3x0ol2eh4esiuxias
```

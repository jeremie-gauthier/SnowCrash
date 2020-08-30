In this level, we only have:

- level09 (binary)
- token (.txt)

```bash
level09@SnowCrash:~$ cat token
f4kmm6p|=�p�n��DB�Du{��
```

Executing `level09` returns the following:

```bash
level09@SnowCrash:~$ ./level09
You need to provied only one arg.
```

So let's try with one arg:

```bash
level09@SnowCrash:~$ ./level09 token
tpmhr
```

Then we now know that `level09` don't read file.

We also can notice how close the input and output are.

```
level09@SnowCrash:~$ ./level09 test
tfuw
level09@SnowCrash:~$ ./level09 abcdef
acegik
```

The `level09` bin seems to increment the ascii value of each letter by its position in the string.

This could be the reason why certain characters are non-printable.

```bash
level09@SnowCrash:~$ hexdump -C token
00000000  66 34 6b 6d 6d 36 70 7c  3d 82 7f 70 82 6e 83 82  |f4kmm6p|=..p.n..|
00000010  44 42 83 44 75 7b 7f 8c  89 0a                    |DB.Du{....|
0000001a
```

Let's write a quick script to reverse this behaviour.

We'll feed our script with the hexadecimal representation of the string and it will output a string from it.

```bash
f3iji1ju5yuevaus41q1afiuq
```

```bash
level09@SnowCrash:~$ su flag09
Password: # Type 'f3iji1ju5yuevaus41q1afiuq'
Don t forget to launch getflag !
flag09@SnowCrash:~$ getflag
Check flag.Here is your token : s5cAJpM8ev6XHw998pRWG728z
```

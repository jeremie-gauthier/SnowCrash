This one is focus on searching informations through a series of communication between two machines.

We got a .pcap file, which must be used with WireShark.

Examining this file, we can notice the following:

```txt
Password: ft_wandr   NDRel L0L
```

But something is weird with this password.

Let's suppose that the whitespace characters are in fact non-printable characters. Like a backspace.

The password would then be:

```txt
ft_waNDReL0L
```

Let's give it a try:

```bash
level01@SnowCrash:~$ su flag01
Password: # Type 'ft_waNDReL0L'
```

This will output the following success message:

```
Don't forget to launch getflag !
```

Running the `getflag` command in the shell will give us the token:

```bash
flag02@SnowCrash:~$ getflag
Check flag.Here is your token : kooda2puivaav1idi4f57q8iq
```

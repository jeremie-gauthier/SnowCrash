I have the following:

- level10 (binary)
- token

Rights associated:

```bash
level10@SnowCrash:~$ ls -l
total 16
-rwsr-sr-x+ 1 flag10 level10 10817 Mar  5  2016 level10
-rw-------  1 flag10 flag10     26 Mar  5  2016 token
```

All are owned by flag10. Token is not readable directly.

```
level10@SnowCrash:~$ ./level10
./level10 file host
	sends file to host if you have access to it
```

Here are the syscall for this program:

```
level10@SnowCrash:~$ nm -u level10
         w _Jv_RegisterClasses
         U __errno_location@@GLIBC_2.0
         w __gmon_start__
         U __libc_start_main@@GLIBC_2.0
         U __stack_chk_fail@@GLIBC_2.4
         U access@@GLIBC_2.0
         U connect@@GLIBC_2.0
         U exit@@GLIBC_2.0
         U fflush@@GLIBC_2.0
         U htons@@GLIBC_2.0
         U inet_addr@@GLIBC_2.0
         U open@@GLIBC_2.0
         U printf@@GLIBC_2.0
         U puts@@GLIBC_2.0
         U read@@GLIBC_2.0
         U socket@@GLIBC_2.0
         U strerror@@GLIBC_2.0
         U write@@GLIBC_2.0
```

It seems to use sockets

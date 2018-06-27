# EcoBot
Ecosia is a search engine which uses profit to plant trees (go check it out at [https://www.ecosia.org/](https://www.ecosia.org/]) !).
This is all cool and stuff, but we humans are lazy. So why don't we let computers lend a hand (or keyboard)? That's where this bot comes in. From now on you can help making the world a better place by doing absolutely nothing!

## Help
```
> python ecobot.py --help
usage: ecobot.py [-h] -l [L] [-v] [--loop] [--save [SAVE]] [--load [LOAD]]
                 [--destroy [DESTROY]] [--nosave]

An 'ecological' bot for ecosia search engine [https://www.ecosia.org/]

optional arguments:
  -h, --help           show this help message and exit
  -l [L]               wordlist.txt or any other file
  -v                   toggle verbose output
  --loop               toggle repeat the same wordlist
  --save [SAVE]        save session under custom name
  --load [LOAD]        load custom session
  --destroy [DESTROY]  destroy a saved session (* = all)
  --nosave             toggle do not store session
```

## Examples
`python ecobot.py -l wordlist.txt`<br>
Iterates one time over your word list and uses each word as a search term.<br>
`python ecobot.py -l wordlist.txt --loop`<br>
Same as above, but keeps repeating the same list over and over again until you are brave enough to hit CTRL + C.<br>
`python ecobot.py -l wordlist.txt --destroy session --save unicorn`<br>
By default, your current session is saved with the name 'session'. This command will delete your previous session, start again from scratch and save it with a new name 'unicorn'.<br>

## Note
This program is not affiliated with Ecosia. Do not use this program as a tool for 'DoS' attacks or any other malicious stuff. The server will probably disconnect you if it receives too many requests anyways.
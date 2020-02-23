# SUID-Crawler

This is a crawler written in python to find files with SUID-Bits. You can use multiple parameters to customize the search. Pipe it into a file or search just in sub-directorys. 

## Commands

```
"-user" will be the user to search for. E.g. 'root'. Default is root.

"-output" will be a path to a file to write to. E.g. ~/Documents/test.txt

"-verbose" will verbose detailed output about the found file.

"path" will be the root-node from where to start to searching. Default '/' (Root-Dir)
```

## Feedback/Improvement

If you found a flaw or a mistake make a pull-request an i will merge it. 
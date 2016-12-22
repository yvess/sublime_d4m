# sublime-d4m
automatic file touch on OS X for docker for mac with d4m-nfs

This is made for [d4m-nfs](https://github.com/IFSight/d4m-nfs).

## Requirements

In your docker xhyve vm the `mnt` folder must be symlinked to `/Users/<myusername>`.

## What It Does

The plugin executes a screen command to touch the file in the vm, to trigger
filesytem notifications.

This is especially useful for auto reloading in development setups, which
listen on ionotify, for example javascript compilers.

## Settings

```json
{
    "file_extensions": ["py", "md"],
    "watch_paths": ["/Users/myuser/myprojects", "/Users/myuser/otherprojects"]
}
```

- file_extenions:  default: [] (all), ["py", "md"], only trigger for this file extensions
- watch_paths: default: $HOME, ["/Users/myuser/myprojects", "/Users/myuser/otherprojects"],
  only trigger if file is in one of this paths, the path must be inside `/Users/myuser`

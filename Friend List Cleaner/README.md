# Friend List Cleaner

This script will remove any people from the Friend List which have not been whitelisted.

# How to add to whitelist

To add a player to the whitelist, go to Line 6 and edit the list; an example of added player(s) would be:

```python
whitelist = [1, 2, 3, 4]
```

All player(s) that have been added to the whitelist will remain on the friend(s) list and will not be removed.

# How to setup with cookie

To setup the script, you must input your cookie so that API request(s) can be authorized which means we can send requests to ROBLOX.

```python
details = {
    'Cookie' : "",
}
```

You can enter your cookie within the 'Cookie' section between the two " "; this is a .ROBLOSECURITY cookie and can be easily grabbed using an extension.

# Requirements to use script

You must have any version of Python installed which supports the libraries below:

```
requests
```

If you do not, the script will not function properly; if you do not know how to run a python script, you probably should not be here.

# Example

https://github.com/whydylan/ROBLOX-Python/assets/111309669/80a90d21-5b64-4ff6-8738-b8dc38596de3


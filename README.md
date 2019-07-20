# Pretty JSON
Tool for printing pretty JSON (just for the missing options in `json.tool`)

For the issues in [Python bug tracker](https://bugs.python.org):
    * [Specifying indent in the json.tool command](https://bugs.python.org/issue29636)
    * [Add an option to json.tool to bypass non-ASCII characters](https://bugs.python.org/issue27413)

## Installing

Install and update using `pip`:

```shell
    pip install -U prettyjson
```


## Usage Examples

#### Example 1
```shell
echo '{"name": "vimfun", "from": "The Earth"}' | python -m prettyjson
```
Result:
```json
{
    "name": "vimfun",
    "from": "The Earth",
    
}
```

#### Example 2
```shell
echo '{"name": "vimfun", "from": "The Earth"}' | python -m prettyjson --indent=2
```
Result:
```json
{
  "name": "vimfun",
  "from": "The Earth"
}
```

#### Example 3
```shell
echo '{"name": "王旭林", "from": "The Earth"}' | python -m prettyjson --indent=2 --no-ensure-ascii
```
Result:
```json
{
  "name": "王旭林",
  "from": "The Earth"
}
```

## Links

* Website: https://github.com/vimfun/prettyjson
* Releases: https://pypi.org/project/prettyjson/
* Code: https://github.com/vimfun/prettyjson
* Issue tracker: https://github.com/vimfun/prettyjson/issues
* Test status:

  * Linux, Mac: https://travis-ci.org/vimfun/prettyjson
  * Windows: https://ci.appveyor.com/project/vimfun/prettyjson

* Test coverage: https://codecov.io/gh/vimfun/prettyjson

# domainr.py v0.2

Just a simple wrapper for the domai.nr API.

## Examples

Contains toy scripts for looking for weird domains.

With Unix you can do fun things: 

`echo "tilde" | ./domain_check.py`

or

`cat /usr/share/dict/words | grep -v \' | sort -R | head | sed -e 's/.*/\0.club/' | ./domain_check.py`

;)

See: https://domainr.com/api/docs/json for reference.
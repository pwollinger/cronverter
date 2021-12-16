
# Cronverter
A translator of CRON time to english.

It works beeing a terminal app or beein a package.
 
## Using the functions
**cronverter()** => the main function, it expect to receive an string with the CRON expression. It's the responsable for the translation.
```python:
cronverter("15 8 * * *")
#At 8:15 everyday
```
**TODO:** make the other functions more user friendly.

## As a terminal app
You only need to run `` python cronverter.py `` then pass the CRON expression as a string. The program will return the english sentence in a string printed on the terminal.
```bash:
python cronverter.py "15 8 * * *"
#At 8:15 everyday
```

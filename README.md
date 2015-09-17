# Band Name Generator

Put words you like in a comma-separated text file named 'words_file.txt' like this.

```
rolling
stone, stones
flaming
lip, lips
```

Run like this.

```
./band_name_generator.py words_file.txt
```

Words on the same line shouldn't be combo'd. The output of above example is this.

```
rolling stone
rolling stones
rolling flaming
rolling lip
rolling lips
stone stone
stone stones
stone flaming
stone lip
stone lips
stones rolling
stones flaming
stones lip
stones lips
flaming stone
flaming stones
flaming flaming
flaming lip
flaming lips
lip stone
lip stones
lip flaming
lip lip
lip lips
lips rolling
lips flaming
lips lip
lips lips
```

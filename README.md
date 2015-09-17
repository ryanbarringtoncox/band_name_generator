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
That's 26 band names from 6 words.

rolling stone
rolling stones
rolling flaming
rolling lip
rolling lips
stone rolling
stone flaming
stone lip
stone lips
stones rolling
stones flaming
stones lip
stones lips
flaming rolling
flaming stone
flaming stones
flaming lip
flaming lips
lip rolling
lip stone
lip stones
lip flaming
lips rolling
lips stone
lips stones
lips flaming
```

# About
Pentopix LLM Spacy application. Built on python and OpenAI's GPT-4 LLM API with custom scene evaluation to detect SUBJECT, VERBS and OBJECT from the scene.

# Structure
```
.
├── Code
│   ├── config.cfg
│   ├── convert_to_csv.py
│   ├── parts_of_sentence.json
│   └── pentopix.py
└── Data
    ├── barbie.pdf
    └── scene_1.csv

```


# Output screenshots

![Output screenshot](https://i.ibb.co/61KM318/Screen-Shot-2023-12-22-at-3-54-39-AM.png) <br><br><br><br>
![Output screenshot](https://i.ibb.co/xhX9rdf/Screen-Shot-2023-12-22-at-3-51-24-AM.png)



# Additional files
Within the repository, there are few files that are non-relevant to the challenge, 
but are other experimental ways of implementing the scene eval using multiple Data files using:

- pandas


# Running the application
To run the application locally, navigate to the `Code` directory:

Make sure to insert the `OPEN_AI_API` and `ORGANIZATION_ID` keys

`$ python3 pentopix.py`


# Tech Stack
- spacy-llm
- LLM: OpenAI's GPT-4 LLM




# Scene Data

## Scene 1
```
EXT. A DESERT-LIKE LANDSCAPE. DAY
Like Kubrick’s 2001, but with little girls, not apes. And with baby dolls, not sticks and stuff.
HELEN MIRREN (V.O.)
Since the beginning of time, since the first little girl ever existed, there have been dolls.
These little girls rock their baby dolls, they burp them, they cuddle them: They pretend to be Moms.
HELEN MIRREN (V.O.)
But the dolls were always and forever baby dolls. The girls who played with them could only ever play at being MOTHERS. Which can be fun, at least for a while anyway...
Ask your mother.
(pause)
This continued, until...
One of the girls looks UP.
Something has appeared in their midst. Something NEW.
It’s a GIANT BARBIE DOLL - BARBIE MARGOT, the 1950s Barbie, with her black and white swimsuit and lipstick.
The girls react with awe.
They’re stirred up and excited by this Barbie Margot not unlike the apes in that Kubrick masterpiece. They try to touch her, and one little girl starts smashing her baby doll against the ground until it breaks into pieces. She lets out a child’s howl!
One by one the little girls follow suit: whooping, screaming, throwing their baby dolls away in fits of joyful anger.
A final little girl throws her baby doll up in the air, and it is spinning, spinning - with a match cut to:
```

## Scene 2
```
INT. WHITE SPACE
Barbie stands in a empty space of the soon-to-be formed Barbie Land - it’s a void, a limbo - but clearly in a film studio. The World of Barbie is a Technicolor Soundstage.
HELEN MIRREN (V.O.)
Yes Barbie changed everything! Then she changed it all again!
We go through all the changes to Barbie Margot, as she moves through the decades.
HELEN MIRREN (V.O.)
```
All of these women are Barbie, and Barbie is all of these women. She might have started out as just a lady in a bathing suit, but she became so much more.
We see a row of Barbies. As we move back we see that “Barbie” is a EVERY different kind of woman -- every profession, every ethnicity, every body shape, every different ability and every gift. As we pan by each one, we hear:
HELEN MIRREN (V.O.)
She has her own money, her own house, her own car, her own career. Because Barbie can be anything, women can be anything.

# Spacy based LLM parsing pipeline
import os
import pandas as pd
from spacy_llm.util import assemble


os.environ["OPENAI_API_KEY"] = "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"
os.environ["ORGANIZATION_ID"] = "org-PDgZdabgwEQG4CKvJHhH4ALa"

nlp = assemble("config.cfg")

# df = pd.read_csv('../Data/scene_1.csv')
# scene = df.to_csv(index=False)

scene = """EXT. A DESERT-LIKE LANDSCAPE. DAY
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
"""

lines = scene.splitlines()
entities = []

for line in lines:
    doc = nlp(line)

    print("Scene: ", doc.text)
    print("Entities: ", [(ent.text, ent.label_) for ent in doc.ents])
    entities.append(doc.ents)

print(entities)








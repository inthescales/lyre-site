---
layout: post
title: "Future Work"
excerpt: "On possible future additions to Lyre's Dictionary."
tags: how
---

Although Lyre's Dictionary has existed for several years, and at the time of writing I am not actively working on it, I still consider it an ongoing project. Over these years I've had many ideas for future work, and while I may never realize all of them, I share them here to give some idea of how I see a more ideal version of this work.

## Expanding the range of word origins

### More roots

Currently, Lyre's Dictionary only uses roots from Latin and Greek to make words, and the easiest way to add more content to the corpus will be to add more roots from these languages. My process has mostly been to research the origins of English words one at a time and add their components to the corpus as [morphs](). But I surely haven't exhausted the supply of roots found the English language. I could spend some dedicated time reading through dictionaries, including ones focused on archaic and obscure words, to find more material.

So far I've mostly limited the corpus to roots that actually appear in at least one English word, but I can start further building it out by adding roots directly from the Latin and Greek lexicons. This will require new sources for research, since I could no longer rely even on English dictionaries, and would have to look into Latin and Greek word lists (which would require some actual Greek study, which I've mostly avoided so far). These "speculative" roots, as I call them, would probably be coded to appear less frequently than those attested in English words, but I think they will still be a valuable addition.

### Sound changes

Of course English isn't made up only of parts from these two languages. However, adding more origin languages will require deep new technical work to handle the sound changes involved in the transition from languages like Old English into Modern English. While it's simple enough to take a Latin word like 'narrare' and make it into the English 'narrate', it's a bit less straightforward (for me, anyway) to go from the Old English 'belyfan' to 'believe'. Vowels have to shift, and consonants may change when roots or affixes are added (like the change in f → v from 'belief' to 'believe'). At least if I want to include Old English roots in the corpus in their original form (and I suspect I will have to in order to reliably handle the way they can change with affixes or compounds) it will be necessary to have a way to compute these sound changes. But once this is done, it will unlock huge tracts of English that I haven't been able to touch at all yet.

This doesn't just apply to converting Old English to Modern English. Once such a system exists, it could be applied to other origin languages as well — we could create a corpus of Old French roots, convert them to Middle English, then convert that to Modern English. We could even take the Latin corpus we have, and convert through French and then into English. This would allow us to generate [doublet](https://en.wikipedia.org/wiki/Doublet_(linguistics)) words like 'camera' (Latin) and 'chamber' (French), and French-inflect forms of Latin words that never made it into French. Or we could pull in Old Norse, which also contributed significantly to early English.

After tracing the main lines of English's development, we could go on to pull in roots from languages that contributed to those nearer tributaries — Greek through Latin (with its attendant mutations), Frankish through French, Arabic through French or Latin or both, origins as far distant as we want to imagine, ancient or modern.

### Modern English formations

While I've spent a lot of time thinking about how to simulate the historical processes that led to English, I don't want to overlook the fact that English in its present day form also has its own processes of word-formation. While some of them are very obvious to us (e.g. adding '-er' to a verb to mean "someone who does that verb"), others are intriguingly subtle. For instance, consider the suffix '-y'. When applied to a fluid, like 'milky' or 'watery', it can mean "containing or resembling", but it can also, as in 'muddy' or 'bloody' mean "covered in". And this latter meaning can apply to other kinds of coverings as well, like growing things as in 'mossy' or 'grassy'. How many meanings might we tease out of this simple suffix?

While these modern elements have historical origins, '-y' itself dates back quite far in Old English, allowing them to play in a modern context opens new possibilities for combination, as they can combine with elements that didn't exist at their time of origin. And of course, modern-style word-formation lets us use modern elements, including new concepts like 'blog' or 'latex' but also more recently coined affixes like '-style' and '-aholic'.

### More processes

Beyond adding more roots, there are also new ways to use morphs that can be added.

One is simply the possibility of single-element words, which Lyre's Dictionary currently doesn't produce. While producing single-morph words from common roots like 'cat' may not be very interesting, they could be a valuable addition when made from roots from ancestor languages. These could be taken more or less straight, as in words like "corpus" and "demon", but will be especially interesting if we add the possibility of computing historical sound changes, to transform roots into unfamiliar forms, or generate modern forms of ancient roots that have since been lost (for example, [ADD ANGLISH EXAMPLE HERE]).

Compounding roots would also add a lot of new possibilities, though it would require some new concepts for how to make roots relate to each other beyond my current method of creating affixes based off of roots by hand. One place to start may be annotating adjective morphs that can also be used as adverbs, and using these as combining elements with verbs, but I suspect some kind of semantic filtering will be necessary to get good results.

## Generating more nuanced definitions

Outside of generating more different words, I think there's also a lot of room to improve on how Lyre's Dictionary writes definitions for them.

For one, it tends to interpret roots' meanings very literally: 'inscribe' is 'to write in', 'astral' is 'pertaining to stars', 'belligerent' is 'bearing war'. It would be good if we could capture some of the more nuanced extensions of the meanings — 'astral' may also refer to the heavens / outer space more generally, while 'belligerent' is more naturally glossed as 'hostile' or 'warlike'.

### Polyglosses

One relatively simple way to do this might be to create a new corpus of what we might call "polyglosses": combinations of tokens that, when they occur together in a word, use a single combined gloss instead of those tokens' individual glosses. In the example above, we could create a polygloss of 'aster' + '-al' with a gloss like "pertaining to stars or heavenly phenomena". This could also come into play in larger chains – 'astrality' could combine the meaning of the additional '-ity' suffix with this combined meaning.

But better than annotating a combination of specific morphs would be a combination of *meanings*. If these could be standardized in the morph corpus, then morphs from different origins but with the same meaning could share the same polygloss. This way, the same combination gloss could be shared between the Latinate forms 'astral' and 'stellar', as well as the English 'starry'.

A corpus like this would also allow the program to simulate calquing – translating a word or phrase from one language to another by translating the individual elements. Items could be added to the corpus based on their meaning in one language, and this meaning would be applied to similar formations of roots in a different language. But for the sake of not collapsing the possibilities, we probably wouldn't want to do it all the time in all cases.

### Metaphorism

One way that words gain unexpected meanings is through metaphor. 'Mellifluous' comes from the word for honey, 'mellis', but it doesn't refer to honey. Rather it uses this image to suggest sweetness. Similarly, 'sanguinary' doesn't refer literally to blood but to violence. These metaphorical meanings can be carried into any construction formed with these elements.

Similar to the idea of polyglosses, we might consider building a corpus of metaphorical meanings for different lexical items, linked to morphs but not bound to specific ones so that they can be shared between synonyms. Based on 'mellifluous' from Latin we might imagine 'melissorrheic' from Greek, or 'honey-flowing' in English.

These metaphorical meanings could come from actual observed metaphors in English and its ancestors, either within words or in how words are used, or they could come from general patterns of meaning change such as hyperbole, synecdoche, lewd innuendo, etc.

### External input

While I think both of the above ideas could produce very interesting results, they're also both very labor intensive to imagine. It also would require me in building it to either hew only to metaphors that are observed in the actual lexicons of the languages involved, or for me to innovate based on my own sense to cover other cases. If it were possible to find some external source for these linkings, that would make this work much more feasible and broader in extent than I could create on my own by hand.

I'm not sure whether any kind of corpora of meanings or metaphors may already exist that could be used here. If not, there may be some statistical means that could serve here. I'm not very familiar with these types of techniques, but it may be worth investigating word embeddings or other machine learning language modeling. However, I have various reservations about this sort of thing — for one, I would likely be uncomfortable with the loss of control of the program's output that it would entail. Still, I mention them here because I do see some possibilities.

## Analysis

While there are some ways of improve the program's generation that I can set out here, there are doubtlessly other currents in word-formation that I am totally unaware of. My knowledge is based on the haphazard walk I've taken through investigation into etymology, and I've never made any systematic study. So, I suspect there would be some benefit in a comprehensive analysis of English words.

What might this look like? In my imagining, it would be a list of English words, as many as I can possibly handle, broken down into their constituent elements. These should match the morphs in my morph corpus, so that I could search for how a particular morph is used. For instance, I could search for a suffix and get a list of every root it is attached to. This would give a quick way to find patterns or cases my requirement annotation on the suffix morph might have missed. Or I could search for morphs with particular semantic categories (animals, verbs that involve joining things together, etc) and see whether there are any affixes peculiar to them, or that take an unusual meaning.

Beyond just words broken into morphs, it would also be helpful to be able to find how those morphs are expressed in spelling, and how their meanings might vary. When a morph can take a slightly different form or meaning in different cases, seeing these together might clarify what conditions lead to what outcome.

This would also give an opportunity to break more complex words up by different patterns. For example, Lyre's Dictionary has a notion of a unusual combination patterns like "preposition + noun + suffix" (as in 'intermural'), and "number + noun + suffix" (as in 'trigeminal'). Other cases like this may exist that I haven't identified yet.

This would, of course, be a tremendously laborious undertaking, basically impossible to finish in one lifetime. Still, I have to admit it is an intriguing possibility.

– Robin, Summer 2023
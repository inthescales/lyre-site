---
title: "Notes on Using Old English Roots"
description: "Process notes on recent work to generate words from Old English roots"
tags: how
---

Earlier this year, I added a new component to the Lyre's Dictionary program that enables it to generate words [using roots that come from Old English](http://localhost:8000/blog/2024-2-18-old-english-roots.html), including both roots that still exist, as well as others that were lost to the language hundreds of years ago. Here, I want to give some insight into the process of that work: how it works, the decisions involved, things I learned, and other reflections.

## Roots and their types

One difference in how I am handling Old English roots compared with Latin and Greek ones is the introduction of what I have been calling "speculative" roots. These are roots that do not appear anywhere in modern English as best I can tell, but which existed in earlier forms of the language (at any time before the year 1600, more or less). While the Latin and Greek corpora I built include (almost) no speculative roots, instead generating new words by remixing roots found in modern words with different prefixes and suffixes, many of the Old English roots I included are speculative. With these roots, we can simulate historical sound change to turn an Old English word that was lost before the modern era into a new word with a modern sound and form.

However, I also wanted to include common modern roots that derive from Old English, words like "child", "throw", "bitter", and so on. Judging that it would be boring to see the program generate words like "child (n): a child", I made the decision that common roots can only appear with extra parts added on (making new words like "bechild", "throwsome", "bitteren"), while speculative roots can appear in modernized form on their own (making words like "whirve" and "margh") or with added elements ("whirvester", "marghcote").

### Obscure roots

Some words, however, didn't sit neatly as either speculative or common. How should we treat words that, though they did occur at some point in the modern era with modern spellings, are today archaic or very obscure. Should we consider words like "ween" or "blin" (both attested as late as the 1800s) to be the same as the ones that fell out of use earlier? People who aren't familiar with the word may be interested in an entry defining it, but the program isn't really producing anything new in that case, which feels unsatisfying.

This led me to introduce a third category of "obscure" words — words that do appear in the modern era, and have modern forms, but which I guessed that most English speakers wouldn't be familiar with. I've configured the program so that these words _can_ appear on their own, but are found more frequently in combinations. Now though, I don't feel satisfied with this decision, and may treat them as equivalent to common roots in the future.

### Canonical forms

Since there seems to be some randomness in how a word changes as it evolves into a modern form, I added a "canonical" form to still-existing roots so that they don't unaccountably come out wrong (for example "gote" instead of "goat"), which might have made some entries confusing or broken-seeming. But since this alternation does show something of other ways English could have been, I included this as a new type of entry that can appear, in forms like "gote (n): alternate form of "goat""

### Homophones

Many of the speculative words, even though they may have had distinct sounds in Old English, when put through a process of modernizing sound change become homonyms of common words. The Old English _midl_ (a horse's bit) becomes "middle", and _heoru_ (sword) becomes "here" or "hear". These results feel less interesting to me, so I've set these roots to appear less frequently. Currently I've labeled them by hand. In the future, it may be convenient to look for a way to identify them automatically.

### Multiple meanings

In [a previous post](http://www.lyresdictionary.com/blog/2023-2-19-constructing-the-corpus.html), I wrote about how I selected among the different possible meanings of roots. With Latin and Greek, where nearly all of the roots are found in modern words, I tended to choose whatever meaning seemed to best reflect the present-day usage of that root. But how should we gloss speculative roots, where there is no present-day usage to look to? In the Old English corpus, for speculative roots and common roots as well, I leaned strongly toward including all or most of the historical meanings, choosing randomly between them in each instance. Similar to canonical forms, I separated one principal meaning that captures the present-day usage of non-speculative roots, and set the program to use these more frequently than the alternate meanings.

## Dialects

A few surprises came up for me related to different English dialects.

### In Old English

My sources for Old English words list alternate forms for many of them. Old English had several dialects of its own, with modern standard English descending primarily from the Mercian dialect of Old English and the Midlands dialect of Middle English, spoken in the regions to the north of London. However, some of our modern words come from other dialects instead. For example, "hale" and "screed" are from a northern dialect, while "vat" and "vixen" come from the south.

To reflect some of this, I included alternate Old English forms in the data that are used occasionally in place of more standard ones. But a better treatment will be one that reflects the fact that the sounds of English in the different regions of the England evolved in slightly different ways, and could match sound change patterns with the word forms.

### In present-day English

I was surprised by how often I saw that Old English words that were lost in standard English lived on much longer in regional dialects, particularly in Scotland and the north of England.

I started out just by treating these cases the same as words found in the standard dialect, using canonical forms to fix their usual sound and appearance in most cases. However, I realized when I learned of the northern word "lake" (meaning "to play") that it wouldn't be so simple — the long 'a' sound in that word, and its Old English ancestor _lācian_, kept its sound in the north, but in other regions changed to a long 'o', and would more likely have produced a modern form "loke" in standard English.

This created some uncertainty regarding whether to indicate a canonical modern form or not. In most cases, I treat the existing dialect form as canonical, but in "lake" and similar cases where I can know or guess there would be a different standard form, I let the sound change procedure determine the form.

## Linguistic research

Compared to the previous phases of Lyre's Dictionary, writing code to simulate early English sound change has required much more in-depth linguistic understanding, especially of phonology — the study of the sounds of language — and its applications in understanding the history of English. And while I was able to get a good start on writing the sound change code based on [the Wikipedia page for Middle English Phonology](https://en.wikipedia.org/wiki/Middle_English_phonology#Phonological_processes), enhanced by gleanings from various etymologies in _The Oxford English Dictionary_, there are many aspects of it that still remain unclear.

In working to make the program more accurate, I found myself reading a few academic works on the subject, leading to the first reference to [an academic paper](https://www.academia.edu/87208669/Homorganic_Cluster_Lengthening_Pre_Cluster_Shortening_and_preference_based_change_in_Early_English) in the Lyre's Dictionary codebase (though while writing this post I ran across a recent paper contesting some of its assertions — that's academia I guess.). The only purpose of this citation is to remind myself what my reason was for having written the code in a certain way, but I've enjoyed engaging with academic linguistics again for the first time since college.

I expect that more research could solve some of the mysteries that remain and make the program's representation of historical sound changes even more accurate. But that will have to be a project for another time.

## Aesthetic inclination

While bringing linguistic rigor to the project is important to me, and while one way of looking at what Lyre's Dictionary does is to see it as only making visible potential that exists naturally within the English language, it should also be remembered that its working is at every stage given shape by my own artistic motives.

In this post I've already mentioned cases where I made decisions about what the program should do based on what I thought would be interesting for readers online. Beyond that, there were many cases in building the Old English corpus where I was led by my own aesthetic desires. A few:

- I didn't include a canonical form for OE _morgen_, ancestor of the modern "morn" and "morrow", so that it would sometimes generate the alternative "morwen", because I liked its sound.
- I included the unattested but conjectured Old English root _mase_ (related to "maze"), glossing it as "confusion" based on its function in the verb _amasian_ (ancestor of "amaze"), because I loved the compounds I could make it with, like "mazestruck" and "mazemonger".
- I extended the sense of the early Latin loanword _timpana_, which I only saw glossed in dictionaries with the names of medieval instruments like "timbrel" and "tabret", with the modern gloss "drum", reasoning that that's how it would be used if "timpon" existed as a modern word.

I hope that Lyre's Dictionary can be something that's beautiful, aside from any ideas about historical simulation. And I can't help but reveal some part of myself in it, since it's made according to my own sense of beauty.

## Comparison with other Old English root revival projects

As I've mentioned before, I'm not the first person to try deriving hypothetical modern forms from lost Old English roots. I took inspiration from works like [_Uncleftish Beholding_](https://msburkeenglish.wordpress.com/wp-content/uploads/2010/04/uncleftish-beholding-aka-atomic-theory.pdf), David Cowley's _How We'd Talk if the English Had Won in 1066_, and similar projects under the name "Anglish", which set out to create alternate versions of English using only words of Germanic origin, often using revived roots to replace the removed words from French, Latin, and other languages. While I don't agree with the nonsensical idea of "purifying" English, and the 1066 counterfactual feels rather shaky, I've always found these alternate-Englishes fascinating, both in their sounds and in their making. But while I borrowed methods from these prior works, Lyre's Dictionary has its own perspective on how to use them.

First, since Lyre's Dictionary is not a restricted English but an expanded one, I'm free to use roots that some composers of such projects might reject: namely, early borrowings from other languages such as Latin and Old Norse that entered English during or before the Old English period. One everyday word of this sort of word is _cheese_, which comes from the Latin _caseus_, and which in Old English had the form _cese_ or _cyse_. An example I encountered on the way is _cælc_ (a goblet), with Lyre's modernizes as "calch", from the Latin _calix_. In Lyre's Dictionary, we can include multiple "snapshots" of any root from its lives in different times and places, both _cese_ and _caseus_, _cælc_ and _calix_, and follow from all of them to see their many possible efflorescences.

Second, since those trying to create all-Germanic English lexicons have a need to replace the words that were removed, when encountering words with overlapping meanings they are motivated to assign them distinct uses, rather than letting them act as synonyms. For example, they may likely assign "tungle" (from OE _tungol_) to replace "planet" (which comes from Greek) instead of using its sense as "star" (from OE _steorra_). Or they might gloss "shand" (OE _sceand_) with "disgrace" (from French) rather than with the also-Germanic "shame". For the purpose of Lyre's Dictionary synonyms still add variety to the system, and so we have no objection to glossing "tungle" as "star, or "shand" as "shame".

Of course, my methods have their own limitations. So far I have with a very few exceptions restricted compounding in Lyre's to forms I've found in dictionaries, swapping out only one element in a pair. Similarly, I've kept to suffixes that can be found in at least one modern word. But for a project less yoked to the sound and feel of actual present-day English, it's possible one the one hand to be more inventive, and on the other to import constructions from Old English that may sound unusual to modern ears. Compounds like _stonetimber_ for "masonry" (which has an Old English antecedent) or _groundnut_ for "peanut" (which does not) are both outside the scope of what Lyre's could produce at this stage.

## What comes next?

There are many more Old English roots that can be added, and more origin languages beyond that, but before laboring to increase the breadth of the program, I want to spend time revisiting what I've written so far — revising the data format, rearchitecting the code, maybe even a full rewrite in a programming language I feel more proficient in. A tall structure needs a strong foundation.

I could use a break first though.

– Robin, December 2024

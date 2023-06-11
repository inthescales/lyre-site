---
layout: post
title: "Constructing the Corpus"
excerpt: "On the choices that went into assembling the corpus of data for Lyre's Dictionary."
tags: how
---

In [the last post](http://www.inthescales.com/projects/lyres-dictionary/blog/2022/12/20/how-does-it-work.html), I talked about how Lyre's Dictionary works programmatically, operating on data objects called morphs, and combining them to make words. Here, I want to go into more detail about how I make morphs, and the decisions and tradeoffs that are necessary in this.

One of my guiding desires for Lyre's Dictionary is that, in its ultimate ideal, it should be able to produce every actual English word, as well as the much greater number of possible words outside and between those, making no distinction between the two.

I said before that more than any of its technical elements, the most complex part of developing Lyre's Dictionary has been in attempting to identify and model patterns of word-formation. To reach the goal of making it able to generate every actual English word, it's necessary to model some of the particularities and irregularities behind those words. We also want to leave the system open and flexible enough that it can combine parts in lots of genuinely new ways without being too beholden to historical contingency, *but* we want to do so without these new formations being nonsensical or too improbable.

This involves a delicate balance, and there are a lot of things to consider.

## Gathering roots

In the previous post, I alluded to the fact that the way Lyre's Dictionary makes words doesn't exactly resemble the typical process of English word formation. An example of this is a word like 'mural', which comes from a Latin word containing two elements: 'mur' meaning 'wall', and '-al' in this case glossable as something like "belonging to". But 'mur' isn't an element that's used to make new words in English, and while '-al' is seen in new words sometimes, its usage is restricted (in Linguistics terminology, it isn't very productive). They are in a sense "fused" into a single word in actual modern English. Here however, we have the freedom to treat these elements as fully productive, simulating the ways that they were used in the past to make words which English later inherited or borrowed.

### Being selective

When we look to English and its ancestors to build our corpus, a question arises: which elements from these languages should be included? While English borrows many roots from Latin and Greek, it doesn't use all of them. Only some portion of them made it into English. The choice is: should we add roots from ancestor languages to the corpus unconditionally? Or should we only take some and not others?

I think there are advantages to both, and the choice will lend a distinct flavor to the output of the program. Including all morphs greatly expands the possible output of the program, with more material for making more different combinations. This increases the novelty and variability of the results. Alternatively, restricting the selection brings the output closer in line with actual English.

When first releasing Lyre's Dictionary, I made the decision to restrict morphs only to those that appear in at least one actual English word (though I count obscure and archaic cases). The reason for this was that I felt that seeing recognizable components in the words would allow people seeing them online to half-understand them, letting them in on the joke in a way, and showing that the output does have a real linguistic basis.

I'm satisfied with this decision for now, but in the future I would like to move away from it for the sake of progressing toward that ideal of producing all possibilities. But, I may tag unattested morphs in such a way that I can play with their frequency, to try to keep the flavor of the output a little more 'actual' overall, without fully cutting off any potential.

### The benefits of anachronism

While the idea of historical simulation strongly influences my approach to this project, it isn't the whole story either. We see words in English that use Latin or Greek roots but that don't actually follow the patterns found in those languages, or have new meanings, because they are later coinages and so are no longer beholden to the rules and sense those roots once held (for example a word like 'countrify'). Thus, we have freedom on the other side as well — we aren't bound to always follow the rules of these ancestor languages.

Any notion of simulation would have to consider what we are looking at to be less a set of rules and more several, overlapping sets of rules with elements passing more or less freely between them. But while a more complex simulation might be able to handle all these cases, for now it isn't possible.

Instead, the current catalog of morphs to some extent straddles time — it includes both archaic meanings and modern ones, modernizes some spellings, and in some cases crosses the boundaries of language (such as including elements borrowed from Greek into Latin in both lists). It includes on even footing elements used very widely today, like the '-phobia' suffix, and those with only a few instances, like '-rrhea' (as in 'logorrhea'). This expands the catalog of morphs beyond what I would be able to represent with a strictly simulationist approach, and allows me to take inspiration from modern formations.

## The making of a morph

Once we've isolated the historical word-elements we want to use, we can make them into the morph objects that Lyre's Dictionary uses to make words. Sometimes this is straightforward, but it can also involve various kinds of complications.

### Meaning drift

One such complication is how to define a morph when its meaning has changed over time. As an example, let's consider the word '[virus](https://www.etymonline.com/word/virus#etymonline_v_7825)'. In Latin, it referred to sap or juices from plants. In medieval usage, it took on a meaning of "a poisonous substance". And in modern times, it refers to a particular sort of microscopic disease agent.

If we are to include this morph in Lyre's Dictionary, what meaning should it have? One possibility would be to give it its original Latin meaning. In actual history, the word's meaning changed in these certain ways, but we might imagine that things could have played out differently, and the word and any derivitives might still refer to plant juices today. But, it's also reasonable to want to be able to generate words based on its modern meaning, especially since those might be more recognizable. Keeping in mind the ideal of "all actual words and all hypothetical words", we may want to include all these meanings.

But this raises a question — 'virus' started with one meaning, and took on other meanings over time, even though it hypothetically may not have. But what about words that *haven't* changed their meaning over time? This is also an accident of history, and we can imagine that they might have taken other meanings than they did. But how can we catalog meanings that a word has never had? So far, this is not something I have a way of doing, but I see a few possibilities for future work here.

### Spelling change

Another force that shaped the current form of Lyre's Dictionary is historical spelling change, and the difficulty of representing it. As a rule, the sound of a particular word (and insofar as the two are related, its written spelling) changes over time, and when a word is traced back centuries from, say, English to French to Latin, it might have a significantly different form.

Complex changes in sound and spelling are something Lyre's Dictionary doesn't have a way to handle yet. Fortunately many English words closely resemble their Latin ancestors, and for these, it's largely possible to annotate them in their Latin forms, with a few predictable changes, such as removing grammatical endings ('officialis' → 'official') and adding a silent '-e' ('activus' → 'active') as necessary. These have been directly encoded into the morphs '-al' and '-ive', as well as others.

However, if we use these rules uniformly, we wind up with a number of 'near-miss' words, that are slightly off from their actual forms. For example take the word 'juror'. If we hewed strictly to latin forms, we would wind up with 'jurator' instead. The form of 'juror' is actually related to sound changes in French, but since it still uses the '-or' suffix, and feels sufficiently similar, I opted to add an exception to produce 'juror' (and a few other irregular forms) to avoid cases that I thought might appear 'incorrect'.

I may reverse this decision later in the interest of letting the program play out its rules more naturally. In any case, future work that would allow our word-formation to walk down all these different paths would make this sort of hand-made exception redundant.

### Handling ambiguity

Another type of situation requiring decision is that of ambiguity. For instance, in some cases, a word's different actual forms leave uncertainty about how to handle about cases that aren't attested. For example, the Latin verb 'flectere', to bend, combined with different prefixes gives us several modern English words.

    flex            deflect
    circumflex      inflect
    reflex          reflect

We see different endings in different cases. It's easy enough to use morph exceptions to say that 'circum-' should be followed by 'flex' and 'de-' by 'flect'. But what about 're-', which is seen with both? Or what if we have a different, unattested previx, like 'ob-'? So far I haven't thought of any way to decisively handle cases like this. Currently I tend to pick whichever one is most common, or choose one at random if there's no clear winner. In some cases, I have the program choose randomly for each new word.

These are all simple solutions, and a simple solution was necessary to move along with the work. But questions like these open the door to research that might make the simulation richer in the future. Looking at this case, a few hypotheses come to mind. Does the ending depend on when the word was formed (such as borrowings directly from Latin or French vs later coinages in English)? Could it be related to a difference between use as verbs or as nouns? Could some have been produced by backformation? And whichever may be the case, does this apply to other Latin verbs with varying forms like this?

### Lumping vs Splitting

Another recurring theme in building the Lyre's Dictionary corpus is one that writers of actual dictionaries face as well: the choice between [lumping and splitting](https://en.wikipedia.org/wiki/Lumpers_and_splitters). When a morph has multiple meanings, should this be represented by *lumping* them into a single morph that varies based on its context? Or by *splitting* them into multiple morphs with a common form?

The 'virus' morph mentioned above is one example — if we want to capture all three of its meanings, should we have one morph with multiple glosses? Or should they be three different morphs, that all just happen to have the 'vir-' stem?

Or, for a more egregious example, consider the Latin '-ate' suffix, which has a dizzying multitude of meanings: to use an instrument (flagellate), to produce a bodily fluid (lactate, urinate), to act in a role (adjudicate), to put something in a certain state (alienate, activate), forming frequentatives (dictate), forming participiate adjectives (desperate), and so on. Do all of these refer to single *idea*, or to more than one?

In the corpus so far, I've used both of these techniques in different cases, but for technical reasons have tended toward splitting. '-ate', for example, is represented as a different morph for each of these cases. This makes things much easier, since they have different requirements for what they can attach to. Similarly, I'm not sure how I would lump 'virus', since I would apply different semantic tags to them (the definition of plant sap I would want to tag with 'fluid' and 'secretion', but not the others). In general, I haven't written the technical system I would need to lump effectively. But, in simple cases, where it's just a matter of choosing between a different form or gloss either randomly or in exception cases, lumping is possible.

## Pruning it back

In many of the cases above, I've tended toward making the word-formation as expansive as possible, taking every point in the history of English as a possible beginning, and branching out in every direction from there. This serves the goal of expansiveness and variety, as well as the interest of historical simulation, and generally creates a richer and more interesting output.

But there's a danger in this as well — if our method of generation is too permissive, we can end up with forms that feel arbitrary, and definitions that don't make sense. We want some kind of pruning to make the words feel more natural, without cutting off too many interesting possibilities.

### Suffix combinations

The earliest version of Lyre's Dictionary was very permissive. For instance when adding a suffix, the only restriction was that the word's part of speech was one the suffix was compatibile with. This resulted in a lot of strange suffix combinations, like '-itify' (= '-ity' + '-ify') defined as "to make into the quality of being (some thing or characteristic)".

Of course, it's subjective what one considers sufficiently sensible, but I considered constructions like this to not have a clear meaning, and preferred to prune some of these cases. I did this by assigning to each suffix a list of approved other suffixes that can come after it, based on attested examples. So in the current version of the data, the '-ity' suffix can only be followed by '-ous' (as in 'felicity' → 'felicitous').

I think this change improved the quality of the program's output, but it's hard to say what reasonable cases might have been lost. It's also worth noting that which combinations seem reasonable may not be constant. While the Latin '-ox' ending tends to show up in English only with '-ity' or '-ous' suffixes (e.g. 'ferocity' / 'ferocious'), there is also an obsolete 'ferocient'. And while we're familiar with 'sarcasm' and 'sarcastic', other constructions such as 'sarcasmical' have existed, but didn't last. So, limiting ourselves to combinations that are commonly seen today may be over-strict.

### Rejected morphs

There are some morphs that I added but later removed, or that I tried to add but wasn't able to for some reason.

For some, like 'varicate' (as in 'prevaricate'), the reason was just that I couldn't figure out a gloss that made sense. Cases like the '-cle' suffix in 'tentacle', 'vehicle', and 'miracle', were hard to gloss well because to encompass all these words' meanings they would have to have a very vague gloss like "thing that does X", which felt unsatisfying. Some, like 'constant' as a root meaning 'constant', just felt too uninteresting to be worth adding.

Others were rejected because they would have required technical changes to work. A silent '-e' ending morph would have let me generate words like 'temple' and 'face', but failed because they violated some of the assumptions about morphs that the program relies on (since a purely sound-based morph wouldn't convey semantic information in the usual way). Similarly, for the verb 'fervere' (as in 'fervent') I wasn't able to find the grammatical information my system needs. In another case, a '-cule' suffix (as in 'molecule'), would form nouns indicating smallness, but my current system for composing definitions isn't smart enough about word order and so produces things like "small a dog" instead of "a small dog".

I've kept a record of cases like this, and am hoping to be able to use some of them in the future.

### Rejected methods of formation

Outside of individual morphs, there are some patterns of word formation that I opted not to use. As one example, there are a number of English words that are identical to Latin roots themselves, with no suffixes, such as 'status', 'campus', and 'forum'. These are perfectly fine words, but as a way of forming words, it felt too simple to be interesting. Especially early in the life of this project, I wanted every word it produced to involve some kind of change made to the basic elements, so I added a requirement that each word should include at least two morphs. Still, this is an attested method of word-formation, and eventually it should be part of the program.

## The absurdity of it all

As I've said before, Lyre's Dictionary is not very complicated at all from a computational perspective. The real challenge of making it is in attempting to identify and formalize patterns of word-formation, balancing the forces of plausibility and variation, and leaving room for interest and surprise. There is no single correct answer to the questions this brings up. 

The truth is, this project has always been a quixotic game — words are made not by the book but according to whim and circumstance. Still, I can hope that my pattern-eye picks out some pretty shapes from the dictionary's cloudscape.


– Robin, Spring 2023

---
layout: post
title: "How does it work?"
excerpt: "A brief explanation of how Lyre's Dictionary works, and how that determines the kinds of words it makes."
tags: how
---

In this post I'll describe briefly how Lyre's Dictionary works, both mechanically, and in how its way of working determines what kinds of words it makes.

The program has changed over the years since its inception, but while this post describes its current form, it mostly still uses the same basic concepts that it did in the beginning. I'll start by explaining those core concepts.

## Morphs

'Morph' is the term I use to describe the basic word-elements that Lyre's Dictionary combines to make words. They're roughly analogous to what linguists call 'morphemes', though I occasionally play fast and loose with the resemblance to get the results I want.

So what is a morpheme? Morphemes are the smallest, indivisible parts of a word that still have a distinct meaning of their own. For example, in the word 'speaker' we find two morphemes: 'speak' (to make words with your mouth), and '-er' (someone who does something). Now we could divide 'speaker' into smaller parts, down to individual letters. Or we could divide it in two differently, say 'spea' and 'ker'. But those divisions don't have anything to do with the meaning of the word. Our morphemes, on the other hand, we can see are shared with other words with related meanings, such as 'speaking' and 'unspeakable', 'lover' and 'writerly'.

Morphs are the basic material that Lyre's Dictionary uses to create words. The program operates on a catalog of morphs that I've created for it based on analysis of actual words from English and the languages that contributed to it. Here's an example of one morph from the database, from a Latin word for 'flower':

    {
        "key": "flos",
        "form-stem": "flor",
        "type": "noun",
        "declension": 3,
        "gloss": "flower",
        "tags": ["count", "concrete", "living", "bodypart", "bodypart-plant"],
        "origin": "latin"
    }


The key components here are <code>"form-stem"</code>, which tells what this morph should look like when it appears in a word, and <code>"gloss"</code>, which gives it a definition. So with the form 'flor', this morph could be combined with the '-al' suffix to make the word 'floral', and its definition would be something like "related to flowers".

Turning briefly to the other information here: the <code>"origin"</code> tells us that this morph comes from Latin, and <code>"declension"</code> is a category in Latin grammar that affects its behavior in certain English formations. The <code>"tags"</code> give us additional information, mostly to do with the morph's meaning: a flower is a concrete thing, not an abstract concept. It's a living thing, and in the context of a plant, it's a part of a larger organism. These are used in many cases to decide which suffixes this morph can take. For instance, anything tagged as a <code>"bodypart"</code> can take an adjective ending '-ate' meaning to have that part (like in 'vertebrate').

### Combining Morphs

Some morphs, those referring to nouns, adjectives, and verbs, are considered roots. These serve as the core of the words Lyre's Dictionary creates. Other morphs are affixes – prefixes and suffixes – which can't appear on their own but can be added on to roots, or to other affixes.

In the earlier example of 'floral', we saw that '-al' suffix, which changes the word from a noun to an adjective. And suffixes like that are also represented as morphs in Lyre's Dictionary. Here's the '-al' morph:

    {
        "key": "-al",
        "form-final": "al",
        "form-stem": "al",
        "type": "derive",
        "derive-from": "noun",
        "derive-to": "adj",
        "declension": 3,
        "suffixes": ["-ity", "-ize"],
        "gloss": "of or relating to %pl",
        "gloss-relative": "%@",
        "exception": [
            ...
        ],
        "origin": "latin"
    }

This one's more complicated, but to point out just a few things: first, like 'flor' it has form and gloss properties that define its spelling in a word and its definition. It also has <code>"derive-from"</code> and <code>"derive-to"</code> to tell us how it changes the morphs it's attached to – this one attaches to nouns and produces adjectives. Unlike 'flor', the gloss here has a special code in it, <code>%pl</code>. Affix morphs use codes like this to say how their definitions should incorporate the definition of the morph that they're modifying. <code>%pl</code> means to take the previous definition, make it plural, and put it in that place. So taking the original gloss 'flower', we pluralize and wrap it to make "of or relating to flowers".

So, morphs are the central building blocks of words in Lyre's Dictionary — all words are made out of sequences of morphs, whose forms combine to create the spelling of the word, and whose glosses are composed together to create the definition.

### Adding Complexity

Finally, the language for defining morphs offers a few special ways to change how they behave.

One is requirements. Any morph can have requirements added to it, which specify that it can only be used if certain conditions apply. Here's a simple example:

    {
        "key": "-etum",
        "form-final": "etum",
        ...
        "gloss": "[place] where %pl are grown",
        "requires": {
            "follows": {
                "has-tag": "plant"
            }
        },
        "tags": ["count", "concrete"],
        "origin": "latin"
    }

The '-etum' suffix is used to make words for a place where certain plants are grown. The most common English word that uses it is 'arboretum', from a root meaning 'tree', but there are also some more obscure cases, such as 'pinetum' for pines. The requirement here specifies that this suffix can only come after a root that has the 'plant' tag on it. The 'flor' root we saw earlier actually has this tag, so with these rules, we could create a word 'floretum', "A place where flowers are grown".

Another tool we have is exceptions. Exceptions use the same system for specifying certain situations to say that if that case does apply, we should override certain properties of the morph with different ones. For example:

    {
        "key": "scandere",
        "form-stem-present": "scand",
        "form-stem-perfect": "scans",
        ...
        "gloss": "climb",
        "exception": [
            {
                "case": {
                    "follows": {
                        "has-type": "prep"
                    }
                },
                "form-stem-present": "scend",
                "form-stem-perfect": "scens"
            }
        ],
        "tags": ["intransitive", "motion"],
        "origin": "latin"
    }

This morph represents the Latin verb 'scandere', "to climb". The <code>"form-stem-perfect"</code> tells us that, if we add the '-ion' ending to this verb root, it should use the form 'scans'. And if we do so we get the actual English word 'scansion'. But the exception here states that if this morph follows a prepositional prefix, then it should use the form 'scens' instead. And if we were to add the Latin 'ad-' prefix, we would get the actual word 'ascension' (the 'd' is dropped due to the combination of sounds). A number of Latin verbs have similar conditions, resulting in pairs like 'damnation' / 'condemnation', and 'caption' / 'reception'.

## Languages

So where do morphs come from?

English is a Germanic language, in the same family as Dutch, German, Swedish, and others, and its earliest vocabulary is in line with this history. However, over the last thousand years, it's absorbed a tremendous number of words from French, Latin, and other languages, which all coexist together in modern English.

However, just because these words exist in English doesn't mean that all their constituent morphemes became English morphemes along with them. Often, words that were multiple morphemes in their source language become a single morpheme in English, as the original constituent parts may not have been meaningful to English speakers. For example, English adopted the word 'mural' from Latin, but never adopted the root word 'murus' (wall) on its own, nor is 'mur-' used in English to form new words. It was in a sense "fused" with the '-al' ending when it was borrowed.

When we look at English words that derive from Latin, we can still make out some of the patterns of word-formation that existed in Latin, even though they no longer exist actively in English. '-al' was a very common suffix for forming adjectives in Latin, but even though it appears in English words, you can't just use it anywhere. It's generally only seen on words that come from Latin or its descendants, and trying to make a word like 'houseal' or 'earthal' sounds very strange. In linguistics terminology, we would say this morpheme isn't very productive in English. For comparison, a morpheme like the Modern English '-ness' suffix is very productive – you can add it to just about any noun or adjective and it can be understood.

So what is it we're doing in Lyre's Dictionary when we take these elements from Latin and Greek and combine them together? It's not exactly that we're recombining English morphemes. The way we're combining them isn't really in-step with their degree of productivity in English, and many are so thoroughly fused they may not even be considered English morphemes at all. Essentially, I think of it as simulating the morphological (word-formation) processes of these languages as they *might* have occurred *before* English, to create words that might then have been borrowed into English.

To do this, we need to know which language's rules we should be using, and which lists of these historical morphemes we should be working with. Each morph is tagged with an origin language, and will only be combined with morphs from the same language. Languages also define certain rules for how to join morphs together. For example, Latin tends to put a letter 'i' between two morphemes if there would be too many consonants together. For example, 'hort-' (garden) + 'cultura' (cultivation) becomes 'horticulture'. Greek on the other hand tends to use an 'o' for this, as in 'icon-' (holy image) + 'clastes' (one who breaks) → 'iconoclast'.

However, in actual English we *do* see words with components from different languages, whether they were simply coined that way from the start, like 'television' ('tele-' being Greek, 'vision' Latin), or whether they grew over time when a loanword was taken and then had new affixes applied, such as 'distressing' ('distress' being borrowed from Latin via French, and later given the Old English '-ing' suffix). Presently, this is a type of word-formation that Lyre's Dictionary isn't able to do (minus a few exceptional affixes). It will take some additional thought to decide how to make these kinds of formations, though I'm very interested in adding a notion of historical "stages" that a word passes through as it's being built, simulating borrowing from one language into another.

Currently, Lyre's Dictionary has morphs based in Latin and Greek. The main reasons for this are practical – English spelling conventions have made it so that many English words of Latin origin resemble their Latin originals quite closely. This made it easy to assemble a list of morphs from both English and Latin sources. More importantly, Latin and Greek roots also tend to undergo relatively few spelling changes when combining, while Old English is much more complicated in this respect, and so I've left it as a future project to include roots from Old English and other languages.

## Transforms

So we have morphs, taken from different origin languages, and we combine them to make words. The next question is, how do we combine them?

There are a few ways one word can be made from another. The simplest might be to just add suffixes. This can be done repeatedly, like so: 

    sensat- (feel)
    → sensat- (feel) + ion (state or quality)
    → sensation (feeling) + al (related to)
    → sensational (related to feeling)

There are also various prefixes that can be added. Verbs in particular have a lot of possibilities for prefixes: from the same 'scend' (climb) root mentioned earlier we could make 'ascend', 'descend', 'transcend', etc. Unlike with suffixes, the ways that prefixes can be used together are more restricted.

There are also some patterns with more specific meanings that I've identified and modeled. A prepositional prefix and a suffix for making adjectives or verbs can be added around a noun root to create constructions that describe a thing's position relative to something else. For example:

    derm- (skin) 
    → sub- (beneath) + derm- (skin) + -al
    → subdermal (beneath the skin)

Another pattern uses a number prefix to make words related to a certain quantity of a thing. For instance:

    ped- (foot) 
    → bi- (two) + ped- (foot) + -al (having)
    → bipedal (having two feet)

These different kinds of additions that can be made to the word-in-progress I call transforms. Each transform takes in one or more morphs, adds something to it, and passes the result on. This can be done multiple times to create a more and more complex word.

Ultimately, Lyre's Dictionary is based on a model of word-formation as a concatenative process. That is, it's based on taking components and linking them together. This covers many cases in actual English, but it does impose some limitations. It's not clear how the system could be made to represent a transformation that changes the shape of a root instead of adding something to it (such as the sound and spelling changes that occurred in the evolution of Latin into French). And since a suffix like '-al' has a somewhat different meaning when it's just added to a root (as in 'floral') compared to when it's in a three-part construct like 'bipedal', using it in both cases requires either coming up with a rule to treat it differently in different situations, or using two different identical-looking morphs (I've used both of these methods in different cases).

This concatenation is limited too. Lyre's Dictionary is able to take a root and add any number of prefixes and suffixes to it. But, it currently can't freely combine two roots together. This happens not infrequently in English words, such as 'magnanimous' (great-souled), 'diversiloquent' (speaking on many topics), and 'heterochromia' (having different colors). I've managed to represent many of the more common examples of this kind by turning the second element into a suffix, such as '-culture' for the raising of plants and animals, and '-vore' for things that eat other things. But allowing free combinations of roots will require a new way of thinking about how their meanings relate to one another that I haven't established yet.

## Putting it all together

Once we have morphs, and transforms to apply to them, the rest of the process is quite simple. We take a random root, apply a random number of transforms to it, chosen at random, and the result is a finished word: a sequence of morphs that we can use to generate a word's form and definition.

With this framework, it's usually easy to add new data in the form of morphs. Even new transforms, if there's a clear way to define them in terms of the concatenation process we have, can be added without much difficulty. Exceptions and requirements can be used to smooth over cases that produce irregular forms or definitions that aren't meaningful.

Lyre's Dictionary is not very complicated at all from a computational perspective. The real complexity of making it is in attempting to identify and model patterns of word-formation that apply to as many real-world cases as possible, while leaving it open to combine parts in lots of genuinely new ways, while *also* trying to keep these new formations from being too nonsensical. It's not a simple thing. Aligning one case with actual usage often ends up pulling another out of line. If 'oc-cas-ion' and 'de-cis-ion' both come from the same root, which version should I use if I apply a different, third prefix? Should I cut down on nonsensical meanings by putting limits on which suffixes can follow which other suffixes, but at the cost of decreasing the total diversity of words?

There is no answer to these questions. This project has always been a quixotic game — words are made not by the book but according to whim and circumstance, and the best I can hope for is that my pattern-eye picks out some pretty shapes in the dictionary's cloudscape.

– Robin, December 2022

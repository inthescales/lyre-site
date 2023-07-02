---
layout: post
title: "Future Work"
excerpt: "On possible future additions to Lyre's Dictionary."
tags: how
---

Although Lyre's Dictionary has existed for several years, and at the time of writing I am not actively working on it, I still consider it an ongoing project. Over the years since its creation many ideas for future expansion have come to mind, and while I may never realize all of them, I share them here to give some idea of what a more complete version of Lyre's Dictionary might look like.

## Expanding the corpus

### Adding more roots

Currently, Lyre's Dictionary only uses roots from Latin and Greek to make words, and the easiest way to add more content to the corpus would be to add more roots from these languages. My process has mostly been to research the origins of English words one-by-one and add their components to the corpus as [morphs](http://www.inthescales.com/projects/lyres-dictionary/blog/2022/12/20/how-does-it-work.html). I surely haven't exhausted the supply of roots available in the English lexicon — a more focused approach would definitely yield many new ones. I could spend some dedicated time reading through dictionaries, including ones focused on archaic and obscure words, to find more material.

Beyond that, while so far I've mostly limited the corpus to roots that actually appear in at least one English word, I could start building it out further by adding roots directly from the Latin and Greek lexicons. This would require some new research to find good Latin and Greek word lists (and may require some actual Greek study, which I've mostly avoided so far). These "speculative" roots, as I call them, would probably be coded to appear less frequently than those attested in English words, but I think they would still be a valuable addition.

### New sources and sound change

Of course English isn't made up only of elements borrowed from Latin and Greek. However, adding more origin languages would require deep new technical work to handle the sound changes involved in the transition from languages like Old English into Modern English. While it's simple enough to take a Latin word like 'narrare' and make it into the English 'narrate', it's a bit less straightforward (to me, anyway) to go from the Old English 'belyfan' to 'believe'. Vowels need to shift, and consonants may change when roots or affixes are added (like the f → v change from 'leaf' to 'leaves'). If I want to be able to include Old English roots that didn't survive into Modern English, or to record any Old English roots in the corpus in their original form (and I suspect I would have to in order to reliably handle the way they can change with affixes or in compounding) it would be necessary to develop a way to compute these sound changes. But once this is done, it would open the way to vast tracts of English that I haven't been able to touch at all yet.

This doesn't just apply to converting Old English to Modern English. Once such a system exists, with further linguistic research it could be applied to other origin languages as well — we could create a corpus of Old French roots, convert them to Middle English, then convert that to Modern English. We could even take the Latin corpus we have, and convert through French and then into English. This would allow us to generate [doublet](https://en.wikipedia.org/wiki/Doublet_(linguistics)) words like 'camera' (Latin) and 'chamber' (French), and French-inflected forms of Latin words that never made it into French. We could additionally pull in Old Norse, which also contributed significantly to early English.

After tracing the main lines of English's development, we could even go farther and pull in roots from languages that fed into those nearer tributaries — Greek through Latin (with its attendant mutations), Frankish and Gaulish through Old French, Arabic through French or Latin or both, origins as far distant as we want to imagine, ancient and modern.

### Modern English formations

While I've spent a lot of time thinking about how to simulate the historical development of English, I don't want to overlook the fact that English in its present day form also has its own processes of word-formation. While some of them are very obvious to us (e.g. adding '-er' to a verb means "someone who does that verb"), others are intriguingly subtle. For instance, consider the suffix '-y'. When applied to a fluid, like 'milky' or 'watery', it can mean "containing or resembling", but it can also, as in 'muddy' or 'bloody' mean "covered in". And this latter meaning can apply to other kinds of coverings as well, like growing things as in 'mossy' or 'grassy'. How many meanings might we tease out of this simple suffix?

While most of these modern elements have historical origins ('-y' itself dates back quite far, to an '-ig' in Old English) allowing them to play in a modern context opens new possibilities for combination, as they can combine with elements that didn't exist at their time of origin. And including their modern patterns of usage in the corpus gives us a more complete picture of how these elements can move in the English of the present.

And of course, modern-style word-formation lets us use modern elements, including roots for new concepts like 'blog' or 'plastic' as well as more recently coined affixes like '-esque' and '-aholic'.

### New processes

Aside from adding new roots, there are also new ways of using morphs that could be explored.

One is simply the possibility of single-morph words, which Lyre's Dictionary currently doesn't produce. While single-morph words from common roots may not be very interesting ("cat (n) - a cat"), they could be a valuable addition when using roots from ancestor languages. These could be taken more or less straight, as in words like "corpus" and "demon", but would be especially interesting if we add the possibility of computing historical sound changes, to transform roots into unfamiliar forms, or generate modern forms of ancient roots that have since been lost (projects like [Anglish](https://anglish.org) show how the results might look — for example, a hypothetical word 'thild', meaning 'patience', from the Old English 'þyld').

Compounding roots would also add a lot of new possibilities, though it would require some new concepts for how to make roots relate to each other beyond my current method of creating affixes based off of roots by hand. I've observed a few patterns that could be imitated, such as combining an adverbial morph with a verb to describe how the action is done (as in 'pauciloquent' – "speaking little"). I suspect some kind of semantic filtering would be necessary to get good results though, which may require a lot of new morph annotations.

The process of [calquing](https://en.wikipedia.org/wiki/Calque) — translating a word or phrase from one language to another by translating its individual elements — shows another path we could take. Compounds that exist in any language could be built into a corpus together, with a list of the morphs that make them up, and these elements could be translated individually into morphs deriving from language to create a calque word. For example, an archaic name for the element mercury is 'hydrargyrum', from Greek roots meaning 'water' and 'silver'. We could then replace these with Latin roots of the same meaning, creating something like 'aquargent', or with English elements to create 'water-silver' as new names for mercury.

## Generating more nuanced definitions

Outside of generating more different words, I think there's also a lot of room to improve on how Lyre's Dictionary writes definitions for them.

### Gloss fusion

One awkward quality of the definitions in Lyre's Dictionary comes from the fact that when it builds a word, every morph that's added adds some piece to the definition. While this often works well, especially in shorter words, the more morphs there are, the more the definition builds up into a conglomeration that can come to look unweildy, for example, "the quality of being given to paying attention to" for 'attentive'. The way the definition is expressed is never reconsidered as it grows longer — every part exists independently.

One way to address this would be to build a corpus of what we could call 'gloss fusions': multiple-part expressions matched to possible shorter replacements. For example, 'make' + 'full' → 'fill'; 'make' + 'hot' → 'heat'; 'likely to' + 'trust' → 'trusting'. Whenever we see one of these multi-part combinations in the glosses of a word's morphs, we could replace them with their single-word equivalent in order to make the definition flow a little more naturally.

These could also be added on to the definition as a separate sense (more below), or if it results in a single word, a synonym listed at the end of the entry. Of course, there is a danger with this that the definition resulting from the use of fusion could be the same as the word itself, as in 'cred-' + '-ulous' → 'tending to' + 'believe' → 'credulous'. We would want to include a separate check to make sure that the definition doesn't wind up the same as the word we're defining.

This system could also be used to expand upon the idea of compound-based calquing described above. Rather than beginning from a combination of morphs, we could include some less-obvious meaning combinations that appear in one language as gloss fusions, and apply them to the same combination in roots from another language. For example, 'evasion', composed of elements that more literally interpreted mean "going out" or "going away" could have its meaning of "escaping" transferred to similar Greek elements forming a word 'ecbasis' (incidentally, this word is attested in English with the meaning 'digression'. This meaning could reciprocally be applied to the Latinate 'evasion' by the same process).

### Metaphorism

Another limitation in how Lyre's Dictionary creates definitions is that it tends to interpret roots' meanings very literally: 'astral' is "pertaining to stars", and 'levity' is "the quality of being light". It would be good if we could capture some of the more nuanced extensions of the meanings — 'astral' may also refer to the heavens or outer space more generally, while 'levity' connotes humor or lightheartedness.

One way that words gain these additional meanings is through metaphor. 'Mellifluous' comes from the word for honey, 'mellis', but it doesn't refer to literal honey here. Rather it uses this image to suggest pleasantness. Similarly, in the example of 'levity', there's a meaning of "humor" through the metaphor of emotional lightness, while in the case of 'astral', the singular "star" stands in for the sphere that contains those stars. Roots with these metaphorical or extended meanings can then carry them into any construction they help form.

Similar to the idea of gloss fusions, we might consider building a corpus of metaphorical meanings for different lexical items, that may be associated with one or more morphs so that they can be shared between synonyms. Based on 'mellifluous' from Latin we might imagine 'melissorrheic' from Greek, or 'honey-flowing' in English, and the extended meaning of 'astral' would apply just as well to 'stellar' and 'starry'.

These metaphorical meanings could come from actual observed usages in English and its relatives, either in word formation or in how words are used, or they could come from general patterns of meaning change in language such as hyperbole, synecdoche, lewd innuendo, etc.

### External input

While building new corpuses for these new processes would open up a lot of new possibilities, it would also be very labor-intensive, and it would require me in building them to either hew only to cases that are observed in the actual lexicons of the languages involved, or for me to innovate based on my own sense to cover other cases. If it were possible to find some external source of information to populate these, that would make this work much more feasible and broader in extent than I could create on my own by hand.

I'm not sure whether any kind of corpora of meanings or metaphors may already exist that could be used here. If so, it could serve as a good resource for this. If not, there may be some statistical means that could be used. I'm not very familiar with them, but it may be worth investigating word embeddings or other machine learning language modeling methods. While I haven't been interested in using these to generate words, since they seem to pass over the questions of structure and etymology that are most compelling to me, there may be some good use for them in generating definitions, where, due to meaning drift, strict correctness is less of a concern. However, I have various reservations about this sort of thing — most practically, I would likely be too uncomfortable with the loss of control of the program's output that using them directly would entail. Still, I mention them here because I do see some possibilities that could be interesting to explore.

### Senses

In a version of Lyre's Dictionary where it's possible for morphs and the words they make up to have multiple meanings, the question arises of how to pick one. If we want to keep all of them as possibilities, one option would be to choose randomly each time a word is made. But there is another route: listing all of them, as actual dictionaries do. This would require some technical work to allow adding different ways of using a morph as a sort of "morph within a morph". Senses would share the same written form and any contextual behaviors that form has, but would have their own glosses, semantic tags, and potentially their own part of speech (in the example of 'mellifluous', 'mellis' is a noun when used literally, but in the metaphorical case is acting more like an adverb). Generated entries could include one definition, all of them, or a certain set, if for instance some possible definitions might be too similar to want to present together.

## Ornaments

Right now Lyre's Dictionary produces entries that would be very bare-bones for an actual dictionary. A good dictionary entry is more than just a word and a definition. Additional details like pronunciation, etymologies, and example usages could make the entries the program produces more interesting, and add some imitational richness.

Etymologies could potentially be constructed from the morphs that make up the word similarly to way we produce the form and definition. Many morphs represent actual etymons (that is, historical morphemes) in a relatively straightforward way, so the basis of an etymology section could be built from a simple list of those etymons presented in their earlier forms (e.g. instead of the English-style 'injunction', the Latinate 'iniunctio').

Pronunciations could also be built alongside written forms, though care would have to be taken to represent sound changes that may occur as more parts are added to the word. There may also be a lot of ambiguity with this, perhaps particularly with stress, but it may be possible to come up with something plausible in most cases. And if we are generating words in a way that involves sound change (as described above), we may already have pronunciations on hand.

Example sentences present a challenge, but I think there are some possibilities here as well. One would be to use [Tracery](https://www.tracery.io/) or a similar system to build up sentences out of component templates. Semantic tags on the word could be used to select from these templates so that the sentences feel a little less generic (for instance, anything tagged as an animal could use "I saw a ____ at the zoo today"), though I think it would be difficult to do this in a way that really demonstrates the meaning of the word. Alternatively, this is another case where some kind of generative language model might perform well.

## Delivery

Currently the only ways for anyone to see Lyre's Dictionary at work is to follow it on Twitter or Mastodon, or download the code and run it themself.

### New feeds

As I see it, a social media feed is a natural way to publish a generative work like this — it has no fixed beginning or end, so it can't be definitively contained. Its results don't need to be viewed in any particular order, and it's not engaging enough to want to read a lot of it at one time, so it can be interspersed with other things, and there's no loss if some parts are skipped.

One avenue for expansion would be to post to more sites. Twitter and Mastodon are the main ones I use personally, so I started with those, but if it lets more people enjoy it it could be good to create accounts on more platforms. I'm also curious about the possibilities that sites with richer text formatting like Tumblr or Cohost might allow — it would let the entries contain longer, mixed content, like the embellishments described above, without hitting the eye like a brick.

### New formats

While the feed format has been suitable for this project, a few other possibilities interest me as well. A "word of the day" style email has some charm, and some potential benefits: some may find a word a day more palatable than the dozen posts that it currently makes each day on social media, and the context may encourage reading with a more thoughtful eye. These could be published with RSS as well.

Ideally, I would also like it if the Lyre's Dictionary homepage were able to display a new random word on each visit (currently it cycles through a few hand-selected entries). It seems fitting to me for the web site to be able to really demonstrate the thing it represents, without needing an external link.

Finally, if there ever comes a time when I consider this project to be complete, whether because I've realized every idea I had, or because it just feels like time to end it, I might generate some large number of words, alphabetize them, and format them into a PDF or other document to serve as a compiled edition of Lyre's Dictionary. While of course a fixed form like that wouldn't contain the full contents the program is capable of generating, and while the fact of the generation may be more interesting than the words themselves, I think it could be a satisfying final artifact to carry on from this part of my life.

## Analysis

While I've set out a few ways to expand the program's word generation here, there are doubtlessly other currents in word-formation that I am totally unaware of. My knowledge is based on the haphazard walk I've taken through investigations into etymology, and I've never made any kind of systematic study of the English lexicon. A more comprehensive analysis of this kind may suggest new paths for development, or clear up current confusions.

What might this look like? I imagine a list of English words, as many as I can possibly handle, broken down into their constituent elements, annotating the specifics of meaning and form. These should match the morphs in my morph corpus as much as possible, so that I could query this list based on morphs and their properties and get a list of matching words. For example, if a suffix morph can have multiple meanings, being able to quickly group words using that suffix according to which meaning they take might show when those meanings do and don't apply (for instance, when does '-ify' mean "to make into", as in 'deify', and when does it mean "to produce", as in 'speechify'?). Or, if an element has different spellings in different words, pulling up a list of every word that uses one form or the other could clarify whether it's affected by the letters around it.

This would also give an opportunity to break words with more complex structures up by the different patterns they use. For example, Lyre's Dictionary has a notion of a distinct combination patterns like "preposition + noun + suffix" (as in 'intermural'), and "number + noun + suffix" (as in 'trigeminal'). Other cases like this may exist that I haven't identified yet.

This would, of course, be a tremendously laborious undertaking, basically impossible to finish. Still, I have to admit it is an intriguing possibility.

## The future

I don't have any plans to work more on this project in the near term, but who knows what the future holds? Whatever new developments may come, I'll write about them here on this blog.

– Robin, Summer 2023

---
layout: post
title: "Old English Roots"
excerpt: "Showing some ongoing work on generating words from Old English roots"
tags: what
---

---

This post is based on a short talk I gave at the monthly event Wordhack on January 18, 2024, held at [Wonderville](https://www.wonderville.nyc/) in New York City. Some changes were made to suit the format.

---

One of the major limitations of Lyre's Dictionary that I've wanted to work through for a long time is that it can only create words based on Latin and Greek roots. This, of course, does not reflect the makeup of English overall. In fact, the most common English words of today can be traced back to English's original form, the language called Old English, or to its earlier Germanic roots. Recently I've been working on a new system for making words from Old English roots, and have made some good progress.

First, some background:

## Old English

Old English refers to the earliest period of the English language, as it was spoken between about the 6th and 12th centuries. This language was distinct from Modern English in many ways, and it both looks and sounds so different that it cannot be readily understood by Modern English speakers.

As an example, consider these first few passages of the Lord's Prayer as it was written in Old English (you can hear it spoken [here](https://upload.wikimedia.org/wikipedia/commons/2/23/Faederureaudio2.ogg)) with its modern form:

<table style="width: 100%; margin: auto;">
<tr><td><i>Fæder ūre þū þe eart on heofonum,</i></td><td>Our Father, who art in heaven,</td></tr>
<tr><td><i>Sīe þīn nama ġehālgod.</i></td><td>Hallowed be thy name.</td></tr>
<tr><td><i>Tōbecume þīn rīċe,</i></td><td>Thy kingdom come,</td></tr>
<tr><td><i>Ġeweorðe þīn willa, on eorðan swā swā on heofonum.</i></td><td>Thy will be done on earth as in heaven.</td></tr>
</table>

Although it may appear totally alien at first, with examination, it is possible to see connections between the Old and Modern English words. '<i>Fæder</i>' becomes 'father', '<i>heofonum</i>' changes to 'heaven', '<i>nama</i>' to 'name'.

It's not just that these words happen to look similar – there are more or less well defined
changes that transformed the earlier forms of the words into the later ones. And to the extent that these changes can be defined, they can be simulated as well. This is what I have attempted to do in adding Old English to Lyre's Dictionary.

## The Results So Far

This table shows some output from the new code that I've been writing. It takes in the Old English words on the left, and produces their modern forms on the right:

<table style="width: 100%; margin: auto;">
<tr><th>OE written</th><th>OE sounds</th><th>ME sounds</th><th>Modern form</th></tr>
<tr><td>bāt</td><td>/baːt/</td><td>/bɔːt/</td><td>boat</td></tr>
<tr><td>heofon</td><td>/xeofon/</td><td>/xɛːvən/</td><td>heaven</td></tr>
<tr><td>ċild</td><td>/tʃild/</td><td>/tʃiːld/</td><td>child</td></tr>
<tr><td>dæġ</td><td>/dæj/</td><td>/dai/</td><td>day</td></tr>
<tr><td>frēond</td><td>/freːond/</td><td>/freːnd/</td><td>friend</td></tr>
<tr><td>nama</td><td>/nama/</td><td>/naːm/</td><td>name</td></tr>
<tr><td>eorðe</td><td>/eorθe/</td><td>/erð/</td><td>earth</td></tr>
<tr><td>bryċġ</td><td>/brydʒ/</td><td>/bridʒ/</td><td>bridge</td></tr>
<tr><td>gōd</td><td>/ɣoːd/</td><td>/goːd/</td><td>good</td></tr>
<tr><td>hlæhhan</td><td>/xlæxxan/</td><td>/laux/</td><td>laugh</td></tr>
<tr><td>stelan</td><td>/stelan/</td><td>/stɛːl/</td><td>steal</td></tr>
</table>

This is a three step process, moving from the first column to the fourth.

1. Start with Old English written forms, generally in their standard form from about the year 900, along with some sound annotations used by modern scholars (these are the dots and lines you see above some letters).

2. Determine the pronunciation of this word in Old English. This tends to be straightforward, as Old English was usually written the way it was pronounced (and the added sound annotations clarify the ambiguous cases). The table here uses my own rough phonemic representation of the sounds of Old English.

3. Put this pronunciation through about six hundred years of simulated historical sound change, approximating how it would have sounded in Middle English (a later form of the language) around the late 15th century. The reason we stop there is because, while English spelling is notoriously confusing, part of the reason is because we still use spellings that were developed during this time, which weren't updated as pronunciations changed over the last 500 years.

4. Determine a modern form for the word, based on observed modern-day spelling conventions.

As the table shows, this procedure works pretty well. It's able to produce the correct spellings of all of these words based only on their Old English forms.

However, this table hides some of the complexity. These next tables show some of the ambiguities and uncertainties in this process:

<table style="width: 100%; margin: auto;">
<tr><th>OE written</th><th>OE sounds</th><th>ME sounds</th><th>Modern form</th></tr>
<tr><td>bāt</td><td>/baːt/</td><td>/bɔːt/</td><td>bote <span style="color:red;">(boat)</span></td></tr>
<tr><td>māra</td><td>/maːra/</td><td>/mɔːr/</td><td>moar <span style="color:red;">(more)</span></td></tr>
<tr><td>ċēowan</td><td>/tʃeːowan/</td><td>/tʃiu/</td><td>chue <span style="color:red;">(chew)</span></td></tr>
<tr><td>trēwe</td><td>/treːwe/</td><td>/triu/</td><td>trew <span style="color:red;">(true)</span></td></tr>
</table>

Like before, the input to the program is on the left, and the output is on the right. I've also added annotations in red. As you can see, sometimes the program produces unexpected results. But although these spellings aren't the ones we see in actual English today, they seem to be plausible. We might just as well have ended up with 'bote' instead of 'boat' — as far as I can tell, it's a matter of chance. In these cases, I've coded the system to produce one or the other at random.

Pronunciations can also diverge during historical change:

<table style="width: 100%; margin: auto;">
<tr><th>OE written</th><th>OE sounds</th><th>ME sounds</th><th>Modern form</th></tr>
<tr><td>clyċċan</td><td>/klytʃtʃan/</td><td>/klitʃ/</td><td>clitch <span style="color:red;">(clutch)</span></td></tr>
<tr><td>hȳdan</td><td>/xyːdan/</td><td>/xuːd/</td><td>houd <span style="color:red;">(hide)</span></td></tr>
<tr><td>wicu</td><td>/wiku/</td><td>/wik/</td><td>wick <span style="color:red;">(week)</span></td></tr>
<tr><td>wudu</td><td>/wudu/</td><td>/wud/</td><td>wud <span style="color:red;">(wood)</span></td></tr>
</table>

Cases like these occur because the historical changes and spelling conventions aren't completely predictable: a single sound might change differently in different cases, and standard modern forms might derive from any one of multiple Old English dialects.

And there are some cases I can't explain at all. Either my system doesn't account for some historical processes, or these words simply changed unpredictably:

<table style="width: 100%; margin: auto;">
<tr><th>OE written</th><th>OE sounds</th><th>ME sounds</th><th>Modern form</th></tr>
<tr><td>camb</td><td>/kamb/</td><td>/kamb/</td><td>camb <span style="color:red;">(comb)</span></td></tr>
<tr><td>ċīcen</td><td>/tʃiːken/</td><td>/tʃiːkən/</td><td>chiken <span style="color:red;">(chicken)</span></td></tr>
<tr><td>dūst</td><td>/duːst/</td><td>/duːst/</td><td>doust <span style="color:red;">(dust)</span></td></tr>
<tr><td>nēdl</td><td>/neːdl/</td><td>/nedəl/</td><td>neddle <span style="color:red;">(needle)</span></td></tr><tr></tr>
</table>

While I may discover more historical rules that explain some of these differences, I'll never be able to write a system that could account for all of the historical happenstances that created all our modern words. Some words will always be mysterious.

So, there is necessarily some ambiguity in this process, and one Old English form may have multiple plausible modern forms. But overall, the program does seem to generally produce plausible output. And once we have this system, we can do something very interesting with it — we can take words that fell out of the language along the way, and see what they might look like if they still existed today:

<table style="width: 100%; margin: auto;">
<tr><th>OE written</th><th>OE sounds</th><th>ME sounds</th><th>Modern form</th></tr>
<tr><td>drēfan</td><td>/dreːfan/</td><td>/dreːv/</td><td>dreeve</td></tr>
<tr><td>friþ</td><td>/friθ/</td><td>/friθ/</td><td>frith</td></tr>
<tr><td>heolfriġ</td><td>/xeolfrij/</td><td>/xelvrəj/</td><td>helvry</td></tr>
<tr><td>hremman</td><td>/xremman/</td><td>/rem/</td><td>rem</td></tr>
<tr><td>līg</td><td>/liːɣ/</td><td>/liːx/</td><td>ligh</td></tr>
<tr><td>nyten</td><td>/nyten/</td><td>/nitən/</td><td>nitten</td></tr>
<tr><td>racente</td><td>/rakente/</td><td>/rakənt/</td><td>rackent</td></tr>
<tr><td>snytru</td><td>/snytru/</td><td>/snitər/</td><td>snitter</td></tr>
<tr><td>swincan</td><td>/swinkan/</td><td>/swink/</td><td>swink</td></tr>
<tr><td>þild</td><td>/θild/</td><td>/θiːld/</td><td>thild</td></tr><tr></tr>
</table>

For example, Old English had a word '<i>drefan</i>', meaning "to hinder"; if it still existed today, it might look like 'dreeve'. '<i>snytru</i>', meaning 'wisdom', might be 'snitter'. With this process, we can create lots of new words which the program would have had no way of producing before, and get a much more complete picture of the possibilities latent in English.

## Work to be Done

There's still some work to do before this is ready. While the basic sound change and spelling components are looking good, it'll take some additional work to be able to support things like affixes and compounds. I also want to do some more testing against real words to make sure that I'm catching as many uncommon cases as possible – my research is still turning up new rules for sound change, and there are some spelling ambiguities that might become clearer with more examples to work from. Maybe the biggest piece of remaining work, I'll also need to create a whole new corpus of Old English roots. This will require a lot of research work, and I'll need to decide how I want to handle alternate forms and dialects.

But, this is very exciting not just because of the promise of creating words from Old English roots, but because it proves that this kind of sound change simulation is possible. In the future, I hope it will be possible to use a similar process for different etymological pathways, such as deriving French forms from Latin, Middle English from Old French, and more.

– Robin, February 2024

---
layout: home
title: "Lyre's Dictionary"
---

Lyre's Dictionary is a computer program that generates novel English words based on existing roots and patterns. For example:

<script type="text/javascript">
    function test() {
        var title = "";
        var type = "";
        var body = "";

        var choice = Math.floor(Math.random() * 21);

        switch (choice) {
            case 0:
                title = "cogniture";
                type = "noun";
                body = "The result of knowing";
                break;
            case 1:
                title = "futurarium";
                type = "noun";
                body = "a place for the future";
                break;
            case 2:
                title = "gymnasis";
                type = "noun";
                body = "the act or state of training";
                break;
            case 3:
                title = "aristophile";
                type = "noun";
                body = "one who has a love of the best things";
                break;
            case 4:
                title = "generatile";
                type = "adjective";
                body = "capable of being begotten";
                break;
            case 5:
                title = "synthalassic";
                type = "adjective";
                body = "of the same sea";
                break;
            case 6:
                title = "plumbivory";
                type = "noun";
                body = "the quality of eating lead";
                break;
            case 7:
                title = "philoclast";
                type = "noun";
                body = "one who breaks love";
                break;
            case 8:
                title = "botanize";
                type = "noun";
                body = "to make a plant";
                break;
            case 9:
                title = "enigmatorrheic";
                type = "adjective";
                body = "pertaining to flowings of riddles";
                break;
            case 10:
                title = "bibible";
                type = "adjective";
                body = "able to be drunk";
                break;
            case 11:
                title = "perort";
                type = "verb";
                body = "to rise through";
                break;
            case 12:
                title = "morsive";
                type = "adjective";
                body = "given to biting";
                break;
            case 13:
                title = "culminant";
                type = "noun";
                body = "one who reaches the highest point";
                break;
            case 14:
                title = "pamphorete";
                type = "noun";
                body = "one who carries everything";
                break;
            case 15:
                title = "taragmatic";
                type = "adjective";
                body = "pertaining to that which is disturbed";
                break;
            case 16:
                title = "plenify";
                type = "verb";
                body = "to make full";
                break;
            case 17:
                title = "pretercoloral";
                type = "adjective";
                body = "beyond a color";
                break;
            case 18:
                title = "mathogenic";
                type = "adjective";
                body = "producing learning";
                break;
            case 19:
                title = "misbellify";
                type = "verb";
                body = "to make beautiful incorrectly";
                break;
            case 20:
                title = "rubritude";
                type = "adjective";
                body = "the quality of being red";
                break;
        }

        var output = "";
        output += "<span class=\"title\">" + title + "</span> &#183; <i>" + type + "</i><br>";
        output += "<span class=\"body\">" + body + "</span>";
        return output;
    }
</script>

<div class="excerpt">
    <p>
        <script>document.write(test());</script>

    </p>
</div>

It also exists as a bot on [Twitter](https://www.twitter.com/lyresdictionary) and on [Mastodon](https://botsin.space/@lyresdictionary), where it posts several new words every day.

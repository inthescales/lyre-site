function choose_example() {
	var choice = Math.floor(Math.random() * 30);
    switch (choice) {
        // Latin ---------------------
        case 0:
            title = "bibible";
            type = "adjective";
            body = "able to be drunk";
            break;
        case 1:
            title = "cogniture";
            type = "noun";
            body = "The result of knowing";
            break;
        case 2:
            title = "culminant";
            type = "noun";
            body = "one who reaches the highest point";
            break;
        case 3:
            title = "futurarium";
            type = "noun";
            body = "a place for the future";
            break;
        case 4:
            title = "generatile";
            type = "adjective";
            body = "capable of being begotten";
            break;
        case 5:
            title = "misbellify";
            type = "verb";
            body = "to make beautiful incorrectly";
            break;
        case 6:
            title = "morsive";
            type = "adjective";
            body = "given to biting";
            break;
        case 7:
            title = "perort";
            type = "verb";
            body = "to rise through";
            break;
        case 8:
            title = "plenify";
            type = "verb";
            body = "to make full";
            break;
        case 9:
            title = "plumbivory";
            type = "noun";
            body = "the quality of eating lead";
            break;
        case 10:
            title = "pretercoloral";
            type = "adjective";
            body = "beyond a color";
            break;
        case 11:
            title = "rubritude";
            type = "adjective";
            body = "the quality of being red";
            break;
        // Greek ---------------------
        case 12:
            title = "aristophile";
            type = "noun";
            body = "one who has a love of the best things";
            break;
        case 13:
            title = "botanize";
            type = "noun";
            body = "to make a plant";
            break;
        case 14:
            title = "enigmatorrheic";
            type = "adjective";
            body = "pertaining to flowings of riddles";
            break;
        case 15:
            title = "gymnasis";
            type = "noun";
            body = "the act or state of training";
            break;
        case 16:
            title = "mathogenic";
            type = "adjective";
            body = "producing learning";
            break;
        case 17:
            title = "pamphorete";
            type = "noun";
            body = "one who carries everything";
            break;
        case 18:
            title = "philoclast";
            type = "noun";
            body = "one who breaks love";
            break;
        case 19:
            title = "synthalassic";
            type = "adjective";
            body = "of the same sea";
            break;
        case 20:
            title = "taragmatic";
            type = "adjective";
            body = "pertaining to that which is disturbed";
            break;
        // Old English ---------------------
        case 21:
            title = "margh";
            type = "noun";
            body = "a horse";
            break;
        case 22:
            title = "mimmer";
            type = "adjective";
            body = "kept in memory";
            break;
        case 23:
            title = "quethesome";
            type = "adjective";
            body = "easy to say";
            break;
        case 24:
            title = "quild";
            type = "noun";
            body = "plague, pestilence";
            break;
        case 25:
            title = "redewright";
            type = "noun";
            body = "someone who makes plans";
            break;
        case 26:
            title = "selk";
            type = "verb";
            body = "to become idle";
            break;
        case 27:
            title = "smeeker";
            type = "noun";
            body = "one who fumigates";
            break;
        case 28:
            title = "thester";
            type = "verb";
            body = "to darken";
            break;
        case 29:
            title = "wilven";
            type = "noun";
            body = "a she-wolf";
            break;
    }

    return [title, type, body];
}

function format_entry(title, type, body) {
	var output = "<div class=\"excerpt\">\n<p>\n";
    output += "<span class=\"title\">" + title + "</span> &#183; <i>" + type + "</i><br>\n";
    output += "<span class=\"body\">" + body + "</span>\n";
    output += "</p>\n"
    output += "</div>\n"
    return output;
}
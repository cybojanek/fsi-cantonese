#!/usr/bin/env python3
import sys

characters = {
    "佢": "keoi5",
    "姓": "sing3",
    "家": "gaa1",
    "我": "ngo5",
    "王": "wong4",
    "而": "ji4",
    "你": "nei5",
    "陳": "can4",
    "哋": "dei6",
    "講": "gong2",
    "何": "ho4",
    "學": "hok6",
    "早": "zou2",
    "晨": "san4",
    "李": "lei5",
    "對": "deoi3",
    "唔": "m4",
    "住": "zyu6",
    "係": "hai6",
    "姐": "ze2",
    "小": "siu2",
    "緊": "gan2",
    "再": "zoi3",
    "廣": "gwong2",
    "東": "dung1",
    "人": "jan4",
    "貴": "gwai3",
    "朋": "pang4",
    "友": "jau5",
    "英": "jing1",
    "國": "gwok3",
    "咩": "me1",
    "美": "mei5",
}

words = {
    "聽住": "teng1zyu6",
    "生": "saang1",
    "太": "taai2",
    "呀": "aa3",
    "再見": "zoi3gin3",
    "唔緊要": "m4gan2jiu3",
    "先生": "sin1saang1",
    "學生": "hok6saang1",
    "乜嘢": "me1je5",
    "上海": "soeng6hoi2",
    "上海人": "soeng6hoi2jan4",
    "呢": "ne1",
    "嘅": "ge3",
    "㗎": "gaa3",
}

has_multiple = set("聽生太呀要見乜上呢嘅㗎")

special_characters = "； 。「」﹁﹂\"、‧《》〈〉﹏…——～,?;，!-？"

def dtext(characters, jyutping):
    return "\\dtext{%s}{%s}" % (characters, jyutping)

def atext(sentence):
    jyutping = ""
    chars = [x for x in sentence]

    word = ""
    for i, x in enumerate(chars):
        is_stop = False
        if x in special_characters:
            is_stop = True
        elif i == len(chars) - 1:
            word = word + x
            is_stop = True

        if not is_stop:
            word = word + x
        else:
            w = " " if len(jyutping) > 0 else ""
            if word in words:
                w = w + words[word]
            else:
                for char in word:
                    if char in has_multiple:
                        print("ERROR: char %s has multiple tones" % (char))
                        sys.stderr.write("ERROR: char %s has multiple tones\n" % (char))
                        sys.exit(1)
                    if char not in characters:
                        print("ERROR: char %s has unknown tone" % (char))
                        sys.stderr.write("ERROR: char %s has unknown tone\n" % (char))
                        sys.exit(1)
                    w = w + characters[char]
            jyutping = jyutping + w
            word = ""
    return dtext(sentence, jyutping)

def main():
    return atext(" ".join(sys.argv[1:]))

if __name__ == '__main__':
    print(main())

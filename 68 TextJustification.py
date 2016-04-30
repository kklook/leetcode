

#Ð´µÄÃÉ±Æ
class Solution(object):
    
    def fullJustify(self, words, maxWidth):
        if len(words[0]) == 0 and maxWidth == 0:
            return [""]
        resultList = [""]
        wordcount = 0
        num = []
        for word in words:
            if wordcount == 0:
                resultList[-1] += word
                num.append(len(resultList[-1]))
                wordcount = len(resultList[-1])
            elif wordcount + len(word) + 1 <= maxWidth:
                resultList[-1] += " " + word
                num.append(len(resultList[-1]))
                wordcount = len(resultList[-1])
            else:
                t = list(resultList[-1])
                p = 0
                pd = 0
                if len(num) - 1 > 0:
                    p = (maxWidth - len(resultList[-1])) % (len(num) - 1)
                for i in range(len(num) - 1):
                    if p:
                        p -= 1
                        time = (maxWidth - len(resultList[-1])) / (len(num) - 1) + 1
                    else:
                        time = (maxWidth - len(resultList[-1])) / (len(num) - 1)
                    for j in range(time):
                        t.insert(num[i] + pd + 1, ' ')
                    pd += time
                for i in range(maxWidth - len(t)):
                    t.append(' ')
                resultList[-1] = "".join(t)
                resultList.append("")
                resultList[-1] += word
                num = [len(resultList[-1])]
                wordcount = len(resultList[-1])
        for i in range(maxWidth - len(resultList[-1])):
            resultList[-1] += ' '
        return resultList
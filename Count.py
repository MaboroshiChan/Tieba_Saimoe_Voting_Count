import re
class Count:
    def __init__(self, raw, data):
        self.load = raw  ##[]
        self.data = data  ##[[]]

    def CountCont(self):
        Cont = re.findall(".*: (.*)\[\[弃权]](.*).*", self.load)
        return Cont

    def getCont(self, Cont):
        vote = {}
        for i in range(len(Cont)):
            vote[Cont[i][0]] = 0
            vote[Cont[i][1]] = 0
        return vote

    def start(self, vote):
        for sheet in self.data:
            plusOne = re.findall('.*\[\[(.*)]].*', sheet)
            for name in plusOne:
                if name in vote:
                    vote[name] += 1
        return vote

    def result(self,Cont, vote):
        result = ""
        for i in range(len(Cont)):
            result += ("Area" + str(i + 1) + ":\n"
            +Cont[i][0] + " " + str(vote[Cont[i][0]])
            +"\n" + Cont[i][1] + " " + str(vote[Cont[i][1]]) + "\n\n")
        return result

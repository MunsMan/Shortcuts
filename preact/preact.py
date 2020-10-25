#!/usr/bin/python3
import os
import sys


def getInput(args):
    """[summary]

        Args:
            args (list[str]): [description]
        Return:
            List of Tuples, which contain the command and their args
    """
    inputs = []
    for word in args:
        if word[0:2] == "--":
            inputs.append((word[2:], []))
        elif word[0:1] == "-":
            inputs.append((word[1:], []))
        else:
            inputs[-1][1].append(word)
    return inputs


class Manager:

    def setName(self, name):
        self.name = name

    def createModule(self):
        wdir = os.path.abspath(os.getcwd())
        fdir = sys.path[0]
        dir = os.path.join(wdir, self.name)
        os.mkdir(dir)
        f = open(os.path.join(dir, "index.tsx"), "w+")
        r = open(os.path.join(fdir, "presets/index.tsx"))
        for line in r:
            uppername = self.name[0].upper() + self.name[1:]
            line = line.replace("Name", uppername)
            line = line.replace("name", self.name)
            f.write(line)
        f.close()
        r.close()
        f = open(os.path.join(dir, "style.css"), "w+")
        f.close()
        f = open(os.path.join(dir, "style.css.d.ts"), "w+")
        r = open(os.path.join(fdir, "presets/style.css.d.ts"))
        for line in r:
            f.write(line)
        f.close()
        r.close()

    def createFile(self):
        wdir = os.path.abspath(os.getcwd())
        fdir = sys.path[0]
        dir = os.path.join(wdir, self.name)
        os.mkdir(dir)
        f = open(os.path.join(dir, "index.tsx"), "w+")
        r = open(os.path.join(fdir, "presets/index.tsx"))
        for line in r:
            uppername = self.name[0].upper() + self.name[1:]
            line = line.replace("name", self.name)
            line = line.replace("Name", uppername)
            f.write(line)
        f.close()
        r.close()

    def createStorybook(self):
        wdir = os.path.abspath(os.getcwd())
        fdir = sys.path[0]
        dir = os.path.join(wdir, self.name)
        f = open(os.path.join(
            dir, "index.stories.tsx"), "w+")
        r = open(os.path.join(fdir, "presets/index.stories.tsx"))
        for line in r:
            uppername = self.name[0].upper() + self.name[1:]
            line = line.replace("name", self.name)
            line = line.replace("Name", uppername)
            f.write(line)
        f.close()
        r.close()


manager = Manager()

commands = {
    "name": (1, manager.setName), "n": (1, manager.setName),
    "module": (0, manager.createModule), "m": (0, manager.createModule),
    "file": (0, manager.createFile), "f": (0, manager.createFile),
    "story": (0, manager.createStorybook), "s": (0, manager.createStorybook)
}

if __name__ == "__main__":
    op = getInput(sys.argv[1:])
    for (cmd, opt) in op:
        nProps, fun = commands[cmd]
        if nProps == len(opt):
            fun(*opt)

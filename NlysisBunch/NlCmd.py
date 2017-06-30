import cmd
import string


class NlCmd(cmd.Cmd):
    FRIENDS = [ 'Alice', 'Adam', 'Barbara', 'Bob' ]
    prompt = 'Nl> '
    intro = "Simple command processor example."

    def __init__(self):
        super(NlCmd, self).__init__()
        
    def do_use(self, module):
        print(module)

    def complete_use(self, text, line, begidx, endidx):
        # dynamically import module list
        if not text:
            completions = []
        else:
            completions = []
        return completions

    def do_greet(self, person):
        if person:
            print("hi, " + person)
        else:
            print("hi")

    def complete_greet(self, text, line, begidx, endidx):
        if not text:
            completions = self.FRIENDS[:]
        else:
            completions = [
                f
                for f in self.FRIENDS
                if f.startswith(text)
            ]
        return completions

    def do_quit(self, line):
        return True

    def postloop(self):
        print()


if __name__ == "__main__":
    nc = NlCmd()
    nc.cmdloop()
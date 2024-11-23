class WordsFinder:
    def __init__(self, file_names):
        self.file_names = file_names
    def get_all_words(self):
        all_words = {}
        l = ''
        punc = [',', '.', '=', '!', '?', ';', ':', ' - ']
        with open(self.file_names, encoding='utf-8') as file:
            for line in file:
                line = line.lower()
                for i in line:
                   if i in punc:
                        line = line.replace(i,'')
                l = l + line
            all_words.update({self.file_names:l.split()})
        return all_words
    def find(self,txt):
        dist = {}
        world = self.get_all_words()[self.file_names]
        for i in range(len(world)):
            if txt.lower() == world[i]:
                dist.update({self.file_names: i+1})
                return dist
    def count(self,txt):
        dist = {}
        n = 1
        world = self.get_all_words()[self.file_names]
        dist.update({self.file_names: world.count(txt.lower())})
        return dist


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))


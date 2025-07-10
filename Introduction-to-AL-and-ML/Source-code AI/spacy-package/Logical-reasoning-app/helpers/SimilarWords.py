class SimilarWords:
    def __init__(self,st,title,model):
        self.st = st
        self.title = title
        self.model = model
        self.words_list = []
        self.score_list = []
        self.word = ''


    def render(self):
        self.st.header(self.title)
        word=self.st.text_input('Enter the Word')
        self.resolve(word)

    def resolve(self,word):
        if self.st.button('Find the Words'):
            try:
                result = self.model.most_similar(word)
                
                #Assign to the Self Object 
                self.word = word
                self.words_list = [w for w,s in result[:5]]
                self.score_list = [s for w,s in result[:5]]

                self.st.success(f'Top 5 Similar Words are:')
                for w,s in result[:5]:
                    self.st.markdown(f' **{w}** ({s:.2f})') 
            except Exception as e:
                self.st.error(f'Error {e}')

    def getWords(self):
        return self.words_list
    
    def getScores(self):
        return self.score_list
    
    def getOriginalWord(self):
        return self.word
    
    def getSt(self):
        return self.st
        
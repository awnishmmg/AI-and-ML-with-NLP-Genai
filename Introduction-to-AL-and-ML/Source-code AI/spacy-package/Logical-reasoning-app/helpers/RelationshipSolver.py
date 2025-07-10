class RelationshipSolver:
    def __init__(self,st,title,model):
        self.st = st
        self.title = title
        self.model = model

    def render(self):
        self.st.header(self.title)
        word_1=self.st.text_input('word 1 (+ve)','king')
        word_2=self.st.text_input('word 2 (+ve)','woman')
        word_3=self.st.text_input('word 3 (-ve)','man')
        self.resolve(word_1,word_2,word_3)

    def resolve(self,word_1,word_2,word_3):
        if self.st.button('Solve'):
            try:
                result = self.model.most_similar(positive=[word_1,word_2],negative=[word_3])
                self.st.success(f'Top Prediction:{result[0][0]}')
            except Exception as e:
                self.st.error(f'Error {e}')
        
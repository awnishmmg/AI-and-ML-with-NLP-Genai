class OddOneOut:
    def __init__(self,st,title,model):
        self.st = st
        self.title = title
        self.model = model

    def render(self):
        self.st.header(self.title)
        words=self.st.text_input('Enter the Words (word 1,word 2,word 3)')
        self.resolve(words)

    def resolve(self,words):
        if self.st.button('Find Odd'):
            try:
                word_list = [word.strip().lower() for word in words.split(',')]
                result = self.model.doesnt_match(word_list)
                self.st.warning(f' The Odd One Out : **{result}** ')
            except Exception as e:
                self.st.error(f'Error {e}')

        
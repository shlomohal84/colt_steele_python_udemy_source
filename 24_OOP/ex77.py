class Comment:
    def __init__(self,username,text,likes = 0):
        self.username = username
        self.text = text
        self.likes = likes
    


comment1 = Comment("Pussifism", "HAHAHAHA")

print(comment1.text)
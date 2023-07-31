class Comment:
    def __init__(self,username,text,likes = 124):
        self.username = username
        self.text = text
        self.likes = likes
    


comment1 = Comment("Pussifism", "HAHAHAHA")

print(f"{comment1.username}: {comment1.text} ({comment1.likes})")
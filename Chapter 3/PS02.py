name = input("Enter your name: ")

letter = '''
            Dear <|Name|>,
            You are selected!
            <|Date|>
         '''
print(letter.replace("<|Name|>", name).replace("<|Date|>","20 May"))

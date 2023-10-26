import releword as rw
import model
intents, predicts = model.model("text.txt", "model.txt")
for i in range(len(intents)):
    print(f"{rw.find_phrases(intents[i])} - {predicts[i].strip()}")




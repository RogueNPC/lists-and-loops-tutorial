#Q1
songs = ["ROCKSTAR", "Do It", "For The Night"]

#Q2
print(songs[0])
print(songs[2])
print(songs[1:])

#Q3
songs[2] = "Army of Two"
print(songs)

#Q4
songs.extend (["Message in the Wind", "Threads", "Not Afraid"])
del songs[1]
print(songs)

#Q6
animals = ["Sea Turtle", "Komodo Dragon", "Black Bear"]
animals.append("Green Aracari")
print(animals[2])
del animals[0]
for i in range(len(animals)):
    print(animals[i])
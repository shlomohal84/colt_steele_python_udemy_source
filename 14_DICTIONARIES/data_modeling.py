playlist = {
    "title": "Patagonia Bus",
    "author": "Colt Steele",
    "songs": [
        {
            "id": 0,
            "title": "Turn It Off",
            "artist": [
                "Culture Abuse",
            ],
            "album":"Peach",
            "duration":2.5,
        },
        {
            "id": 1,
            "title": "Eating Hooks",
            "artist": [
                "Moderat",
                "Siriusmo",
                "solomun"
            ],
            "album":"Eating Hooks",
            "duration":5.25,

        },
    ],
}
# print(playlist)

total_length = 0
for song in playlist['songs']:
    total_length += song["duration"]

print(total_length)

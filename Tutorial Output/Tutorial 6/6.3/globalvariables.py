messageID = 2

myStart = 0

countToMaxLength = 0

durationCounter = 0

message1 = [[10,10,17,10,17,10,17,17,17,10,10,17,10,10,10,10],
            [10,10,17,10,17,10,17,10,10,10,17,10,17,10,10,10],
            [10,10,17,10,17,10,17,10,10,10,17,10,17,10,10,10],
            [10,10,17,10,17,10,17,10,10,10,17,10,17,10,10,10],
            [10,10,17,10,17,10,17,17,17,10,17,17,17,10,10,10],
            [10,10,17,10,17,10,10,10,17,10,17,10,17,10,10,10],
            [10,10,17,10,17,10,10,10,17,10,17,10,17,10,10,10],
            [10,10,10,17,10,10,17,17,17,10,17,10,17,10,10,10]]


message2 = [[10,10,12,10,12,10,12,12,12,10,12,10,10,10,10,12,12,10,10,12,10,10,12,10,12,10,12,12,12,10,10,10,10,10,10],
            [10,10,12,10,12,10,12,10,10,10,12,10,10,10,12,10,10,10,12,10,12,10,12,12,12,10,12,10,10,10,10,10,10,10,10],
            [10,10,12,10,12,10,12,10,10,10,12,10,10,10,12,10,10,10,12,10,12,10,12,10,12,10,12,10,10,10,10,10,10,10,10],
            [10,10,12,10,12,10,12,12,10,10,12,10,10,10,12,10,10,10,12,10,12,10,12,10,12,10,12,12,10,10,10,10,10,10,10],
            [10,10,12,10,12,10,12,12,10,10,12,10,10,10,12,10,10,10,12,10,12,10,12,10,12,10,12,12,10,10,10,10,10,10,10],
            [10,10,12,10,12,10,12,10,10,10,12,10,10,10,12,10,10,10,12,10,12,10,12,10,12,10,12,10,10,10,10,10,10,10,10],
            [10,10,12,12,12,10,12,10,10,10,12,10,10,10,12,10,10,10,12,10,12,10,12,10,12,10,12,10,10,10,10,10,10,10,10],
            [10,10,12,10,12,10,12,12,12,10,12,12,12,10,10,12,12,10,10,12,10,10,12,10,12,10,12,12,12,10,10,10,10,10,10]]


message3 = [[10,10,14,10,10,10,10,10,10,10,10,10,10,10,10,10],
            [10,10,10,14,10,10,10,10,10,10,10,10,10,10,10,10],
            [10,10,10,10,14,10,10,10,10,10,10,10,10,10,10,10],
            [10,10,10,10,10,14,10,10,10,10,10,10,10,10,10,10],
            [10,10,10,10,10,10,14,10,10,10,10,10,10,10,10,10],
            [10,10,10,10,10,10,10,14,10,10,10,10,10,10,10,10],
            [10,10,10,10,10,10,10,10,14,10,10,10,10,10,10,10],
            [10,10,10,10,10,10,10,10,10,14,10,10,10,10,10,10],
            [10,10,10,10,10,10,10,10,10,10,14,10,10,10,10,10],
            [10,10,10,10,10,10,10,10,10,10,10,14,10,10,10,10],
            [10,10,10,10,10,10,10,10,10,10,10,10,14,10,10,10],
            [10,10,10,10,10,10,10,10,10,10,10,10,10,14,10,10],
            [10,10,10,10,10,10,10,10,10,10,10,10,10,10,14,10],
            [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,14],
            [10,10,10,10,10,10,10,10,10,10,10,10,10,10,14,10],
            [10,10,10,10,10,10,10,10,10,10,10,10,10,14,10,10],
            [10,10,10,10,10,10,10,10,10,10,10,10,14,10,10,10],
            [10,10,10,10,10,10,10,10,10,10,10,14,10,10,10,10],
            [10,10,10,10,10,10,10,10,10,10,14,10,10,10,10,10],
            [10,10,10,10,10,10,10,10,10,14,10,10,10,10,10,10],
            [10,10,10,10,10,10,10,10,14,10,10,10,10,10,10,10],
            [10,10,10,10,10,10,10,14,10,10,10,10,10,10,10,10],
            [10,10,10,10,10,10,14,10,10,10,10,10,10,10,10,10],
            [10,10,10,10,10,14,10,10,10,10,10,10,10,10,10,10],
            [10,10,10,10,14,10,10,10,10,10,10,10,10,10,10,10],
            [10,10,10,14,10,10,10,10,10,10,10,10,10,10,10,10]]



message4 = [[10,10,15,10,10,10,10,10,10,10,10,10,10,10,10,10],
            [10,10,15,10,10,10,10,10,10,10,10,10,10,10,10,10],
            [10,10,10,10,15,10,10,10,10,10,10,15,10,10,10,10],
            [10,10,10,15,15,10,10,10,10,10,10,15,10,10,10,10],
            [10,10,10,15,10,10,15,10,10,10,10,15,10,10,10,10],
            [10,10,10,15,10,10,10,10,10,15,10,15,10,10,10,10],
            [10,10,10,10,10,10,10,10,10,15,10,10,10,10,10,10],
            [10,10,10,10,10,10,10,10,10,15,10,10,10,10,10,10],
            [10,10,10,10,10,10,10,10,10,10,10,10,10,15,10,10],
            [10,10,10,10,10,10,10,15,10,10,10,15,10,10,10,10],
            [10,10,15,10,10,10,10,15,10,10,10,15,10,15,10,10],
            [10,10,15,10,10,10,15,10,10,10,10,10,10,15,10,10],
            [10,10,15,10,10,10,10,10,10,10,10,10,15,10,10,10],
            [10,10,15,10,10,15,10,15,10,10,10,10,15,10,10,15],
            [10,10,10,10,10,10,10,10,10,10,10,10,15,10,15,15],
            [10,10,10,10,10,15,10,10,10,10,10,10,10,10,10,15],
            [10,10,10,10,10,15,10,10,10,10,10,10,10,10,15,10],
            [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,15],
            [10,10,10,10,10,10,15,10,10,10,15,10,10,10,10,10],
            [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],
            [10,10,10,10,15,10,15,10,15,10,10,10,15,10,10,10],
            [10,10,10,10,15,10,15,10,10,10,10,10,15,10,10,10],
            [10,10,10,10,15,10,15,10,15,10,10,10,15,10,10,10],
            [10,10,10,10,10,10,10,10,15,10,10,10,10,10,10,10],
            [10,10,10,15,10,10,10,10,10,10,10,10,10,10,10,10],
            [10,10,15,15,10,10,10,10,10,10,10,10,10,10,10,10]]
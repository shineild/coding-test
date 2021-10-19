hambuger = []
for i in range(3):
    hambuger.append(int(input()))
hambuger.sort()
juce = []
for i in range(2):
    juce.append(int(input()))
juce.sort()
print(hambuger[0] + juce[0] - 50)

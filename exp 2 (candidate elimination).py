import csv

# Create training data
data = [
    ["Sky", "AirTemp", "Humidity", "Wind", "Water", "Forecast", "EnjoySport"],
    ["Sunny", "Warm", "Normal", "Strong", "Warm", "Same", "Yes"],
    ["Sunny", "Warm", "High", "Strong", "Warm", "Same", "Yes"],
    ["Rainy", "Cold", "High", "Strong", "Warm", "Change", "No"],
    ["Sunny", "Warm", "High", "Strong", "Cool", "Change", "Yes"]
]

# Save data into CSV file
with open("trainingdata.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

# Read CSV file
with open("trainingdata.csv", "r") as file:
    rows = list(csv.reader(file))

# Remove header
data = rows[1:]

# Number of attributes
n = len(data[0]) - 1

# Initial hypotheses
S = ["0"] * n
G = [["?"] * n]

# Candidate Elimination
for row in data:
    x = row[:-1]
    label = row[-1]

    if label == "Yes":

        # Generalize S
        for i in range(n):
            if S[i] == "0":
                S[i] = x[i]
            elif S[i] != x[i]:
                S[i] = "?"

    elif label == "No":

        # Specialize G
        new_G = []

        for g in G:
            for i in range(n):
                if g[i] == "?":
                    if S[i] != x[i]:
                        h = g.copy()
                        h[i] = S[i]
                        new_G.append(h)

        G = new_G

print("Final Specific Hypothesis (S):")
print(S)

print("\nFinal General Hypotheses (G):")
for g in G:
    print(g)
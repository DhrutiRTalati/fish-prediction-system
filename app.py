from flask import Flask, render_template
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

# load dataset
df = pd.read_csv("Fish.csv")
df = df[df['Weight'] > 0]

# ---------------- HOME PAGE ----------------
@app.route("/")
def home():
    species_list = df["Species"].unique()
    return render_template("index.html", fishes=species_list)

# ---------------- FISH DETAIL PAGE ----------------
@app.route("/fish/<name>")
def fish_detail(name):
    fish_data = df[df["Species"] == name].copy()

    # simulate location & time
    fish_data["Location"] = np.random.choice(["Coastal", "Deep Sea", "River"], size=len(fish_data))
    fish_data["Time"] = np.random.choice(["Morning", "Afternoon", "Evening"], size=len(fish_data))

    # best values
    best_location = fish_data.groupby("Location")["Weight"].mean().idxmax()
    best_time = fish_data.groupby("Time")["Weight"].mean().idxmax()

    # create static folder if not exists
    if not os.path.exists("static"):
        os.makedirs("static")

    # 📊 CREATE GRAPH FOR THIS FISH
    plt.figure()
    fish_data.groupby("Location")["Weight"].mean().plot(kind='bar')
    plt.title(f"{name} - Avg Weight by Location")
    plt.savefig(f"static/{name}.png")
    plt.close()

    return render_template("fish.html",
                           fish=name,
                           location=best_location,
                           time=best_time,
                           graph=f"{name}.png")

# ---------------- RUN APP ----------------
if __name__ == "__main__":
    app.run(debug=True)
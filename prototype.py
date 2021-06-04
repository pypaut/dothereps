#!/usr/bin/python3

import time


workouts = {
    "upperbody" : {
        "nb_sets" : 3,
        "rest_time" : 3,
        "exercises" : [
            "L-PULL UPS, PIKE PUSH UPS",
            "L-ROWS, HANDSTAND HOLDS",
        ],
    },

    "legs" : {
        "nb_sets" : 3,
        "rest_time" : 3,
        "exercises" : [
            "PISTOLS + 20kg",
            "CALVES + 20kg",
            "INDIVIDUAL LEG RAISES",
        ]
    },

    "abs" : {
        "nb_sets" : 3,
        "rest_time" : 3,
        "exercises" : [
            "STANDING AB WHEEL",
            "ADVANCED PLANCK",
            "OBLIQUES + 10kg",
        ]
    }
}


def main():
    """
    main function
    """
    workout = workouts[input("Workout? > ").lower()]
    for ex in workout["exercises"]:
        for current_set in range(workout["nb_sets"]):
            print(f"{ex}, SET {current_set + 1}. LET'S GO!")
            while input("Press RETURN when done") != "":
                continue
            print("Rest now")
            time.sleep(workout["rest_time"])


if __name__ == "__main__":
    main()

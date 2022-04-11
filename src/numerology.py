import math
import re

def number_to_numerology(number: int) -> [str, str]:
    lookup = {
        10: ["🎳", "Bowler Donation"],
        1010: ["🎳🎳", "2x Bowler Donation"],
    	101010: ["🎳🎳🎳🦃🔥🔥🔥", "3x Bowler Donation - Turkey!"],
    	10101010: ["🎳🎳🎳🎳🦃🦃🔥🔥🔥", "4x Bowler Donation - 2x Turkey!"],
    	1010101010: ["🎳🎳🎳🎳🎳🦃🦃🦃🔥🔥🔥", "5x Bowler Donation - 3x Turkey!"],

        6006: ["🎱🎱", "Skinny Boobs Donation"],
        6008: ["🎱🎱", "Right-Heavy Boobs Donation"],
        8006: ["🎱🎱", "Left-Heavy Boobs Donation"],
        8008: ["🎱🎱", "Boobs Donation"],

        2: ["🦆💩", ""],
        22: ["🦆🦆", "Ducks In-A-Row Donation"],
        222: ["🦆🦆🦆", "3x Ducks In-A-Row Donation"],
        2222: ["🦆🦆🦆🦆", "4x Ducks In-A-Row Donation"],
        22222: ["🦆🦆🦆🦆🦆🔥", "5x Ducks In-A-Row Donation"],
        222222: ["🦆🦆🦆🦆🦆🦆🔥🔥🔥", "6x Ducks In-A-Row Donation"],
        2222222: ["🦆🦆🦆🦆🦆🦆🦆🔥🔥🔥", "7x Ducks In-A-Row Donation"],

        11: ["🎲", "Dice Donation"],
        1111: ["🎲🎲", "Dice Donation"],
        111111: ["🎲🎲🎲🔥🔥🔥", "Dice Donation"],

        21: ["🪙", "Bitcoin Donation"],
        2121: ["🪙🪙", "Bitcoin Donation"],
        212121: ["🪙🪙🪙🔥🔥🔥", "Bitcoin Donation"],

        33: ["✨", "Magic Number Donation"],
        333: ["✨", "Magic Number Donation"],
        3333: ["✨✨", "Magic Number Donation"],
        33333: ["✨✨🔥", "Magic Number Donation"],
        69: ["💋", "Swasslenuff Donation"],
        6969: ["💋💋", "Swasslenuff Donation"],
        696969: ["💋💋💋🔥🔥🔥", "Swasslenuff Donation"],

        73: ["👋", "Greetings Donation"],
        7373: ["👋👋", "Greetings Donation"],
        737373: ["👋👋👋🔥🔥🔥", "Greetings Donation"],

        88: ["🥰", "Love and Kisses Donation"],
        8888: ["🥰🥰", "Love and Kisses Donation"],
        888888: ["🥰🥰🥰🔥🔥🔥", "Love and Kisses Donation"],

        420: ["✌👽💨", "Stoner Donation"],
        420420: ["✌👽💨✌👽💨🔥🔥🔥", "Stoner Donation"],

        666: ["😈", "Devil Donation"],
        666666: ["😈😈🔥🔥🔥", "Devil Donation"],

        1776: ["🇺🇸", "America Fuck Yeah Donation"],

        1867: ["🇨🇦", "Canada Skookum as Frig Donation"],

        9653: ["🐺", "Wolf Donation"],

        314: ["🥧", "Pi Donation"],
        3141: ["🥧🥧", "2x Pi Donation"],
        31415: ["🥧🥧🥧🔥", "3x Pi Donation"],
        314159: ["🥧🥧🥧🥧🔥🔥🔥", "4x Pi Donation"],
        3141592: ["🥧🥧🥧🥧🥧🔥🔥🔥", "5x Pi Donation"],
        314314: ["🥧🥧🔥🔥🔥", "Triple-Lit 2x Pi Donation"],
        1314: ["🥧", "Pi Donation"],
        3142: ["🥧", "Pi Donation"],

        321: ["💥", "Countdown Donation"],
        4321: ["💥💥", "2x Countdown Donation"],
        54321: ["💥💥💥🔥🔥", "3x Countdown Donation"],
        654321: ["💥💥💥💥🔥🔥🔥", "4x Countdown Donation"],
        7654321: ["💥💥💥💥💥🔥🔥🔥", "5x Countdown Donation"],
        87654321: ["💥💥💥💥💥💥🔥🔥🔥", "6x Countdown Donation"],
        987654321: ["💥💥💥💥💥💥💥🔥🔥🔥", "7x Countdown Donation"],

        2169: ["🪙💋", "Bitcoin Swasslenuff Donation"],
        6921: ["💋🪙", "Swasslenuff Bitcoin Donation"],
        3369: ["✨💋", "Magic Kiss Donation"],
        6933: ["💋✨", "Kiss Magic Donation"],
        1021: ["🎳🪙", "Bowling Bitcoin Donation"],
        1011: ["🎳🎲", "Lucky Strike Donation"],
        2110: ["🪙🎳", "Bitcoin Bowling Donation"],
        1069: ["🎳💋", "Blessed Balls Donation"],
        6910: ["💋🎳", "Extra-Blessed Balls Donation"],
        7388: ["👋🥰", "Blowing Kisses Donation"],
        8873: ["🥰👋", "Blowing Kisses Donation"],
        31433: ["🥧✨🔥", "Lit Magic Pi Donation"],
        69314: ["💋🥧🔥🔥", "Cherry Pi Lipstick Donation"],
        10321: ["🎳💥🔥", "Strike Donation"],
        32121: ["💥🪙🔥", "Buy the Dip Donation"]
    }

    try:
        return lookup[number]
    except KeyError:
        return ["", ""]
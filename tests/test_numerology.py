import pytest

from src.numerology import number_to_numerology


def test_bowler_donations():
    assert number_to_numerology(10) == ["🎳", "Bowler Donation"]
    assert number_to_numerology(1010) == ["🎳🎳", "2x Bowler Donation"]
    assert number_to_numerology(101010) == ["🎳🎳🎳🦃🔥🔥🔥", "3x Bowler Donation - Turkey!"]
    assert number_to_numerology(10101010) == ["🎳🎳🎳🎳🦃🦃🔥🔥🔥", "4x Bowler Donation - 2x Turkey!"]
    assert number_to_numerology(1010101010) == ["🎳🎳🎳🎳🎳🦃🦃🦃🔥🔥🔥", "5x Bowler Donation - 3x Turkey!"]

def test_boobs_donations():
    assert number_to_numerology(6006) == ["🎱🎱", "Skinny Boobs Donation"]
    assert number_to_numerology(6008) == ["🎱🎱", "Right-Heavy Boobs Donation"]
    assert number_to_numerology(8006) == ["🎱🎱", "Left-Heavy Boobs Donation"]
    assert number_to_numerology(8008) == ["🎱🎱", "Boobs Donation"]

def test_ducksinarow_donations():
    assert number_to_numerology(2) == ["🦆💩", ""]
    assert number_to_numerology(22) == ["🦆🦆", "Ducks In-A-Row Donation"]
    assert number_to_numerology(222) == ["🦆🦆🦆", "3x Ducks In-A-Row Donation"]
    assert number_to_numerology(2222) == ["🦆🦆🦆🦆", "4x Ducks In-A-Row Donation"]
    assert number_to_numerology(22222) == ["🦆🦆🦆🦆🦆🔥", "5x Ducks In-A-Row Donation"]
    assert number_to_numerology(222222) == ["🦆🦆🦆🦆🦆🦆🔥🔥🔥", "6x Ducks In-A-Row Donation"]
    assert number_to_numerology(2222222) == ["🦆🦆🦆🦆🦆🦆🦆🔥🔥🔥", "7x Ducks In-A-Row Donation"]

def test_dice_donations():
    assert number_to_numerology(11) == ["🎲", "Dice Donation"]
    assert number_to_numerology(1111) == ["🎲🎲", "Dice Donation"]
    assert number_to_numerology(111111) == ["🎲🎲🎲🔥🔥🔥", "Dice Donation"]

def test_bitcoin_donations():
    assert number_to_numerology(21) == ["🪙", "Bitcoin Donation"]
    assert number_to_numerology(2121) == ["🪙🪙", "Bitcoin Donation"]
    assert number_to_numerology(212121) == ["🪙🪙🪙🔥🔥🔥", "Bitcoin Donation"]

def test_magicnumber_donations():
    assert number_to_numerology(33) == ["✨", "Magic Number Donation"]
    assert number_to_numerology(333) == ["✨", "Magic Number Donation"]
    assert number_to_numerology(3333) == ["✨✨", "Magic Number Donation"]
    assert number_to_numerology(33333) == ["✨✨🔥", "Magic Number Donation"]

def test_swasslenuff_donations():
    assert number_to_numerology(69) == ["💋", "Swasslenuff Donation"]
    assert number_to_numerology(6969) == ["💋💋", "Swasslenuff Donation"]
    assert number_to_numerology(696969) == ["💋💋💋🔥🔥🔥", "Swasslenuff Donation"]

def test_greetings_donations():
    assert number_to_numerology(73) == ["👋", "Greetings Donation"]
    assert number_to_numerology(7373) == ["👋👋", "Greetings Donation"]
    assert number_to_numerology(737373) == ["👋👋👋🔥🔥🔥", "Greetings Donation"]

def test_love_and_kisses_donations():
    assert number_to_numerology(88) == ["🥰", "Love and Kisses Donation"]
    assert number_to_numerology(8888) == ["🥰🥰", "Love and Kisses Donation"]
    assert number_to_numerology(888888) == ["🥰🥰🥰🔥🔥🔥", "Love and Kisses Donation"]

def test_stoner_donations():
    assert number_to_numerology(420) == ["✌👽💨", "Stoner Donation"]
    assert number_to_numerology(420420) == ["✌👽💨✌👽💨🔥🔥🔥", "Stoner Donation"]

def test_devil_donations():
    assert number_to_numerology(666) == ["😈", "Devil Donation"]
    assert number_to_numerology(666666) == ["😈😈🔥🔥🔥", "Devil Donation"]

def test_america_donations():
    assert number_to_numerology(1776) == ["🇺🇸", "America Fuck Yeah Donation"]

def test_canada_donations():
    assert number_to_numerology(1867) == ["🇨🇦", "Canada Skookum as Frig Donation"]

def test_wolf_donations():
    assert number_to_numerology(9653) == ["🐺", "Wolf Donation"]

def test_pi_donations():
    assert number_to_numerology(314) == ["🥧", "Pi Donation"]
    assert number_to_numerology(3141) == ["🥧🥧", "2x Pi Donation"]
    assert number_to_numerology(31415) == ["🥧🥧🥧🔥", "3x Pi Donation"]
    assert number_to_numerology(314159) == ["🥧🥧🥧🥧🔥🔥🔥", "4x Pi Donation"]
    assert number_to_numerology(3141592) == ["🥧🥧🥧🥧🥧🔥🔥🔥", "5x Pi Donation"]
    assert number_to_numerology(314314) == ["🥧🥧🔥🔥🔥", "Triple-Lit 2x Pi Donation"]
    assert number_to_numerology(1314) == ["🥧", "Pi Donation"]
    assert number_to_numerology(3142) == ["🥧", "Pi Donation"]


def test_countdown_donations():
    assert number_to_numerology(321) == ["💥", "Countdown Donation"]
    assert number_to_numerology(4321) == ["💥💥", "2x Countdown Donation"]
    assert number_to_numerology(54321) == ["💥💥💥🔥🔥", "3x Countdown Donation"]
    assert number_to_numerology(654321) == ["💥💥💥💥🔥🔥🔥", "4x Countdown Donation"]
    assert number_to_numerology(7654321) == ["💥💥💥💥💥🔥🔥🔥", "5x Countdown Donation"]
    assert number_to_numerology(87654321) == ["💥💥💥💥💥💥🔥🔥🔥", "6x Countdown Donation"]
    assert number_to_numerology(987654321) == ["💥💥💥💥💥💥💥🔥🔥🔥", "7x Countdown Donation"]


def test_combinations():
	assert number_to_numerology(2169) == ["🪙💋", "Bitcoin Swasslenuff Donation"]
	assert number_to_numerology(6921) == ["💋🪙", "Swasslenuff Bitcoin Donation"]
	assert number_to_numerology(3369) == ["✨💋", "Magic Kiss Donation"]
	assert number_to_numerology(6933) == ["💋✨", "Kiss Magic Donation"]
	assert number_to_numerology(1021) == ["🎳🪙", "Bowling Bitcoin Donation"]
	assert number_to_numerology(1011) == ["🎳🎲", "Lucky Strike Donation"]
	assert number_to_numerology(2110) == ["🪙🎳", "Bitcoin Bowling Donation"]
	assert number_to_numerology(1069) == ["🎳💋", "Blessed Balls Donation"]
	assert number_to_numerology(6910) == ["💋🎳", "Extra-Blessed Balls Donation"]
	assert number_to_numerology(7388) == ["👋🥰", "Blowing Kisses Donation"]
	assert number_to_numerology(8873) == ["🥰👋", "Blowing Kisses Donation"]
	assert number_to_numerology(31433) == ["🥧✨🔥", "Lit Magic Pi Donation"]
	assert number_to_numerology(69314) == ["💋🥧🔥🔥", "Cherry Pi Lipstick Donation"]
	assert number_to_numerology(10321) == ["🎳💥🔥", "Strike Donation"]
	assert number_to_numerology(32121) == ["💥🪙🔥", "Buy the Dip Donation"]

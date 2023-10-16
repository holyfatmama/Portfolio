-- Keep a log of any SQL queries you execute as you solve the mystery.
SELECT * FROM crime_scene_reports WHERE month = '7' AND day = '28' AND street = 'Humphrey Street';

time of crime: 1015am

id of crime scene report = 295

SELECT * FROM interviews WHERE month = '7' AND day = '28';
id 161, RUTH
id 162, EUgene
id 163, Lily

| 161 | Ruth    | 2021 | 7     | 28  | Sometime within ten minutes of the theft, I saw the thief get into a car in the bakery parking lot and drive away. If you have security footage from the bakery parking lot, you might want to look for cars that left the parking lot in that time frame.                                                          |
| 162 | Eugene  | 2021 | 7     | 28  | I don't know the thief's name, but it was someone I recognized. Earlier this morning, before I arrived at Emma's bakery, I was walking by the ATM on Leggett Street and saw the thief there withdrawing some money.                                                                                                 |
| 163 | Raymond | 2021 | 7     | 28  | As the thief was leaving the bakery, they called someone who talked to them for less than a minute. In the call, I heard the thief say that they were planning to take the earliest flight out of Fiftyville tomorrow. The thief then asked the person on the other end of the phone to purchase the flight ticket. |

Car, parking lot, exit by 1025am, 28 July

161 Ruth
SELECT * FROM bakery_security_logs WHERE month = '7' AND day = '28' AND hour = '10' AND activity = 'exit' AND minute <= '25';

162 Eugene
ATM, Leggett Street, withdraw
SELECT * FROM atm_transactions WHERE month = '7' AND day = '28' AND atm_location = 'Leggett Street' And transaction_type = 'withdraw';
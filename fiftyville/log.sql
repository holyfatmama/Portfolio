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
possible list of suspects for car
SELECT * FROM bakery_security_logs WHERE month = '7' AND day = '28' AND hour = '10' AND activity = 'exit' AND minute <= '25';

162 Eugene
ATM, Leggett Street, withdraw
possible suspects for withdrawal
SELECT * FROM atm_transactions WHERE month = '7' AND day = '28' AND atm_location = 'Leggett Street' And transaction_type = 'withdraw';

163 Raymond
call, less than minute, thief take earliest flight out of fiftyville the day after (29 July), ticket bought

possible suspects for call
SELECT * FROM phone_calls WHERE month = '7' AND day = '28' AND duration <= '60' ORDER BY duration ASC;

fiftyville airport id = 8
destination = airport id 4 = LaGuardia Airport, New York City, flight id = 36

possible suspects for flight
SELECT * FROM passengers WHERE flight_id = 36;

suspect list from car
SELECT * FROM people WHERE license_plate IN (SELECT license_plate FROM bakery_security_logs WHERE month = '7' AND day = '28' AND hour = '10' AND activity = 'exit' AND minute <= '25');

suspect list from call
SELECT * FROM people WHERE phone_number IN (SELECT caller FROM phone_calls WHERE month = '7' AND day = '28' AND duration <= '60' ORDER BY duration ASC);

suspect list from flight
SELECT * FROM people WHERE passport_number IN (SELECT passport_number FROM passengers WHERE flight_id = 36);
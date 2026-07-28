# FastF1-Telemetry-Analysis-Tool

Built using FastF1 (MIT License): https://github.com/theOehrly/Fast-F1

Python function that allows users to visualise the differences in driver inputs during F1 practice, qualifying and race sessions. This function utilises data provided from the FastF1 API displaying these overlaid traces: speed, throttle, brake, gear, time delta

This function is currently limited to two drivers for analysis; in practice, any more than 2 would be messy and difficult to comprehend.



A note on how the function should be used; the inputs should be treated like so:
       
the 'year' variable is simply an integer, and so it should be input like so:
       
-> 'year = 2025' or 'year = 2019' 
       
The same can be said about the 'round_number' variable, it too is an integer and
should be treated the same way:
       
-> 'round_number = 5' or 'round_number = 8'

The 'session' variable is a string. It should be used like so:

-> 'session_name = "Q"' or 'session_name = "R"' 
       
The drivers variable is slightly different, this is a list that requires strings
for exactly two drivers. The three letter all caps initials used in the F1 broadcast 
should be used here, like so:
       
-> 'drivers = ["VER", "HAM"]' or 'drivers = ["RUS", "NOR"]'



A few examples for usage of the function and its outputs:

calling of the function with its required inputs:

-> telemetry_data = fastf1_telemetry_analysis(2026, 6, "Q", ["ANT", "VER"])

This would then produce this graph:

<img width="1920" height="967" alt="VerAnt" src="https://github.com/user-attachments/assets/98ef2580-6437-459b-b133-6db34d27941e" />

another calling:

-> telemetry_data = fastf1_telemetry_analysis(2026, 11, "Q", ["NOR", "HAM"])

Producing this graph

<img width="1920" height="967" alt="NorHam" src="https://github.com/user-attachments/assets/fae05579-48fe-464f-9c6e-db69e783b957" />

This tool uses the FastF1 library to access Formula 1 timing and telemetry data. This project is unofficial and not affiliated with Formula 1, FOM, or the FIA. F1, FORMULA ONE, and related marks are trademarks of Formula One Licensing B.V. Telemetry data is fetched live at runtime and is not redistributed as part of this repository.




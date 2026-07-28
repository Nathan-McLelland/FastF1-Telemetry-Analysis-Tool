# FastF1-Telemetry-Analysis-Tool

Built using FastF1 (MIT License): https://github.com/theOehrly/Fast-F1

Python function that allows users to visualise the differences in driver inputs during F1 practice, qualifying and race sessions. This function utilises data provided from the FastF1 API displaying these overlaid traces: speed, throttle, brake, gear, time delta

## Aim of the project

This function is currently limited to two drivers for analysis; in practice, any more than 2 would be messy and difficult to comprehend. It allows those who are interested in lap time data to look at a reduced set of channels which paint a pretty general picture about differences in driver style or car setup differences downforce, deployment etc.

## Current developments and potential future scope

Currently, I am working on implementing a GG-plot feature, which allows users to visualise the approximate friction envelope for each car to make clearer and more data-informed comments about differences in the car.

Unfortunately, current attempts at a GG-plot feature haven't worked as expected and produced unphysical results.

## Example prompts, and how to use the function

### **year** variable
       
the `year` variable is an integer, and so it should be input like so:

```python       
year = 2025
```
### **round_number** variable

The same can be said about the `round_number` variable:

```python
round_number = 5
```

*Future versions of this tool may look at switching from round number to `event name`, this however is* **not the case**.

### **session** variable

The `session` variable is a string:

```python
session_name = "Q"
```

*Note here, that you are not restricted to "Q", "FP1", etc. you can input "Qualifying", "Race", etc.*

### **drivers** variable

The `drivers` variable is slightly different, this is a list that requires strings
for exactly two drivers. The three letter all caps initials used in the F1 broadcast 
should be used here:
       
```python
drivers = ["VER", "HAM"]
```

### Example usage and outputs

An example of calling of the function with its required inputs:

```python
telemetry_data = fastf1_telemetry_analysis(2026, 6, "Q", ["ANT", "VER"])
```

This would then produce this graph:

<img width="1920" height="967" alt="VerAnt" src="https://github.com/user-attachments/assets/98ef2580-6437-459b-b133-6db34d27941e" />

another calling:

```python
telemetry_data = fastf1_telemetry_analysis(2026, 11, "Q", ["NOR", "HAM"])
```

Producing this graph

<img width="1920" height="967" alt="NorHam" src="https://github.com/user-attachments/assets/fae05579-48fe-464f-9c6e-db69e783b957" />

## IMPORTANT INFO

This tool uses the FastF1 library to access Formula 1 timing and telemetry data. This project is unofficial and not affiliated with Formula 1, FOM, or the FIA. F1, FORMULA ONE, and related marks are trademarks of Formula One Licensing B.V. Telemetry data is fetched live at runtime and is not redistributed as part of this repository.




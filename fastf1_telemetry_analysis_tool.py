def fastf1_telemetry_analysis(year: int, round_number: int, session_name: str, drivers: list):
    
    import fastf1.plotting
    import matplotlib.pyplot as plt

    session = fastf1.get_session(year, round_number, session_name)
    session.load()

    laps = session.laps

    data_list = []

    for driver in drivers:

        driver_fastest_lap = laps.pick_drivers(driver).pick_fastest()

        if driver_fastest_lap.empty:

            raise ValueError(f"{driver} does not have a valid lap for this session")

        driver_telemetry   = driver_fastest_lap.get_car_data().add_distance()
        driver_colour      = fastf1.plotting.get_driver_color(driver, session)

        data_list.append({

            "Driver Fastest Lap": driver_fastest_lap,
            "Driver Telemetry": driver_telemetry,
            "Driver Colour": driver_colour,
            "Tire Compound": driver_fastest_lap["Compound"]

        })

    time_delta, driver1_telemetry, driver2_telemetry = fastf1.utils.delta_time(data_list[0]["Driver Fastest Lap"], data_list[1]["Driver Fastest Lap"])

    track_info = session.get_circuit_info()

    fig, ax = plt.subplots(5, 1, figsize = (15, 10), sharex = True, gridspec_kw = {"height_ratios" : [2, 1, 1, 1, 1]})

    ax[0].plot(data_list[0]["Driver Telemetry"]["Distance"], data_list[0]["Driver Telemetry"]["Speed"], color = data_list[0]["Driver Colour"],
               label = f"{drivers[0]}: {data_list[0]["Tire Compound"]}, {data_list[0]["Driver Fastest Lap"]["LapTime"].total_seconds()}s")
    ax[0].plot(data_list[1]["Driver Telemetry"]["Distance"], data_list[1]["Driver Telemetry"]["Speed"], color = data_list[1]["Driver Colour"],
               label = f"{drivers[1]}: {data_list[1]["Tire Compound"]}, {data_list[1]["Driver Fastest Lap"]["LapTime"].total_seconds()}s")

    ax[0].set_xlabel("Distance [m]")
    ax[0].set_ylabel("Speed [km/h]")

    ax[0].legend()

    ax[1].plot(data_list[0]["Driver Telemetry"]["Distance"], data_list[0]["Driver Telemetry"]["Throttle"], color = data_list[0]["Driver Colour"])
    ax[1].plot(data_list[1]["Driver Telemetry"]["Distance"], data_list[1]["Driver Telemetry"]["Throttle"], color = data_list[1]["Driver Colour"])

    ax[1].set_ylabel("Throttle Position [%]")

    ax[2].plot(data_list[0]["Driver Telemetry"]["Distance"], data_list[0]["Driver Telemetry"]["Brake"], color = data_list[0]["Driver Colour"])
    ax[2].plot(data_list[1]["Driver Telemetry"]["Distance"], data_list[1]["Driver Telemetry"]["Brake"], color = data_list[1]["Driver Colour"])

    ax[2].set_ylabel("Brake - Boolean Value")

    ax[3].plot(data_list[0]["Driver Telemetry"]["Distance"], data_list[0]["Driver Telemetry"]["nGear"], color = data_list[0]["Driver Colour"])
    ax[3].plot(data_list[1]["Driver Telemetry"]["Distance"], data_list[1]["Driver Telemetry"]["nGear"], color = data_list[1]["Driver Colour"])

    ax[3].set_ylabel("Gear")

    ax[4].plot(driver1_telemetry["Distance"], time_delta, color = "green")

    ax[4].set_ylabel("Time Delta [s]")

    ax[0].vlines(track_info.corners["Distance"], 0, 360, colors = "rebeccapurple", linestyles = "--")

    for distance, number in zip(track_info.corners["Distance"], track_info.corners["Number"]):

        ax[0].text(distance, 390, f"T{number}", color = "black", verticalalignment = "bottom", horizontalalignment = "center", fontsize = 8)

    plt.suptitle(f"Fastest Lap Comparison \n {session.event["EventName"]}")

    plt.tight_layout()

    for a in ax:

        a.grid(True)

    plt.show()

    return data_list
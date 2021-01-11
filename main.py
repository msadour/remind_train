from constants import NAME_OF_WORKER
from worker import Worker

if __name__ == "__main__":
    worker = Worker(name=NAME_OF_WORKER)
    print(
        "Hello {worker_name}. It is soon {time_reach_station} so it is time to leave! Please check the different "
        "road(s) to come back to your home below.".format(
            worker_name=worker.name, time_reach_station=worker.time_reach_station
        )
    )
    print("Wait a little bit please (less than 30 seconds) ...")
    print("\n")
    roads = worker.get_roads_possible()
    for num_road, road in enumerate(roads):
        print(
            "******************** Road number "
            + str(num_road + 1)
            + " ********************"
        )
        for num_direction, direction in road.items():
            print(
                "Step "
                + str(num_direction + 1)
                + " : go to the station "
                + direction["station"]
                + " for "
                + direction["departure"]
                + " with the line "
                + direction["line"]
                + " to "
                + direction["destination"]
            )

        print("\n\n")

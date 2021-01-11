import requests

from constants import (
    TIME_REACH_STATION,
    HOME_STATION_ID,
    WORK_ADDRESS_LATITUDE,
    WORK_ADDRESS_LONGITUDE,
)


class Worker:
    """class Worker."""

    def __init__(self, name):
        self.name = name
        self.time_reach_station = TIME_REACH_STATION

    def get_roads_possible(self) -> list:
        """Get all the roads possible from the work place to the station.

        Returns:
            List of roads possible.
        """
        roads_possible = []
        geo_points_work_address = {
            "latitude": WORK_ADDRESS_LATITUDE,
            "longitude": WORK_ADDRESS_LONGITUDE,
        }
        all_nearby_stations = requests.get(
            "https://v5.vbb.transport.rest/stops/nearby?latitude={latitude}&longitude={longitude}".format(
                latitude=geo_points_work_address["latitude"],
                longitude=geo_points_work_address["longitude"],
            )
        ).json()

        for station in all_nearby_stations:
            directions_from_station = requests.get(
                "https://v5.vbb.transport.rest/journeys?from={from_station}&to={to_station}&departure=today+{time_reach_station}".format(
                    from_station=station["id"],
                    to_station=HOME_STATION_ID,
                    time_reach_station=self.time_reach_station,
                )
            ).json()
            for road in directions_from_station["journeys"]:
                travels = {}
                road = road["legs"]
                try:
                    for step, connection in enumerate(road):
                        step += 1
                        travels[step] = {
                            "station": connection["origin"]["name"],
                            "destination": connection["destination"]["name"],
                            "departure": connection["departure"],
                            "line": connection["line"]["id"],
                        }
                except:
                    pass
                else:
                    roads_possible.append(travels)
        return roads_possible

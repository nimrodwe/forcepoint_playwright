import csv
from typing import Dict, List, Tuple
import os


def request_ride(file_path: str) -> list[Tuple[str, str, int]]:
    requests = []
    with open(file_path, 'r') as file:
        data = csv.reader(file)
        next(data)
    for row in data:
        company, destination, number_of_rides_requested = str(row[0]), str(row[1]), int(row[2])
        requests.append((company, destination, number_of_rides_requested))

    return requests


def aggregate_requests(requests: List[Tuple[str, str, int]]) -> Dict[str, int]:
    aggregated_requests = {}
    for company, destination, number_of_rides_requested in requests:
        if destination in aggregated_requests:
            aggregated_requests[destination] += number_of_rides_requested
        else:
            aggregated_requests[destination] = number_of_rides_requested

    return aggregated_requests


def distribute_rides(requests: List[Tuple[str, str, int]], approved_rides: Dict[str, int]) -> List[
    Tuple[str, str, int]]:
    distributed = []

    request_map = {}
    for company, destination, number_of_rides_requested in requests:
        if destination not in request_map:
            request_map[destination] = []
        request_map[destination].append((company, number_of_rides_requested))

    for destination, approved in approved_rides.items():
        if destination not in request_map:
            continue

        total_requested = sum(num for _, num in request_map[destination])
        proportional_allocations = {
            company: (num_rides * approved) // total_requested
            for company, num_rides in request_map[destination]
        }

        allocated = {company: (rides // 100) * 100 for company, rides in proportional_allocations.items()}
        remaining = approved - sum(allocated.values())

        for company, num_rides in sorted(request_map[destination], key=lambda x: x[1], reverse=True):
            if remaining >= 100 and allocated[company] + 100 <= num_rides:
                allocated[company] += 100
                remaining -= 100

        for company, rides in allocated.items():
            if rides > 0:
                distributed.append((company, destination, rides))

    return distributed


def write_rides_csv(csv_file: str, distributed_rides):
    abs_path = os.path.join(os.getcwd(), csv_file)

    with open(abs_path, 'w') as file:
        write = csv.writer(file)
        write.writerow(["company_name", "destination", "number_of_rides_approved"])
        write.writerow(distributed_rides)


if __name__ == "__main__":
    file_input = "ride_requests.csv"
    request = request_ride("ride_requests.csv")
    aggregated_requests = aggregate_requests(request)

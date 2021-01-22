import csv
import requests
import time


def getOrderbook(asset_pair):
    orderbook = requests.get("https://api.sfox.com/v1/markets/orderbook/" + str(asset_pair)).json()
    best_bid = orderbook["bids"][0][0]
    best_ask = orderbook["asks"][0][0]
    spread = best_ask - best_bid
    mid = (best_ask + best_bid) * 0.5
    timestamp = time.time()
    return timestamp, best_bid, best_ask, spread, mid


def OBrecorder():
    output = [None for i in range(60)]
    for i in range(60):
        output[i] = getOrderbook(asset_pair)
        time.sleep(1)
    return output


asset_pair = input()
i = 1
while i > 0:
    data = OBrecorder()
    with open('OBfile_' + str(i) + '.csv', 'x', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        for r in range(len(data)):
            csv_writer.writerow(data[r])
    i += 1

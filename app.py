import csv
from collections import defaultdict


def refresh_onspd_small():
    with open("constituencies.csv") as f:
        constituency_lookup = {
            x[1]: x[2]
            for x in csv.reader(f)}
    with open("ONSPD.csv") as fi:
        with open("onspd_small.csv", "w") as fo:
            writer = csv.writer(fo)
            reader = csv.DictReader(fi)
            _ = writer.writerow(("postcode", "constituency"))
            for row in reader:
                try:
                    con = constituency_lookup[row["pcon"]]
                except KeyError:
                    continue
                _ = writer.writerow((row["pcd"].replace(" ", ""), con))


with open("onspd_small.csv") as f:
    postcode_lookup = {
        x["postcode"]: x["constituency"]
        for x in csv.DictReader(f)}

output = defaultdict(int)
with open("data.csv") as f:
    reader = csv.DictReader(f)
    for x in reader:
        con = postcode_lookup.get(x["postcode"].replace(" ", ""))
        if not con:
            print("Postcode not found: {}".format(x["postcode"]))
        # elif x["updates_opt_in"].startswith("Yes"):
        else:
            output[con] += 1

with open("output.csv", "w") as fh:
    out = csv.writer(fh)
    out.writerow(("Constituency", "Total"))
    out.writerows(output.items())

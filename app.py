import argparse
import csv


def refresh_onspd_lookup():
    print("Refreshing ONSPD lookup ...")
    with open("constituencies.csv") as f:
        constituency_lookup = {
            x[1]: x[2]
            for x in csv.reader(f)}
    with open("ONSPD.csv") as fi:
        with open("onspd_lookup.csv", "w") as fo:
            writer = csv.writer(fo)
            reader = csv.DictReader(fi)
            _ = writer.writerow(("postcode", "GSS ID", "constituency name"))
            for row in reader:
                try:
                    con = constituency_lookup[row["pcon"]]
                except KeyError:
                    continue
                _ = writer.writerow((
                    row["pcd"].replace(" ", ""),
                    row["pcon"],
                    con,
                ))
    print("Done.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Geocode a CSV of postcodes")
    parser.add_argument(
        "input_filename",
        help="Input CSV file")
    parser.add_argument(
        "--refresh",
        action="store_true",
        help="Refresh ONSPD lookup")
    args = parser.parse_args()

    if args.refresh:
        refresh_onspd_lookup()

    with open("onspd_lookup.csv") as f:
        postcode_lookup = {
            x["postcode"]: x["GSS ID"]
            for x in csv.DictReader(f)}

    output = []
    with open(args.input_filename) as f:
        reader = csv.DictReader(f)
        for x in reader:
            postcode = x["postcode"].replace(" ", "")
            constituency = postcode_lookup.get(postcode)
            if not constituency:
                print("Postcode not found: {}".format(x["postcode"]))
                continue
            else:
                postcode = "{outcode} {incode}".format(
                    outcode=postcode[:-3], incode=postcode[-3:])
            output.append((x["id"], postcode, constituency))

    with open("output.csv", "w") as fh:
        out = csv.writer(fh)
        out.writerow(("pk", "postcode", "constituency"))
        out.writerows(output)

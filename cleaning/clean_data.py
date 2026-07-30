"""
Cleans the raw Spanish Wine Quality dataset (Kaggle) for the
"value for money by region" Tableau visualization.

Input:  data/wines_SPA_raw.csv
Output: data/wines_SPA_cleaned.csv

What this script does, and why:
1. Drops wines with very few reviews (num_reviews < MIN_REVIEWS).
   A wine rated 4.9 by 3 people isn't a reliable data point --
   it would distort the "best value" story with noise.
2. Groups small regions (fewer than MIN_REGION_COUNT wines) into
   "Other". With 76 distinct regions, coloring every single one
   would make the chart unreadable -- we keep the ones with enough
   wines to actually show a pattern.
3. Flags non-vintage wines (year == "N.V.") instead of dropping them,
   since non-vintage is a real, common category in Spanish wine
   (especially sparkling/Cava) -- not missing data.
4. Adds a `price_log` column, since price is heavily right-skewed
   (median ~29 EUR, max ~3,119 EUR). Tableau can compute a log
   scale on the fly, but having it precomputed makes the field
   available for calculated fields/tooltips too.
"""

import csv
from pathlib import Path
from math import log10
from collections import Counter

INPUT_PATH = Path(__file__).parent.parent / "data" / "wines_SPA_raw.csv"
OUTPUT_PATH = Path(__file__).parent.parent / "data" / "wines_SPA_cleaned.csv"

MIN_REVIEWS = 20        # drop wines with fewer reviewers than this
MIN_REGION_COUNT = 100  # regions with fewer wines than this get grouped into "Other"


def load_rows(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def main():
    rows = load_rows(INPUT_PATH)
    total_in = len(rows)

    # Count region sizes on the FULL dataset (before filtering by reviews)
    # so small regions are judged on their true size, not a filtered subset.
    region_counts = Counter(r["region"] for r in rows)

    kept = []
    dropped_low_reviews = 0

    for row in rows:
        try:
            num_reviews = int(float(row["num_reviews"]))
            price = float(row["price"])
            rating = float(row["rating"])
        except (ValueError, KeyError):
            dropped_low_reviews += 1  # malformed row, treat as unusable
            continue

        if num_reviews < MIN_REVIEWS:
            dropped_low_reviews += 1
            continue

        region = row["region"]
        region_grouped = region if region_counts[region] >= MIN_REGION_COUNT else "Other"

        is_non_vintage = row["year"].strip().upper() == "N.V." or row["year"].strip() == ""

        kept.append({
            "winery": row["winery"],
            "wine": row["wine"],
            "year": "" if is_non_vintage else row["year"],
            "is_non_vintage": "TRUE" if is_non_vintage else "FALSE",
            "rating": rating,
            "num_reviews": num_reviews,
            "region": region,
            "region_grouped": region_grouped,
            "price": price,
            "price_log": round(log10(price), 4),
            "type": row["type"],
            "body": row["body"],
            "acidity": row["acidity"],
        })

    fieldnames = list(kept[0].keys())
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_PATH, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(kept)

    print(f"Input rows:                {total_in}")
    print(f"Dropped (low reviews/bad): {dropped_low_reviews}")
    print(f"Output rows:                {len(kept)}")
    print(f"Regions kept individually:  {sum(1 for c in region_counts.values() if c >= MIN_REGION_COUNT)}")
    print(f"Wrote: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()

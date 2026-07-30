<<<<<<< HEAD
# Spain's Wine Price Ceiling: Where Rating Stops Rewarding You
=======
 Spain's Wine Price Ceiling: Where Rating Stops Rewarding You
>>>>>>> 685fde000c794a49888b5f18d30e5f9961653494

**[View the live interactive dashboard on Tableau Public →](https://public.tableau.com/views/SpanishWineValueAnalysis/SpainsWinePriceCeilingWhereRatingStopsRewardingYou)**

![Dashboard preview](images/final_viz.png)

## The Question

Does a higher price actually get you a better-rated Spanish wine — or are some regions
quietly overdelivering while others charge a premium for the same quality?

## The Approach

- **Dataset:** [Spanish Wine Quality Dataset](https://www.kaggle.com) (Kaggle), ~7,500 wines
  with price, critic rating, region, and review count
- **Cleaning:** grouped the 63 smallest wine regions into "Other" to keep the chart readable,
  flagged non-vintage wines instead of dropping them, and added a log-scaled price field to
  handle the wide price range (€5–€3,119). Full cleaning script in [`cleaning/clean_data.py`](cleaning/clean_data.py).
- **Tool:** Tableau Public

## The Finding

<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 685fde000c794a49888b5f18d30e5f9961653494
Across most of the price range — roughly €5 to €300 — average rating barely moves,
holding steady around 4.2–4.4 regardless of price. It's only once you cross into
luxury pricing (€300+) that ratings climb meaningfully, up toward 4.7–4.9. In plain
terms: for the vast majority of Spanish wines in this dataset, paying more doesn't
buy you a meaningfully better rating — it's only at the very top of the market that
price and quality actually move together.
<<<<<<< HEAD
=======
*(Most wines cluster around a 4.2–4.4 rating regardless of price up into the hundreds of euros, and only wines above roughly €300–500 start showing a real jump toward 4.7–4.9. In plain terms: paying more only meaningfully improves your odds of a top-rated bottle once you're well into luxury pricing — for the vast majority of the price range, you're not buying a better rating, just a bigger price tag.)*
>>>>>>> 02fe95f5aca5c4653c763e180b9bd8e82d4e3b2d
=======
>>>>>>> 685fde000c794a49888b5f18d30e5f9961653494

## What This Shows

This project was built to demonstrate:
- Working with a real, imperfect dataset (missing years, skewed pricing, uneven region sizes)
  and making explicit, documented cleaning decisions
- Choosing a visual form that fits the data's actual shape, not a default chart type
- Turning a dataset into a specific, answerable business question rather than just
  describing what's in it

## Repo Structure
```
wine-value-analysis/
├── README.md
├── data/
│   ├── wines_SPA_raw.csv
│   └── wines_SPA_cleaned.csv
├── cleaning/
│   └── clean_data.py
└── images/
    └── final_viz.png
```


<h1 align="center">
Whine Quality Clasification

## Marvelous ML Ops with Databricks Project

- **Dataset:** wine quality publicly shared datasets from UC Irvine. [Found here](https://archive.ics.uci.edu/dataset/186/wine+quality)

- **Goal:** model wine quality based on physicochemincal tests.

- **Observation:** the dataset target is highly imbalanced (quality column):

    | quality | count |
    | --- | --- |
    | 6	| 2198 |
    | 5	| 1457 |
    | 7	| 880 |
    | 8	| 175 |
    | 4	| 63 |
    | 3	| 20 |
    | 9	| 5 |

    So I decided to pre-classify qualities of 8,4,3 and 9 to a class '101' and after that anything that is classified there to process to the proper class of 8,4,3 or 9.







## Getting Started

### Prerequisites

Only tested with Python 3.7.1

```
pip install - r requirements.txt
```

OR

```
pip install pandas
```

### Running the tests for Questions 1 and 2

```
python -m unittest question_2.py
```

```
python -m unittest question_2.py
```


### Example usage for Question 3


```
df = pd.DataFrame({'id': [1, 2, 3, 4, 5],
                   'url': ['1.com', '2.com', '3.com', '4.com', '5.com'],
                   'rating': [1, 4, 5, 8, 10],
                   'date': [date.today() - timedelta(days=x) for x in range(5)]})


FindId.greater_than(df, 3)
FindId.less_than(df, 3)
FindId.equal_to(df, 3)
FindId.is_in(df, [1,2,3])
FindId.is_not_in(df, [1,2,3])

FindUrl.equal_to(df, '4.com')

FindDate.greater_than(df, date.today() - timedelta(days=3))
FindDate.less_than(df, date.today() - timedelta(days=3))
FindDate.equal_to(df, date.today() - timedelta(days=3))

FindRating.greater_than(df, 5)
FindRating.less_than(df, 5)
FindRating.equal_to(df, 5)
```


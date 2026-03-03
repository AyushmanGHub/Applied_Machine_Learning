
# Assignment 03: Testing & Model Serving  

**Spam Classification – Unit Testing & Flask Deployment**


### 1. unit testing

* In **score.py**, write a function with the following signature that scores a trained model on a text:
```python
def score(text:str, model:sklearn.estimator, threshold:float) -> 
                    prediction:bool, propensity:float

```


* In **test.py**, write a unit test function **test_score(...)** to test the score function. You may reload and use the best model saved during experiments in **train.ipynb** (in joblib/pkl format) for testing the score function.
You may consider the following points to construct your test cases:
* does the function produce some output without crashing (smoke test)
* are the input/output formats/types as expected (format test)
* is prediction value 0 or 1 (sanity check)
* is propensity score between 0 and 1 (sanity check)
* if you put the threshold to 0 does the prediction always become 1 (edge case input)
* if you put the threshold to 1 does the prediction always become 0 (edge case input)
* on an obvious spam input text is the prediction 1 (typical input)
* on an obvious non-spam input text is the prediction 0 (typical input)



### 2. flask serving

* In **app.py**, create a flask endpoint **/score** that receives a text as a POST request and gives a response in the json format consisting of prediction and propensity
* In **test.py**, write an **integration test** function **test_flask(...)** that does the following:
* launches the flask app using command line (e.g. use os.system)
* test the response from the localhost endpoint
* closes the flask app using command line


#### In coverage.txt produce the coverage report output of the unit test and integration test using pytest

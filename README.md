# pyAlphaVantage
A mighty small (thanks to a bit of **Black_Magic**) python package for all AlphaVantage API.

## Step 1
Install it however you want (git clone / pip)

## Step 2 use it
```python
import pyAlphaVantageAPI.AlphaVantageAPI as AVA

api = AVA.AlphaVantage(api_key=<your api key>)
#make a call with arguments as definied in AlphaVantage documentation
data = api.TIME_SERIES_DAILY_ADJUSTED(symbol=SYMBOL, datatype="csv", outputsize="full")
```

*TIME_SERIES_DAILY_ADJUSTED* can be replaced by any function in the documentation as long as it is part of the API and defined in *api.functions_defs*.

## Adding a function to definitions can be done using
```python
api.add_function_definitions(function_name, argument_list)
```

## To know all functions available

```python
api.get_available_functions()
```

## To know the arguments of an available function

```python
api.get_function_arguments(function_name)
```

# That's it

Cheers,

T.

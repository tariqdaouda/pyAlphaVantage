
class AlphaVantage(object):
    """This class can make any call to AlphaVantage api"""
    def __init__(self, api_key, default_outputsize = "full", default_datatype = "csv"):
        super(AlphaVantage, self).__init__()
        self.api_key = api_key
        self.accepted_datatypes = ("csv", "json")
        
        if default_datatype not in self.accepted_datatypes :
            raise ValueError( '%s datatype is not among the accepted: %s' % (self.accepted_datatypes, default_datatypes))
       
        self.defaults = {
            "outputsize" : default_outputsize,
            "datatype" : default_datatype,
        }
        
        self.functions_defs = {
            #STOCKS
            "TIME_SERIES_INTRADAY" : ("symbol", "interval", "outputsize", "datatype"),
            "TIME_SERIES_DAILY" : ("symbol", "outputsize", "datatype"),   
            "TIME_SERIES_DAILY_ADJUSTED" : ("symbol", "outputsize", "datatype"),
            "TIME_SERIES_WEEKLY" : ("symbol", "datatype"),
            "TIME_SERIES_WEEKLY_ADJUSTED" : ("symbol", "datatype"),
            "TIME_SERIES_WEEKLY_ADJUSTED" : ("symbol", "datatype"),
            "TIME_SERIES_MONTHLY" : ("symbol", "datatype"),
            "TIME_SERIES_MONTHLY_ADJUSTED" : ("symbol", "datatype"),
            "GLOBAL_QUOTE" : ("symbol", "datatype"),
            "SYMBOL_SEARCH" : ("keywords", "datatype"),
            #FOREX
            "CURRENCY_EXCHANGE_RATE" : ("from_currency", "to_currency", "datatype"),
            "FX_INTRADAY" : ("from_symbol", "to_symbol", "interval", "outputsize", "datatype"),
            "FX_DAILY" : ("from_symbol", "to_symbol", "interval", "outputsize", "datatype"),
            "FX_WEEKLY" : ("from_symbol", "to_symbol", "interval", "outputsize", "datatype"),
            "FX_MONTHLY" : ("from_symbol", "to_symbol", "interval", "outputsize", "datatype"),
            #CRYPTO
            "CURRENCY_EXCHANGE_RATE" : ("from_currency", "to_currency", "datatype"),
            "DIGITAL_CURRENCY_DAILY" : ("symbol", "market", "datatype"),
            "DIGITAL_CURRENCY_WEEKLY" : ("symbol", "market", "datatype"),
            "DIGITAL_CURRENCY_MONTHLY" : ("symbol", "market", "datatype"),
            #INDICTORS
            "SMA" : ("symbol", "interval", "series_type", "datatype"),
            "EMA" : ("symbol", "interval", "series_type", "datatype"),
            "WMA" : ("symbol", "interval", "series_type", "datatype"),
            "DEMA" : ("symbol", "interval", "series_type", "datatype"),
            "TEMA" : ("symbol", "interval", "series_type", "datatype"),
            "TRIMA" : ("symbol", "interval", "series_type", "datatype"),
            "KAMA" : ("symbol", "interval", "series_type", "datatype"),
            "MAMA" : ("symbol", "interval", "series_type", "datatype"),
            "T3" : ("symbol", "interval", "series_type", "datatype"),
            "MACD" : ("symbol", "interval", "series_type", "datatype"),
            "MACDEXT" : ("symbol", "interval", "series_type", "datatype"),
            "STOCH" : ("symbol", "interval", "series_type", "datatype"),
            "STOCHF" : ("symbol", "interval", "series_type", "datatype"),
            "RSI" : ("symbol", "interval", "series_type", "datatype"),
            "STOCHRSI" : ("symbol", "interval", "series_type", "datatype"),
            "WILLR" : ("symbol", "interval", "series_type", "datatype"),
            "ADX" : ("symbol", "interval", "series_type", "datatype"),
            "ADXR" : ("symbol", "interval", "series_type", "datatype"),
            "APO" : ("symbol", "interval", "series_type", "datatype"),
            "PPO" : ("symbol", "interval", "series_type", "datatype"),
            "MOM" : ("symbol", "interval", "series_type", "datatype"),
            "BOP" : ("symbol", "interval", "series_type", "datatype"),
            "CCI" : ("symbol", "interval", "series_type", "datatype"),
            "CMO" : ("symbol", "interval", "series_type", "datatype"),
            "ROC" : ("symbol", "interval", "series_type", "datatype"),
            "ROCR" : ("symbol", "interval", "series_type", "datatype"),
            "AROON" : ("symbol", "interval", "series_type", "datatype"),
            "AROONOSC" : ("symbol", "interval", "series_type", "datatype"),
            "MFI" : ("symbol", "interval", "series_type", "datatype"),
            "TRIX" : ("symbol", "interval", "series_type", "datatype"),
            "ULTOSC" : ("symbol", "interval", "series_type", "datatype"),
            "DX" : ("symbol", "interval", "series_type", "datatype"),
            "MINUS_DI" : ("symbol", "interval", "series_type", "datatype"),
            "PLUS_DI" : ("symbol", "interval", "series_type", "datatype"),
            "MINUS_DM" : ("symbol", "interval", "series_type", "datatype"),
            "PLUS_DM" : ("symbol", "interval", "series_type", "datatype"),
            "BBANDS" : ("symbol", "interval", "series_type", "datatype"),
            "MIDPOINT" : ("symbol", "interval", "series_type", "datatype"),
            "MIDPRICE" : ("symbol", "interval", "series_type", "datatype"),
            "SAR" : ("symbol", "interval", "series_type", "datatype"),
            "TRANGE" : ("symbol", "interval", "series_type", "datatype"),
            "ATR" : ("symbol", "interval", "series_type", "datatype"),
            "NATR" : ("symbol", "interval", "series_type", "datatype"),
            "AD" : ("symbol", "interval", "series_type", "datatype"),
            "ADOSC" : ("symbol", "interval", "series_type", "datatype"),
            "OBV" : ("symbol", "interval", "series_type", "datatype"),
            "HT_TRENDLINE" : ("symbol", "interval", "series_type", "datatype"),
            "HT_SINE" : ("symbol", "interval", "series_type", "datatype"),
            "HT_TRENDMODE" : ("symbol", "interval", "series_type", "datatype"),
            "HT_DCPERIOD" : ("symbol", "interval", "series_type", "datatype"),
            "HT_DCPHASE" : ("symbol", "interval", "series_type", "datatype"),
            "HT_PHASOR" : ("symbol", "interval", "series_type", "datatype")
        }

    def add_function_definitions(self, function_name, argument_list) :
        """add (or overwrites) a function definition. function_name is the name as definied in AlphaVantage's doc,
        argument_list is a list or tuple of argument names passed to that function"""

        self.functions_defs[function_name] = argument_list

    def get_available_functions(self) :
        """return the names of available functions"""
        return self.functions_defs.keys()

    def get_function_arguments(self, function_name) :
        """return the arguments of a expected by a given function"""
        try:
            return self.functions_defs[function_name]
        except KeyError as e:
            raise KeyError("%s is not among the defined functions. You can add it using self.add_function_definitions(function_name, argument_list)")

    def _get(self, function_name) :
        """You should never have to call this magic function direclty. It will create a function for the API call and return it to you"""
        def __get(**params) :
            import requests 
                
            arg_list = set(self.functions_defs[function_name])
           
            for k in self.defaults :
                if k not in params :
                    params[k] = self.defaults[k] 
            
            args = set(params.keys())

            if arg_list != args :
                raise ValueError("function %s needs the following arguments: %s.\nGot: %s.\nDefaults: %s" % (function_name, arg_list, args, self.defaults) )
            
            if "datatype" in params :
                datatype = params["datatype"]
            else :
                datatype = self.default_datatype

            bind_vars = {
                "apikey": self.api_key,
                "function" : function_name
            }

            bind_vars.update(params)
            
            str_vars = []
            for k, v in bind_vars.items() :
                str_vars.append("%s=%s" % (k, v))
            str_vars = '&'.join(str_vars)

            url = "https://www.alphavantage.co/query?%s" % str_vars
            data = requests.get(url)

            if datatype == "csv" :
                import io
                return io.BytesIO(data.content)

            import json
            return json.loads(data.content) 
        return __get

    def __getattr__(self, k) :
        """If the attribute is not found in the the object and if is present in function definition. Create the function for the api call and return it"""
        defs = object.__getattribute__(self, "functions_defs")
        if k in defs :
            return self._get(k)

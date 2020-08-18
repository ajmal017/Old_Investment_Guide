import pandas as pd
ASX_data = pd.read_csv('https://www.asx.com.au/asx/research/ASXListedCompanies.csv',skiprows=1)
# format to align with yahoo finance ticker
ASX_data["Ticker"] = ASX_data['ASX code']+".AX"
ASX_TICKER_LIST = list(ASX_data['Ticker'])
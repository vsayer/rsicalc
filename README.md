# RSICalc

[![Join the chat at https://gitter.im/vsayer/rsicalc](https://badges.gitter.im/vsayer/rsicalc.svg)](https://gitter.im/vsayer/rsicalc?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

*Relative Strength Index Calculator*

RSICalc calculates RSI values for a set of specified stock ticker symbols using yahoo finance. The RSI or Relative Strength Index of a stock tells one if a stock is oversold or overbought. General consensus is if the value falls below 30, it is oversold; if it the values exceeds 70, it is overbought. It is a way of indicating the momentum of a stock.

Since this tool uses yahoo historical values to calculate the RSI, there is not enough granularity to cover the 1d and 5d graphs yahoo finance shows. So a 14-period RSI here really is a 14-period (days) RSI. The output generated here should be consistent with 1m and longer time intervals on yahoo finance.

## Install
Install RSICalc using pip:
```shell
sudo pip install rsicalc
```

## Usage
#### retrieve GOOG, FB, AAPL for the last 22 days using 14-period RSI
```shell
rsicalc GOOG FB AAPL
```

#### retrieve GOOG, FB, AAPL for the last 10 days using 25-period RSI 
```shell
rsicalc --period=25 --last=10 GOOG FB AAPL
```

#### retrieve GOOG, FB, AAPL but print in row format, i.e., *symbol1:val1,val2,..* newline *symbol2:val1,val2,..*
```shell
rsicalc --row GOOG FB AAPL
```

## Tricks
#### sending stdout to gnuplot
```shell
EDITME
```

## Develop
If you have ideas to further develop RSICalc, please clone this repo and send over a pull request! Thanks!

## License
[BSD 3-Clause](LICENSE)

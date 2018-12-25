# Python Script for Downloading Data from NDFD
This is a super dumb script to download data from National Digital Forecast Database (NDFD). I wrote it in a hurry to just download some data. Everyone is welcomed to use and improve the script. I will try to update it as I find some time. 

The main Python function is: ndfd_download(keyword, year_month_days)
where, 
  keyword: the first four letter of the file you want to download
  Please find more details about it is available here
  https://www.ncdc.noaa.gov/nomads/documentation/user-guide/advanced-data-access-methods
  http://www.nws.noaa.gov/datamgmt/doc/ndfdref.html
  
  year_month_days: list of tuples (year, month, day) containing the days for which you want to download the data

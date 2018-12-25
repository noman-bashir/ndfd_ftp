from ftplib import FTP  
import ftplib
import os
import calendar
import datetime as dt

def ndfd_download(keyword, year_month_days):

    print('Starting connection to NOAA database')

    # Try connecting to the server
    try:
        ftp = FTP('nomads.ncdc.noaa.gov') 
        ftp.login()
        print('Connect successful')
    except ftplib.all_errors as e:
        errorcode_string = str(e).split(None, 1)[0]
        print(errorcode_string)

    ftp.cwd('/NDFD/')
    print('Current working directory is %s' % ftp.pwd())

    for year_month_day in year_month_days: 

        year = year_month_day[0]
        month = year_month_day[1]
        day = year_month_day[2]

        # Change to the NDFD directory to get your data
        print('Changing directory to \"/NDFD/{}/{}/\"'.format(month, day))
        ftp.cwd('/NDFD/{}/{}/'.format(month, day))

        print('Current working directory is %s' % ftp.pwd())

        # getting names of all files in the current working directory
        all_files = ftp.nlst()

        # filtering all the files with desired keyword
        all_files = [key for key in all_files if key.startswith(keyword)]

        # creating a directory to store the data
        directoryName = '{}/{}/{}'.format(year, month, day)
        if not os.path.exists(directoryName):
            os.makedirs(directoryName)

        # Move into the folder
        directoryPath = '%s/%s' % (os.getcwd(), directoryName)
        os.chdir(directoryPath)

        print('Downloading data for {}'.format(day))
        for f in all_files: 

            file = open(f, 'wb')

            try:
                ftp.retrbinary('RETR %s' % f, file.write)
                # print('Successfully downloaded: {}'.format(f))
            except ftplib.all_errors as e:
                print('Error downloading') 
                errorcode_string = str(e).split(None, 1)[0]

            file.close()

        # going 3 directories up 
        os.chdir("../../..")

    ftp.close()

if __name__ == "__main__":
    keyword = "YABZ"
    year = 2012
    month = 1
    day = 1
    year_month_days = []
    no_of_days = 366 if calendar.isleap(year) else 365
    t = dt.datetime(year,month,day)
    for i in range(no_of_days):
        year_month_days.append((t.strftime("%Y"), t.strftime("%Y%m"), t.strftime("%Y%m%d")))
        t = t + dt.timedelta(days = 1)

    ndfd_download(keyword, year_month_days)

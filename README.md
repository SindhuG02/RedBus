# RedBus

attached png files are required for executing the Streamlit application.(please keep all these files in one folder).

Step 1 -> 
creating table -> Create_Table.py -> 

1) in this file we will be creating the required columns for this Project with table name as RedBus.
2) in this file please change the user & passowrd accordingly
3) while running this file if there is any error related to password.(only if required run the command)
   3.1) in that case please run this in cmd (pip install mysql-connector-python if any error related to password)
4) using mysql.connector for connecting to the database via python.
5) by using the sql queries we will be creating the database and the table.


Step 2 -> web scraping  -> getSubContainer_Data.py -> 

1) with the help of Selenium we will be scraping the data for the redBus
2) to be noted - i will be scraping the data seperately as in we have sub container and normal container
   2.1) Sub Container -> we will be having box and on click of VIEW BUSES we will get additional bus details
3) Since each time the website was updating with the offers and start from and some other extra details.
   3.1) which we can't observe all the time.Due to that i have made it as 2 files.
4) for this file to work 
   4.1) replace variable chrome_driver_path with the path where you have installed driver
   4.2) if there is any issue in running the selenium file (uninstall existing one and use this pip install selenium==3.0.0)
   4.3) step 4.2 is only if required.
   4.4) driver.maximize_window() - used to maximize the browser.
5) check code for additional documentation.
6) from this file we get only sub container data

**improvement** -> have to combine step 2 & step 3 in single file.

1) **issue** why i have created different file, Because when i developed redbus UI was different for sub contatiner(it was button click and later it became full container click)
2) and even in length there was problem so i have created seperate file by considering the time and this issue. And even the data extraction was taking time becasue of huge data

Step 3 -> Web Scraping ->step_3_get_container_data.py -> same as above but used to scrap normal container.

**takeaway points** -> 1) learnt selenium to some point.
                   2) leant Streamlit application.
                   3) larnt how to understand the error and to over come it.

**challenges** -> 1) had problem to navigate from page 1-> page 2 and so on.
              2) data kept changing sometimes with start from details and sometimes without start from details.(website display)

**materials** -> geeksforgeeks,W3Schools & YouTube.

Step 4 -> Streamlit Application 

1) all the attached png files are required.
2) we have 3 py files - home.py ,GOVERNMENT_BUSES.py and main_GUI.py
3) main_GUI.py is the main file and the other 2 files i have imported those into mail_GUI file.
4) main_GUI contains the operation on how it should travel.
   4.1) if we select home it will be in home page(default page)
   4.2) if we select on GOVERNMENT_BUSES then it will go to that page.
5) home.py -> based on selected drowdown options in code with the help of SQL query we will be displaying the data
6) GOVERNMENT_BUSES.py -> display all the data that is present in database under that particular Government bus.

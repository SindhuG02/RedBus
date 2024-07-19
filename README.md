# RedBus

attached png files are required for executing the Streamlit application.(please keep all these files in one folder).

Step 1 -> creating table -> Create_Table.py -> in this file we will be creating the required columns for this Project with table name as RedBus.
                                            -> in this file please change the user & passowrd accordingly
                                            -> while running this file if there is any error related to password.(only if required run the command)
                                                  ->in that case please run this in cmd (pip install mysql-connector-python if any error related to password)
                                            -> using mysql.connector for connecting to the database via python.
                                            -> by using the sql queries we will be creating the database and the table.

Step 2 -> web scraping  -> getSubContainer_Data.py -> with the help of Selenium we will be scraping the data for the redBus website.
                                                   -> to be noted - i will be scraping the data seperately as in we have sub container and normal container
                                                     -> Sub Container -> we will be having box and on click of VIEW BUSES we will get additional bus details
                                                   -> Since each time the website was updating with the offers and start from and some other extra details.
                                                     -> which we can't observe all the time.Due to that i have made it as 2 files.
                                                   -> for this file to work 
                                                     ->1) replace variable chrome_driver_path with the path where you have installed driver
                                                     ->2) if there is any issue in running the selenium file (uninstall existing one and use this pip install selenium==3.0.0)
                                                     -> step 2 is only if required.
                                                     ->driver.maximize_window() - used to maximize the browser.
                                                   -> check code for additional documentation.
                                                   -> from this file we get only sub container data

-> improvement -> have to combine step 2 & step 3 in single file.
-> issue why i have created different file, Because when i developed redbus UI was different for sub contatiner(it was button click and later it became full container click)
-> and even in length there was problem so i have created seperate file by considering the time and this issue. And even the data extraction was taking time becasue of huge data

Step 3 -> Web Scraping ->step_3_get_container_data.py -> same as above but used to scrap normal container.

takeaway points -> 1) learnt selenium to some point.
                   2) leant Streamlit application.
                   3) larnt how to understand the error and to over come it.

challenges -> 1) had problem to navigate from page 1-> page 2 and so on.
              2) data kept changing sometimes with start from details and sometimes without start from details.(website display)

materials -> geeksforgeeks,W3Schools & YouTube.

Step 4 -> Streamlit Application -> all the attached png files are required.
                                -> we have 3 py files - home.py ,GOVERNMENT_BUSES.py and main_GUI.py
                                -> main_GUI.py is the main file and the other 2 files i have imported those into mail_GUI file.
                                -> main_GUI contains the operation on how it should travel.
                                  -> if we select home it will be in home page(default page)
                                  -> if we select on GOVERNMENT_BUSES then it will go to that page.
                                -> home.py -> based on selected drowdown options in code with the help of SQL query we will be displaying the data
                                -> GOVERNMENT_BUSES.py -> display all the data that is present in database under that particular Government bus.

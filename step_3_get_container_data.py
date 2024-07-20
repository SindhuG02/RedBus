from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import pandas as pd
from selenium.common.exceptions import NoSuchElementException
import mysql.connector

#replace it with your driver path
chrome_driver_path = r'C:\chromedriver\chromedriver.exe'

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.maximize_window()

#method is used to scroll the web page becuase if we don't scroll then data will not be visible
def scroll_to_bottom(value):
    driver.execute_script(f"window.scrollTo(0,{value});")
    time.sleep(2)


def GoToGovernment_bus(bus_link,value):
    #passiing the government bus links as input parameter
    driver.get(bus_link)
    route_name=[]
    route_link=[]
    bus_name=[]
    bus_type=[]
    start_time=[]
    end_time=[]
    duration=[]
    rating=[]
    price=[]
    Seats_available=[]
    Bus_Route_Link=[]
    Bus_Route_name=[]
    Government_Bus=[]
    governmentBus=["APSRTC", "TSRTC","KERALA_RTC","KTCL","RSRTC","SBSTC","HRTC","ASTC","UPSRTC","WBTC"]
    increment=0
    #to travel from page 1->page 2
    pages=driver.find_element(By.CLASS_NAME,'DC_117_paginationTable')
    for i in pages.text.split('\n'):
        
        i=int(i)
        #in page 1 we need to get the Route_data and Route_link
        #post that onlt we need to change the page to next page so i>1 is used
        if i>1:
            #we get back to the same link 
            driver.get(bus_link)
            #sleep for 5 seconds
            time.sleep(5)
            #using the class name we will locate the element
            Total_pages=driver.find_element(By.CLASS_NAME,'DC_117_paginationTable')
            #once the page is loaded and we are using the string format because we will be such way that
            #for example - page1->get all details(routeName & RouteLink) reload page 1
            #go to page 2 ->get all details(routeName & RouteLink) reload page 1
            #go to page 3 ->get all details(routeName & RouteLink) reload page 1 and so on.
            Next_Page=Total_pages.find_element(By.XPATH,f'//*[@id="root"]/div/div[4]/div[12]/div[{i}]')
            action=ActionChains(driver)
            action.move_to_element(Next_Page).perform()
            time.sleep(5)
            Next_Page.click()
        #each page we are extracting the route_name and storing in List
        routes=driver.find_element(By.XPATH,'//*[@id="root"]/div/div[4]')
        l=routes.text.split('\n')
        for i in l:
            if "to" in i:
                route_name.append(i)
        #finding the href first and then extracting the link
        #each page we are extracting the route_Link and storing in List 
        hrefDetails=driver.find_elements(By.CLASS_NAME,'route')
        for route in hrefDetails:
            val=route.get_attribute('href')
            route_link.append(val)       
    #once we complete all the pages no we will be having Route_name along with Route_link
    increment=0 
    for link in route_link:
        #using the Route_link we will go to each link and get the details
        driver.get(link)
        time.sleep(5)
        #default value to the attribute count
        count=0
        while True:
            
            time.sleep(5)
            count=count+1
            print(count)
            #each time we are incrementing the count value which mean that when we open one route
            #we have to extract the details in a loop.

            #using scroll to get the details into visibility.it's a user defined method
            scroll_to_bottom(count*500)  
            try: 
                time.sleep(5)        
                element=driver.find_element(By.XPATH,f'//*[@id="result-section"]/div[3]/ul/div[{count}]')
            #we are using the execpt block because we have different xpath based on the sub container present.
            except NoSuchElementException:
                #count 1 is becuase we it should fail in the first read only if path is incorrect
                #in that case we use the other possible paths
                if count==1:    
                    try:                                
                        element=driver.find_element(By.XPATH,f'//*[@id="result-section"]/div[2]/ul/div[{count}]')
                    except NoSuchElementException:
                        try:
                            element=driver.find_element(By.XPATH,f'//*[@id="result-section"]/div[1]/ul/div[{count}]')
                        except NoSuchElementException:
                            #if nothing is found then we will be coming out of loop.
                            #since there is no processing left
                            count=0
                            break   
                else:
                    #if nothing is found then we will be coming out of loop.
                            #since there is no processing left
                    count=0
                    break

            full_details=[]
            full_details=element.text.split('\n')
            
            #in few cases when we are extracting the data
            #there are possibility that data would come in other index
            #so additional conditions are added as per safty net.
            for busType_index in range(len(full_details)):
                if 'A/C' in full_details[busType_index]:
                    print("index",busType_index)
                    bustypeindex=busType_index
                    
                elif 'INR' in full_details[busType_index]:
                    print("INR index",busType_index)
                    INRindex=busType_index
                elif 'Seats available' in full_details[busType_index] or 'Seat available' in full_details[busType_index]:
                    print("Seat_avail index",busType_index)
                    Seat_availableindex=busType_index
            bus_type.append(full_details[bustypeindex])
            bus_name.append(full_details[(bustypeindex-1)])
            start_time.append(full_details[bustypeindex+1])
            duration.append(full_details[bustypeindex+3])
            end_time.append(full_details[bustypeindex+4])
            rating.append(full_details[bustypeindex+7]) 
            valueINR=full_details[INRindex] 
            print(valueINR,valueINR[-4:])   
            price.append(valueINR[-4:])
            
            Seats_available.append(full_details[Seat_availableindex])
            Bus_Route_Link.append(link)
            Bus_Route_name.append(route_name[increment]) 
            Government_Bus.append(governmentBus[value])
            print(full_details[(bustypeindex-1)],full_details[bustypeindex],full_details[bustypeindex+1],full_details[bustypeindex+3],full_details[bustypeindex+4],full_details[bustypeindex+7],full_details[INRindex],full_details[Seat_availableindex])
            print("------------------------------------")
        increment=increment+1
        
    busDetails={'Route_Name':Bus_Route_name,'Route_link':Bus_Route_Link,"Bus_name":bus_name,'Bus_Type':bus_type,'Start Time':start_time,'Duration':duration,'End_time':end_time,'Rating':rating,'Price':price,'Seats_available':Seats_available,'Government_Bus':Government_Bus}
    df=pd.DataFrame(data=busDetails)
    #df.to_csv('Sub_Bus_details.csv')
    df=df.drop(['Unnamed: 0'],axis=1)
    #once each government bus gets completed now we will store in SQL
    con = mysql.connector.connect(
            host='localhost',
            user='root',
            password='12345678'
        )
    cursor=con.cursor()
        
    cursor.execute('use redbus')
    data = [tuple(row) for row in df.values]
    print(data)
    sql = "INSERT INTO bus_routes (Route_name, Route_link,Busname,Bustype,Departing_time,Duration,Reaching_time,Star_rating,Price,Seats_available,Government_Bus_name) VALUES (%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

    cursor.executemany(sql, data)
    #save permentaly into db
    con.commit()

red_bus=['https://www.redbus.in/online-booking/apsrtc/?utm_source=rtchometile','https://www.redbus.in/online-booking/tsrtc/?utm_source=rtchometile','https://www.redbus.in/online-booking/ksrtc-kerala/?utm_source=rtchometile','https://www.redbus.in/online-booking/ktcl/?utm_source=rtchometile','https://www.redbus.in/online-booking/rsrtc/?utm_source=rtchometile','https://www.redbus.in/online-booking/south-bengal-state-transport-corporation-sbstc/?utm_source=rtchometile','https://www.redbus.in/online-booking/hrtc/?utm_source=rtchometile','https://www.redbus.in/online-booking/astc/?utm_source=rtchometile','https://www.redbus.in/online-booking/uttar-pradesh-state-road-transport-corporation-upsrtc/?utm_source=rtchometile','https://www.redbus.in/online-booking/wbtc-ctc/?utm_source=rtchometile']

GoToGovernment_bus('https://www.redbus.in/online-booking/apsrtc/?utm_source=rtchometile',0)

for i in len(red_bus):
    GoToGovernment_bus(red_bus[i],i)
    
import streamlit as st
from PIL import Image
import pandas as pd
import mysql.connector

def app():
	FromDetails=[]
	BusType=[]
	StartTime=[]
	Price=[]
	con = mysql.connector.connect(
        host='localhost',
        user='root',
        password='12345678'
    )
	cursor=con.cursor()
	cursor.execute('use redbus')
	query="select DISTINCT(Route_name) from bus_routes "
	cursor.execute(query)
	for data in cursor:
		strValue=str(data)
		FromDetails.append(strValue[2:-3])
	
	query="select DISTINCT(Bustype) from bus_routes "
	cursor.execute(query)
	for data in cursor:
		BusType.append(data)

	query="select DISTINCT(Departing_time) from bus_routes "
	cursor.execute(query)
	time=''
	for data in cursor:
		strTime=str(data)
		val=strTime[20:-3]
		l=val.split(',')
		time=str(int(l[0]))+'-'+l[1]+'-'+l[2]+' '+l[3]+':'+l[4]
		StartTime.append(time)

	query="select DISTINCT(Price) from bus_routes "
	cursor.execute(query)
	for data in cursor:
		strPrice=str(data)
		Price.append(strPrice[10:-7])
    
	st.header("India's No. 1 Online Bus Ticket Booking Site")
	img = Image.open("home.png")
	st.image(img, width=500)
	with st.form("From-To"):
		col1,col2,col3=st.columns(3)
		col4,col5=st.columns(2)
		Frome_To_Details=col1.selectbox("From To",FromDetails)
		Seat_AC_type=col2.selectbox("Select Bus Type",['NON AC SLEEPER','AC SLEEPER','AC SEMI SLEEPER','NON AC'])
		ratings=col3.selectbox("Select the Ratings",["1 to 2","2 to 3","3 to 4","4 to 5"])
		start_time=col4.selectbox("Select Starting Time",StartTime)
		fare_range=col5.selectbox("Bus Fare Range",Price)
		
		Submitted = st.form_submit_button("Search Buses")

	if Submitted:
		
		st.subheader("AVAILABLE BUSES DETAILS")
		rate1=int(ratings[0])
		rate2=int(ratings[-1])
		
		query=f"select * from bus_routes where Route_name='{Frome_To_Details}'  and Price <= {fare_range} and Star_rating BETWEEN {rate1} and {rate2}"
		cursor.execute(query)
		details=[]
		for data in cursor:
			details.append(data)
		print(details)
		df=pd.DataFrame(details,columns=["ID","Route_name","Route_link","Busname","Bustype","Departing_time","Duration","Reaching_time","Star_rating","Price","Seats_available","Government_bus_name"])  
		st.dataframe(df)
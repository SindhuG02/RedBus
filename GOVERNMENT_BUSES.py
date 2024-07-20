from streamlit_image_select import image_select
import streamlit as st
import mysql.connector
import pandas as pd
def app():

    con = mysql.connector.connect(
        host='localhost',
        user='root',
        password='12345678'
    )
    cursor=con.cursor()
    
    query='use redbus'
    cursor.execute(query)

    st.subheader("GOVERNMENT BUSES")
    img = image_select(
        label=None,
        images=[
            "APSRTC.png",
            "TSRTC.png",
            "KERALA_RTC.png",
            "KTCL.png",
            "RSRTC.png",
            "SBSTC.png",
            "HRTC.png",
            "ASTC.png",
            "UPSRTC.png",
            "WBTC.png"
        ],
        captions=["APSRTC", "TSRTC","KERALA_RTC","KTCL","RSRTC","SBSTC","HRTC","ASTC","UPSRTC","WBTC"],
        use_container_width=False,
        return_value="index"
    )

    val=int(img)
    
    details=[]
    Bus_name=["APSRTC", "TSRTC","KERALA_RTC","KTCL","RSRTC","SBSTC","HRTC","ASTC","UPSRTC","WBTC"]
    print(val)
    query=f"select * from bus_routes where Government_Bus_name='{Bus_name[val]}'"
    cursor.execute(query)
    for data in cursor:
        details.append(data)
    df=pd.DataFrame(details,columns=["ID","Route_name","Route_link","Busname","Bustype","Departing_time","Duration","Reaching_time","Star_rating","Price","Seats_available","Government_bus_name"])  
    st.dataframe(df)



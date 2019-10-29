from tkinter import*
import requests
import string
import time
import json
from PIL import  Image,ImageTk

#functions 

#after Clicking send button this fucntion will execute
def sendButtonFunction():

	#Which type of request has to be send is selected from option menu 
	requestType=selectedElement.get()

	print("List Selected : ",requestType)

	#getting url from url text field
	urltosend=urltextField.get("1.0",END).strip()
	datatosend=bodyTextArea.get("1.0",END).strip()
	data_json=json.dumps(datatosend)
	print("Data Json 1 : ",data_json)

	data_json=data_json.replace('"{\\','{')
	print("Data Json 2 : ",data_json)
	data_json=data_json.replace('\\"}"','"}')
	print("Data Json 3 : ",data_json)
	data_json=data_json.replace('\\','')
	print("Data Json 4 : ",data_json)
	#getting execution time of requests
	start_time=time.time()
	

	if requestType=="GET" :
		response=requests.get(url=urltosend)
		
	else :
		response=requests.post(url=urltosend,data=data_json)
	
	end_time=time.time()

	total_time=end_time-start_time

	#clearing response text area 
	responseTextArea.delete(1.0,END)
	responseData=response.json()
	
	#labels data (converted in String)
	responseStatusCode=str(response.status_code)
	responseTime=str(round(total_time,3))
	responseType=str(response.headers.get('content-type'))
	responseSize=str(response.headers.get('content-length'))

	#printing for checking  all is working accordingly
	print("Response :",responseData)
	print("URL Text: ",urltosend)
	print("data to send: ",datatosend)
	print("data json : ",data_json)
	print("Status Code : ",responseStatusCode)
	print("Time :",responseTime)
	print("Type : ",responseType)
	print("Response Json : ",responseSize)

	#Middle Layer Responses Label 
	responseStatusCodeLabel=Label(Mainwindow,text=responseStatusCode)
	responseTimeLabel=Label(Mainwindow,text=responseTime+" "+str("ms"))
	responseSizeLabel=Label(Mainwindow,text=responseSize+" "+str("KB"))
	responseTypeLabel=Label(Mainwindow,text=responseType)


	#Middle Layer Responses Label Positions
	responseStatusCodeLabel.place(x=127,y=125)
	responseTimeLabel.place(x=370,y=125)
	responseSizeLabel.place(x=622,y=125)
	responseTypeLabel.place(x=790,y=125)

	#Inserting the response in response text area
	responseTextArea.insert(END,responseData)

#after Clicking Body button this fucntion will execute

def bodyButtonFunction():
	print("Body button Clicked")

	#When the text area not visible it has to visible at given Place .

	if not bodyTextArea.visible:
		bodyTextArea.visible=True
		bodyTextArea.place(x=190,y=180) 
	
	#when the text area is visible it has to forget where it was placed .
	else:
		bodyTextArea.visible=False
		bodyTextArea.place_forget()

def responseButtonFunction():
	print("Response button Clicked")

	#When the text area not visible it has to visible at given Place .

	if not responseTextArea.visible:
		responseTextArea.visible=True

		responseTextArea.place(x=190,y=360)

	
	#when the text area is visible it has to forget where it was placed .
	else:
		responseTextArea.visible=False
		responseTextArea.place_forget()

		#responseTextArea.insert(END,data)


#main Function starts
Mainwindow=Tk()
#Window Size
Mainwindow.geometry("1000x1000")  



#Window Title
Mainwindow.title("Rest API") 
#Mainwindow.iconbitmap("logo.png")

#Send Button





sendButton=Button(Mainwindow,text="Send",command=sendButtonFunction,height=2,width=5) 
#photo=PhotoImage(file="logo.png")
#sendButton.config(image=photo,width="70",height="50")
sendButton.place(x=940,y=20)

#URL TextField
urltextField=Text(Mainwindow,relief=RAISED,height=3,width=90) 
urltextField.place(x=190,y=20)

#Option Menu
selectedElement=StringVar(Mainwindow)
selectedElement.set("GET")  #what you want to set First Option By Default in the Option menu 

methodOptions=OptionMenu(Mainwindow,selectedElement,"GET","POST")
methodOptions.place(x=70,y=20,height=53,width=100)

#Labels at Middle Layer
statusLabel=Label(Mainwindow,text="STATUS")
timeLabel=Label(Mainwindow,text="TIME")
sizeLabel=Label(Mainwindow,text="SIZE")
typeLabel=Label(Mainwindow,text="TYPE")



#Label Positions
statusLabel.place(x=125,y=100)
timeLabel.place(x=375,y=100)
sizeLabel.place(x=625,y=100)
typeLabel.place(x=875,y=100)

#Body Button
#photo=PhotoImage(file="coding1.png")
#photo = ImageTk.PhotoImage(Image.open("logo.png"))

bodyButton=Button(Mainwindow,text="Body",command=bodyButtonFunction,height=3,width=12) 
#bodyButton.config(image=photo,width="70",height="50")
bodyButton.place(x=70,y=180)


#Body Text Area
bodyTextArea=Text(Mainwindow,height=10,width=90) 
bodyTextArea.visible=False

#Response Button
responseButton=Button(Mainwindow,text="Response",command=responseButtonFunction,height=3,width=12) 
responseButton.place(x=70,y=360)


#Response Text Area
responseTextArea=Text(Mainwindow,height=17,width=90) 
responseTextArea.visible=False

Mainwindow.mainloop()
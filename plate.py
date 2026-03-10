import requests

API_KEY="YOUR_API_KEY"
url="https://api.platerecognizer.com/v1/plate-reader/"
headers={
	"Authorization":f"Token {API_KEY}" 
}
image_path="/home/sahanasarop7/myenv/vehicle.jpeg"

with open(image_path,"rb")as image_file:
	response=requests.post(
	url,
	headers=headers,
	files={"upload":image_file}
	)

data=response.json()

if "results" in data and len(data["results"])>0:
	plate=data["results"][0]["plate"]
	print("Detected Vehicle Number:",plate.upper())
else:
	print("No plate detected")


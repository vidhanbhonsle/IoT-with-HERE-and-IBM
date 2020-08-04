
# Build a location aware IoT Ecosystem with HERE and IBM Cloud – Part 1

### Introduction
Purpose: To monitor a person's temperate and guide them to reach the nearest hospital in case of emergency. This will be done by tracking their location, sending them the routing instructions and showing the route on map.

This code Pattern will help you understand how an IoT endpoint communicates with the IBM cloud using MQTT protocol over publish-subscribe architecture. You will get an overview of HERE Location Services and learn how to integrate HERE Location service with your IoT device. 
 
## Learning outcomes

- Singup/login to IBM Cloud
- Create 'Internet of Things Platform' service on IBM Cloud
- Connect IoT endpoint with IBM Cloud
- MQTT protocol in publish-subscribe architecture
- Integrating HERE Location Services in IoT endpoint

## Step 1: IBM Cloud Signup/Login 

To create a Free IBM Cloud account click  https://ibm.biz/HERETech5 
You will be redirected to a Sign up page, if you haven't created one yet , Just fill out all the relevant fields and Click on the Create Account button

![image](https://user-images.githubusercontent.com/16270682/89181501-5330ff80-d5ad-11ea-874c-5fd5f4541ee7.png)

An email from IBM Cloud is sent to your Email address that you mentioned when signing up

![image1](https://user-images.githubusercontent.com/16270682/89181700-ad31c500-d5ad-11ea-9689-c93c79f5207e.png)

You will have to check your inbox on the email ID that you mentioned when creating the IBM Cloud account. There you will received an confirmation email from IBM Cloud.Click on Confirm Account Button to activate your Free IBM Cloud account.

![image2](https://user-images.githubusercontent.com/16270682/89181729-b7ec5a00-d5ad-11ea-84a0-cb26ba5db70e.png)

Congrats !, you have now landed on the dashboard of IBM Cloud now we can get started with our workshop

![image4](https://user-images.githubusercontent.com/16270682/89181755-c175c200-d5ad-11ea-9baf-1e0194c79ac9.png)



## Step 2: Create 'Internet of Things Platform' service on IBM Cloud

From the IBM Cloud console, click on Catalog, Select services, Internt of Things, and then select Internet of Things Platform. From here, you can choose a service plan. The Lite plan is free of charge and provides enough capability for most small projects.

<img width="738" alt="1" src="https://user-images.githubusercontent.com/16270682/89185240-5af3a280-d5b3-11ea-93c6-b93b51406114.PNG">

Once you create an IoT platform service instance, you can click on the “Launch” button from the “manage” section to launch it.

<img width="935" alt="2" src="https://user-images.githubusercontent.com/16270682/89185799-3fd56280-d5b4-11ea-834f-2456c83e1592.PNG">

Note down the “Organization ID” of your platform instance in the “Settings” screen.

<img width="667" alt="3" src="https://user-images.githubusercontent.com/16270682/89189801-f5ef7b00-d5b9-11ea-8c4c-5d6cdf00208c.PNG">

## Step 3: Connect IoT endpoint with IBM Cloud

We’ll be using a Raspberry Pi as a gateway between the devices and the IoT Platform service. We need to create a new gateway device type and register it in our IoT Platform service that we just created. You can follow the instructions in the Watson IoT Platform documentation for registering your device.

From the Watson IoT Platform dashboard, select Devices from the sidebar, and then select Device Types. Click Add Device Type.

<img width="891" alt="4" src="https://user-images.githubusercontent.com/16270682/89191450-613a4c80-d5bc-11ea-8177-5febf7765354.PNG">

Add your device with the selected device type, and use the wizard to register your gateway device.

<img width="1428" alt="iotplatform-device" src="https://user-images.githubusercontent.com/16270682/89191736-cb52f180-d5bc-11ea-89b5-8c55d730d218.png">

On the final wizard screen, copy the device credentials, as you’ll not be able to see them again, and we’ll be needing them later on.

<img width="1437" alt="iotplatform-device-credentials" src="https://user-images.githubusercontent.com/16270682/89191794-e1f94880-d5bc-11ea-8979-2f40b2563038.png">


## Step 2: Acquire credentials from HERE Developer Portal
To access any of the APIs, first get your credentials by signing up for a freemium account

[Register](https://developer.here.com/events/community-sa) for a free developer account</br>

## Step 3: Generate apikeys

![RegistrationGif](https://user-images.githubusercontent.com/20164776/89283385-b339ab80-d66a-11ea-963a-646976c6888a.gif)


# TophatAutomator
OBJECTIVE: Pulls the most recent message from a discord channel which pings the TopHat code and automates the process of  having to type in the code for attendance during the lecture 

Documentation of the script 


retreive_messages(): this function takes in the channel id of the discord channel as input which can be changed when calling the function. The function uses an authorization key to log into the account specified in the headers dictionary. Returns the most recent message of the channel 

fill(): This function takes in the tophat code which is returned by the previous function and the authorization headers to submit a post request to the discord API on a channel 

fill_top(): this function does the same as the fill function except it submits a patch/put request to the tophat API 


USE CASE: To automate the need to put tophat codes for attendance even if the student was not there


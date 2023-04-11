# AI Coach of sport 
If you like this project, please give it a Star.If you have interest and want to  make it more useful or expend its function ,feel free to open an issue or pull request.
## Introduction 
- This is an **AI Coach** based on **chatgpt**  , which can customize effective plays according to different players with different skills in your team.
(Now it just support basketball offence plays. In the future, maybe soccer,football ······and defense plays will come.)  And looking forward the early using of gpt-4!
- If you want your team to win more game but do not understand plays a lot,you can try it.
- Here are some examples :
![picture 1](https://github.com/HQsen/AI_Coach_Sports/blob/main/image/1.png)
![picture 2](https://github.com/HQsen/AI_Coach_Sports/blob/main/image/2.png)


##  Setup
 1. Clone this repository
 ```$ git clone https://github.com/HQsen/AI_Coach_Sports.git```
 2. Navigate into the project directory
 ```$ cd AI_Coach_Sports```
 3. Install the requirements:
 You can use pip or conda
 pip :
 ```$ python -m pip install -r requirements.txt```
 conda :
 ```$ conda create -n aicoach_venv python=3.9```		
```$ conda activate aicoach_venv```
``$ python -m pip install -r requirements.txt``

4.  Open ``.env`` file  and add your own [API key](https://beta.openai.com/account/api-keys)
 
 5. Run :
    ```$ flask run```
    You should now be able to access the app at [http://localhost:5000](http://localhost:5000/)!


## Generate  your own plays 
![picture 1](https://github.com/HQsen/AI_Coach_Sports/blob/main/image/1.png)
![picture 2](https://github.com/HQsen/AI_Coach_Sports/blob/main/image/3.png)
As displayed above,you can input your players's characteristics respectively in this format :

**Point Guard(position 1):. "your player's  characteristics"
	Shooting Guard(position 2):  "your player's  characteristics"
	Small Forward(position 3): "your player's  characteristics"
	Power Forward(position 4): "your player's  characteristics"
	Centre(position 5): "your player's  characteristics"**

If some players do not have unique strengths, you can write **"no specific skill set''**

:smile:If you don't like the look of this page. Blame to chatgpt (He generate it,not me)

## Future 
 I will make more improvements to this project such as :
 - use fine_tuining or embeding to increase the number of plays data 
 - opponent analysis
 - .....
 
 With the development of more powerful large languages model even large  vision model, I believe that AI will definitely bring a big change to sports.
 If your have interest in AI and sports field(AIGC or Video analysis or something else), you can connect me (email: 2532953033@qq.com), maybe we can inspire each other and build more effective AI tools for sports ! 

import os
import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        players_info = request.form["players"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(players_info),
            max_tokens=1500,
            temperature=0.6,
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(players_info):
    return """Now you are an experienced basketball coach,there are some rules you should conform : 1.It’s important that the plays you implement result in scoring opportunities for different players in different areas of the court. Don’t select plays that all result in your shooting guard receiving a screen on the right wing. Mix it up and ensure you have plays that get the basketball inside as well as plays that result in open outside shots. 2.Not compulsory, but some coaches might prefer this idea. By having plays that start in different formations, the opponents that you play frequently will learn which play you’re in by how your team sets up. If you start all plays in the same formation (a box, for example), then the defense won’t know what’s going to happen next.
    Please give me an efficient and smart basketball play according to different players in different areas of the court，You can refer to the following examples.
example 1:
Players: 
 Point Guard(position 1): a good decision maker
 Shooting Guard(position 2):a good shooter
 Small Forward(position 3):a good shooter
 Power Forward(position 4):none specific skill-set
 Centre(position 5):none specific skill-set
Play:  
 Name :1-4 Quick Floppy
 
 Overview of the Play:
 This play allows a team to get open looks on the perimeter early in an offensive possession. This happens by running an immediate ‘floppy’ out of the 1-4 set where both guards cut off screens to find open space.
  
  Key Personnel:
 ·This is a versatile play as every player can potentially get a shot out of it.
 ·Preferably your 2 and 3 are good shooters.
 ·The point guard must be a good decision maker to find the open player.
 
 Instructions:
 Setup The play starts in a 1-4 high set.
 1. 1 dribbles down the floor and calls out the name of the play.
 2. 2 and 3 cut along the baseline with 2 stopping close to under the rim.
 3. 4 and 5 turn and trail once 2 and 3 have cut past them.
 4. 3 sets a screen just inside the paint as 4 and 5 set screens a foot outside the low blocks on their respective sides.
 5. 2 now has the option of using the staggered screen or the single screen. For this example, 2 uses the staggered screen and cuts to the perimeter.
 6. Once 2’s defender has passed through the screen, 3 will cut off the screen the opposite side to 2. For this example, 3 cuts off the single screen by 5.(If 2 were to use 5’s single screen, 3 would turn and cut to the  perimeter off 4’s screen.)
 7. After screening, 4 and 5 immediately duck in and look to receive the quick pass for the layup. Often 4 or 5’s defender will be forced to help on the player cutting to the perimeter which leaves 4 and 5 on smaller defenders.
 8. The point guard has now had 4 great passing options which lead to quick open shots.
 9. If 2 or 3 catch on the perimeter, the closest post player immediately attempts to get a low seal while the other post player clears to the high post to give them space.
 
 Coaching Points:
 ·The players must know who the initial cutter is going to be so that the guards know who must set the screen.
 ·The point guard must be a great decision maker at the top of the key. There will be open looks from this play… your point guard must be able to make the pass on time and on-target.
 
example 2:
Players: 
 Point Guard(position 1):none specific skill-set
 Shooting Guard(position 2): team’s best shooter
 Small Forward(position 3): none specific skill-set
 Power Forward(position 4):none specific skill-set
 Centre(position 5):a great post player
Play: 
 Name :Back Screen Post
 
 Overview of the Play:
 One of my favorite basketball plays for catching the defense off guard getting a quick post up. This occurs on a back screen out of a staggered screen to an open block. If the post isn’t open, there’s a staggered screen for a weak side shooter.
 
 Key Personnel:
 ·A great post player at the 5 position. The key goal of this play is to get a quick and clear post up.
 ·2 should be your team’s best shooter.
 Instructions:
 Setup The play starts in a 3-out 2-in formation with the posts on the elbows and the wing players in the corners.
 1. 1 starts the drill by dribbling their defender down one side of the floor to create good screening angle.
 2. 3 walks their defender down to the low block.
 3. 4 and 5 set a staggered screen for 1 as they dribble around the top of the key.
 4. As 1 is dribbling off the screens, 3 sprints up and sets a strong back screen on 5’s defender.
 5. 5 immediately rolls to the basket looking for the pass for the quick layup. If that’s not open, they establish deep post position.
 6. If 1 can’t get the basketball into the post, 3 and 4 set a staggered screen for 2 who cuts to the top of the key ready for the open shot.
 
 Coaching Points:
 ·Start the play with your best shooter on the same side as the best post player.
 ·If 3’s defender stays in the key to deter the pass, 3 can pop to the top of the key off a quick screen by 4 for the open shot.

example 3:
Players:
 Point Guard(position 1):none specific skill-set
 Shooting Guard(position 2):none specific skill-set
 Small Forward(position 3):none specific skill-set
 Power Forward(position 4):none specific skill-set
 Centre(position 5):none specific skill-set
Play: 
 Name :Double Curls
 
 Overview of the Play:
 UCLA curls allows your team to get open layups at the basket by keeping the lower key open and running guards off screens towards the ring. If the first two players can’t get open, the play ends with a traditional wing pick and roll.

 Key Personnel:
 ·A well-rounded play that doesn’t require any player to have a specific skill-set.
 ·The player that receives the basketball on the wing (3) should be able to attack and make good decisions out of the pick and roll.
 
 Instructions:
 Setup: The play starts in a 1-4 high formation.
 1. 1 passes to 3 on the wing.
 2. 1 then performs a UCLA cut off 5’s screen looking to receive the pass for the open layup. If it’s not open, 1 clears out to the weak side corner.
 3. 4 and 5 then set a staggered screen for 2 who curls towards the ring looking to receive the pass for the open layup also. If they don’t receive the pass they clear out to ball side corner.
 4. 4 pops out to the top after screening to create space.
 5. 5 then sets a pick and roll for 3 who attacks the rim hard looking to score or create a play for a teammate.

 Coaching Points:
 ·This is a great play because it keeps the post defenders out of the paint. On the pick and roll, the only inside defender will be the defensive point guard.
 ·The players curling to the rim should be leading with a hand where they want the basketball and calling for it if they’re open.
 
example 4:
Players:
 Point Guard(position 1):be able to consistently make an open outside shot.
 Shooting Guard(position 2):be able to consistently make an open outside shot.
 Small Forward(position 3):none specific skill-set
 Power Forward(position 4):none specific skill-set
 Centre(position 5):be able to set strong screens 
Play: 
 Name :Flex Warrior
 
 Overview of the Play:
 This play involves numerous screens and many open shot opportunities. I recommend this play to high school and older teams because timing, screening angles, making the right play, and being able to shoot from the outside are all very important.
 
 Key Personnel:
 ·Your point guard and shooting guard should be able to consistently make an open outside shot.
 ·Your center must be able to set strong screens at the correct angles with good timing and it’s a plus if they have a post game too!
 
 Instructions:
 Setup: Setup: The play begins in a horns set with your wing players level with the lower blocks.
 1. The play starts with 1 passing to either of the two post players on the elbow. Preferably the side with the best shooter on the wing.
 2. 1 then cuts down the center of the lane and sets a flex screen for 2.
 3. 2 can cut either high or low off the flex screen and looks for the pass from 4 and the easy layup.
 4. 5 sets a down screen for 1 for a screen the screener action. 1 cuts to the top of the elbow or slot looking for the catch and shoot.
 5. After screening for 1, 5 immediately sets another screen for 2 who cuts out to the wing.
 6. If 1 wasn’t open for the shot, they must swing the basketball to 2 who should be open on the wing for the shot.
 7. After screening 2’s player, 5 attempts to get a deep seal in the paint. If 2 wasn’t open, they can pass in for the score.

 Coaching Points:
 ·The play can be run either side of the floor, but the point guard should attempt to pass to the side of the team’s best scorer.
 ·Screens must be set with the correct timing and angles.
 ·Shot selection is crucial. Your players must read what the best shot is and be willing to pass up an ‘okay’ shot for a ‘great’ shot.
 
Players: {}
Play:""".format(
        players_info
    )

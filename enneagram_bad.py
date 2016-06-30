import random
import os

print("Enter in the number that corresponds with the way that you feel suits you best.")
print("")
name = str(input("What is your name? "))
print("")

os.system('clear')

the_peacemaker = the_loyalist = the_achiever = the_reformer = the_individualist = the_helper = the_challenger = the_investigator = the_enthusiast = 0


questions = [0,"I've been romantic and imaginative (1) or I've been pragmatic and down-to-earth (2): ","I have tended to take on confrontations (1) or I have tended to avoid confrontations (2): ","I have typically been diplomatic, charming, and ambitious (1) or I have typically been direct, formal, and idealistic (2): ","I have tended to be focused and intense (1) or I have tended to be spontaneous and fun-loving (2): ","I have been the_peacemaker hospitable person and have enjoyed welcoming new friends into my life (1) or I have been a private person and have not mixed much with others (2): ","It's been difficult for me to relax and stop worrying about potential problems (1) or It's been difficult for me to get myself worked up about potential problems (2): ","I've been more of a 'street-smart' survivor (1) or I've been more of a 'high-minded' idealist (2): ","I have needed to show people affection (1) or I have preferred to maintain some distance with people (2): ","When presented with a new experience, I've usually asked myself if it would be useful to me (1) or When presented with a new experience, I've usually asked myself if it would be enjoyable (2): ","I have tended to focus too much on myself (1) or I have tended to focus too much on others (2): ","Others have depended on my insight and knowledge (1) or Others have depended on my strength and decisiveness (2): ","I have come across as being too unsure of myself (1) or I have come across as being too sure of myself (2): ","I have been more relationship-oriented than goal-oriented (1) or I have been more goal-oriented than relationship-oriented (2): ","I have not been able to speak up for myself very well (1) or I have been outspoken--I've said what others wished they had the nerve to say (2): ","It's been difficult for me to stop considering alternatives and do something definite (1) or It's been difficult for me to take it easy and be more flexible (2): ","I have tended to be careful and hesitant (1) or I have tended to be bold and domineering (2): ","My reluctance to get too involved has gotten into trouble people (1) or My eagerness to have people depend on me has gotten me into trouble with them (2): ","Usually, I have been able to put my feelings aside to get the job done (1) or Usually, I have needed to work through my feelings before I could act (2): ","Generally, I've been methodical and cautious (1) or Generally, I've been adventurous and taken risks (2): ","I have tended to be a supportive, giving person who seeks intimacy with others (1) or I have tended to be a serious, reserved person who likes discussing issues (2): ","I've often felt the need to be a 'Pillar of Strength' (1) or I've often felt the need to perform perfectly (2): ","I've typically been interested in asking tough questions and maintaining my independence (1) or I've typically been interested in maintaining my stability and peace of mind (2): ","I've been a bit cynical and skeptical (1) or I've been a bit mushy and sentimental (2): ","I've often worried that I'm missing out on something better (1) or I've often worried that if I let down my guard, someone will take advantage of me (2): ","My habit of being 'stand-offish' has annoyed people (1) or My habit of telling people what to do has annoyed people (2): ","I have tended to get anxious if there was too much excitement and stimulation (1) or I have tended to get anxious if there wasn't enough excitement and stimulation (2): ","I have depended on my friends and they have known that they can depend on me (1) or I have not depended on people; I have done things on my own (2): ","I have tended to be detached and preoccupied (1) or I have tended to be moody and self-absorbed (2): ","I have liked to challenge people and 'shake them up' (1) or I have liked to comfort people and calm them down (2): ","I have generally been an outgoing, sociable person (1) or I have generally been an earnest, self-disciplined person (2): ","I've wanted to 'fit in' with others--I get uncomfortable when I stand out too much (1) or 've wanted to stand out from others--I get uncomfortable when I don't distinguish myself (2): ","Pursuing my personal interests has been more important to me than having stability and security (1) or Having stability and security has been more important to me than pursuing my personal interests (2): ","When I've had conflicts with others, I've tended to withdraw (1) or When I've had conflicts with others, I've rarely backed down (2): ","I have given in too easily and let others push me around (1) or I have been too uncompromising and demanding with others (2): ","I've been appreciated for my unsinkable spirit and resourcefulness (1) or I've been appreciated for my deep caring and personal warmth (2): ","I have wanted to make a favorable impression on others (1) or I have cared little about making a favorable impression on others (2): ","I've depended on my perseverance and common sense (1) or I've depended on my imagination and moments of inspiration (2): ","Basically, I have been easy-going and agreeable (1) or Basically, I have been hard-driving and assertive (2): ","I have worked hard to be accepted and well-liked (1) or Being accepted and well-liked has not been a high priority for me (2): ","In reaction to pressure from others, I have become more withdrawn (1) or In reaction to pressure from others, I have become more assertive (2): ","People have been interested in my because I've been outgoing, engaging, and interested in them (1) or People have been interested in me because I've been quiet, unusual, and deep (2): ","Duty and responsibility have been important values for me (1) or Harmony and acceptance have been important values for me (2): ","I've tried to motivate people by making big plans and big promises (1) or I've tried to motivate people by pointing out the consequences of not following my advice (2): ","I have seldom been emotionally demonstrative (1) or I have often been emotionally demonstrative (2): ","Dealing with details has not been one of my strong suits (1) or I have excelled at dealing with details (2): ","I have often emphasized how different I am from most people, especially my family (1) or I have often emphasized how much I have in common with most people, especially my family (2): ","When situations have gotten heated, I have tended to stay on the sidelines (1) or When situations have gotten heated, I have tended to get right into the middle of things (2): ","I have stood by my friends, even when they have been wrong (1) or I have not wanted to compromise what is right, even for friendship (2): ","I've been a well-meaning supporter(1) or I've been a highly-motivated go-getter (2): ","When troubled, I have ended to brood about my problems (1) or When troubled, I have tended to find distractions for myself (2): ","Generally, I've had strong convictions and a sense of how things should be (1) or Generally, I've had serious doubts and have questioned how things seemed to be (2): ","I've created problems with others by being pessimistic and complaining (1) or I've created problems by being bossy and controlling (2): ","I have tended to act on my feelings and let the 'chips fall where they may' (1) or I have tended not to act on my feelings lest they stir up more problems (2): ","Being the center of attention has usually felt natural to me (1) or Being the center of attention has usually felt strange to me (2): ","I've been careful and have tried to prepare for unforeseen problems (1) or I've been spontaneous and have referred to improvise as problems come up (2): ","I have gotten angry when others have not shown enough appreciation for what I have done for them (1) or I have gotten angry when others have not listened to what I have told them (2): ","Being independent and self-reliant has been important to me (1) or Being valued and admired has been important to me (2): ","When I've debated with friends, I've tended to press my arguments forcefully (1) or When I've debated with friends, I've tended to let things go to prevent hard feelings (2): ","I have often been possessive of loved ones--I have had trouble letting them be (1) or I have often 'tested' loved ones to see if they were really there for me (2): ","Organizing resources and making things happen has been one of my major strengths (1) or Coming up with new ideas and getting people excited about them has been one of my major strengths (2): ","I've tended to be driven and very hard on myself (1) or I've tended to be too emotional and rather undisciplined (2): ","I have tried to keep my life fast-paced, intense, and exciting (1) or I have tried to keep my life regular, stable, and peaceful (2): ","Even though I've had successes, I've tended to doubt my abilities (1) or Even though I've had setbacks, I've had a lot of confidence in my abilities (2): ","I generally have tended to dwell on my feelings and to hold onto them for a long time (1) or I generally have tended to minimize my feelings and not pay very much attention to them (2): ","I have provided many people with attention and nurturance (1) or I have provided many people with direction and motivation (2): ","I've been a bit serious and strict with myself (1) or I've been a bit free-wheeling and permissive with myself (2): ","I've been self-assertive and driven to excel (1) or I've been modest and have been happy to go at my own pace (2): ","I have been proud of my clarity and objectivity (1) or I have been proud of my reliability and commitment (2): ","I have spent a lot of time looking inward--understanding my feelings has been important to me (1) or I have not spent much time looking inward--getting things done has been important to me (2): ","Generally, I have thought of myself as a sunny, casual person (1) or Generally, I have thought of myself as a serious, dignified person (2): ","I've had an agile mind and boundless energy (1) or I've had a caring heart and deep dedication (2): ","I have pursued activities that had a substantial potential for reward and personal recognition (1) or I have been willing to give up reward and personal recognition if it meant doing work I was really interested in (2): ","Fulfilling social obligations has seldom been high on my agenda (1) or I have usually taken my social obligations very seriously (2): ","In most situations, I have preferred to take the lead (1) or In most situations, I have preferred to let someone else take the lead (2): ","Over the years, my values and lifestyle have changed several times (1) or Over the years, my values and lifestyle have remained fairly constant (2): ","Typically, I have not had much self-discipline (1) or Typically, I have not had much connection with people (2): ","I have tended to withhold my affection and have wanted others to come into my world (1) or I have tended to give my affection too freely and have wanted to extend myself to others (2): ","I have had a tendency to think of worst-case scenarios (1) or I have had a tendency to think that everything will work out for the best (2): ","People have trusted me because I am confident and can look out for them (1) or People have trusted me because I am fair and will do what is right (2): ","Often, I have been so involved in my own projects that I have become isolated from others (1) or Often, I have been so involved with others that I have neglected my own projects (2): ","When meeting someone new, I have usually been poised and self-contained (1) or When meeting someone new, I have usually been chatty and entertaining (2): ","Generally speaking, I have tended to be pessimistic (1) or Generally speaking, I have tended to be optimistic (2): ","I have preferred to inhabit my own little world (1) or I have preferred to let the world know I'm here (2): ","I have often been troubled by nervousness, insecurity, and doubt (1) or I have often been troubled by anger, perfectionism, and impatience (2): ","I realize that I have often been too personal and intimate (1) or I realize that I have often been too cool and aloof (2): ","I have lost out because I have not felt up to taking opportunities (1) or I have lost out because I have pursued too many possibilities (2): ","I have tended to take a long time to get into action (1) or I have tended to get into action quickly (2): ","I usually have had difficulty making decisions (1) or I seldom have had difficulty making decisions (2): ","I have had a tendency to come on a little too strong with people (1) or I have had a tendency not to assert myself enough with people (2): ","Typically, I have been even-tempered (1) or Typically, I have had strong changes of mood (2): ","When I've been unsure of what to do, I've often sought the advice of others (1) or When I've been unsure of what to do, I've tried different things to see what worked best for me (2): ","I have worried that I would be left out of others' activities (1) or I have worried that others' activities would distract me from what I had to do (2): ","Typically, when I have gotten angry, I have told people off (1) or Typically, when I have gotten angry, I have become distant (2): ","I've tended to have trouble falling asleep (1) or I've tended to fall asleep easily (2): ","I have often tried to figure out how I could get closer to others (1) or I have often tried to figure out what others want from me (2): ","I have usually been measured, straight-talking, and deliberate (1) or I have usually been excitable, fast-talking, and witty (2): ","Often, I have not spoken up when I've seen others making a mistake (1) or Often, I have helped others see that they are making a mistake (2): ","During most of my life, I have been a stormy person who has had many volatile feelings (1) or During most of my life, I have been a steady person in whom 'still waters run deep' (2): ","When I have disliked people, I have usually tried hard to stay cordial--despite my feelings (1) or When I have disliked people, I have usually let them know it--one way or the other (2): ","Much of my difficulty with people has come from my touchiness and taking everything too personally (1) or Much of my difficulty with people has come from my not caring about social conventions (2): ","My approach has been to jump in and rescue people (1) or My approach has been to show people how to help themselves (2): ","Generally, I have enjoyed 'letting go' and pushing the limits (1) or Generally, I have not enjoyed losing control of myself very much (2): ","I've been overly concerned with doing better than others (1) or I've been overly concerned with making things okay for others (2): ","My thoughts generally have been speculative--involving my imagination and curiosity (1) or My thoughts generally have been practical--just trying to keep things going (2): ","One of my main assets has been my ability to take charge of situations (1) or One of my main assets has been my ability to describe internal states (2): ","I have pushed to get things done correctly, even if it made people uncomfortable (1) or I have not liked feeling pressured, so I have not liked pressuring anyone else (2): ","I've often taken pride in how important I am in others' lives (1) or I've often taken pride in my gusto and openness to new experiences (2): ","I have perceived that I've often come across to others as presentable, even admirable (1) or I have perceived that I've often come across to others as unusual, even odd (2): ","I have mostly done what I had to do (1) or I have mostly done what I wanted to do (2): ","I have usually enjoyed high-pressure, even difficult situations (1) or I have usually disliked being in high-pressure, even difficult, situations (2): ","I've been proud of my ability to be flexible--what's appropriate or important often changes (1) or I've been proud of my ability to take a stand--I've been firm about what I believe in (2): ","My style has leaned toward spareness and austerity (1) or My style has leaned toward excess and overdoing things (2): ","My own health and well-being have suffered because of my strong desire to help others (1) or My relationships have suffered because my strong desire to attend to my personal needs (2): ","Generally speaking, I've been too open and naive (1) or Generally speaking, I've been too wary and guarded (2): ","I have sometimes put people off by being too aggressive (1) or I have sometimes put people off by being too 'uptight' (2): ","Being of service and attending to the needs of others has been a high priority for me (1) or Finding alternatives ways of seeing and doing things has been a high priority for me (2): ","I've been single-minded and persistent in pursuing my goals (1) or I've preferred to explore various courses of action to see where they lead (2): ","I have frequently been drawn to situations that stir up deep, intense emotions (1) or I have frequently been drawn to situations that make me feel calm and at ease (2): ","I have cared less about practical results than about pursuing my interests (1) or I have been practical and have expected my work to have concrete results (2): ","I have had a deep need to belong (1) or I have had a deep need to feel balanced (2): ","In the past, I've probably insisted on too much closeness in my friendships (1) or In the past, I've probably kept too much distance in my friendships (2): ","I've had a tendency to keep thinking about things from the past (1) or I've had a tendency to keep anticipating things I'm going to do (2): ","I've tended to see people as intrusive and demanding (1) or I've tended to see people as disorganized and irresponsible (2): ","Generally, I have not had much confidence in myself (1) or Generally, I have had confidence only in myself (2): ","I've probably been too passive and uninvolved (1) or I've probably been too controlling and manipulative (2): ","I've frequently been stopped in my tracks by my self-doubt (1) or I've rarely let self-doubt stand in my way (2): ","Given a choice between something familiar and something new, I've usually chosen something new (1) or I've generally chosen what I knew I already liked: why be disappointed with something I might not like? (2): ","I have given a lot of physical contact to reassure others about how I feel about them (1) or I have generally felt that real love does not depend on physical contact (2): ","When I've needed to confront someone, I've often been too harsh and direct (1) or When I've needed to confront someone, I've often 'beaten around the bush' too much (2): ","I have been attracted to subjects that others would probably find disturbing, even frightening (1) or I have preferred not to spend my time dwelling on disturbing, frightening, subjects (2): ","I have gotten into trouble with people by being too intrusive and interfering (1) or I have gotten into trouble with people by being too evasive and uncommunicative (2): ","I've worried that I don't have the resources to fulfill the responsibilities I've taken on (1) or I've worried that I don't have the self-discipline to focus on what will really fulfill me (2): ","Generally, I've been a highly intuitive, individualistic person (1) or Generally, I've been a highly organized, responsible person (2): ","Overcoming inertia has been one of my main problems (1) or Being unable to slow down has been one of my main problems (2): ","When I've felt insecure, I've reacted by becoming dismissive (1) or When I've felt insecure, I've reacted by becoming defensive and argumentative (2): ","I have generally been open-minded and willing to try new approaches (1) or I have generally been self-revealing and willing to share my feelings with others (2): ","I've presented myself to others as tougher than I really am (1) or I've presented myself to others as caring more than I really do (2): ","I usually have followed my conscience and reason (1) or I usually have followed my feelings and impulses (2): ","Serious adversity has made me feel hardened and resolute (1) or Serious adversity has made me feel discouraged and resigned (2): ","I usually have made sure that I had some kind of 'safety net' to fall back on (1) or I usually have chosen to live on the edge and to depend on others as little as possible (2): ","I've had to be strong for others, so I haven't had time to deal with my feelings and fears (1) or I've had difficulty coping with my feelings and fears, so it's been hard for me to be strong for others (2): ","I have often wondered why people focus on the negative when there is so much that's wonderful about life (1) or I have often wondered why people are so happy when so much in life is messed up (2): ","I have tried hard not to be seen as a selfish person (1) or I have tried hard not to be seen as a boring person (2): ","I have avoided intimacy when I feared I would be overwhelmed by people's needs and demands (1) or I have avoided intimacy when I feared I would not be able to live up to people's expectations of me (2): "]
array = []

def shufarray():
    count = 0
    while(count != 144):
        count += 1
        array.append(count)
    random.shuffle(array)

shufarray()

numb = [0]
def time():
    order = 0
    while(order != 144):
        order += 1
        numb.append(order)

time()

q = [0]
z = 1

the_helper = open('questions.txt','w')
for item in questions:
    the_helper.write(str(item) + '\n')

for x in array:
    print(numb[z], end=". "),
    n = input(questions[x])
    while(n != '1' and n != '2'):
        print("Please try again")
        n = input()
    q.append(n)
    print('')
    z += 1
    os.system('clear')

for x in range(len(q)):
    if q[x] == '1' or q[x] == '2':
        q[x] = int(q[x])
    else:
        q[x] = 0

if (q[1] == 1):
    the_individualist += 1
if (q[1] == 2):
    the_loyalist += 1

if (q[2] == 1):
    the_challenger += 1
if (q[2] == 2):
    the_peacemaker += 1

if (q[3] == 1):
    the_achiever += 1
if (q[3] == 2):
    the_reformer += 1

if (q[4] == 1):
    the_investigator += 1
if (q[4] == 2):
    the_enthusiast += 1

if (q[5] == 1):
    the_helper += 1
if (q[5] == 2):
    the_individualist += 1

if (q[6] == 1):
    the_loyalist += 1
if (q[6] == 2):
    the_peacemaker += 1

if (q[7] == 1):
    the_challenger += 1
if (q[7] == 2):
    the_reformer += 1

if (q[8] == 1):
    the_helper += 1
if (q[8] == 2):
    the_investigator += 1

if (q[9] == 1):
    the_achiever += 1
if (q[9] == 2):
    the_enthusiast += 1

if (q[10] == 1):
    the_individualist += 1
if (q[10] == 2):
    the_peacemaker += 1

if (q[11] == 1):
    the_investigator += 1
if (q[11] == 2):
    the_challenger += 1

if (q[12] == 1):
    the_loyalist += 1
if (q[12] == 2):
    the_reformer += 1

if (q[13] == 1):
    the_helper += 1
if (q[13] == 2):
    the_achiever += 1

if (q[14] == 1):
    the_individualist += 1
if (q[14] == 2):
    the_enthusiast += 1

if (q[15] == 1):
    the_investigator += 1
if (q[15] == 2):
    the_reformer += 1

if (q[16] == 1):
    the_loyalist += 1
if (q[16] == 2):
    the_challenger += 1

if (q[17] == 1):
    the_peacemaker = a + 1
if (q[17] == 2):
    the_helper = f + 1

if (q[18] == 1):
    the_achiever = c + 1
if (q[18] == 2):
    the_individualist = e + 1

if (q[19] == 1):
    the_loyalist = b + 1
if (q[19] == 2):
    the_enthusiast = i + 1

if (q[20] == 1):
    the_helper = f + 1
if (q[20] == 2):
    the_reformer = d + 1

if (q[21] == 1):
    the_challenger = g + 1
if (q[21] == 2):
    the_achiever = c + 1

if (q[22] == 1):
    the_investigator = h + 1
if (q[22] == 2):
    the_peacemaker = a + 1

if (q[23] == 1):
    the_loyalist = b + 1
if (q[23] == 2):
    the_helper = f + 1

if (q[24] == 1):
    the_enthusiast = i + 1
if (q[24] == 2):
    the_challenger = g + 1

if (q[25] == 1):
    the_individualist = e + 1
if (q[25] == 2):
    the_reformer = d + 1

if (q[26] == 1):
    the_peacemaker = a + 1
if (q[26] == 2):
    the_enthusiast = i + 1

if (q[27] == 1):
    the_loyalist = b + 1
if (q[27] == 2):
    the_achiever = c + 1

if (q[28] == 1):
    the_investigator = h + 1
if (q[28] == 2):
    the_individualist = e + 1

if (q[29] == 1):
    the_challenger = g + 1
if (q[29] == 2):
    the_helper = f + 1

if (q[30] == 1):
    the_enthusiast = i + 1
if (q[30] == 2):
    the_reformer = d + 1

if (q[31] == 1):
    the_peacemaker = a + 1
if (q[31] == 2):
    the_achiever = c + 1

if (q[32] == 1):
    the_investigator = h + 1
if (q[32] == 2):
    the_loyalist = b + 1

if (q[33] == 1):
    the_individualist = e + 1
if (q[33] == 2):
    the_challenger = g + 1

if (q[34] == 1):
    the_peacemaker = a + 1
if (q[34] == 2):
    the_reformer = d + 1

if (q[35] == 1):
    the_enthusiast = i + 1
if (q[35] == 2):
    the_helper = f + 1

if (q[36] == 1):
    the_achiever = c + 1
if (q[36] == 2):
    the_investigator = h + 1

if (q[37] == 1):
    the_loyalist = b + 1
if (q[37] == 2):
    the_individualist = e + 1

if (q[38] == 1):
    the_peacemaker = a + 1
if (q[38] == 2):
    the_challenger = g + 1

if (q[39] == 1):
    the_achiever = c + 1
if (q[39] == 2):
    the_reformer = d + 1

if (q[40] == 1):
    the_investigator = h + 1
if (q[40] == 2):
    the_enthusiast = i + 1

if (q[41] == 1):
    the_helper = f + 1
if (q[41] == 2):
    the_individualist = e + 1

if (q[42] == 1):
    the_loyalist = b + 1
if (q[42] == 2):
    the_peacemaker = a + 1

if (q[43] == 1):
    the_challenger = g + 1
if (q[43] == 2):
    the_reformer = d + 1

if (q[44] == 1):
    the_investigator = h + 1
if (q[44] == 2):
    the_helper = f + 1

if (q[45] == 1):
    the_enthusiast = i + 1
if (q[45] == 2):
    the_achiever = c + 1

if (q[46] == 1):
    the_individualist = e + 1
if (q[46] == 2):
    the_peacemaker = a + 1

if (q[47] == 1):
    the_investigator = h + 1
if (q[47] == 2):
    the_challenger = g + 1

if (q[48] == 1):
    the_loyalist = b + 1
if (q[48] == 2):
    the_reformer = d + 1

if (q[49] == 1):
    the_helper = f + 1
if (q[49] == 2):
    the_achiever = c + 1

if (q[50] == 1):
    the_individualist = e + 1
if (q[50] == 2):
    the_enthusiast = i + 1

if (q[51] == 1):
    the_reformer = d + 1
if (q[51] == 2):
    the_investigator = h + 1

if (q[52] == 1):
    the_loyalist = b + 1
if (q[52] == 2):
    the_challenger = g + 1

if (q[53] == 1):
    the_helper = f + 1
if (q[53] == 2):
    the_peacemaker = a + 1

if (q[54] == 1):
    the_achiever = c + 1
if (q[54] == 2):
    the_individualist = e + 1

if (q[55] == 1):
    the_loyalist = b + 1
if (q[55] == 2):
    the_enthusiast = i + 1

if (q[56] == 1):
    the_helper = f + 1
if (q[56] == 2):
    the_reformer = d + 1

if (q[57] == 1):
    the_challenger = g + 1
if (q[57] == 2):
    the_achiever = c + 1

if (q[58] == 1):
    the_investigator = h + 1
if (q[58] == 2):
    the_peacemaker = a + 1

if (q[59] == 1):
    the_helper = f + 1
if (q[59] == 2):
    the_loyalist = b + 1

if (q[60] == 1):
    the_challenger = g + 1
if (q[60] == 2):
    the_enthusiast = i + 1

if (q[61] == 1):
    the_reformer = d + 1
if (q[61] == 2):
    the_individualist = e + 1

if (q[62] == 1):
    the_enthusiast = i + 1
if (q[62] == 2):
    the_peacemaker = a + 1

if (q[63] == 1):
    the_loyalist = b + 1
if (q[63] == 2):
    the_achiever = c + 1

if (q[64] == 1):
    the_individualist = e + 1
if (q[64] == 2):
    the_investigator = h + 1

if (q[65] == 1):
    the_helper = f + 1
if (q[65] == 2):
    the_challenger = g + 1

if (q[66] == 1):
    the_reformer = d + 1
if (q[66] == 2):
    the_enthusiast = i + 1

if (q[67] == 1):
    the_achiever = c + 1
if (q[67] == 2):
    the_peacemaker = a + 1

if (q[68] == 1):
    the_investigator = h + 1
if (q[68] == 2):
    the_loyalist = b + 1

if (q[69] == 1):
    the_individualist = e + 1
if (q[69] == 2):
    the_challenger = g + 1

if (q[70] == 1):
    the_peacemaker = a + 1
if (q[70] == 2):
    the_reformer = d + 1

if (q[71] == 1):
    the_enthusiast = i + 1
if (q[71] == 2):
    the_helper = f + 1

if (q[72] == 1):
    the_achiever = c + 1
if (q[72] == 2):
    the_investigator = h + 1

if (q[73] == 1):
    the_individualist = e + 1
if (q[73] == 2):
    the_loyalist = b + 1

if (q[74] == 1):
    the_challenger = g + 1
if (q[74] == 2):
    the_peacemaker = a + 1

if (q[75] == 1):
    the_achiever = c + 1
if (q[75] == 2):
    the_reformer = d + 1

if (q[76] == 1):
    the_enthusiast = i + 1
if (q[76] == 2):
    the_investigator = h + 1

if (q[77] == 1):
    the_individualist = e + 1
if (q[77] == 2):
    the_helper = f + 1

if (q[78] == 1):
    the_loyalist = b + 1
if (q[78] == 2):
    the_peacemaker = a + 1

if (q[79] == 1):
    the_challenger = g + 1
if (q[79] == 2):
    the_reformer = d + 1

if (q[80] == 1):
    the_investigator = h + 1
if (q[80] == 2):
    the_helper = f + 1

if (q[81] == 1):
    the_achiever = c + 1
if (q[81] == 2):
    the_enthusiast = i + 1

if (q[82] == 1):
    the_individualist = e + 1
if (q[82] == 2):
    the_peacemaker = a + 1

if (q[83] == 1):
    the_investigator = h + 1
if (q[83] == 2):
    the_challenger = g + 1

if (q[84] == 1):
    the_loyalist = b + 1
if (q[84] == 2):
    the_reformer = d + 1

if (q[85] == 1):
    the_helper = f + 1
if (q[85] == 2):
    the_achiever = c + 1

if (q[86] == 1):
    the_individualist = e + 1
if (q[86] == 2):
    the_enthusiast = i + 1

if (q[87] == 1):
    the_investigator = h + 1
if (q[87] == 2):
    the_reformer = d + 1

if (q[88] == 1):
    the_loyalist = b + 1
if (q[88] == 2):
    the_challenger = g + 1

if (q[89] == 1):
    the_helper = f + 1
if (q[89] == 2):
    the_peacemaker = a + 1

if (q[90] == 1):
    the_achiever = c + 1
if (q[90] == 2):
    the_individualist = e + 1

if (q[91] == 1):
    the_loyalist = b + 1
if (q[91] == 2):
    the_enthusiast = i + 1

if (q[92] == 1):
    the_helper = f + 1
if (q[92] == 2):
    the_reformer = d + 1

if (q[93] == 1):
    the_challenger = g + 1
if (q[93] == 2):
    the_achiever = c + 1

if (q[94] == 1):
    the_investigator = h + 1
if (q[94] == 2):
    the_peacemaker = a + 1

if (q[95] == 1):
    the_helper = f + 1
if (q[95] == 2):
    the_loyalist = b + 1

if (q[96] == 1):
    the_challenger = g + 1
if (q[96] == 2):
    the_enthusiast = i + 1

if (q[97] == 1):
    the_individualist = e + 1
if (q[97] == 2):
    the_reformer = d + 1

if (q[98] == 1):
    the_enthusiast = i + 1
if (q[98] == 2):
    the_peacemaker = a + 1

if (q[99] == 1):
    the_achiever = c + 1
if (q[99] == 2):
    the_loyalist = b + 1

if (q[100] == 1):
    the_individualist = e + 1
if (q[100] == 2):
    the_investigator = h + 1

if (q[101] == 1):
    the_helper = f + 1
if (q[101] == 2):
    the_challenger = g + 1

if (q[102] == 1):
    the_enthusiast = i + 1
if (q[102] == 2):
    the_reformer = d + 1

if (q[103] == 1):
    the_achiever = c + 1
if (q[103] == 2):
    the_peacemaker = a + 1

if (q[104] == 1):
    the_investigator = h + 1
if (q[104] == 2):
    the_loyalist = b + 1

if (q[105] == 1):
    the_challenger = g + 1
if (q[105] == 2):
    the_individualist = e + 1

if (q[106] == 1):
    the_reformer = d + 1
if (q[106] == 2):
    the_peacemaker = a + 1

if (q[107] == 1):
    the_helper = f + 1
if (q[107] == 2):
    the_enthusiast = i + 1

if (q[108] == 1):
    the_achiever = c + 1
if (q[108] == 2):
    the_investigator = h + 1

if (q[109] == 1):
    the_loyalist = b + 1
if (q[109] == 2):
    the_individualist = e + 1

if (q[110] == 1):
    the_challenger = g + 1
if (q[110] == 2):
    the_peacemaker = a + 1

if (q[111] == 1):
    the_achiever = c + 1
if (q[111] == 2):
    the_reformer = d + 1

if (q[112] == 1):
    the_investigator = h + 1
if (q[112] == 2):
    the_enthusiast = i + 1

if (q[113] == 1):
    the_helper = f + 1
if (q[113] == 2):
    the_individualist = e + 1

if (q[114] == 1):
    the_peacemaker = a + 1
if (q[114] == 2):
    the_loyalist = b + 1

if (q[115] == 1):
    the_challenger = g + 1
if (q[115] == 2):
    the_reformer = d + 1

if (q[116] == 1):
    the_helper = f + 1
if (q[116] == 2):
    the_investigator = h + 1

if (q[117] == 1):
    the_achiever = c + 1
if (q[117] == 2):
    the_enthusiast = i + 1

if (q[118] == 1):
    the_individualist = e + 1
if (q[118] == 2):
    the_peacemaker = a + 1

if (q[119] == 1):
    the_investigator = h + 1
if (q[119] == 2):
    the_challenger = g + 1

if (q[120] == 1):
    the_loyalist = b + 1
if (q[120] == 2):
    the_reformer = d + 1

if (q[121] == 1):
    the_helper = f + 1
if (q[121] == 2):
    the_achiever = c + 1

if (q[122] == 1):
    the_individualist = e + 1
if (q[122] == 2):
    the_enthusiast = i + 1

if (q[123] == 1):
    the_investigator = h + 1
if (q[123] == 2):
    the_reformer = d + 1

if (q[124] == 1):
    the_loyalist = b + 1
if (q[124] == 2):
    the_challenger = g + 1

if (q[125] == 1):
    the_peacemaker = a + 1
if (q[125] == 2):
    the_helper = f + 1

if (q[126] == 1):
    the_individualist = e + 1
if (q[126] == 2):
    the_achiever = c + 1

if (q[127] == 1):
    the_enthusiast = i + 1
if (q[127] == 2):
    the_loyalist = b + 1

if (q[128] == 1):
    the_helper = f + 1
if (q[128] == 2):
    the_reformer = d + 1

if (q[129] == 1):
    the_challenger = g + 1
if (q[129] == 2):
    the_achiever = c + 1

if (q[130] == 1):
    the_investigator = h + 1
if (q[130] == 2):
    the_peacemaker = a + 1

if (q[131] == 1):
    the_helper = f + 1
if (q[131] == 2):
    the_loyalist = b + 1

if (q[132] == 1):
    the_challenger = g + 1
if (q[132] == 2):
    the_enthusiast = i + 1

if (q[133] == 1):
    the_individualist = e + 1
if (q[133] == 2):
    the_reformer = d + 1

if (q[134] == 1):
    the_peacemaker = a + 1
if (q[134] == 2):
    the_enthusiast = i + 1

if (q[135] == 1):
    the_achiever = c + 1
if (q[135] == 2):
    the_loyalist = b + 1

if (q[136] == 1):
    the_investigator += 1
if (q[136] == 2):
    the_individualist += 1

if (q[137] == 1):
    the_challenger += 1
if (q[137] == 2):
    the_helper += 1

if (q[138] == 1):
    the_reformer += 1
if (q[138] == 2):
    the_enthusiast += 1

if (q[139] == 1):
    the_achiever += 1
if (q[139] == 2):
    the_peacemaker += 1

if (q[140] == 1):
    the_loyalist += 1
if (q[140] == 2):
    the_investigator += 1

if (q[141] == 1):
    the_challenger += 1
if (q[141] == 2):
    the_individualist += 1

if (q[142] == 1):
    the_peacemaker += 1
if (q[142] == 2):
    the_reformer += 1

if (q[143] == 1):
    the_helper += 1
if (q[143] == 2):
    the_enthusiast += 1

if (q[144] == 1):
    the_investigator += 1
if (q[144] == 2):
    the_achiever += 1

w = str('The Peacemaker ')
r = str('The Loyalist ')
t = str('The Achiever ')
y = str('The Reformer ')
u = str('The Individualist ')
o = str('The Helper ')
p = str('The Challenger ')
m = str('The Investigator ')
j = str('The Enthusiast ')


def main():
    print(w,the_peacemaker)
    print(r,the_loyalist)
    print(t,the_achiever)
    print(y,the_reformer)
    print(u,the_individualist)
    print(o,the_helper)
    print(p,the_challenger)
    print(m,the_investigator)
    print(j,the_enthusiast)

def write():
    n = str(name)
    s = open('enneagram.txt','the_peacemaker')
    s.write(n)
    s.write('\n')
    s.write(w)
    s.write(str(the_peacemaker))
    s.write('\n')
    s.write(r)
    s.write(str(the_loyalist))
    s.write('\n')
    s.write(t)
    s.write(str(the_achiever))
    s.write('\n')
    s.write(y)
    s.write(str(the_reformer))
    s.write('\n')
    s.write(u)
    s.write(str(the_individualist))
    s.write('\n')
    s.write(o)
    s.write(str(the_helper))
    s.write('\n')
    s.write(p)
    s.write(str(the_challenger))
    s.write('\n')
    s.write(m)
    s.write(str(the_investigator))
    s.write('\n')
    s.write(j)
    s.write(str(the_enthusiast))
    s.write('\n')
    s.write('\n')
    s.close()

write()

main()

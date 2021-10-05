# 测试题目来自：http://wizardmore.com/sorting-hat-x/

# 定义四个学院的初始值
G=0
R=0
H=0
S=0



# 问题
print(G,R,H,S)
i=0
print('Dawn or dusk?/你更喜欢破晓还是黄昏？\nA.Dawn/破晓\nB.Dusk/黄昏\n请输入选项：')
while i==0:
    Key=input()
    if (Key=='A'):
        G+=1
        R+=1
        i=1
    elif (Key=='B'):
        H+=1
        S+=1
        i=1
    else:
        print('输入不合法，请重新输入：')

# 问题
print(G,R,H,S)
i=0
print('Forest or river?/你更喜欢森林还是河流？\nA.Forest/森林\nB.River/河流\n请输入选项：')
while i==0:
    Key=input()
    if (Key=='A'):
        G+=1
        R+=1
        i=1
    elif (Key=='B'):
        H+=1
        S+=1
        i=1
    else:
        print('输入不合法，请重新输入：')

# 问题
print(G,R,H,S)
i=0
print('Moon or stars?/你更喜欢月亮还是星辰？\nA.Moon/月亮\nB.Stars/星辰\n请输入选项：')
while i==0:
    Key=input()
    if (Key=='A'):
        R+=1
        S+=1
        i=1
    elif (Key=='B'):
        G+=1
        H+=1
        i=1
    else:
        print('输入不合法，请重新输入：')

# 问题
print(G,R,H,S)
i=0
print('Which of the following would you most hate people to call you?/你最讨厌人们称你：\nA.Ordinary/平凡\nB.Ignorant/无知\nC.Cowardly/胆小\nD.Selfish/自私\n请输入选项：')
while i==0:
    Key=input()
    if (Key=='A'):
        S+=1
        i=1
    elif (Key=='B'):
        R+=1
        i=1
    elif (Key=='C'):
        G+=1
        i=1
    elif (Key=='D'):
        H+=1
        i=1
    else:
        print('输入不合法，请重新输入：')

# 问题
print(G,R,H,S)
i=0
print('After you\'ve died, what would you most like people to do when they hear your name?/你去世后，你希望世人听到你的名字时作出什么反应？\nA.miss you, but smile/带着笑容缅怀你\nB.ask for more stories about your adventures/询问更多关于你奇遇的故事\nC.think with admiration of your achievements/想起你令人钦佩的成就\nD.I don\'t care what people think of me after I\'m dead; it\'s what they think of me while I\'m alive that counts/我才不介意去世后人们如何评价我，我活着的时候他们怎么评价我才重要\n请输入选项：')
while i==0:
    Key=input()
    if (Key=='A'):
        H+=1
        i=1
    elif (Key=='B'):
        G+=1
        i=1
    elif (Key=='C'):
        R+=1
        i=1
    elif (Key=='D'):
        S+=1
        i=1
    else:
        print('输入不合法，请重新输入：')

# 问题
print(G,R,H,S)
i=0
print('How would you like to be known to history/你想在让后人认为你是个？\nA.the wise/智者\nB.the good/好人\nC.the great/伟人\nD.the bold/勇者\n请输入选项：')
while i==0:
    Key=input()
    if (Key=='A'):
        R+=1
        i=1
    elif (Key=='B'):
        H+=1
        i=1
    elif (Key=='C'):
        S+=1
        i=1
    elif (Key=='D'):
        G+=1
        i=1
    else:
        print('输入不合法，请重新输入：')

# 问题
print(G,R,H,S)
i=0
print('Once every century, the Flutterby bush produces flowers that adapt their scent to attract the unwary. If it lured you , it would smell of/振翅灌木每个世纪盛开一次，用花朵变幻的气味引诱粗心者。如果它要引诱你，你闻到的的味道会是\nA.A crackling log fire/燃烧得滋滋作响的木头\nB.The sea/大海\nC.Fresh parchment/崭新的羊皮纸\nD.Home/家\n请输入选项：')
while i==0:
    Key=input()
    if (Key=='A'):
        G+=1
        i=1
    elif (Key=='B'):
        S+=1
        i=1
    elif (Key=='C'):
        R+=1
        i=1
    elif (Key=='D'):
        H+=1
        i=1
    else:
        print('输入不合法，请重新输入：')

# 问题
print(G,R,H,S)
i=0
print('Four goblets are placed before you. Which would you choose to drink?/你面前有四个高脚杯。你会选择喝？\nA.The foaming, frothing, silvery liquid that sparkles as though containing ground diamonds/泡沫绵密，像含有碎钻石般闪耀着的银色液体\nB.The smooth, thick, richly purple drink that gives off a delicious smell of chocolate and plums/香滑浓稠，闻着像巧克力和李子口味的紫色饮料\nC.The golden liquid so bright that it hurts the eye, and which makes sunspots dance all around the room/耀眼的金色液体，令房间里充满了跳动的光斑\nD.The mysterious black liquid that gleams like ink, and gives off fumes that make you see strange visions/像墨水般闪烁的神秘黑色液体，散发出的烟雾令你眼前浮现出奇怪的幻象\n请输入选项：')
while i==0:
    Key=input()
    if (Key=='A'):
        R+=1
        i=1
    elif (Key=='B'):
        H+=1
        i=1
    elif (Key=='C'):
        G+=1
        i=1
    elif (Key=='D'):
        S+=1
        i=1
    else:
        print('输入不合法，请重新输入：')

# 问题
print(G,R,H,S)
i=0
print('What kind of instrument most pleases your ear?/哪种乐器最让你耳目一新？\nA.The violin/小提琴\nB.The trumpet/小号\nC.The piano/钢琴\nD.The drum/鼓\n请输入选项：')
while i==0:
    Key=input()
    if (Key=='A'):
        S+=1
        i=1
    elif (Key=='B'):
        H+=1
        i=1
    elif (Key=='C'):
        R+=1
        i=1
    elif (Key=='D'):
        G+=1
        i=1
    else:
        print('输入不合法，请重新输入：')

# 问题
print(G,R,H,S)
i=0
print('You enter an enchanted garden. What would you be most curious to examine first?/你进入了一个魔法花园。最令你好奇，让你忍不住立即前去仔细观察的是？\nA.The silver leafed tree bearing golden apples/一棵长着银叶子金苹果的树\nB.The fat red toadstools that appear to be talking to each other/一堆厚厚的红色毒蕈，似乎正在相互交谈\nC.The bubbling pool, in the depths of which something luminous is swirling/冒着泡泡的池塘，里面好像有什么发光的东西在旋转\nD.The statue of an old wizard with a strangely twinkling eye/一名年纪很大的巫师的塑像，奇怪地眨着一只眼睛\n请输入选项：')
while i==0:
    Key=input()
    if (Key=='A'):
        R+=1
        i=1
    elif (Key=='B'):
        H+=1
        i=1
    elif (Key=='C'):
        S+=1
        i=1
    elif (Key=='D'):
        G+=1
        i=1
    else:
        print('输入不合法，请重新输入：')

# 问题
print(G,R,H,S)
i=0
print('Four boxes are placed before you, which would you try and open?/你面前有四个盒子，你会打开：\nA.The small tortoiseshell box, embellished with gold, inside which some small creature seems to be squeaking/有金色装饰的龟壳做的小盒子，里面似乎有什么小动物在发出吱吱的叫声\nB.The gleaming jet black box with a silver lock and key, marked with a mysterious rune that you know to be the mark of Merlin/亮黑色有银锁和钥匙的盒子，上面神秘的符文是梅林的标志\nC.The ornate golden casket, standing on clawed feet, whose inscription warns that both secret knowledge and unbearable temptation lie within/有着爪型支架的华丽金匣子，上面的铭文警示着匣子里有秘密知识和令人无法抵抗的诱惑\nD.The small pewter box, unassuming and plain, with a scratched message upon it that reads \'I open only for the worthy‘/一个平凡无奇的小锡盒，上面潦草地刻着“只有配得上的人才能将我打开”\n请输入选项：')
while i==0:
    Key=input()
    if (Key=='A'):
        H+=1
        i=1
    elif (Key=='B'):
        S+=1
        i=1
    elif (Key=='C'):
        R+=1
        i=1
    elif (Key=='D'):
        G+=1
        i=1
    else:
        print('输入不合法，请重新输入：')

# 问题
print(G,R,H,S)
i=0
print('A troll has gone berserk in the Headmaster\'s study at Hogwarts. It is about to smash, crush and tear several irreplaceable items and treasures. In which order would you rescue these objects from the troll’s club, if you could?/一只巨怪在霍格沃茨校长办公室里疯狂乱砸。它马上要毁掉几个不可替代的物件和珍宝。如果可以，你会以下面哪种顺序从巨怪的棍子下抢救这些东西？\nA.First, a nearly perfected cure for dragon pox. Then student records going back 1000 years. Finally, a mysterious handwritten book full of strange runes./首先，接近完美的龙痘治疗方案，然后，一千年以来的学生记录，最后，一本神秘的满是奇怪符文的手写书籍\nB.First, student records going back 1000 years. Then a mysterious handwritten book full of strange runes. Finally, a nearly perfected cure for dragon pox./首先，一千年以来的学生记录，然后，一本神秘的满是奇怪符文的手写书籍，最后，接近完美的龙痘治疗方案\nC.First, a mysterious handwritten book full of strange runes. Then a nearly perfected cure for dragon pox. Finally, student records going back 1000 years./首先，一本神秘的满是奇怪符文的手写书籍，然后，接近完美的龙痘治疗方案，最后，一千年以来的学生记录\nD.First, a nearly perfected cure for dragon pox. Then a mysterious handwritten book full of strange runes. Finally, student records going back 1000 years./首先，接近完美的龙痘治疗方案，然后，一本神秘的满是奇怪符文的手写书籍，最后，一千年以来的学生记录\nE.First student records going back 1000 years. Then, a nearly perfected cure for dragon pox. Finally, a mysterious handwritten book full of strange runes./首先，一千年以来的学生记录，然后，接近完美的龙痘治疗方案，最后，一本神秘的满是奇怪符文的手写书籍\nF.First, a mysterious handwritten book full of strange runes. Then student records going back 1000 years. Finally, a nearly perfected cure for dragon pox./首先，一本神秘的满是奇怪符文的手写书籍，然后，一千年以来的学生记录，最后，接近完美的龙痘治疗方案\n请输入选项：')
while i==0:
    Key=input()
    if (Key=='A'):
        G+=1
        H+=1
        i=1
    elif (Key=='B'):
        S+=1
        i=1
    elif (Key=='C'):
        R+=1
        i=1
    elif (Key=='D'):
        G+=1
        i=1
    elif (Key=='E'):
        H+=1
        i=1
    elif (Key=='F'):
        R+=1
        S+=1
        i=1
    else:
        print('输入不合法，请重新输入：')

# 问题
print(G,R,H,S)
i=0
print('Which of the following do you find most difficult to deal with?/你认为以下哪种情况最难应对？\nA.Hunger/饥饿\nB.Cold/寒冷\nC.Loneliness/孤单\nD.Boredom/无聊\nE.Being ignored/被忽略\n请输入选项：')
while i==0:
    Key=input()
    if (Key=='A'):
        R+=1
        H+=1
        i=1
    elif (Key=='B'):
        H+=1
        S+=1
        i=1
    elif (Key=='C'):
        G+=1
        H+=1
        i=1
    elif (Key=='D'):
        G+=1
        S+=1
        i=1
    elif (Key=='E'):
        R+=1
        S+=1
        i=1
    else:
        print('输入不合法，请重新输入：')

# 问题
print(G,R,H,S)
i=0
print('Which would you rather be?/你愿意被他人____？\nA.envied/嫉妒\nB.imitated/模仿\nC.trusted/信任\nD.praised/表扬\nE.liked/喜爱\nF.feared/畏惧\n请输入选项：')
while i==0:
    Key=input()
    if (Key=='A'):
        R+=1
        S+=1
        i=1
    elif (Key=='B'):
        R+=1
        i=1
    elif (Key=='C'):
        H+=1
        i=1
    elif (Key=='D'):
        G+=1
        S+=0.5
        i=1
    elif (Key=='E'):
        H+=1
        i=1
    elif (Key=='F'):
        S+=1
        i=1
    else:
        print('输入不合法，请重新输入：')

# 问题
print(G,R,H,S)
i=0
print('If you could have any power, which would you choose?/如果你可以拥有任何能力，你想选以下哪种？\nA.The power to read minds/读心术\nB.The power of invisibility/隐形术\nC.The power of superhuman strength/超人的力量\nD.The power to speak to animals/与动物交流的能力\nE.The power to change the past/改变过去的能力\nF.The power to change your appearance at will/随意改变样貌的能力\n请输入选项：')
while i==0:
    Key=input()
    if (Key=='A'):
        R+=1
        S+=1
        i=1
    elif (Key=='B'):
        G+=1
        H+=0.5
        i=1
    elif (Key=='C'):
        H+=1
        S+=0.5
        i=1
    elif (Key=='D'):
        R+=1
        H+=1
        i=1
    elif (Key=='E'):
        G+=0.5
        S+=1
        i=1
    elif (Key=='F'):
        G+=0.5
        R+=1
        i=1
    else:
        print('输入不合法，请重新输入：')

# 问题
print(G,R,H,S)
i=0
print('What are you most looking forward to learning at Hogwarts?/你最期待在霍格沃茨学什么？\nA.Apparition and Disapparition/幻影显形\nB.Transfiguration/变形术\nC.Flying on a broomstick/飞天扫帚飞行\nD.Hexes and jinxes/恶咒\nE.All about magical creatures, and how to befriend/care for them/神奇动物和如何与它们交朋友或照顾它们\nF.Secrets about the castle/城堡的秘密\nG.Every area of magic I can/我所能学的所有魔法领域\n请输入选项：')
while i==0:
    Key=input()
    if (Key=='A'):
        G+=1
        S+=1
        i=1
    elif (Key=='B'):
        R+=1
        i=1
    elif (Key=='C'):
        G+=1
        H+=1
        i=1
    elif (Key=='D'):
        S+=1
        i=1
    elif (Key=='E'):
        H+=1
        i=1
    elif (Key=='F'):
        G+=1
        i=1
    elif (Key=='G'):
        R+=1
        i=1
    else:
        print('输入不合法，请重新输入：')

# 问题
print(G,R,H,S)
i=0
print('Which of the following would you most like to study?/你最想研究以下哪种生物？\nA.Centaurs/马人\nB.Goblins/妖精\nC.Merpeople/人鱼\nD.Ghosts/鬼魂\nE.Vampires/吸血鬼\nF.Werewolves/狼人\nG.Trolls/巨怪\n请输入选项：')
while i==0:
    Key=input()
    if (Key=='A'):
        G+=1
        R+=1
        i=1
    elif (Key=='B'):
        R+=1
        S+=0.5
        i=1
    elif (Key=='C'):
        H+=1
        S+=1
        i=1
    elif (Key=='D'):
        G+=1
        R+=1
        i=1
    elif (Key=='E'):
        S+=1
        i=1
    elif (Key=='F'):
        G+=1
        H+=1
        i=1
    elif (Key=='G'):
        H+=1
        S+=1
        i=1
    else:
        print('输入不合法，请重新输入：')

# 问题
print(G,R,H,S)
i=0
print('You and two friends need to cross a bridge guarded by a river troll who insists on fighting one of you before he will let all of you pass. Do you:/你和两个朋友要通过一座河流巨怪看守着的桥，河怪坚持你们中必须有一人需要战胜它，才能让你们三人通行，你会：\nA.Attempt to confuse the troll into letting all three of you pass without fighting?/尝试把河流巨怪搞糊涂，让它允许你和朋友们不用跟它打，直接通过\nB.Suggest drawing lots to decide which of you will fight?/建议大家抽签决定谁来上\nC.Suggest that all three of you should fight (without telling the troll)?/（瞒着巨怪）提议你们三人一同战斗\nD.Volunteer to fight?/自告奋勇，你行你上？\n请输入选项：')
while i==0:
    Key=input()
    if (Key=='A'):
        R+=1
        i=1
    elif (Key=='B'):
        H+=1
        i=1
    elif (Key=='C'):
        S+=1
        i=1
    elif (Key=='D'):
        G+=1
        i=1
    else:
        print('输入不合法，请重新输入：')

# 问题
print(G,R,H,S)
i=0
print('One of your house mates has cheated in a Hogwarts exam by using a Self-Spelling Quill. Now he has come top of the class in Charms, beating you into second place. Professor Flitwick is suspicious of what happened. He draws you to one side after his lesson and asks you whether or not your classmate used a forbidden quill. What do you do?/有一位与你在同一个学院的同学在霍格沃茨考试中作弊，使用了自动拼写羽毛笔。现在他在魔咒课上成了第一名，第二名是你。弗立维教授怀疑事情的真相，并在课后让你留下，问你这个同学有没有用不合规定的羽毛笔。你会怎么做？\nA.Lie and say you don’t know (but hope that somebody else tells Professor Flitwick the truth)./撒谎，说你不知道（不过希望有其他人告诉弗立维教授真相）\nB.Tell Professor Flitwick that he ought to ask your classmate (and resolve to tell your classmate that if he doesn’t tell the truth, you will)./告诉弗立维教授他应该去问这个同学（然后决心告诉这个同学，如果他不说实话，你会对教授说出实情）\nC.Tell Professor Flitwick the truth. If your classmate is prepared to win by cheating, he deserves to be found out. Also, as you are both in the same house, any points he loses will be regained by you, for coming first in his place./对弗立维教授说出真相。如果你的同学觉得自己能通过作弊取胜，被曝光也是罪有应得。另外，你们属于同一个学院，所以你取代他获得第一会弥补他失去的学院分。\nD.You would not wait to be asked to tell Professor Flitwick the truth. If you knew that somebody was using a forbidden quill, you would tell the teacher before the exam started./不用等弗立维教授提出疑问，你发现时就会说出实情。如果你知道有人用作弊羽毛笔，在考试开始前你就会告诉老师。\n请输入选项：')
while i==0:
    Key=input()
    if (Key=='A'):
        H+=1
        i=1
    elif (Key=='B'):
        G+=1
        i=1
    elif (Key=='C'):
        R+=1
        i=1
    elif (Key=='D'):
        S+=1
        i=1
    else:
        print('输入不合法，请重新输入：')

# 问题
print(G,R,H,S)
i=0
print('A muggle confronts you and says that they are sure you are a witch or wizard. Do you:/一个麻瓜向你对峙，说他确定你是个巫师，你会：\nA.Ask what makes them think so/问他为什么有这种想法\nB.Agree, and ask whether they\'d like a free sample of a jinx/承认，并问他要不要免费体验一下恶咒\nC.Agree, and walk away, leaving them to wonder whether you are bluffing/承认，然后走开，让他自己琢磨你是不是在吹牛\nD.Tell them that you are worried about their mental health, and offer to call a doctor/告诉他你怀疑他精神方面有问题，并提出帮忙给医生打电话\n请输入选项：')
while i==0:
    Key=input()
    if (Key=='A'):
        R+=1
        i=1
    elif (Key=='B'):
        S+=1
        i=1
    elif (Key=='C'):
        G+=1
        i=1
    elif (Key=='D'):
        H+=1
        i=1
    else:
        print('输入不合法，请重新输入：')

# 问题
print(G,R,H,S)
i=0
print('What nightmare would frighten you most?/你最害怕哪种噩梦？\nA.Standing on top of something very high and realizing suddenly that there are no hand- or footholds, nor any barrier to stop you falling./站在某处的最高点，突然发现四周没有任何你的手脚能够着的地方，也没有护栏。\nB.An eye at the keyhole of the dark, windowless room in which you are locked./被关在四周漆黑，没有窗户的房间里，发现门锁眼中有一只眼睛看着你。\nC.Waking up to find that neither your friends nor your family have any idea who you are./一觉醒来发现你的家人朋友都不认识你了。\nD.Being forced to speak in such a silly voice that hardly anyone can understand you, and everyone laughs at you./被迫用一种愚蠢的声音讲话，几乎没人听能得懂你说的话，大家都嘲笑你。\n请输入选项：')
while i==0:
    Key=input()
    if (Key=='A'):
        R+=1
        i=1
    elif (Key=='B'):
        G+=1
        i=1
    elif (Key=='C'):
        H+=1
        i=1
    elif (Key=='D'):
        S+=1
        i=1
    else:
        print('输入不合法，请重新输入：')

# 问题
print(G,R,H,S)
i=0
print('Which road tempts you most?/那条路对你最有吸引力？\nA.The wide, sunny grassy lane/阳光明媚的宽阔草地\nB.The narrow, dark latern-let alley/黑暗狭窄，点着灯笼的小巷\nC.The twisting, leaf-strewn path through woods/森林中洒满落叶的曲折小径\nD.The cobbled street lined with ancient buildings/两边都是古老建筑的鹅卵石街道\n请输入选项：')
while i==0:
    Key=input()
    if (Key=='A'):
        H+=1
        i=1
    elif (Key=='B'):
        S+=1
        i=1
    elif (Key=='C'):
        G+=1
        i=1
    elif (Key=='D'):
        R+=1
        i=1
    else:
        print('输入不合法，请重新输入：')

# 问题
print(G,R,H,S)
i=0
print('Late at night, walking alone down the street, you hear a peculiar cry that you believe to have a magical source. Do you/夜晚，在街上独自行走的时候听到一声你认为有魔法踪迹的古怪的哭叫声，你会：\nA.Proceed with caution, keeping one hand on your concealed wand and an eye out for any disturbance?/小心走过去，一只手偷偷握着魔杖，谨慎防备着任何潜在的危险\nB.Draw your wand and try to discover the source of the noise?/抽出魔杖，尝试找出噪音的来源\nC.Draw your wand and stand your ground?/抽出魔杖，坚守阵地\nD.Withdraw into the shadows to await developments, while mentally reviewing the most appropriate defensive and offensive spells, should trouble occur?/躲在阴影中观察事情的进展，并在脑海里演练合适的攻击和防御咒语，时刻准备着\n请输入选项：')
while i==0:
    Key=input()
    if (Key=='A'):
        H+=1
        i=1
    elif (Key=='B'):
        G+=1
        i=1
    elif (Key=='C'):
        S+=1
        i=1
    elif (Key=='D'):
        R+=1
        i=1
    else:
        print('输入不合法，请重新输入：')

# 问题
print(G,R,H,S)
i=0
print('If you were attending Hogwarts, which pet would you choose to take with you?/如果你要到霍格沃茨上学，你想带哪种宠物？\nA.tabby cat  虎斑猫\nB.siamese cat  暹罗猫\nC.ginger cat  姜黄色猫\nD.black cat  黑猫\nE.white cat  白猫\nF.tawny owl  灰林鸮\nG.screech owl  长耳猫头鹰\nH.brown owl  褐色猫头鹰\nI.snowy owl  雪鸮\nJ.barn owl  仓鸮\nK.common toad  大蟾蜍\nL.natterjack toad  黄条背蟾蜍\nM.dragon toad  龙蟾\nN.harlequin toad  彩蟾蜍\nO.three toed tree toad  三趾树蟾蜍\n请输入选项：')
while i==0:
    Key=input()
    if (Key=='A'):
        G+=0.5
        S+=0.5
        i=1
    elif (Key=='B'):
        G+=0.25
        S+=1
        i=1
    elif (Key=='C'):
        G+=0.25
        S+=1
        i=1
    elif (Key=='D'):
        G+=0.25
        S+=1
        i=1
    elif (Key=='E'):
        G+=0.25
        S+=1
        i=1
    elif (Key=='F'):
        G+=0.25
        R+=1
        i=1
    elif (Key=='G'):
        G+=0.25
        R+=1
        i=1
    elif (Key=='H'):
        G+=0.25
        R+=1
        i=1
    elif (Key=='I'):
        G+=0.25
        R+=0.5
        H+=0.5
        i=1
    elif (Key=='J'):
        G+=0.25
        R+=1
        i=1
    elif (Key=='K'):
        G+=0.25
        H+=1
        i=1
    elif (Key=='L'):
        G+=0.25
        H+=1
        i=1
    elif (Key=='M'):
        G+=0.5
        H+=0.5
        i=1
    elif (Key=='N'):
        G+=0.25
        H+=1
        i=1
    elif (Key=='O'):
        G+=0.25
        R+=0.5
        H+=0.5
        i=1
    else:
        print('输入不合法，请重新输入：')

# 问题
print(G,R,H,S)
i=0
print('Black or white?  /黑色还是白色？\nA.Black/黑色\nB.White/白色\n请输入选项：')
while i==0:
    Key=input()
    if (Key=='A'):
        G+=1
        S+=1
        i=1
    elif (Key=='B'):
        R+=1
        H+=1
        i=1
    else:
        print('输入不合法，请重新输入：')

# 问题
print(G,R,H,S)
i=0
print('Heads or tails? /抛硬币的时候你觉得是正面向上还是反面向上？\nA.Heads/正面\nB.Tails/反面\n请输入选项：')
while i==0:
    Key=input()
    if (Key=='A'):
        R+=1
        H+=1
        i=1
    elif (Key=='B'):
        G+=1
        S+=1
        i=1
    else:
        print('输入不合法，请重新输入：')

# 问题
print(G,R,H,S)
i=0
print('Left or right?/左边还是右边？\nA.Left/左\nB.Right/右\n请输入选项：')
while i==0:
    Key=input()
    if (Key=='A'):
        R+=1
        S+=1
        i=1
    elif (Key=='B'):
        G+=1
        H+=1
        i=1
    else:
        print('输入不合法，请重新输入：')

# 归一化百分比

G=(100*G/(G+R+H+S))
R=(100*R/(G+R+H+S))
H=(100*H/(G+R+H+S))
S=(100*S/(G+R+H+S))

# 输入姓名
print("请输入姓名：")
Name=input()

# 打印结果
print(Name,"的分院测试结果：\n","Gryffindor/格兰芬多：",G,'%\n',"Ravenclaw/拉文克劳：",R,'%\n',"Hufflepuff/赫奇帕奇：",H,'%\n',"Slytherin/斯莱特林：",S,'%\n')
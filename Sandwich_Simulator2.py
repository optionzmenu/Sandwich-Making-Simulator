yes = ["y", "yes"]
no = ["n", "no"]
Or = ["o", "or"]

def yesorno():
    while True:
        try:
            answer = input("Yes or No?").lower()
        except ValueError:
            print("Wrong input")
        if answer in yes:
            return True
        elif answer in no:
            return False
        elif answer in Or:
            print ("Very Funny!")
            continue
        else:
            print("Did you read the question?")
            continue

def sandwich():
    print("Welcome to the **SANDWICH MAKING SIMULATOR** ")
    print("\nPlease choose from the list of ingredients to customize your Sandwich!\n")
    sandwichingredients = {1: "Bread", 2: "Meat", 3: "Cheese", 4: "Mayo", 5: "Pickles"}
    choseningredients=set()
    print("You see "+ ", ".join(sandwichingredients.values())+".")
    while True:
        try:
            print(*[f"{number}. {ingredient}" for number, ingredient in sandwichingredients.items()], sep="\n")
            print ("Select the ingredients based on number. Which would you like to grab?")
            response=int(input("Select ingredients: ")) 
            if response in choseningredients:
                print("\nYou already have that ingredient.\n")
                continue
            elif response not in sandwichingredients.keys():
                print("\nThat is not an ingredient.\n")
                continue
            choseningredients.add(response)
            
            if choseningredients == set([1,2,3,4,5]): #All ingredients (Full sandwich)
                print("\nYou've collected all the ingredients! Wow, that's an amazing sandwich.\n")
                break

            elif choseningredients == set([1]): #Just Bread
                print("\nA nice sesame seed bun! The best way to start building a sandwich!\n")
                print("Continue making sandwich?")
                answer = yesorno()
                if answer is True:
                    continue
                if answer is False:
                    print("\nWow, you are really going to eat just bread. Okay. Hey, it's your life. You eat just the plain old bread.\n")
                    break
            
            elif choseningredients == set([2]): #Just Meat
                print("\nCan't have a sandwich without meat! (Actually... you probably could, but anyway!)\n")
                print("Continue making sandwich?")
                answer = yesorno()
                if answer is True:
                    continue
                if answer is False:
                    print("\nPrime Carnivore! You just just the meat!\n")
                    break
            
            elif choseningredients == set([3]): #Just Cheese
                print("\nYou grab a piece of cheese to start your sandwich!\n")
                print("Continue making sandwich?")
                answer = yesorno()
                if answer is True:
                    continue
                if answer is False:
                    print("\nYou know these aren't cheese sticks right? Okaaay, well, you eat just a slice of cheese.\n")
                    break
            
            elif choseningredients == set([4]): #Just Mayo
                print("\nYou grab a jar of mayo\n")
                print("Continue making sandwich?")
                answer = yesorno()
                if answer is True:
                    continue
                if answer is False:
                    print("\nAre you really just going to scoop mayo out of the jar with your hand? This is not sandwich! You know what I don't even care anymore. Sure, you eat mayo.\n")
                    break

            elif choseningredients == set([1,2]): #Bread and Meat
                print("\nKind of plain so far but okay.\n")
                print("Continue making sandwich?")
                answer = yesorno()
                if answer is True:
                    continue
                if answer is False:
                    break

            elif choseningredients == set([1,2,3]): #Bread, Meat, and cheese
                print("\nYum! Okay, lookin' good!\n")
                print("Continue making sandwich?")
                answer = yesorno()
                if answer is True:
                    continue
                if answer is False:
                    print("\nAlright now thats a sandwich!\n")
                    break

            elif choseningredients == set([1,4]): #Bread and Mayo
                print("\nKind of plain so far but okay.\n")
                print("Continue making sandwich?")
                answer = yesorno()
                if answer is True:
                    continue
                if answer is False:
                    print("\nWho eats bread and mayo? Hey it's your life you can eat what you want I guess!\n")
                    break

            elif choseningredients == set([2,4]): #Meat and Mayo
                print("\nOkay, I'm liking so far!\n")
                print("Continue making sandwich?")
                answer = yesorno()
                if answer is True:
                    continue
                if answer is False:
                    print("\nI think you may actually be insane, but okay! You eat just meat with mayo on top!\n")
                    break

            elif choseningredients == set([1,3]): #Bread and Cheese
                print("\nBread and cheese is a good combo!\n")
                print("Continue making sandwich?")
                answer = yesorno()
                if answer is True:
                    continue
                if answer is False:
                    print("\nLike a grill cheese? I'll allow it!\n")
                    break

            elif choseningredients == set([1,2,4]): #Bread, Meat and Mayo
                print("\nNow this is looking like a sandwich!\n")
                print("Continue making sandwich?")
                answer = yesorno()
                if answer is True:
                    continue
                if answer is False:
                    print("\nNice job! No cheese but you might be lack tose intolerant I dont know! You eat the sandwich!\n")
                    break
           
            elif choseningredients == set([2,3,4]): #Meat, Cheese, Mayo (no bread)
                print("\nWhy are you putting together the ingredients without bread?\n")
                print("Continue making sandiwch (Please say yes)?")
                answer = yesorno()
                if answer is True:
                    continue
                if answer is False:
                    print("\nWow you really hate bread huh? It's kind of messy, but you eat this sandwich!\n")
                    break
            
            elif choseningredients == set([1,3,4]): #No Meat
                print("\nNice! You only have ingredient left\n")
                print("Continue making sandwich?")
                answer = yesorno()
                if answer is True:
                    continue
                if answer is False:
                    print("\nI guess that's still a sandwich technically! You eat this!\n")
                    break

            elif choseningredients == set([3,4]): #Just Cheese and mayo
                print("\nNice! Gathering the toppings first isn't a back idea.\n")
                print("Continue making sandwich?")
                answer = yesorno()
                if answer is True:
                    continue
                if answer is False:
                    print("\nHow does... how does that work? Are you gonna dip the cheese in mayo or-- whatever. You eat this concoction of ingredients.\n")
                    break
        
            elif choseningredients == set([5]): #Just Pickles
                print("\nYou grab a wonderful Jar of pickles!\n")
                print("Continue making sandwich?")
                answer = yesorno()
                if answer is True:
                    continue
                if answer is False:
                    print("\nBut these... usually go on a SANDWICH-- oh who am I to judge. You just eat pickles right out the jar. \n")
                    break

            elif choseningredients == set([5,1]): #Pickles and Bread
                print("\nOkay! We're slowly starting to look like a sandwich!\n")
                print("Continue making sandwich?")
                answer = yesorno()
                if answer is True:
                    continue
                if answer is False:
                    print("\nYou're really just going to sit there and eat pickles and bread? Okay, well you eat that. I guess?\n")
                    break
            
            elif choseningredients == set([5,1,2]): #Pickles, Bread and Meat
                print("\nSandwich-Nirvana is just around the corner!\n")
                print("Continue making sandwich?")
                answer = yesorno()
                if answer is True:
                    continue
                if answer is False:
                    print("\nYou know what? I'm okay with this! Not the greatest, but solid! You eat this sandwich!\n")
                    break
            
            elif choseningredients == set([5,1,2,3]): #Pickles, Bread, Meat, and Cheese
                print("\nWow, even I'm starting to get hungry now!\n")
                print("Continue making sandwich?")
                answer = yesorno()
                if answer is True:
                    continue
                if answer is False:
                    print("\n*Sniff* You're missing an ingredient, but you know what, this is an amazing sandwich! You eat this sandwich proudly!\n")
                    break
            
            elif choseningredients == set([5,4]): #Pickles and Mayo
                print("\nYou now have two jars of ingredients!\n")
                print("Continue making sandwich?")
                answer = yesorno()
                if answer is True:
                    continue
                if answer is False:
                    print("\nWow. I think this has to be against the law right? So you just slather the pickles with mayo? Yuck! Okay it's your life. you eat whatever... this is.")
                    break
            
            elif choseningredients == set([5,3]): #Pickles and Cheese
                print("\nThis is coming along great!\n")
                print("Continue making sandwich?")
                answer = yesorno()
                if answer is True:
                    continue
                if answer is False:
                    print("\nDid you mistype? What is this, is this even a thing? Well hey it's not MY stomach. You eat pickles and cheese!\n")
                    break
            
            elif choseningredients == set([5,2]): #Pickles and Meat
                print("\nDon't stop now!\n")
                print("Continue making sandwich?")
                answer = yesorno()
                if answer is True:
                    continue
                if answer is False:
                    print("\nOkay. Well. That's new. You on a diet maybe? Low carb? I support you! You eat just meat and pickles!\n")
                    break
            
            elif choseningredients == set([5,2,3]): #Pickles, Meat and Cheese
                print("\nGrab some bread! Quick!\n")
                print("Continue making sandwich?")
                answer = yesorno()
                if answer is True:
                    continue
                if answer is False:
                    print("\nWhen I was thinking of a sandwich, this wasn't QUITE what I had in mind? E for Effort I guess? You eat this! \n")
                    break
            
            elif choseningredients == set([5,2,3,4]): #Pickles, Meat, Cheese, Mayo
                print("\nAlmost there! So close!\n")
                print("Continue making sandwich?")
                answer = yesorno()
                if answer is True:
                    continue
                if answer is False:
                    print("\n.... Why though? No Bread? You know what a sandwich is right? Why didnt you just make a salad? Whatever, I'm done! You eat this Kinda-Salad-But-Definitely-Not-A-Sandwich Sandwich. \n")
                    break
        except ValueError:
            print("\nPlease enter an integer!\n")
    #now you can print the ingredient names by using the dictionary
    print("Your sandwich has the following ingredients: " + ", ".join([sandwichingredients[i] for i in choseningredients]))

sandwich()
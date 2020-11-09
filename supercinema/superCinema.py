print("WELCOME TO SUPERCINEMA")
#SELECT THE LETTER WITH THE CORRECT OPTION
ans = "yes"
while ans == "yes":
    Location = input ("Select a lettet in the option to view the movie of your choice: \n(a)FANTASTIC BEASTS \n(b)WIDOWS \n(c)ROBIN HOOD \n(d)KING OF BOYS \n(e)CREED II \n(f)SPIDER-MAN: Into the Spider-Verse \n(g)AQUAMAN \n")
    import datetime
    a = datetime.datetime.today().weekday()
    if a == 0:
        print("Today is Monday")
    elif a == 1:
        print("Today is Tuesday")
    elif a == 2:
        print("Today is Wednesday")
    elif a == 3:
        print("Today is Thursday")
    elif a == 4:
        print("Today is Friday")
    elif a == 5:
        print("Today is Saturday")
    elif a == 6:
        print("Today is Sunday")
        
    if (Location.lower() == "a"):
        print("FANTASTIC BEASTS 134MINS\n \nThe second installment of the series set in J.K. Rowling's Wizarding World featuring the adventures of magizoologist Newt Scamander. \n Starring: Claire Foy, Sylvia Hoeks, Lakeith Stanfield \n \n TIME: 10:00AM, 12:40PM, 3:25PM, 4:45PM, 6:10PM, 8:50PM \n")
    else:
        if (Location.lower() == "b"):
            print("WIDOWS 129MINS \n \n Set in contemporary Chicago, amid a time of turmoil, four women with nothing in common except a debt left behind by their dead husbands' criminal activities, take fate into their own hands, and conspire to forge a future on their own terms. \n Starring: Viola Davis, Michelle Rodriguez, Elizabeth Debicki \n \n TIME: 10:00AM, 12:50PM, 3:20PM, 5:05PM, 6:35PM, 8:55PM \n")
        else:
            if (Location.lower() == "c"):
                print("ROBIN HOOD 134MINS \n \n A war-hardened Crusader and his Moorish commander mount an audacious revolt against the corrupt English crown in a thrilling action-adventure packed with gritty battlefield exploits, mind-blowing fight choreography, and a timeless romance.\n Starring: Taron Egerton, Jamie Foxx, Ben Mendelsohn \n \n TIME: 10:00AM, 2:35PM, 5:05PM, 8:55PM \n")
            else:
                if (Location.lower() == "d"):
                    print("KING OF BOYS 210MINS \n \n King of Boys follows the story of Alhaja Eniola Salami, a businesswoman and philanthropist with a checkered past and a promising political future. She is a pillar of society -- loved by many, feared by most, and truly known by a select few. As her political ambitions see her outgrowing the underworld connections responsible for her considerable wealth, she's drawn into a power struggle that threatens everything she holds dear. To come out of this on top, she will need every ounce of the cunning, ruthlessness, and strategy that took her to the top, as well as the loyalty of those closest to her. But who can she really trust? \n Starring: Sola Sobowale, Remilekun Reminisce Safaru, Adesua Etomi \n \n TIME: 10:00AM, 12:50PM, 3:20PM, 5:05PM, 6:35PM, 8:55PM \n")
                else:
                    if (Location.lower() == "e"):
                        print("CREED II \n \n Under the tutelage of Rocky Balboa, light heavyweight contender Adonis Creed faces off against Viktor Drago, son of Ivan Drago. \n Starring: Michael B. Jordan, Sylvester Stallone, Tessa Thompson \n \n TIME: 12:30PM, 5:05PM, 7:55PM \n")
                    else:
                        if (Location.lower() == "f"):
                            print("SPIDER-MAN: Into the Spider-Verse \n COMING SOON!!! \n \n Miles Morales becomes the Spider-Man of his reality and crosses paths with his counterparts from other dimensions to stop a threat to all reality. \n")
                        else:
                            if (Location.lower() == "g"):
                                print("AQUAMAN \n COMING SOON!!! \n \n Arthur Curry learns that he is the heir to the underwater kingdom of Atlantis, and must step forward to lead his people and be a hero to the world. \n")
                            else:
                                print ("Please be sure to select the available options.")
    ans = input ("Enter yes if you would like to choose other option or no to Exit: ")
ans = "no"
while ans == "no":
    Location = input (" \nThank You and Enjoy Your Movie!!! \n")
    
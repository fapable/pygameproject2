import psycopg2

#####################
def interact_with_database(command):
    connection = psycopg2.connect(" host = localhost dbname= project2 user= postgres password = vulhier je wachtwoord")

    cursor = connection.cursor()

    # Execute the command
    cursor.execute(command)
    connection.commit()

    # Save results
    results = None
    try:
        results = cursor.fetchall()
    except psycopg2.ProgrammingError:
        # Nothing to fetch
        pass

    # Close connection
    cursor.close()
    connection.close()

    return results


def update_score(name, score):
    upload_score(name, score)

def dubbel(name):
    if interact_with_database("SELECT name FROM player WHERE name != ('{}')".format(name)):
        return True
    else:
        return False
    print("database")
def upload_score(name, score):
    interact_with_database("UPDATE player SET score = {} WHERE name = '{}'"
                           .format(score, name))

def insert_naam(name, score):
        interact_with_database("INSERT INTO player VALUES ('{}',{})".format(name, score))
        update_score(name,score)
        print("database")



def download_top_score():
    result = interact_with_database("SELECT name,score FROM player ORDER BY score DESC")[0][0]
    return result

def download_top_name():
    result = interact_with_database("SELECT * FROM player ORDER BY score DESC")[0][1]
    return str(result)

def download_top_score2():
    result = interact_with_database("SELECT name,score FROM player ORDER BY score DESC")[1][0]
    return result

def download_top_name2():
    result = interact_with_database("SELECT * FROM player ORDER BY score DESC")[1][1]
    return str(result)

def download_top_score3():
    result = interact_with_database("SELECT name,score FROM player ORDER BY score DESC")[2][0]
    return result

def download_top_name3():
    result = interact_with_database("SELECT * FROM player"
                                    " ORDER BY score DESC")[2][1]
    return str(result)

def scherm():

    score = str(download_top_score())
    naam = str(download_top_name())
    score2 = str(download_top_score2())
    naam2 = str(download_top_name2())
    score3 = str(download_top_score3())
    naam3 = str(download_top_name3())

    screen = pygame.display.set_mode((1700, 1000))
    screen.fill((255,255,255))
    pygame.display.set_caption("ontsnapperdam")
    myfont = pygame.font.SysFont("Comic Sans MS", 30)
    highscore = pygame.image.load("highscore.png")

    eerste = myfont.render("1.", 200, (0, 0, 0))
    tweede = myfont.render("2.", 200, (0, 0, 0))
    derde = myfont.render("3. ", 200, (0, 0, 0))

    label = myfont.render((score), 200, (0,0,0))
    label1 = myfont.render((naam), 200, (0, 0, 0))
    label2 = myfont.render((score2), 200, (0, 0, 0))
    label3 = myfont.render((naam2), 200, (0, 0, 0))
    label4 = myfont.render((score3), 200, (0, 0, 0))
    label5 = myfont.render((naam3), 200, (0, 0, 0))

    screen.blit(highscore, (0, 0))
    screen.blit(eerste, (460, 190))
    screen.blit(label,  (480, 190))
    screen.blit(label1, (700, 190))
    screen.blit(tweede, (460, 220))
    screen.blit(label2, (480, 220))
    screen.blit(label3, (700, 220))
    screen.blit(derde,  (460, 250))
    screen.blit(label4, (480, 250))
    screen.blit(label5, (700, 250))


    pygame.display.flip()
    # event loop
    while True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                raise SystemExit
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if highscore.get_rect().collidepoint(x, y):
                    HoofdmenuNL()

#############################################################################################################

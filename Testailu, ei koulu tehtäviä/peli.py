import curses
import random
import time

def main(stdscr):
    # Alustetaan terminaali
    curses.curs_set(0)       # Piilotetaan vilkkuva kursori
    stdscr.nodelay(1)        # Ei pysäytetä ohjelmaa odottamaan näppäimen painallusta
    
    # Määritellään värit
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)    # Pelaaja
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)     # Vihollinen
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)  # Laser
    curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_BLACK)   # Tähdet
    curses.init_pair(5, curses.COLOR_MAGENTA, curses.COLOR_BLACK) # Räjähdyshiukkaset

    # Ruudun mitat
    sh, sw = stdscr.getmaxyx()
    
    # Pelaajan tilastot
    player_x = sw // 2
    player_y = sh - 3
    player_hp = 100
    score = 0
    
    # Peliobjektit
    lasers = []
    enemies = []
    particles = []
    # Luodaan satunnainen tähtitaivas (x ja y floatteina pehmeää liikettä varten)
    stars = [[random.random() * sh, random.randint(0, sw-1)] for _ in range(50)]
    
    game_over = False
    
    while not game_over:
        # Päivitetään ruudun mitat, jos käyttäjä muuttaa ikkunan kokoa
        new_sh, new_sw = stdscr.getmaxyx()
        if new_sh != sh or new_sw != sw:
            sh, sw = new_sh, new_sw
            player_y = sh - 3
            
        stdscr.erase() # Tyhjennetään ruutu uutta framea varten
        
        # --- 1. SYÖTTEIDEN KÄSITTELY ---
        while True:
            key = stdscr.getch()
            if key == -1:
                break # Ei uusia painalluksia
            
            if key == ord('q') or key == ord('Q'):
                game_over = True
            elif key == curses.KEY_LEFT and player_x > 3:
                player_x -= 2
            elif key == curses.KEY_RIGHT and player_x < sw - 4:
                player_x += 2
            elif key == ord(' '):
                lasers.append([player_y - 1, player_x]) # Ammutaan laser
                
        # --- 2. TAUSTA JA TÄHDET ---
        for star in stars:
            star[0] += 0.15  # Tähdet liikkuvat hitaasti alaspäin
            if star[0] >= sh - 1:
                star[0] = 0
                star[1] = random.randint(0, sw-1)
            try:
                stdscr.addch(int(star[0]), star[1], '.', curses.color_pair(4))
            except curses.error: pass
            
        # --- 3. VIHOLLISTEN LOGIIKKA ---
        # Spawnataan uusia vihollisia dynaamisella todennäköisyydellä
        if random.random() < 0.04 + (score * 0.0001): 
            enemies.append([0, random.randint(2, sw-3), 3]) # [y, x, hp]
            
        for enemy in enemies[:]:
            enemy[0] += 0.3 # Vihollisen nopeus (alle 1 = pehmeämpi putoaminen)
            if enemy[0] >= sh - 1:
                enemies.remove(enemy)
                player_hp -= 10 # Sakotetaan pelaajaa ohi päässeistä
            else:
                try:
                    stdscr.addch(int(enemy[0]), enemy[1], 'V', curses.color_pair(2) | curses.A_BOLD)
                except curses.error: pass
                
        # --- 4. LASERIT ---
        for laser in lasers[:]:
            laser[0] -= 1.0 # Laser lentää nopeasti ylös
            if laser[0] < 1:
                lasers.remove(laser)
            else:
                try:
                    stdscr.addch(int(laser[0]), laser[1], '|', curses.color_pair(3) | curses.A_BOLD)
                except curses.error: pass
                
        # --- 5. TÖRMÄYSTEN TARKISTUS ---
        # Laser osuu viholliseen
        for laser in lasers[:]:
            for enemy in enemies[:]:
                if abs(int(enemy[0]) - int(laser[0])) <= 1 and abs(enemy[1] - laser[1]) <= 1:
                    if laser in lasers: lasers.remove(laser)
                    enemy[2] -= 1 # Vähennä vihollisen HP
                    if enemy[2] <= 0:
                        if enemy in enemies: enemies.remove(enemy)
                        score += 10
                        # Generoidaan hiukkasia räjähdykseen
                        for _ in range(8):
                            particles.append([enemy[0], enemy[1], random.uniform(-1, 1), random.uniform(-1.5, 1.5), 10])
                    break
                    
        # Vihollinen osuu pelaajaan
        for enemy in enemies[:]:
            if abs(int(enemy[0]) - player_y) <= 1 and abs(enemy[1] - player_x) <= 2:
                if enemy in enemies: enemies.remove(enemy)
                player_hp -= 20
                for _ in range(15): # Iso räjähdys pelaajasta
                    particles.append([player_y, player_x, random.uniform(-1.5, 1.5), random.uniform(-2, 2), 15])

        # --- 6. HIUKKASJÄRJESTELMÄ (Räjähdykset) ---
        for p in particles[:]:
            p[0] += p[2] # Y-nopeus
            p[1] += p[3] # X-nopeus
            p[4] -= 1    # Elinikä (Life)
            if p[4] <= 0 or p[0] < 1 or p[0] >= sh - 1 or p[1] < 1 or p[1] >= sw - 1:
                particles.remove(p)
            else:
                try:
                    stdscr.addch(int(p[0]), int(p[1]), '*', curses.color_pair(5))
                except curses.error: pass

        # --- 7. PELAAJAN PIIRTÄMINEN ---
        try:
            stdscr.addstr(player_y, player_x - 1, "/^\\", curses.color_pair(1) | curses.A_BOLD)
            stdscr.addstr(player_y + 1, player_x - 2, "[-|-]", curses.color_pair(1) | curses.A_BOLD)
        except curses.error: pass
        
        # --- 8. KÄYTTÖLIITTYMÄ (UI) ---
        ui_text = f" HP: {player_hp} | PISTEET: {score} | OHJAUS: Nuolet | AMMU: Välilyönti | LOPETA: Q "
        try:
            # Keskitetään käyttöliittymä ruudun yläreunaan
            stdscr.addstr(0, 0, ui_text.center(sw), curses.color_pair(1) | curses.A_REVERSE | curses.A_BOLD)
        except curses.error: pass
        
        # --- 9. PELIN PÄÄTTYMINEN ---
        if player_hp <= 0:
            try:
                msg = f" GAME OVER - LOPULLISET PISTEET: {score} "
                stdscr.addstr(sh//2, sw//2 - len(msg)//2, msg, curses.color_pair(2) | curses.A_REVERSE | curses.A_BOLD)
                stdscr.refresh()
                time.sleep(4)
            except curses.error: pass
            game_over = True
            
        stdscr.refresh() # Päivitetään ruutu käyttäjälle
        time.sleep(0.03) # Noin ~33 FPS

if __name__ == '__main__':
    # wrapper palauttaa terminaalin normaalitilaan automaattisesti, jos ohjelma kaatuu
    curses.wrapper(main)
import pygame
from math import sqrt
from random import randint


class GoodGuy:
    """Player character. Defining color and starting size and location."""
    def __init__(self):
        self.color = (0, 100, 0)
        self.color_fill = (0, 255, 0)
        self.radius = 50
        self.radius_fill = self.radius - 4
        self.x = window_width/2 - self.radius
        self.y = window_height/2 - self.radius

    def give_coordinates(self):
        return self.x, self.y

    def give_center_x(self):
        return self.x + self.radius

    def give_center_y(self):
        return self.y + self.radius


class BadGuy:
    """Enemy blobs. Defining color, size and starting location."""
    def __init__(self):
        self.color = (100, 0, 0)
        self.color_fill = (255, 0, 0)
        self.radius = randint(20, 30)
        self.radius_fill = self.radius - 4

        """Enemy blobs can spawn from any direction of window and with variating speed.
         1 is for left upper corner, 2 if for upper mid etc."""
        starting_point = randint(1, 8)
        if starting_point == 1:
            self.x = randint(-50, 0) - self.radius
            self.y = randint(-50, 0) - self.radius
            self.x_speed = randint(10, 21) / 10
            self.y_speed = randint(10, 21) / 10
        elif starting_point == 2:
            self.x = randint(0, 800) - self.radius
            self.y = randint(-50, 0) - self.radius
            self.x_speed = randint(-2, 2) / 10
            self.y_speed = randint(10, 21) / 10
        elif starting_point == 3:
            self.x = randint(800, 850) - self.radius
            self.y = randint(-50, 0) - self.radius
            self.x_speed = randint(-21, -10) / 10
            self.y_speed = randint(10, 21) / 10
        elif starting_point == 4:
            self.x = randint(-50, 0) - self.radius
            self.y = randint(0, 800) - self.radius
            self.x_speed = randint(10, 21) / 10
            self.y_speed = randint(-2, 2) / 10
        elif starting_point == 5:
            self.x = randint(800, 850) - self.radius
            self.y = randint(0, 800) - self.radius
            self.x_speed = randint(-21, -10) / 10
            self.y_speed = randint(-2, 2) / 10
        elif starting_point == 6:
            self.x = randint(-50, 0) - self.radius
            self.y = randint(800, 850) - self.radius
            self.x_speed = randint(10, 21) / 10
            self.y_speed = randint(-21, -10) / 10
        elif starting_point == 7:
            self.x = randint(0, 800) - self.radius
            self.y = randint(800, 850) - self.radius
            self.x_speed = randint(-2, 2) / 10
            self.y_speed = randint(-21, -10) / 10
        elif starting_point == 8:
            self.x = randint(800, 850) - self.radius
            self.y = randint(800, 850) - self.radius
            self.x_speed = randint(-21, -10) / 10
            self.y_speed = randint(-21, -10) / 10

    def give_coordinates(self):
        return self.x, self.y

    def give_center_x(self):
        return self.x + self.radius

    def give_center_y(self):
        return self.y + self.radius


class Ammo:
    """Ammo that is shot by player character. Defining color, radius, starting location, speed and direction."""
    def __init__(self, x, y, target_x, target_y):
        self.color = (0, 100, 0)
        self.color_fill = (0, 255, 0)
        self.radius = 5
        self.radius_fill = 4
        self.x = x
        self.y = y
        self.target_x = target_x
        self.target_y = target_y
        self.x_speed = 0
        self.y_speed = 0

    def give_coordinates(self):
        return self.x, self.y


class Sweet:
    """Blobs that can be collected. Created when enemy blob is hit  with ammo.
    Defining color, size, location and speed. Size, location and speed is got from original enemy blob."""
    def __init__(self, x, y, x_speed, y_speed, radius):
        self.color = (0, 100, 0)
        self.color_fill = (0, 255, 0)
        self.radius = radius
        self.radius_fill = radius - 4
        self.x = x
        self.y = y
        self.x_speed = x_speed
        self.y_speed = y_speed

    def give_coordinates(self):
        return self.x, self.y


def does_bad_guy_hit(bad_guy: BadGuy, good_guy: GoodGuy):
    """Function that calculates if enemy blob hits player character."""
    if sqrt((bad_guy.x - good_guy.x) ** 2 + (bad_guy.y - good_guy.y) ** 2) <= bad_guy.radius + good_guy.radius:
        bad_guy_hits(bad_guy, good_guy)


def bad_guy_hits(bad_guy: BadGuy, good_guy: GoodGuy):
    """Function that defines what happens when enemy blob hits player character."""
    bad_guy_list.remove(bad_guy)
    good_guy.radius -= 15
    good_guy.radius_fill -= 15
    does_game_end(good_guy)


def does_ammo_hit(bad_guy: BadGuy, ammo: Ammo):
    """Function that calculates if ammo hits enemy blob."""
    if sqrt((bad_guy.x - ammo.x) ** 2 + (bad_guy.y - ammo.y) ** 2) <= bad_guy.radius + ammo.radius:
        ammo_hits(bad_guy, ammo)


def ammo_hits(bad_guy: BadGuy, ammo: Ammo):
    """Function that defines what happens when ammo hits enemy blob."""
    try:
        sweets_list.append(
            Sweet(bad_guy.x, bad_guy.y, bad_guy.x_speed / 5, bad_guy.y_speed / 5, bad_guy.radius))
        bad_guy_list.remove(bad_guy)
        ammo_list.remove(ammo)
    except ValueError:
        pass


def does_sweet_hit(sweet: Sweet, good_guy: GoodGuy):
    """Function that calculates if sweet hits player character."""
    if sqrt((sweet.x - good_guy.x) ** 2 + (sweet.y - good_guy.y) ** 2) <= sweet.radius + good_guy.radius:
        sweet_hits(sweet, good_guy)


def sweet_hits(sweet: Sweet, good_guy: GoodGuy):
    """Function that defines what happens when sweet hits player character."""
    good_guy.radius += 2
    good_guy.radius_fill += 2
    sweets_list.remove(sweet)


def does_game_end(good_guy: GoodGuy):
    """Function that checks if game is over."""
    if good_guy.radius <= 7:
        global game_over
        game_over = True


def good_guy_speeds(good_guy_x, good_guy_y, mouse_x, mouse_y):
    """Function that calculates x and y speed vector. Sum of vectors is always 1. """

    """First calculations check if x or y vector is 0. If x or y are not 0 bot x and y vectors are calculated."""
    if good_guy_x == mouse_x and good_guy_y == mouse_y:
        returning_x_speed = 0
        returning_y_speed = 0

    elif good_guy_x == mouse_x:
        returning_x_speed = 0
        if good_guy_y > mouse_y:
            returning_y_speed = -1
        else:
            returning_y_speed = 1

    elif good_guy_y == mouse_y:
        if good_guy_x > mouse_x:
            returning_x_speed = -1
        else:
            returning_x_speed = 1
        returning_y_speed = 0

    else:
        if good_guy_x > mouse_x and good_guy_y > mouse_y:
            returning_x_speed = - sqrt(1 / (1 + ((good_guy_y - mouse_y) / (good_guy_x - mouse_x)) ** 2))
            returning_y_speed = (good_guy_y - mouse_y) / (good_guy_x - mouse_x) * returning_x_speed

        elif good_guy_x < mouse_x and good_guy_y > mouse_y:
            returning_x_speed = sqrt(1 / (1 + ((good_guy_y - mouse_y) / (mouse_x - good_guy_x)) ** 2))
            returning_y_speed = -(good_guy_y - mouse_y) / (mouse_x - good_guy_x) * returning_x_speed

        elif good_guy_x > mouse_x and good_guy_y < mouse_y:
            returning_x_speed = - sqrt(1 / (1 + ((mouse_y - good_guy_y) / (good_guy_x - mouse_x)) ** 2))
            returning_y_speed = -(mouse_y - good_guy_y) / (good_guy_x - mouse_x) * returning_x_speed

        else:
            returning_x_speed = sqrt(
                1 / (1 + ((mouse_y - good_guy_y) / (mouse_x - good_guy_x)) ** 2))
            returning_y_speed = (mouse_y - good_guy_y) / (mouse_x - good_guy_x) * returning_x_speed

    return returning_x_speed, returning_y_speed


def random():
    """Returns randomly true or false. Used for enemy blob spawn frequency. True = enemy spawn, false = no spawn."""
    random_number = randint(1, 100)
    if random_number < 6:
        return True
    return False


def app():
    """Application itself. First game is initialized."""
    pygame.init()
    window = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Blob goes brr!")
    clock = pygame.time.Clock()
    points = 0
    target_x = window_width / 2 - player.radius
    target_y = window_height / 2 - player.radius
    counter = 0
    score_printed = False
    global game_over

    """Loop that keeps window refreshed."""
    while True:
        while not game_over:
            window.fill((0, 0, 0))

            """Game button listeners. Esc = quit game, space = new game, 
            mouse1 = shoot to target location and mouse2 = move to target location."""
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        exit()

                    if event.key == pygame.K_SPACE:
                        bad_guy_list.clear()
                        ammo_list.clear()
                        sweets_list.clear()
                        player.radius = 50
                        player.radius_fill = 46
                        player.x = window_width / 2 - player.radius
                        player.y = window_height / 2 - player.radius
                        target_x = window_width / 2 - player.radius
                        target_y = window_height / 2 - player.radius
                        points = 0
                        game_over = False
                        break

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed(3)[2]:
                        target_x = event.pos[0]
                        target_y = event.pos[1]

                    if pygame.mouse.get_pressed(3)[0]:
                        ammo_x = event.pos[0]
                        ammo_y = event.pos[1]
                        ammo_list.append(Ammo(player.x, player.y, ammo_x, ammo_y))
                        ammo_list[-1].x_speed, ammo_list[-1].y_speed = \
                            good_guy_speeds(player.x, player.y, ammo_x, ammo_y)
                        player.radius -= 1
                        player.radius_fill -= 1
                        does_game_end(player)

            """Moves ammos on screen. Calculated before drawing every frame."""
            for ammo in ammo_list:
                if ammo.x < -50 or ammo.x > window_width + 50 or ammo.y < -50 or ammo.y > window_height + 50:
                    ammo_list.remove(ammo)
                ammo.x += ammo.x_speed * 5
                ammo.y += ammo.y_speed * 5

                """Initializes ammo render."""
                pygame.draw.circle(window, ammo.color, ammo.give_coordinates(), ammo.radius)
                pygame.draw.circle(window, ammo.color_fill, ammo.give_coordinates(), ammo.radius_fill)

            """Moves sweets on screen. Calculated before drawing every frame."""
            for sweet in sweets_list:
                sweet.x += sweet.x_speed
                sweet.y += sweet.y_speed
                if sweet.x < -50 or sweet.x > window_width + 50 or sweet.y < -50 or sweet.y > window_height + 50:
                    sweets_list.remove(sweet)
                does_sweet_hit(sweet, player)

                """Initializes sweet render."""
                pygame.draw.circle(window, sweet.color, sweet.give_coordinates(), sweet.radius)
                pygame.draw.circle(window, sweet.color_fill, sweet.give_coordinates(), sweet.radius_fill)

            """Moves enemy blobs on screen. Calculated before drawing every frame."""
            for bad_guy in bad_guy_list:
                bad_guy.x += bad_guy.x_speed
                bad_guy.y += bad_guy.y_speed
                if bad_guy.x < -50 or bad_guy.x > window_width + 50 or bad_guy.y < -50 \
                        or bad_guy.y > window_height + 50:
                    bad_guy_list.remove(bad_guy)
                does_bad_guy_hit(bad_guy, player)

                """Initializes enemy blob render."""
                pygame.draw.circle(window, bad_guy.color, bad_guy.give_coordinates(), bad_guy.radius)
                pygame.draw.circle(window, bad_guy.color_fill, bad_guy.give_coordinates(), bad_guy.radius_fill)

                """Checks if ammo hits enemy blob."""
                for ammo in ammo_list:
                    does_ammo_hit(bad_guy, ammo)

            """Moves player character on screen. Calculated before drawing every frame."""
            good_guy_x_speed, good_guy_y_speed = good_guy_speeds(player.x, player.y, target_x, target_y)
            if not target_x - 1 < player.x < target_x + 1:
                player.x += good_guy_x_speed
            if not target_y - 1 < player.y < target_y + 1:
                player.y += good_guy_y_speed

            """Initializes player character render."""
            pygame.draw.circle(window, player.color, player.give_coordinates(), player.radius)
            pygame.draw.circle(window, player.color_fill, player.give_coordinates(), player.radius_fill)

            """Checks if new enemy blob is added to game."""
            if random():
                bad_guy_list.append(BadGuy())

            """Player character loses size when time passes."""
            counter += 1
            if counter == 120:
                player.radius -= 1
                player.radius_fill -= 1
                counter = 0
                does_game_end(player)

            """Adds and initializes score render"""
            points += 1
            font = pygame.font.SysFont("comicsans", 32)
            text = font.render(f"Points: {points//60}", True, (0, 200, 0))
            window.blit(text, (window_width - 135, 10))

            """Initializes instructions render."""
            font = pygame.font.SysFont("comicsans", 26)
            text = font.render(
                f"Mouse 1: Shoot        Mouse 2: Move", False, (0, 90, 20))
            window.blit(text, (window_width / 2 - text.get_width() / 2, window_height - 30))

            """Renders initialized circles to window."""
            pygame.display.flip()
            clock.tick(60)

        """When game is over, game window is froze and score is shown."""
        while game_over:

            """Listeners for player buttons. Esc = quit and space = new game."""
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        exit()
                    if event.key == pygame.K_SPACE:
                        bad_guy_list.clear()
                        ammo_list.clear()
                        sweets_list.clear()
                        player.radius = 50
                        player.radius_fill = 46
                        player.x = window_width / 2 - player.radius
                        player.y = window_height / 2 - player.radius
                        target_x = window_width / 2 - player.radius
                        target_y = window_height / 2 - player.radius
                        points = 0
                        game_over = False
                        break

            """Opens, reads and writes high score from score.txt."""
            try:
                with open("score.txt", "r") as file:
                    score = int(file.readline())
            except IOError:
                with open("score.txt", "w") as file:
                    file.write("0")
                score = 0

            """Checks if new score if high score. Initializes score rendering."""
            if score < points//60 and not score_printed:
                font = pygame.font.SysFont("comicsans", 115)
                text = font.render(f"NEW HIGH SCORE!", False, (0, 90, 20))
                window.blit(text, (window_width / 2 - text.get_width() / 2, 100))

                font = pygame.font.SysFont("comicsans", 60)
                text = font.render(
                    f"Previous High score: {score}", False, (0, 90, 20))
                window.blit(text, (window_width / 2 - text.get_width() / 2, window_height / 2 - 30))

                with open("score.txt", "w") as file:
                    file.write(str(points // 60))

                score_printed = True

            elif score >= points//60 and not score_printed:
                font = pygame.font.SysFont("comicsans", 60)
                text = font.render(
                    f"High score: {score}", False, (0, 90, 20))
                window.blit(text, (window_width / 2 - text.get_width() / 2, window_height / 2 - 30))
                score_printed = True

            """Initializes instruction rendering."""
            font = pygame.font.SysFont("comicsans", 120)
            text = font.render(
                f"Points: {points // 60}", False, (0, 90, 20))
            window.blit(text, (window_width / 2 - text.get_width() / 2, window_height / 2 - 130))

            font = pygame.font.SysFont("comicsans", 50)
            text = font.render(f"SPACE: New game", True, (0, 90, 20))
            window.blit(text, (window_width / 2 - text.get_width() / 2, window_height / 2 + 60))

            text = font.render(f"ESC: Exit game", True, (0, 90, 20))
            window.blit(text, (window_width / 2 - text.get_width() / 2, window_height / 2 + 100))

            """Renders initialized texts to window."""
            pygame.display.flip()
            clock.tick(60)
        score_printed = False


"""Global variables used game."""
bad_guy_list = []
ammo_list = []
sweets_list = []
window_width = 800
window_height = 800
game_over = False
player = GoodGuy()
app()
